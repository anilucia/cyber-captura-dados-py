import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from malware_lab import workspace
from malware_lab.ransomware import encrypt, decrypt
from malware_lab.detection import inspect
from malware_lab.mail_demo import create_eml


class MalwareLabTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.patcher = patch("malware_lab.workspace.base_directory", return_value=Path(self.temp.name) / "lab_workspace")
        self.patcher.start()
        self.addCleanup(self.patcher.stop)
        self.base = workspace.init_workspace()

    def test_encrypt_decrypt_roundtrip(self):
        original = {name: (self.base / "samples" / name).read_bytes() for name in workspace.SAMPLES}
        self.assertEqual(encrypt(), 3)
        self.assertEqual(encrypt(), 0)
        self.assertEqual(len(inspect()["simulated_encrypted_files"]), 3)
        self.assertEqual(decrypt(), 3)
        self.assertEqual(decrypt(), 0)
        for name, content in original.items():
            self.assertEqual((self.base / "samples" / name).read_bytes(), content)

    def test_report_generated(self):
        result = inspect()
        self.assertEqual(result["risk_level"], "NORMAL (simulação)")
        self.assertTrue((self.base / "reports" / "detection.html").exists())
        self.assertTrue((self.base / "reports" / "detection.json").exists())

    def test_mail_is_local_and_synthetic(self):
        path = Path(create_eml())
        self.assertEqual(path.parent, self.base / "outbox")
        body = path.read_text(encoding="utf-8")
        self.assertIn("EXEMPLO_TESTE", body)
        self.assertIn("example.invalid", body)

    def test_reject_symlink_sample(self):
        sample = self.base / "samples" / "documento.txt"
        sample.unlink()

        try:
            sample.symlink_to(self.base / "reports" / "outside")
        except OSError as error:
            if getattr(error, "winerror", None) == 1314:
                self.skipTest(
                    "Windows sem permissão para criar symlinks"
                )
            raise

        with self.assertRaises(RuntimeError):
            encrypt()


if __name__ == "__main__":
    unittest.main()

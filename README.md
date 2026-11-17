# Python Malware Lab — Ransomware e Keylogger Simulados

> Projeto educacional, **offline**, para estudo de ameaças e defesa cibernética. Não captura teclas globais, não implementa furtividade e não transmite dados para terceiros.

## Objetivos do desafio

- [x] Criar arquivos fictícios de teste
- [x] Criptografar e descriptografar os arquivos com Fernet (criptografia autenticada)
- [x] Exibir uma nota de resgate **fictícia**
- [x] Simular o registro de entradas **apenas do próprio terminal**, com consentimento
- [x] Registrar os eventos em arquivo local `.jsonl` (formato de texto)
- [x] Criar um e-mail `.eml` sintético, **sem enviar pela rede**
- [x] Documentar aspectos de furtividade e transmissão real apenas conceitualmente
- [x] Documentar prevenção, detecção, mitigação e limitações
- [x] Testes automatizados e pipeline GitHub Actions
- [x] **Plus:** gerador de relatório defensivo em JSON e HTML

## Requisitos

Python 3.10+; Windows, Linux ou macOS; pacote `cryptography`. Não são necessárias credenciais, serviços cloud ou conexão de rede para executar (somente para instalar a dependência, se não estiver instalada).

## Instalação

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS:
# source .venv/bin/activate
python -m pip install -r requirements.txt
```

Você pode usar `python run.py <comando>` sem instalar o pacote. Opcionalmente, `pip install -e .` habilita o comando `malware-lab <comando>`.

## Demonstração passo a passo

```bash
python run.py init          # cria pasta lab_workspace e 3 arquivos fictícios
python run.py inspect       # relatório inicial
python run.py encrypt       # criptografa somente as 3 amostras fictícias
python run.py inspect       # evidencia extensões .locked + nota
python run.py decrypt       # restaura as 3 amostras usando chave local
python run.py keyboard      # digite frases fictícias; SAIR encerra
python run.py mail-demo     # gera .eml com dados artificiais, SEM envio
python run.py inspect       # gera reports/detection.json e detection.html
```

Abra `lab_workspace/reports/detection.html` no navegador. Todos os artefatos são locais e ignorados pelo Git.

## Estrutura

```text
python-malware-lab/
├── .github/workflows/tests.yml
├── docs/
│   ├── arquitetura.md
│   ├── ransomware.md
│   ├── keylogger.md
│   └── defesa.md
├── malware_lab/
│   ├── cli.py
│   ├── workspace.py
│   ├── ransomware.py
│   ├── keyboard.py
│   ├── mail_demo.py
│   └── detection.py
├── tests/test_lab.py
├── run.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Testes

```bash
python -m unittest discover -s tests -v
```

## Segurança e limitações

1. O programa opera somente em `lab_workspace` adjacente ao código e em **três arquivos de nomes conhecidos**. Não recebe caminhos externos nem percorre arquivos pessoais.
2. O programa de entrada de texto lê apenas `input()` dentro do próprio terminal. **Não é um keylogger real ou furtivo**.
3. O experimento de e-mail cria um arquivo `.eml` com conteúdo sintético na pasta `outbox`. **Não há SMTP, conexão ou exfiltração.**
4. A chave local existe para permitir reversão. Não há persistência maliciosa, escalonamento ou propagação.
5. O relatório é uma demonstração de heurísticas, não um mecanismo de detecção de ameaças em produção.
6. Nunca use dados pessoais, corporativos ou arquivos importantes neste laboratório. Recomenda-se VM descartável por boa prática.

## Evidências recomendadas para entrega

Capturas de tela dos comandos `init`, `encrypt`, `inspect`, `decrypt`, `keyboard`, `mail-demo`, do HTML do relatório e dos testes passando. Não publique a pasta `lab_workspace`.

## O que aprendi

Criptografia autenticada pode tornar dados indisponíveis sem a chave correta; backups e restauração são parte central da resiliência. Registros de entrada podem expor informações e precisam de autorização e minimização. Eventos como extensões alteradas, surgimento de notas e logs inesperados podem compor estratégias de detecção, mas exigem correlação para reduzir falsos positivos. Veja os detalhes em `docs/defesa.md`.

## Publicação no GitHub

```bash
git init
git add .
git commit -m "feat: laboratorio educacional de malware e defesa"
git branch -M main
# crie um repositório vazio no GitHub e então:
git remote add origin https://github.com/SEU-USUARIO/python-malware-lab.git
git push -u origin main
```

**Licença:** MIT. **Uso:** exclusivamente educacional e autorizado.

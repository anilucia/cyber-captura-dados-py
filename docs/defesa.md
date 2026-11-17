# Prevenção, detecção, resposta e lições aprendidas

| Controle | Mitigação | Exemplo prático |
|---|---|---|
| Backups offline/imutáveis | Recuperação após criptografia | Testar restauração regularmente |
| EDR e antivírus | Visibilidade sobre comportamentos suspeitos | Alertas de alterações em massa |
| Firewall e filtragem de saída | Redução de canais de exfiltração | Bloquear destinos desconhecidos |
| Menor privilégio | Limitar arquivos e sistemas atingíveis | Conta sem permissão administrativa |
| Atualizações | Reduzir vulnerabilidades exploráveis | Correções de SO e apps |
| MFA e proteção de credenciais | Reduzir impacto de senha roubada | MFA resistente a phishing |
| Sandboxing / VM | Isolar testes não confiáveis | Snapshot antes do laboratório |
| Educação do usuário | Evitar anexos e links fraudulentos | Simulações de phishing autorizadas |

## Indicadores demonstrados

- Arquivos `.locked` substituem amostras `.txt` e `.csv`.
- Nota fictícia surge no workspace.
- Arquivos JSONL e EML são produzidos durante as simulações.
- `inspect` usa esses artefatos para produzir um relatório offline.

## Resposta a incidentes (conceitual)

1. Confirmar o alerta e identificar escopo.
2. Isolar sistemas afetados e preservar evidências sem destruir logs.
3. Acionar equipe responsável e avaliar credenciais e acessos.
4. Erradicar causa-raiz, corrigir vulnerabilidades e restaurar de backup confiável.
5. Monitorar reincidência e registrar lições aprendidas.

## Reflexão final

Criptografia legítima também pode ser usada de modo abusivo; por isso sinais isolados não provam infecção. Detecção combina telemetria de processos, arquivos, identidade e rede com contexto. No estudo do keylogger, a diferença entre captura consentida em uma interface e interceptação oculta do sistema é fundamental tanto tecnicamente quanto eticamente.

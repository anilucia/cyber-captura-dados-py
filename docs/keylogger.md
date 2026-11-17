# Estudo: keylogger simulado

## Conceito

Um keylogger pode registrar entradas e revelar conteúdo sensível. Para evitar captura não autorizada, este exercício **não intercepta o teclado global**. Lê exclusivamente as frases que o participante digita voluntariamente no prompt `lab>`.

## Funcionamento

- `keyboard`: exibe aviso explícito e grava timestamp UTC mais a linha digitada em `reports/typing_demo.jsonl`.
- `SAIR`: encerra a captura.
- `mail-demo`: cria um `.eml` com **valores fixos fictícios** e sem acesso à rede; o arquivo pode ser aberto para demonstrar como seria formatada uma mensagem de e-mail.

## Furtividade e exfiltração: estudo conceitual

Em ataques reais, a coleta pode ser ocultada da vítima e os dados enviados para serviços externos. A análise defensiva deve considerar processos inesperados, alterações de inicialização, permissões de captura, acessos anômalos a arquivos e conexões de saída. **O projeto não implementa essas ações.**

## Questões éticas

Coleta de entradas exige autorização específica, minimização de dados, transparência, controle de retenção e proteção das informações. Não registre senhas nem dados de terceiros.

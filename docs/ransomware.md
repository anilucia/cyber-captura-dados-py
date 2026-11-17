# Estudo: ransomware simulado

## Conceito

Ransomware é uma família de ameaças que pode cifrar ou bloquear informações e exigir pagamento. No exemplo, a nota é puramente fictícia e nenhum pagamento é solicitado.

## Etapas implementadas

1. `init` gera 3 arquivos artificiais dentro de `lab_workspace/samples`.
2. `encrypt` cria uma chave Fernet local e cifra exclusivamente esses arquivos, trocando-os por `*.locked`.
3. `RESGATE_SIMULADO.txt` descreve o experimento e ensina como recuperar.
4. `decrypt` verifica a autenticidade dos dados e restaura o conteúdo original.

## Perguntas de análise

- O que muda na disponibilidade antes/depois da cifra?
- Por que uma cópia offline protegida seria essencial em um incidente real?
- Que eventos de segurança sugeririam criptografia suspeita em massa?
- Por que pagar resgate não garante recuperação?

## Evidências

Comparar listagem de `samples` antes/depois; comparar conteúdo de `documento.txt` após restaurar; executar `inspect` nos dois estados.

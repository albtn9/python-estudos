# Python Estudos

Repositório com histórico de exercícios de estudo em Python, organizados por dias.

## Estrutura

- **dia1.py** a **dia60.py** — Um exercício por arquivo, cobrindo:
  - Entrada/saída, operações e condicionais
  - Laços (`while`, `for`)
  - Listas, tuplas, conjuntos e dicionários
  - Tratamento de erros (`try/except`)
  - Módulos (`math`, `random`, `pygame`)
  - Strings e formatação

- **test_dia1.py** — Testes unitários do dia 1 (soma).
- **dia2.py** — Inclui testes no próprio arquivo (rode com `--test`).
- **teste.py** — Código original antes da organização em dias.

## Como rodar

```bash
# Executar um exercício (exemplo: dia 5)
python dia5.py

# Rodar testes do dia 1
python -m unittest test_dia1 -v

# Rodar testes do dia 2 (dentro do próprio arquivo)
python dia2.py --test -v
```

## Requisitos

- Python 3.x
- **dia46.py** (música): `pip install pygame` e é preciso adicionar o arquivo `musica.mp3` na pasta do projeto.

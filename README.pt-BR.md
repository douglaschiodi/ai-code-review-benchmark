# AI Code Review Benchmark Lab — guia em português

Laboratório de avaliação de código com três problemas originais, 13 casos por candidato e pesos explícitos. Compara uma solução de referência com falhas deliberadas. Não representa um ranking de modelos comerciais nem usa testes de processos seletivos.

## Executar

Python 3.11+; standard library only.

```sh
python -m unittest -v
python benchmark.py
```

## O que observar

O relatório JSON mostra cada caso, peso e resultado. A referência passa em todos; o candidato com erros perde pontos em casos de borda. Isso demonstra o método de avaliação, sem comparar modelos comerciais.

## Origem e limites

Projeto novo, criado com assistência de IA para este portfólio. Todos os dados são fictícios. Não contém código de clientes, configurações de produção, credenciais ou histórico dos sistemas existentes.

Os detalhes técnicos, contratos e limitações estão no [README principal](README.md) e em [ARCHITECTURE.md](ARCHITECTURE.md). É uma demonstração educacional; não deve ser apresentada como produto implantado em clientes. Licença MIT para o código original; dependências mantêm suas próprias licenças.

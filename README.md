# Data Quality Lab

Pequeno projeto para processamento e validação de dados, geração de conjuntos de dados e relatórios.

**Sobre**
- Projeto com uma pipeline simples que conecta a fontes de dados, cria datasets e gera relatórios em Excel/PDF.

**Recursos**
- Extrair e transformar dados com `src/pipeline.py`
- Helpers de conexão em `connection/conn.py` e geração de dataset em `connection/create_data_set.py`
- Geração de relatórios em `reports/create_report.py`

**Requisitos**
- Python 3.8+
- Instalar dependências:

```bash
pip install -r requirements.txt
```

**Estrutura do projeto**
- `src/pipeline.py`: entrada principal da pipeline que orquestra processamento.
- `connection/conn.py`: funções de conexão (DB / arquivos).
- `connection/create_data_set.py`: criação e preparação de datasets.
- `reports/create_report.py`: geração de relatórios (Excel / PDF).
- `requirements.txt`: dependências do projeto.
- `.env`: variáveis de ambiente (credenciais / caminhos de entrada/saída).

Veja os arquivos principais: [src/pipeline.py](src/pipeline.py), [connection/conn.py](connection/conn.py), [reports/create_report.py](reports/create_report.py)

**Configuração**
- Crie um arquivo `.env` na raiz com as variáveis necessárias (ex.: credenciais de banco, caminhos de input/output). Os nomes das variáveis usadas pelo código estão em `connection/conn.py`.

**Uso**
- Rodar a pipeline principal:

```bash
python src/pipeline.py
```

- Gerar relatório:

```bash
python reports/create_report.py
```

**Contribuição**
- Abra issues para sugestões e correções. Submeta PRs para melhorias.

**Licença**
- Licença: a definir (adicione uma licença no repositório se desejar).

---

Se quiser, eu adapto este README para inglês, adiciono exemplos de `.env` ou incluo instruções para testes.
# data-quality-lab
Cleaning Data

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


**Versão em Inglês / English Version**

# Data Quality Lab

Small project for data processing and validation, dataset creation and report generation.

**About**
- A simple pipeline that connects to data sources, creates datasets and generates Excel/PDF reports.

**Features**
- Extract and transform data with `src/pipeline.py`
- Connection helpers in `connection/conn.py` and dataset creation in `connection/create_data_set.py`
- Report generation in `reports/create_report.py`

**Requirements**
- Python 3.8+
- Install dependencies:

```bash
pip install -r requirements.txt
```

**Project structure**
- `src/pipeline.py`: main pipeline entry that orchestrates processing.
- `connection/conn.py`: connection helpers (DB / file paths).
- `connection/create_data_set.py`: dataset creation and preparation.
- `reports/create_report.py`: report generation (Excel / PDF).
- `requirements.txt`: project dependencies.
- `.env`: environment variables (credentials / input-output paths).

See the main files: [src/pipeline.py](src/pipeline.py), [connection/conn.py](connection/conn.py), [reports/create_report.py](reports/create_report.py)

**Setup**
- Create a `.env` file in the project root with the variables required by the code (examples below). Variable names used by the code are referenced in `connection/conn.py`.

**Example `.env` / `.env.example`**
Below is a minimal example showing commonly used variables — adapt to your environment:

```env
# Database connection
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_database
DB_USER=my_user
DB_PASS=supersecret

# File paths
INPUT_PATH=./data/input
OUTPUT_PATH=./data/output

# Report options
REPORT_FORMAT=excel  # options: excel, pdf

# Optional flags
DRY_RUN=true
```

Tip: You can keep a `.env.example` in the repo (without secrets) and add `.env` to `.gitignore`.

**Usage**
- Run the main pipeline:

```bash
python src/pipeline.py
```

- Generate report:

```bash
python reports/create_report.py
```

**Testing / Basic checks**
- Install test dependencies (if you plan to add tests):

```bash
pip install pytest
```

- Run unit tests (if present):

```bash
pytest
```

- Smoke / manual checks:
	- Prepare a small sample dataset under `INPUT_PATH`.
	- Run `python src/pipeline.py` and confirm files are produced under `OUTPUT_PATH`.
	- Run `python reports/create_report.py` and verify the generated report(s).

**Contributing**
- Open issues for suggestions and fixes. Submit PRs for improvements.

**License**
- License: to be defined (add a license file to the repository if desired).



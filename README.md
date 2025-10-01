# DemandForecast – Previsão de Demanda com Machine Learning  

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)  [![Scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)](https://scikit-learn.org/stable/)  [![Pandas](https://img.shields.io/badge/pandas-data--analysis-yellow)](https://pandas.pydata.org/)  [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Projeto de **engenharia de dados + machine learning** para construir um **pipeline de previsão de vendas/demanda**, utilizando o dataset da [Rossmann (Kaggle)](https://www.kaggle.com/c/rossmann-store-sales).  
O objetivo é ter um fluxo modular e escalável, com etapas de ETL, treinamento de modelo, avaliação de métricas e geração de previsões, pronto para ser futuramente integrado uma API (via FastAPI).

O código foi desenvolvido de forma **modular e escalável**, incluindo:  
- ETL (Extração, Transformação e Load)  
- Pré-processamento de dados
- Treinamento de modelo ML
- Avaliação das métricas do modelo treinado 
- Geração de previsões salvas em CSV  
- Estrutura organizada para logs, modelos e previsões  

---

## Estrutura do Projeto  

```bash
DemandForecast/
│
├── artifacts/             # Saídas do pipeline
│   ├── logs/              # Logs de execução
│   └── models/            # Modelos salvos (.pkl)
│   
├── data/                  # Dados
│   ├── raw/               # Dados brutos
│   ├── processed/         # Dados tratados
│   └── predictions/       # Resultados de previsão
│
├── src/                   # Código-fonte do pipeline
│   ├── __init__.py
│   ├── etl/               
│   │   ├── extract.py     # Extração dos dados
│   │   ├── transform.py   # Tratamento dos datasets
│   │   └── load.py        # Carrega os datasets tratados
│   │
│   ├── ml/                
│   │   ├── train.py       # Treinamento de modelo ML
│   │   ├── evaluate.py    # Avaliação do modelo ML com métricas de regressão
│   │   ├── preprocess.py  # Realizando Encoding (treinando e salvando encoders)
│   │   └── mlmodels/      # Modelos específicos (RandomForest, etc.)
│
├── artifacts/             # Saídas do pipeline
│   ├── logs/              # Logs de execução
│   └── models/            # Modelos salvos (.pkl)
│
├── main.py                # Código principal, para execução do pipeline ML
├── requirements.txt       # Dependências do projeto (bibliotecas)
├── .gitignore             # Regras de versionamento
└── README.md              # Documentação do projeto

```

---

## Instalação e Uso

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/DemandForecast.git
cd DemandForecast
```
Fazendo alteração do "SEU-USUARIO" para seu usuário github

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o pipeline

* Rodar todas as etapas:

  ```bash
  python main.py all
  ```
* Rodar apenas ETL:

  ```bash
  python main.py etl
  ```
* Treinar modelo:

  ```bash
  python main.py train
  ```
* Gerar previsões:

  ```bash
  python main.py predict
  ```

---

## Tecnologias

* **Python 3.10+**
* **Pandas / NumPy** – manipulação de dados
* **Scikit-learn** – modelos de machine learning
* **Joblib** – salvar modelos encoders
* **Logging** – monitoramento do pipeline
* *(Futuro)* **FastAPI + Uvicorn** – servir modelo via API

---

## Possíveis Próximos Passos

* [ ] Criar API REST com FastAPI para previsões em tempo real
* [ ] Adicionar Dockerfile para deploy simplificado
* [ ] Testes automatizados com pytest
* [ ] CI/CD com GitHub Actions

---

## Autor

**José Gabriel**
Estudante de Engenharia de Software | Focado em Engenharia de Dados
🔗 [LinkedIn](https://www.linkedin.com/jsgabrielpereira) · [GitHub](https://github.com/jgabrielpl)

---

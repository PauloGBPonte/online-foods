# 🍔 Análise de Dados de Pedidos de Comida Online

Este projeto tem como objetivo realizar uma análise exploratória de dados (EDA) sobre um conjunto de pedidos de comida online. Utilizamos Python, Pandas e Jupyter Notebooks para entender padrões de comportamento dos consumidores e extrair insights relevantes a partir dos dados.

## 📁 Estrutura Inicial

online-foods/
│
├── backend/
│   ├── data/                # Arquivos CSV e outros dados brutos
│   ├── notebooks/           # Jupyter Notebooks para EDA e experimentos
│   ├── src/
│   │   ├── data_ingestion/  # Scripts para leitura e pré-processamento dos CSVs
│   │   ├── analysis/        # Scripts para análise exploratória e científica
│   │   └── models/          # Se houver modelos de machine learning ou estatísticos
│   ├── tests/               # Testes unitários ou de integração (se aplicável)
│   └── requirements.txt     # Lista de dependências do Python
│
├── dashboards/
│   ├── src/                 # Código para geração dos dashboards (ex: Dash, Streamlit ou Plotly)
│   └── assets/              # Imagens, CSS, JavaScript ou outros recursos
│
├── frontend/
│   ├── public/              # HTML, CSS e JS, ou um projeto framework (React, Angular, etc.)
│   ├── src/                 # Códigos fonte do front-end
│   └── package.json         # Arquivo de configuração do projeto (se usar Node/npm)
│
├── docs/                    # Documentação do projeto
├── .gitignore               # Arquivo para ignorar arquivos desnecessários no Git
└── README.md                # Documentação geral do projeto


## ✅ O que já foi implementado

- Função `load_csv()` para leitura robusta de arquivos CSV com manipulação de caminhos via `os.path`
- Integração da função com Jupyter Notebooks
- Testes com a base `onlinefoods.csv`

## 🛠️ Tecnologias e Bibliotecas

- Python 3.11+
- Pandas
- os
- Jupyter Notebook
- VSCode

## 🔜 Em desenvolvimento

- Análises estatísticas e visuais
- Tratamento de dados faltantes e inconsistentes
- Geração de dashboards interativos (futuramente)

---

> Este README será atualizado conforme o projeto evolui.
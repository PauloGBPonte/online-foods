# 🍔 Análise de Dados de Pedidos de Comida Online

Este projeto tem como objetivo realizar uma análise exploratória de dados (EDA) sobre pedidos de comida online, com o intuito de entender padrões de comportamento dos consumidores, preferências e outros insights valiosos.

Utilizamos Python, bibliotecas de análise de dados como Pandas, e visualizações interativas com ferramentas modernas. A estrutura do projeto foi pensada para escalabilidade, permitindo futuras implementações como dashboards, modelos preditivos e APIs de consulta.

---

## 📁 Estrutura do Projeto

```text
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
```

---

## ✅ O que já foi implementado

- [x] Função de leitura de CSV com suporte a diferentes caminhos relativos (`load_csv`)
- [x] Organização modular do projeto com divisão por responsabilidade
- [x] Notebook inicial de EDA (`eda.ipynb`)
- [x] Estrutura de diretórios padronizada

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- Pandas
- Jupyter Notebook
- VSCode
- (futuramente) Plotly, Streamlit, Dash

---

## 🚧 Próximos Passos

- [ ] Análise estatística detalhada dos dados
- [ ] Visualizações interativas
- [ ] Desenvolvimento de dashboards web
- [ ] Testes automatizados
- [ ] Modelagem preditiva

---

> Este README será atualizado conforme o projeto evolui.  

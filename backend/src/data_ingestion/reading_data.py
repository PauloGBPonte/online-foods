import pandas as pd
import os

def load_csv(file_name: str, folder: str = '../data/'):
    # Constrói o caminho completo do arquivo com segurança para qualquer sistema operacional
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, folder, file_name)

    try:
        df = pd.read_csv(file_path)
        print(f"Arquivo '{file_name}' carregado com sucesso.")
        return df
    except Exception as e:
        print(f"Erro ao carregar o arquivo '{file_name}': {e}")
        return None

if __name__ == "__main__":
    # Exemplo de uso: ajusta o nome e o caminho conforme necessário
    df_example = load_csv('onlinefoods.csv', folder='backend/data')
    
    if df_example is not None:
        print(df_example.head())

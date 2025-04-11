import pandas as pd
import os

def load_csv(file_name: str, folder: str ='../data/'):
    file_path = os.path.join(os.path.dirname(__file__), '../../data')
    try:
        df = pd.read_csv(file_path)
        print(f"Arquivo '{filename}' carregado com sucesso.")
        return df
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None

if __name__ == "__main__":
    df_example = load_csv('seu_arquivo.csv')
    print(df_example.head())
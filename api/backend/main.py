from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np

# A variável precisa se chamar "app" (é o padrão do FastAPI)
app = FastAPI()

# Configuração do CORS (opcional, mas útil para o frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota de exemplo
@app.get("/")
def home():
    return {"message": "API está funcionando!"}

# Rota de busca (ajuste conforme seu CSV)
@app.get("/buscar")
def buscar_operadoras(termo: str):
    try:
        # Carrega o CSV (ajuste encoding/delimitador conforme necessário)
        df = pd.read_csv("data/Relatorio_cadop.csv", encoding="latin-1", delimiter=";")
        
        # Filtra os resultados
        resultados = df[
            df.astype(str)  # Converte tudo para string
            .apply(lambda x: x.str.contains(termo, case=False, na=False))  # Ignora maiúsculas/minúsculas e NaN
            .any(axis=1)  # Retorna True se qualquer coluna contiver o termo
        ]
        
        # Substitui valores problemáticos antes de converter para JSON
        resultados = resultados.replace([np.inf, -np.inf], np.nan)  # Remove infinitos
        resultados = resultados.fillna("VALOR_VAZIO")  # Substitui NaN por string

        print(f"Termo buscado: '{termo}' | Registros encontrados: {len(resultados)}")
        print(resultados.head())  # Mostra os 5 primeiros resultados
        
        # Converte para dicionário (evitando números muito grandes)
        return resultados.astype(str).to_dict(orient="records")
        
    except Exception as e:
        return {"error": str(e)}
# 🛠️ Teste de Nivelamento - IntuitiveCare

## 📌 Sumário
1. [📁 Estrutura do Projeto](#estrutura-do-projeto)
2. [⚙️ Pré-requisitos](#pré-requisitos)
3. [🚀 Configuração](#configuração)
4. [🧪 Testes Implementados](#testes-implementados)
5. [▶️ Como Executar](#como-executar)
6. [🔒 Considerações de Segurança](#considerações-de-segurança)
7. [✨ Diferenciais Implementados](#diferenciais-implementados)
8. [🌐 Teste de API](#teste-de-api)

---

## 📁 Estrutura do Projeto

```plaintext
api/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── package.json
│   └── src/
banco_dados/
├── 2023/
├── 2024/
├── relatorio/
│   └── Relatorio_cadop.csv
├── scripts.sql
└── requirements.txt
transformacao_dados/
├── main.py
└── requirements.txt
web_scraping/
├── main.py
├── .env
└── requirements.txt
.gitignore
README.md
```

---

## ⚙️ Pré-requisitos

✅ **Softwares necessários:**
- Python 3.10+
- Git
- MySQL 8+ ou PostgreSQL 10+ (para Teste 3)
- Node.js 18+ (para Teste 4)
- FastAPI (para backend)
- Vue.js 3+ (para frontend, opcional)

---

## 🚀 Configuração

```bash
# Configuração inicial
git clone https://github.com/a-abreur/intuitivecare-teste.git
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\\venv\\Scripts\\activate  # Windows

# Instalação das dependências
cd web_scraping && pip install -r requirements.txt
cd ../transformacao_dados && pip install -r requirements.txt
cd ../api/backend && pip install -r requirements.txt
```

---

## 🧪 Testes Implementados

### 1️⃣ Web Scraping 🕵️
```bash
cd web_scraping && python main.py
```

### 2️⃣ Transformação de Dados 🔄
```bash
cd transformacao_dados && python main.py
```

### 3️⃣ Banco de Dados 🗄️
```sql
-- Importação de dados
LOAD DATA LOCAL INFILE 'relatorio/Relatorio_cadop.csv'
INTO TABLE operadoras
CHARACTER SET latin1;
```

### 4️⃣ API 🌐
```bash
cd api/backend && uvicorn main:app --reload
```

---

## 🌐 Teste de API

### Backend (FastAPI)
```python
@app.get("/buscar")
def buscar_operadoras(termo: str):
    resultados = df[df.apply(lambda x: x.str.contains(termo, case=False))]
    return resultados.to_dict(orient="records")
```

### Frontend (Vue.js - opcional)
```bash
cd api/frontend && npm install && npm run dev
```

---

## ▶️ Como Executar

| Módulo         | Comando                          | Porta  |
|----------------|----------------------------------|--------|
| Web Scraping   | `cd web_scraping && python main.py` | -      |
| Banco de Dados | `mysql -u root -p < scripts.sql` | 3306   |
| API Backend    | `uvicorn main:app --reload`      | 8000   |
| API Frontend   | `npm run dev`                    | 5173   |

---

## 🔒 Considerações de Segurança
- Variáveis sensíveis isoladas em `.env`
- Validação de inputs na API:
  ```python
  @app.get("/buscar")
  def buscar_operadoras(termo: str = Query(min_length=2)):
  ```

---

## ✨ Diferenciais Implementados
- Documentação Swagger automática (FastAPI)
- Tratamento de CORS na API
- Frontend opcional com Vue.js 3
- Sistema de logs em todos os módulos
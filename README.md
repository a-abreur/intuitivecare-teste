# 🛠️ Teste de Nivelamento - IntuitiveCare

## 📌 Sumário
1. [📁 Estrutura do Projeto](#Estrutura-do-projeto)
2. [⚙️ Pré-requisitos](#Pré-requisitos)
3. [🚀 Configuração](#Configuração)
4. [🧪 Testes Implementados](#Testes-implementados)
5. [▶️ Como Executar](#Como-executar)
6. [🔒 Considerações de Segurança](#Considerações-de-segurança)
7. [✨ Diferenciais Implementados](#Diferenciais-implementados)

---

## 📁 Estrutura do Projeto
```bash
intuitivecare_teste/
├── web_scraping/
│   ├── main.py
│   ├── .env
│   └── requirements.txt
├── transformacao_dados/
│   ├── main.py
│   └── requirements.txt
├── banco_dados/
│   ├── scripts.sql
│   └── requirements.txt
├── api/
│   ├── backend/
│   └── frontend/
├── .gitignore
└── README.md
```

---

## ⚙️ Pré-requisitos
✅ **Softwares necessários:**
- Python **3.10+**
- Git
- **MySQL 8+** ou **PostgreSQL 10+** (para Teste 3)
- **Node.js** (opcional, para Teste 4)

---

## 🚀 Configuração

1️⃣ **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/intuitivecare-teste.git
```

2️⃣ **Configure o ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.env\Scripts\activate   # Windows
```

3️⃣ **Instale as dependências:**
```bash
cd web_scraping && pip install -r requirements.txt
```

---

## 🧪 Testes Implementados

### 1️⃣ Web Scraping 🕵️
- Acessa o site da **ANS** e baixa os Anexos I e II em **PDF**.
#### 📌 Como executar:
```bash
cd web_scraping && python main.py
```

### 2️⃣ Transformação de Dados 🔄
- Extrai tabelas do **PDF** para **CSV**.
#### 📌 Como executar:
```bash
cd transformacao_dados && python main.py
```

### 3️⃣ Banco de Dados 🗄️
- Scripts SQL para análise de operadoras.
#### 📌 Como executar:
- Importe o **scripts.sql** no seu **SGBD**.

---

## 🔒 Considerações de Segurança
✅ O arquivo **.env** contém apenas URLs públicas.
✅ Em projetos reais, utilize um **.env.example** com variáveis fictícias.

---

## ✨ Diferenciais Implementados
✅ **Controle de versão** com Git 📂
✅ **Documentação detalhada** 📜
✅ **Estrutura modularizada** 📦

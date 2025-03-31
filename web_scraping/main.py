import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from dotenv import load_dotenv
from pathlib import Path


# Carrega as variáveis de ambiente do arquivo .env
env_path = Path('.env')
load_dotenv(env_path)

BASE_URL = os.getenv("URL_ANS")
OUTPUT_DIR = os.getenv("PASTA_OUTPUT", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def baixar_pdf(url, nome_arquivo):
    """Baixa exclusivamente arquivos PDF."""
    try:
        # Verifica se a URL termina com .pdf (case insensitive)
        if not url.lower().endswith('.pdf'):
            print(f"⚠️ Ignorando não-PDF: {url}")
            return False
            
        resposta = requests.get(url, stream=True, timeout=30)
        resposta.raise_for_status()
        
        caminho = os.path.join(OUTPUT_DIR, nome_arquivo)
        with open(caminho, 'wb') as f:
            for chunk in resposta.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"✅ PDF baixado: {nome_arquivo}")
        return True
        
    except Exception as e:
        print(f"❌ Falha ao baixar {url}: {str(e)}")
        return False

def baixar_pdf(url, nome_arquivo):
    """Baixa exclusivamente arquivos PDF."""
    try:
        # Verifica se a URL termina com .pdf (case insensitive)
        if not url.lower().endswith('.pdf'):
            print(f"⚠️ Ignorando não-PDF: {url}")
            return False
            
        resposta = requests.get(url, stream=True, timeout=30)
        resposta.raise_for_status()
        
        caminho = os.path.join(OUTPUT_DIR, nome_arquivo)
        with open(caminho, 'wb') as f:
            for chunk in resposta.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"✅ PDF baixado: {nome_arquivo}")
        return True
        
    except Exception as e:
        print(f"❌ Falha ao baixar {url}: {str(e)}")
        return False

def encontrar_pdfs_anexos():
    """Encontra apenas links PDF para os Anexos I e II."""
    try:
        resposta = requests.get(BASE_URL, timeout=30)
        resposta.raise_for_status()
        soup = BeautifulSoup(resposta.text, 'html.parser')
        
        # Mapeamento dos anexos
        anexos = {
            'Anexo I': ['anexo i', 'rol de procedimentos'],
            'Anexo II': ['anexo ii', 'diretrizes']
        }
        
        links_validos = []
        
        for nome_anexo, termos in anexos.items():
            for link in soup.find_all('a', href=True):
                texto_link = link.get_text().lower()
                href = link['href'].lower()
                
                # Critérios: contém termo E é PDF
                if (any(termo in texto_link for termo in termos) and href.endswith('.pdf')):
                    url_completa = urljoin(BASE_URL, link['href'])
                    nome_arquivo = f"{nome_anexo.replace(' ', '_')}.pdf"
                    links_validos.append((nome_arquivo, url_completa))
                    break  # Pega apenas o primeiro match
        
        return links_validos
        
    except Exception as e:
        print(f"❌ Erro ao buscar anexos: {str(e)}")
        return []

if __name__ == "__main__":
    print("🔍 Buscando Anexos I e II...")
    pdfs = encontrar_pdfs_anexos()
    
    if not pdfs:
        print("⚠️ Nenhum PDF encontrado. Verifique:")
        print(f"- A URL no .env: {BASE_URL}")
        print("- Se os anexos estão disponíveis como PDFs")
    else:
        for nome_arquivo, url in pdfs:
            baixar_pdf(url, nome_arquivo)
        print("✅ Download concluído. Verifique a pasta 'output'.")
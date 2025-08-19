####Configurar IA Gemini para fazer buscas atualizadas no Google####


# Lembre-se de instalar as bibliotecas no seu terminal antes de rodar:
# pip install google-generativeai python-dotenv

import os
import google.generativeai as genai
from dotenv import load_dotenv

# --- Configuração Segura da API Key ---
# Carrega as variáveis do arquivo .env (que deve conter sua GOOGLE_API_KEY)
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("A chave da API do Google não foi encontrada. Verifique seu arquivo .env")

genai.configure(api_key=api_key)

# --- Inicialização do Modelo ---
# Usando um nome de modelo atual e configurando a ferramenta de busca
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    tools=['google_search'] # Habilita a busca do Google de forma simplificada
)

# --- Execução da Pergunta ---
pergunta = "Quando é a próxima Imersão IA com Google Gemini da Alura?"
print(f"Fazendo a pergunta: '{pergunta}'")

# Gera o conteúdo usando a busca do Google como ferramenta
response = model.generate_content(pergunta)

# --- Exibição dos Resultados ---
# Tratamento de erro básico para o caso de a resposta não vir como esperado
try:
    print("\n--- Resposta ---")
    print(response.text)

    # Acessando os metadados da busca (grounding metadata)
    # É uma boa prática verificar se a estrutura de dados existe antes de tentar acessá-la
    if response.candidates and response.candidates[0].grounding_metadata:
        metadata = response.candidates[0].grounding_metadata
        
        # Verifica se a lista de queries não está vazia
        if metadata.web_search_queries:
            print(f"\nBusca realizada: {metadata.web_search_queries[0]}")
        
        # Verifica se a lista de chunks (fontes) não está vazia
        if metadata.grounding_chunks:
            # Pega os títulos das fontes, tratando casos onde o título pode não existir
            titulos_fontes = [chunk.web.title for chunk in metadata.grounding_chunks if chunk.web and chunk.web.title]
            if titulos_fontes:
                print(f"Páginas utilizadas na resposta: {', '.join(titulos_fontes)}")

except Exception as e:
    print(f"\nOcorreu um erro ao processar a resposta: {e}")
    print("\nDetalhes da resposta completa:")
    print(response)


print("\n--- Fim da Execução ---")
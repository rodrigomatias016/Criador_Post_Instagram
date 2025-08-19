####Configurar IA Gemini para fazer buscas atualizadas no Google####


import pip

pip -q install google-genai

# Configura a API Key do Google Gemini

import os
from google.colab import userdata

os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')

# Configura o cliente da SDK do Gemini

from google import genai

client = genai.Client()

MODEL_ID = "gemini-2.0-flash"

# Pergunta ao Gemini uma informação mais recente que seu conhecimento

from IPython.display import HTML, Markdown

# Perguntar pro modelo quando é a próxima imersão de IA ###############################################
resposta = client.models.generate_content(
    model=MODEL_ID,
    contents='Quando é a próxima Imersão IA com Google Gemini da Alura?',
)

# Exibe a resposta na tela
display(Markdown(f"Resposta:\n {resposta.text}"))

# Pergunta ao Gemini uma informação utilizando a busca do Google como contexto

response = client.models.generate_content(
    model=MODEL_ID,
    contents='Quando é a próxima Imersão IA com Google Gemini da Alura?',
    config={"tools": [{"google_search": {}}]}
)

# Exibe a resposta na tela
display(Markdown(f"Resposta:\n {response.text}"))

# Exibe a busca
print(f"Busca realizada: {response.candidates[0].grounding_metadata.web_search_queries}")
# Exibe as URLs nas quais ele se baseou
print(f"Páginas utilizadas na resposta: {', '.join([site.web.title for site in response.candidates[0].grounding_metadata.grounding_chunks])}")
print()
display(HTML(response.candidates[0].grounding_metadata.search_entry_point.rendered_content))
####Criador de post para Instagram através de 4 agentes da IA Gemini utilizando API do Google####

# ==============================================================================
# 1. IMPORTAÇÕES E CONFIGURAÇÕES INICIAIS
# ==============================================================================
# Lembre-se de rodar no terminal antes: pip install -q google-adk requests
import asyncio
import textwrap
from datetime import date
import warnings

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types

warnings.filterwarnings("ignore")

# ==============================================================================
# 2. DEFINIÇÃO DOS AGENTES (PRINCÍPIO DRY)
# Os agentes são definidos UMA VEZ aqui, fora da lógica principal.
# Isso torna o código mais limpo, eficiente e fácil de manter.
# ==============================================================================

# Modelos de IA a serem usados (usando nomes atuais e estáveis)
MODELO_FLASH = "gemini-1.5-flash-latest"
MODELO_PRO = "gemini-1.5-pro-latest" # Um modelo mais robusto para tarefas complexas

BUSCADOR = Agent(
    name="agente_buscador",
    model=MODELO_FLASH,
    instruction="""Você é um assistente de pesquisa. Sua tarefa é usar a ferramenta de busca do google (google_search)
    para recuperar as últimas notícias de lançamentos muito relevantes sobre o tópico fornecido.
    Foque em no máximo 5 lançamentos relevantes, com base na quantidade e entusiasmo das notícias sobre ele.
    Esses lançamentos devem ser atuais, de no máximo um mês antes da data de hoje.""",
    tools=[google_search]
)

PLANEJADOR = Agent(
    name="agente_planejador",
    model=MODELO_PRO, # Usando um modelo mais poderoso para planejamento
    instruction="""Você é um planejador de conteúdo especialista em redes sociais. Com base na lista de
    lançamentos fornecida, use a ferramenta de busca do Google (google_search) para aprofundar a pesquisa
    e identificar os pontos mais relevantes de cada um. Ao final, escolha o TEMA MAIS PROMISSOR
    e retorne um plano detalhado para um post de Instagram, incluindo os principais ângulos a serem abordados.""",
    tools=[google_search]
)

REDATOR = Agent(
    name="agente_redator",
    model=MODELO_PRO,
    instruction="""Você é um Redator Criativo para a Alura, a maior escola de tecnologia do Brasil.
    Com base no plano de post fornecido, escreva um rascunho de post para Instagram.
    O post deve ser engajador, informativo, com linguagem acessível e tom entusiasmado.
    Inclua de 2 a 4 hashtags relevantes no final.""",
)

REVISOR = Agent(
    name="agente_revisor",
    model=MODELO_FLASH,
    instruction="""Você é um Editor de Conteúdo meticuloso para o Instagram.
    Revise o rascunho de post fornecido, focando em clareza, concisão, correção e tom (adequado para um público jovem, 18-30 anos).
    Se o rascunho estiver excelente, responda apenas 'O rascunho está ótimo e pronto para publicar!'.
    Caso contrário, aponte os problemas e forneça uma versão melhorada do texto.""",
)

# ==============================================================================
# 3. FUNÇÕES AUXILIARES
# ==============================================================================

# Serviço de sessão em memória (pode ser compartilhado)
SESSION_SERVICE = InMemorySessionService()

async def executar_agente(agent: Agent, prompt: str) -> str:
    """Função centralizada para criar uma sessão e chamar um agente."""
    session = await SESSION_SERVICE.create_session(app_name=agent.name, user_id="user1")
    runner = Runner(agent=agent, app_name=agent.name, session_service=SESSION_SERVICE)
    content = types.Content(role="user", parts=[types.Part(text=prompt)])

    final_response = ""
    async for event in runner.run_async(user_id="user1", session_id=session.id, new_message=content):
        if event.is_final_response():
            for part in event.content.parts:
                if part.text:
                    final_response += part.text
    return final_response.strip()

def imprimir_resultado(titulo: str, texto: str):
    """Função para exibir texto formatado no terminal, substituindo o `display(to_markdown)`."""
    print(f"\n--- 📝 {titulo} ---\n")
    # Usa textwrap para formatar o texto, tornando-o mais legível no terminal
    texto_formatado = textwrap.indent(texto, '> ', predicate=lambda _: True)
    print(texto_formatado)
    print("\n" + "-"*60)

# ==============================================================================
# 4. FUNÇÃO PRINCIPAL DE ORQUESTRAÇÃO (LÓGICA DO PROGRAMA)
# ==============================================================================

async def main():
    """Função principal que orquestra a execução dos agentes de forma assíncrona."""
    print("🚀 Iniciando o Sistema de Criação de Posts para Instagram com 4 Agentes 🚀")

    topico = input("❓ Por favor, digite o TÓPICO sobre o qual você quer criar o post de tendências: ")
    if not topico:
        print("❌ Você esqueceu de digitar o tópico! Encerrando.")
        return

    print(f"\n✅ Maravilha! Iniciando o trabalho sobre novidades em '{topico}'...")

    try:
        # --- ETAPA 1: BUSCA ---
        data_hoje = date.today().strftime("%d/%m/%Y")
        prompt_buscador = f"Tópico: {topico}\nData de hoje: {data_hoje}"
        lancamentos = await executar_agente(BUSCADOR, prompt_buscador)
        imprimir_resultado("Resultado do Agente 1 (Buscador)", lancamentos)

        # --- ETAPA 2: PLANEJAMENTO ---
        prompt_planejador = f"Tópico: {topico}\nLançamentos recentes encontrados: {lancamentos}"
        plano = await executar_agente(PLANEJADOR, prompt_planejador)
        imprimir_resultado("Resultado do Agente 2 (Planejador)", plano)

        # --- ETAPA 3: REDAÇÃO ---
        prompt_redator = f"Tópico: {topico}\nPlano do post: {plano}"
        rascunho = await executar_agente(REDATOR, prompt_redator)
        imprimir_resultado("Resultado do Agente 3 (Redator)", rascunho)

        # --- ETAPA 4: REVISÃO ---
        prompt_revisor = f"Tópico: {topico}\nRascunho para revisar: {rascunho}"
        post_final = await executar_agente(REVISOR, prompt_revisor)
        imprimir_resultado("Resultado do Agente 4 (Revisor Final)", post_final)

    except Exception as e:
        print(f"\n🚨 Ocorreu um erro durante a execução: {e}")
        print("Por favor, verifique sua chave de API e a conexão com a internet.")

# ==============================================================================
# 5. PONTO DE ENTRADA DO SCRIPT
# É aqui que dizemos ao Python para executar nossa função `main` assíncrona.
# ==============================================================================
if __name__ == "__main__":
    asyncio.run(main())
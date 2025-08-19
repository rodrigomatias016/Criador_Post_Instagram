# 🤖 Criador de Post para Instagram com IA

![Capa do Projeto](https://user-images.githubusercontent.com/109214425/229344426-3d60f948-c8dc-4c57-a50d-b4f0a996c567.png)

## 📝 Descrição

Este projeto é um script em Python que utiliza a API da OpenAI para gerar automaticamente frases inspiradoras e, em seguida, cria uma imagem de post para o Instagram com a frase gerada sobre um fundo branco. É uma ferramenta simples e poderosa para automatizar a criação de conteúdo.

Este foi um projeto desenvolvido para aplicar e aprofundar meus conhecimentos em Python, consumo de APIs e manipulação de imagens com a biblioteca Pillow.

## ✨ Funcionalidades

* **Geração de Frases com IA**: Conecta-se à API da OpenAI para gerar frases únicas e inspiradoras.
* **Criação de Imagens**: Utiliza a biblioteca Pillow para criar uma imagem no formato de post do Instagram (1080x1080 pixels).
* **Texto Personalizado**: Centraliza a frase gerada na imagem, quebrando a linha de forma inteligente para melhor legibilidade.
* **Fácil de Usar**: Basta executar o script para ter uma nova imagem pronta para postar.

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem principal do projeto.
* **Pillow (PIL)**: Biblioteca para manipulação e criação de imagens.
* **OpenAI API**: Para geração de texto com inteligência artificial.
* **dotenv**: Para gerenciar as chaves de API de forma segura.

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para rodar o projeto na sua máquina.

**1. Clone o repositório:**
```bash
git clone [https://github.com/rodrigomatias016/Criador_Post_Instagram.git](https://github.com/rodrigomatias016/Criador_Post_Instagram.git)
cd Criador_Post_Instagram
```

**2. Crie e ative um ambiente virtual (recomendado):**
```bash
# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Configure sua chave de API:**
   * Crie um arquivo chamado `.env` na raiz do projeto.
   * Dentro deste arquivo, adicione sua chave da OpenAI da seguinte forma:
     ```
     API_KEY="sua_chave_secreta_da_openai_aqui"
     ```

**5. Execute o script:**
```bash
python main.py
```

Pronto! A imagem será gerada e salva na pasta do projeto com o nome `post.png`.

## 🚀 Próximos Passos

Este projeto foi um ótimo aprendizado! Algumas ideias para melhorá-lo seriam:
* Adicionar diferentes templates de fundo.
* Permitir que o usuário escolha o tema da frase.
* Criar uma interface gráfica simples para facilitar o uso.

---
*Este projeto foi desenvolvido por Rodrigo Matias como parte da minha jornada de transição de carreira para a programação Python.*

import os
from util import chain_invoke
from loaders.web_loader import web_loader
from loaders.youtube_loader import yt_loader
from loaders.pdf_loader import pdf_loader
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("API_KEY")

print("Digite 'exit' para encerrar o chat.\n")


"""_summary_
    @https://python.langchain.com/v0.1/docs/modules/chains/

    from_message recebe uma lista de tuplas e concatena com 
    user_messages recebido via parâmetro da função.

 Returns
    invoke(input: str) return output: str
"""


def generate_bot_chain(user_messages):
    language_model = ChatGroq(model="deepseek-r1-distill-qwen-32b")

    chat_config = [
        (
            "system",
            "Você sempre responde de forma objetiva, e tem acesso as informações em {loader_infos}",
        ),
        ("user", "{input}"),
    ]

    chat_prompt_template = ChatPromptTemplate.from_messages(chat_config + user_messages)
    chain = chat_prompt_template | language_model

    response = chain.invoke(
        # Bot loader
        {
            "loader_infos": "",
            "input": "{input}",
        },
        # Web loader
        # {
        #     "loader_infos": web_loader(
        #         "https://dev.to/rutamstwt/langchain-document-loading-36j3"
        #     ),
        #     "input": "{input}",
        # },
        # Yt Loader
        # {
        #     "loader_infos": yt_loader(
        #         "https://www.youtube.com/watch?v=93vlav_LIdY&list=PLY90cjA1Q2GLJBcOJNTUjl8Z_iEglyPLZ&index=5"
        #     ),
        #     "input": "{input}",
        # },
        # Pdf loader - É necessário passar o path completo
        # {
        #     "loader_infos": pdf_loader(
        #         "C:/Users/igord/Code/chatbot-python/loaders/ex-data/FICHA_BRASFELS.pdf"
        #     ),
        #     "input": "{input}",
        # },
    ).content

    return response

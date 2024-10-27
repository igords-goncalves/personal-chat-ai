import os
from loaders.web_loader import web_loader
from loaders.youtube_loader import yt_loader
from loaders.pdf_loader import pdf_loader
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate


api_key = "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"
os.environ["GROQ_API_KEY"] = api_key

language_model = ChatGroq(model="llama-3.1-70b-versatile")

print("Digite 'exit' para encerrar o chat.\n")


"""_summary_
    @https://python.langchain.com/v0.1/docs/modules/chains/

    from_message recebe uma lista de tuplas e concatena com 
    user_messages recebido via parâmetro da função.

 Returns
    invoke(input: str) return output: str
"""


def generate_bot_chain(user_messages):
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
        {
            "loader_infos": pdf_loader(
                "C:/Users/igord/Code/chatbot-python/loaders/data/FICHA_BRASFELS.pdf"
            ),
            "input": "{input}",
        },
    ).content

    return response

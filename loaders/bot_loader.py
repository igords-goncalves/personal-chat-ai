import os
from loaders.web_loader import init_loader
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


def generate_bot_response(user_messages):
    chat_config = [
        (
            "system",
            "Você sempre responde de forma objetiva, e tem acesso as informações: {loader_infos}",
        ),
        ("user", "{input}"),
    ]

    chat_prompt_template = ChatPromptTemplate.from_messages(chat_config + user_messages)
    chain = chat_prompt_template | language_model

    response = chain.invoke(
        {
            "loader_infos": init_loader( "https://dev.to/rutamstwt/langchain-document-loading-36j3"),
            "input": "{input}",
        },
    ).content

    return response

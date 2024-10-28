from loaders.bot_chain import generate_bot_chain


def app():
    message_log = []
    chatting = True

#     menu = """Pergunte o que quiser ou digite:\n
# 1 - Análise de vídeos do Youtube 
# 2 - Análise de documentos em PDF 
# 3 - Web scramping\n
# >>> """

#     user_selection = input(menu)

    while chatting:
        chat_input = input("★ Usuario: ")

        finish_chat = chat_input.lower() == "exit"

        if finish_chat:
            chatting = False

        # Concatena o input e resposta em uma tupla
        message_log.append(("user", chat_input))

        # Reposta do bot
        response = generate_bot_chain(message_log)

        message_log.append(("assistant", response))
        print(f"▲ Bot: {response}\n")


app()

"""_sumary_
    TIP: Se quiser ver o log de mensagens, 
    ou converter para algun formato use:

    print(message_log)
    
    messages data structure example:
    [
        {"role": "user", "content": "Olá tudo bem?"},
        {"role": "assistant", "content": "Resposta do bot"},
        {"role": "user", "content": "Questão 1"},
        {"role": "assistant", "content": "Resposta do bot"},
    ]
"""

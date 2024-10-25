from loaders.bot_loader import generate_bot_response


def app():
    message_log = []
    chat = True

    # while True:
    while chat:
        chat_input = input("★ Usuario: ")

        finish_chat = chat_input.lower() == "exit"

        if finish_chat:
            chat = False
            # break outra forma

        message_log.append(("user", chat_input))

        response = generate_bot_response(message_log)

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

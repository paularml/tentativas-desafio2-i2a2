from chatterbot_corpus import ChatBot
from chatterbot_corpus.data import ChatterBotCorpusTrainer

# Criação do chatbot
chatbot = ChatBot("Therapist")

# Criação do treinador e treinamento usando o conjunto de dados de diálogos pré-definidos
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")


# Função para interação com o chatbot
def eliza_chat():
    print("Therapist\n---------")
    print("Talk to the program by typing in plain English. Enter 'quit' when done.")
    print("=" * 72)
    print("Hello. How can I assist you today?")

    # Loop de interação com o usuário
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Thank you for talking with me. Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(response)


# Inicia a interação do chatbot
if __name__ == "__main__":
    eliza_chat()

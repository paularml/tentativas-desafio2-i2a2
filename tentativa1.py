from nltk.chat.util import Chat, reflections
import random
import spacy
import requests

# Carrega o modelo de idioma do spaCy
nlp = spacy.load("en_core_web_sm")


# Função para realizar o processamento de linguagem natural usando o spaCy
def process_nlp(input_text):
    doc = nlp(input_text)
    entities = [ent.text for ent in doc.ents]

    # Correção: Verifica se o texto possui sentimentos positivos ou negativos
    sentiment = process_sentiment(doc)

    return entities, sentiment


# Função para processar sentimentos
def process_sentiment(doc):
    # Exemplo simples: verifica se há palavras positivas ou negativas no texto
    positive_words = [
        "good",
        "happy",
        "positive",
        "well",
        "cheerful",
        "pleased",
        "in a good mood",
        "glad",
        "delighted",
    ]
    negative_words = [
        "bad",
        "sad",
        "negative",
        "unhappy",
        "miserable",
        "upset",
        "broken-hearted",
        "heartbroken",
        "heartsick literary",
        "devastated",
        "distraught",
        "depressed",
        "down",
        "low",
    ]

    positive_count = sum(1 for word in doc if word.text.lower() in positive_words)
    negative_count = sum(1 for word in doc if word.text.lower() in negative_words)

    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"


# Exemplo de respostas variadas para o padrão "Tell me more."
tell_me_more_responses = [
    "I'm interested to hear more about that.",
    "I'd love to hear more. Go ahead.",
    "Feel free to share more details with me.",
    "I'm all ears. Please provide more details.",
    "I'm curious to know more. Could you give me more information?",
    "Feel free to go into more detail. I'm here to listen.",
]

# Exemplo de respostas variadas para o padrão "Can you elaborate on that?"
elaborate_responses = ["I'm here to help you. But only you have the right answer."]

psychologist_responses = [
    "What do you think might be the underlying cause?",
    "It's okay to feel that way. Can you explain why?",
    "How have you been coping with these emotions?",
]


# ... Outras listas de respostas variadas para diferentes padrões ...
# Função para responder com base nas funcionalidades específicas
def chatbot_responder(input_text, is_psychologist_mode=False):
    entities, sentiment = process_nlp(input_text)

    if "depressed" or "anxious" in input_text.lower():
        return random.choice(psychologist_responses)

    # Exemplo: Responder com base em sentimentos
    elif sentiment == "positive":
        return (
            "I'm glad to hear that you're feeling positive!"
            + " "
            + random.choice(tell_me_more_responses)
        )
    elif sentiment == "negative":
        return "I'm sorry to hear that you're feeling down. Is there something you'd like to talk about?"

    # Exemplo: Responder a uma saudação
    if any(greeting in input_text.lower() for greeting in ["hello", "hi"]):
        return random.choice(
            ["Hello!", "Hi there!", "Hello, how can I assist you today?"]
        )

    # Exemplo: Responder a uma pergunta sobre notícias
    if "the news" in input_text.lower():
        return "I'm not up-to-date with the latest news, but I'm here to chat with you!"
    if "feeling" and sentiment == "negative" in input_text.lower():
        return random.choice(tell_me_more_responses)
    if (
        "What can I do"
        or "I don't know what to do"
        or "Can you help me" in input_text.lower()
    ):
        return random.choice(elaborate_responses)
    # ... Adicione mais padrões e listas de respostas aqui ...

    # Se nenhuma funcionalidade específica for acionada, retorna uma resposta pré-definida
    responses = ["Can you elaborate on that?"]
    return random.choice(responses)


# Função principal para a interação do chatbot
def eliza_chat():
    print("Therapist\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print("=" * 72)
    print("Hello. How can I assist you today?")

    # Loop de interação com o usuário
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Thank you for talking with me. Goodbye!")
            break
        response = chatbot_responder(user_input)
        print(response)


# Inicia a interação do chatbot
if __name__ == "__main__":
    eliza_chat()

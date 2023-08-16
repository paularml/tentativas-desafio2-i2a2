from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

# Carrega o modelo GPT-2
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Defina o token de preenchimento
model.config.pad_token_id = tokenizer.eos_token_id

# Cria um pipeline de geração de texto
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Resto do seu código existente...
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


# Função para responder com base nas funcionalidades específicas
def chatbot_responder(input_text):
    entities, sentiment = process_nlp(input_text)

    # Gera respostas usando o pipeline de geração de texto
    generated_text = generator(
        input_text, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2
    )

    return generated_text[0]["generated_text"]


# Função principal para a interação do chatbot
def eliza_chat():
    # Restante do seu código existente...
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

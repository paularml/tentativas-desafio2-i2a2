import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carregar modelo GPT-2 pré-treinado
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Definir sementes para reproduzibilidade
torch.manual_seed(42)
model.eval()


# Função para gerar respostas do chatbot
def generate_response(prompt, max_length=100, temperature=0.2):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    response_ids = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=temperature,
    )
    response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response


# Iniciar conversa com o chatbot
print("Chatbot: Olá! Como posso ajudar você hoje?")

while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "bye", "adeus"]:
        print("Chatbot: Até mais!")
        break
    response = generate_response(
        user_input, max_length=50, temperature=0.8
    )  # Ajuste a temperatura conforme necessário
    print("Chatbot:", response)

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Carrega o modelo GPT-2
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Defina o token de preenchimento
model.config.pad_token_id = tokenizer.eos_token_id

# Configuração para gerar respostas mais curtas e coerentes
max_length = 50
num_return_sequences = 1
no_repeat_ngram_size = 2
temperature = 0.7
top_k = 50


# Função para responder com base nas funcionalidades específicas
def chatbot_responder(input_text):
    # Gera respostas usando o modelo GPT-2
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=num_return_sequences,
            no_repeat_ngram_size=no_repeat_ngram_size,
            pad_token_id=tokenizer.eos_token_id,
            temperature=temperature,
            top_k=top_k,
        )
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text


# Função principal para a interação do chatbot
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
        response = chatbot_responder(user_input)
        print(response)


# Inicia a interação do chatbot
if __name__ == "__main__":
    eliza_chat()

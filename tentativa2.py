from transformers import GPT2LMHeadModel, GPT2Tokenizer


def main():
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Defina o token de preenchimento
    model.config.pad_token_id = tokenizer.eos_token_id

    print("Chatbot: Hello! I'm your chatbot. Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break

        input_ids = tokenizer.encode(user_input, return_tensors="pt")

        # Crie uma máscara de atenção
        attention_mask = input_ids.new_ones(input_ids.shape)

        # Defina o parâmetro max_length
        max_length = 100  # Defina o valor máximo desejado

        output = model.generate(
            input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2
        )
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        print("Chatbot:", generated_text)


if __name__ == "__main__":
    main()

import openai

# Set your OpenAI API key here
openai.api_key = 'your_openai_api_key'

def chat_with_gpt(prompt, max_tokens=50, temperature=0.7, engine="davinci"):
    """Interact with GPT-3.5 through OpenAI's API."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature,
        engine=engine
    )
    return response.choices[0].message['content']

def main():
    print("Welcome to the ChatGPT demo! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        response = chat_with_gpt(user_input)
        print("ChatGPT:", response)

if __name__ == "__main__":
    main()

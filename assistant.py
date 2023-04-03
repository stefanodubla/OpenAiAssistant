import json
import openai

with open("secret.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_key"]

openai.api_key = api_key

def get_response(messages:list) :
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 1.0
    )
    return response.choices[0].message

if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "Sei un assistente virtuale chiamata JOI e parli italiano."}
    ]
    try:
        while True:
            user_input = input("\nTu: ")
            messages.append({"role": "user", "content": user_input})
            new_message = get_response(messages=messages)
            print(f"\nJOI: {new_message['content']}")
            messages.append(new_message)
    except KeyboardInterrupt:
        print("A presto!")

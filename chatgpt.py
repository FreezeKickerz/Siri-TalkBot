import listen
import speech_recognition as sr
import openai
import speak

openai.api_key="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"

messages = [
        {
            "role": "system",
            "content": "Act as siri with me"
        }
    ]

def chat_with_gpt(user_input):
    messages.append({'role': 'user', 'content': f'{user_input}'})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens = 50,
        messages=messages,
        temperature=1,
        top_p=0, 
        frequency_penalty=1, 
        presence_penalty=1
    )
    r = response['choices'][0]['message']['content']
    messages.append({'role': 'assistant', 'content': f'{r}'})
    return r

def main():
    print("ChatGPT Terminal Chatbot (say 'quit' to exit)") 
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()    
    while True:
        user_input = listen.recognize_speech_from_mic(recognizer, microphone)
        if type(user_input) == None:
            continue
        if 'quit' in user_input.lower():
            break
        response = chat_with_gpt(user_input)
        print("ChatGPT:", response)
        speak.speak(response)

main()
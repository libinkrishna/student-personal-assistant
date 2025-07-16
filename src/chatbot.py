import os
from openai import OpenAI

client = OpenAI()

def ask_question():
    print("\nGPT Academic Q&A Chatbot. Type 'exit' to return to the main menu.")

    while True:
        question = input("Ask your question: ").strip()
        if question.lower() == "exit":
            break

        try:
            response = client.chat.completions.create(
                model="gpt-4o-preview",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful academic assistant for students. Answer clearly and concisely."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )
            print("\nAssistant:", response.choices[0].message.content.strip())
        except Exception as e:
            print("Error:", e)

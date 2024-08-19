from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}
Question: {question}

Answer:
"""


model = OllamaLLM(model="gemma2:2b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    context = ""
    print("Ask your queries... Type 'exit' to quit")
    while True:
        user_input = input("you: ")
        if user_input.lower() == "exit":
            break

        response = ""

        for result in chain.stream({"context": context, "question": user_input}):

            print(result, end="", flush=True)

            response += result

        print()
        context += f"\nUser: {user_input}\nAI: {response}"


if __name__ == "__main__":
    handle_conversation()

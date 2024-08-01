from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo')


chat_history = []

# Set initial system message
system_message = SystemMessage(content="You are an expert Software Engineer.")

# Add system message to chat history
chat_history.append(system_message)

# Chat Loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    # Get a response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")


print("----- Message History -----")
print(chat_history)
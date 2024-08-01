from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo')


# SystemMessage:
# Message for priming AI behavior, usually passed in as the first of a sequence of input messages.

# HumanMessage:
# Message from a human to AI model.

messages = [
    SystemMessage(content="Solve the following problem"),
    HumanMessage(content="What is 420-21?")
]


# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI:  {result.content}")


# AIMessage: Message from AI

messages = [
    SystemMessage(content="Solve the following problem"),
    HumanMessage(content="What is 2+2?"),
    AIMessage(content="2+2 is 4."),
    HumanMessage(content="What is 53-23?")
]


result = model.invoke(messages)
print(f"Answer from AI  {result.content}")
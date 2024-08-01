from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()

messages = [
    SystemMessage(content="Solve the following problems."),
    HumanMessage(content="What is 4 multiply 3?")
]


# ------- Langchain OpenAI Chat Model Example -------

# Create a ChatOpenAI model
model = ChatOpenAI(model='gpt-3.5-turbo')

result = model.invoke(messages)
print(f"Answers from OpenAI: {result.content}")


# ------- Anthropic Chat Model Example --------

# Create a Anthropic Model
model = ChatAnthropic(model='claude-3-opus-20240229')

result = model.invoke(messages)
print(f"Answer from Anthropic: {result.content}")



# ------- Google Chat Model Example --------

# Create a Google Model
model = ChatGoogleGenerativeAI(model='claude-3-opus-20240229')

result = model.invoke(messages)
print(f"Answer from Google: {result.content}")

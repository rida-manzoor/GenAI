from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo')

# Define a prompt templates
prompt_template = ChatPromptTemplate(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human","Tell me {joke_count} jokes.")
    ]
)

# Create the combined chain using Langchain Expression Language(LCEL)
chain = prompt_template | model | StrOutputParser()
# chain = prompt_template | model

# Run the chain
result = chain.invoke({"topic":"lawyers", "joke_count":3})

print(result)
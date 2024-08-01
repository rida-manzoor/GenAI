# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Document: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Load environment variables
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model='gpt-3.5-turbo')

# Invoke the model with a message
result = model.invoke("What is 21+9?")
print("Full results:")
print(result)
print("Content only:")
print(result.content)
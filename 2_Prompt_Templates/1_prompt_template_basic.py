# Prompt Template Docs:
# https://python.langchain.com/v0.2/docs/concepts/


from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


# Part 1: Create a ChatPromptTemplate using a template string
# template = "Tell me a joke {topic}"
# prompt_template = ChatPromptTemplate.from_template(template)

# print("------Prompt from Template ------")
# prompt = prompt_template.invoke({"topic":"cats"})
# print(prompt)



# Part 2: Prompt with Multiple PlaceHolders
# template_multiple = """ You are a helpfull assistant.
# Human: Tell me a {adjective} story about a {animal}.
# Assistant: """
# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({"adjectives": "funny", "animal":"cat"})
# print("\n ------ Prompt with Multiple Placeholders ------ \n")
# print(prompt)



# Part 3: Prompt with System and Human Messages (using tuples)
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human","Tell me {joke_count} jokes.")
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count":3})
print("---------- Prompt with System and Human Messages -------")
print(prompt)

# Following works:
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    HumanMessage(content="Tell me 3 jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers"})
print("---------- Prompt with System and Human Messages -------")
print(prompt)


# Following Does not work
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    HumanMessage(content="Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count":3})
print("---------- Prompt with System and Human Messages -------")
print(prompt)

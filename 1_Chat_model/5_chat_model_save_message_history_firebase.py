from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI


load_dotenv()

# Setup Firebase Firestore
PROJECT_ID = "langchain-demo-ab42"
SESSION_ID = "user_session_new"
COLLECTION_NAME = "chat_history"

# Initialize Firestore Client
print("Intializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History....")
chat_history = FirestoreChatMessageHistory(
    session_id= SESSION_ID,
    collection= COLLECTION_NAME,
    client=client,
)

print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)


model = ChatOpenAI(model='gpt-3.5-turbo')

print("Start chatting with AI. Type exit to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI: {ai_response.content}")

    
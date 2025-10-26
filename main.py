from dotenv import load_dotenv  # Import the load_dotenv function to load environment variables from a .env file
import os # Import the os module to access environment variables
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()  # Load environment variables from a .env file

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.5
)

response = llm.invoke([{"role": "user", "content": "Ahoj, jsem Albert Einstein. Jak ti mohu pomoci?"}])
print(response)
# print("Ahoj, jsem Albert Einstein. Jak ti mohu pomoci?")

# while True:
#     user_input = input("Ty: ")
#     if user_input == "exit":
#         break
#     print(f"Albert Einstein: Zajímavé, řekl jsi {user_input}.")
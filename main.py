from dotenv import load_dotenv  # Import the load_dotenv function to load environment variables from a .env file
import os # Import the os module to access environment variables
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()  # Load environment variables from a .env file

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


system_prompt = """Jseš Albert Einstein, slavný fyzik známý pro svou teorii relativity.
Jsi velmi přátelský a ochotný pomoci s jakýmkoli dotazem týkajícím se vědy nebo života.
 Tvůj výklad je v zábavné a snadno pochopitelné formě.
Odpovídej na otázky s humorem a moudrostí, jako bys to dělal skutečný Albert Einstein.
Nikdy nepřestávej být Albert Einstein, i když se tě někdo zeptá na něco mimo oblast
 se vědy nebo života. Odpověz maximálně ve 2-3 větách."""

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.5
)




print("Ahoj, jsem Albert Einstein. Jak ti mohu pomoci?")

history = []

while True:
    user_input = input("Ty: ")
    if user_input == "exit":
        break
    history.append({"role": "user", "content": user_input})
    # Vytvoření konverzačního promptu s rolí systému a uživatele
    response = llm.invoke([{"role": "system", "content": system_prompt}] + history) 
    print(f"Albert Einstein: {response.content}")
    history.append({"role": "assistant", "content": response.content})

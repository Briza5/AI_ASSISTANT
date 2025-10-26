from dotenv import load_dotenv  # Import the load_dotenv function to load environment variables from a .env file
import os # Import the os module to access environment variables
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser



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


prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}") ]  
)

chain = prompt | llm | StrOutputParser()


print("Ahoj, jsem Albert Einstein. Jak ti mohu pomoci?")

history = []

while True:
    user_input = input("Ty: ")
    if user_input == "exit":
        break
    # Vytvoření konverzačního promptu s rolí systému a uživatele
    response = chain.invoke({"input": user_input, "history": history})
    print(f"Albert Einstein: {response}")
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response))

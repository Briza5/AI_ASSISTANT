from dotenv import load_dotenv  # Import the load_dotenv function to load environment variables from a .env file
import os # Import the os module to access environment variables
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
import gradio as gr




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


# Define the chat function to handle user input and history
def chat(user_input, hist):
    print(user_input, hist)

    

    langchain_history = []
    for item in hist:
        if item['role'] == 'user':
            langchain_history.append(HumanMessage(content=item['content']))
        elif item['role'] == 'assistant':
            langchain_history.append(AIMessage(content=item['content']))

    response = chain.invoke({"input": user_input, "history": langchain_history})

    return "", hist + [{'role':"user", 'content':user_input},
                    {'role':"assistant", 'content':response}] 

def clear_chat():
    return "", []

page = gr.Blocks(
    title="Chat s Albertem Einsteinem",
    theme=gr.themes.Soft(),
)

with page:
    gr.Markdown(
        """
        # Chat s Albertem Einsteinem
        Vítejte u chatbota, který simuluje rozhovor s Albertem Einsteinem! Zeptejte se na cokoli týkající se vědy nebo života a získejte odpovědi plné humoru a moudrosti.

        """
    )

    chatbot = gr.Chatbot(type="messages",
                          avatar_images=[None, 'einstein.png'],
                          show_label=False)

    msg = gr.Textbox(show_label=False,
                     placeholder="Napište svou zprávu a stiskněte Enter...")

    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Vymazat historii", variant="secondary")
    clear.click(clear_chat, outputs=[msg, chatbot])



page.launch()
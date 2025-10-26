# 🧠 AI Chatbot s Albertem Einsteinem / Albert Einstein AI Chatbot

> **🇨🇿 Česká verze níže** | **🇬🇧 English version below**

---

## 🇨🇿 ČESKÁ VERZE

Interaktivní chatbot postavený na Google Gemini AI, který simuluje konverzaci se slavným fyzikem Albertem Einsteinem. Projekt využívá LangChain pro práci s AI a Gradio pro vytvoření moderního webového rozhraní.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-🦜-green.svg)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-blue.svg)

### 📋 Obsah
- [Vlastnosti](#-vlastnosti)
- [Rychlý start](#-rychlý-start)
- [Instalace](#-instalace)
- [Použití](#-použití)
- [Konfigurace](#️-konfigurace)
- [Struktura projektu](#-struktura-projektu)
- [Jak to funguje](#-jak-to-funguje)
- [Řešení problémů](#-řešení-problémů)
- [Licence](#-licence)

### ✨ Vlastnosti

- 🤖 **AI Powered** - Využívá Google Gemini 2.5 Flash model
- 💬 **Konverzační paměť** - Chatbot si pamatuje celou konverzaci
- 🎨 **Moderní UI** - Webové rozhraní vytvořené pomocí Gradio
- 🎭 **Roleplay** - AI se chová a odpovídá jako Albert Einstein
- ⚡ **Rychlé odpovědi** - Optimalizováno pro rychlou interakci
- 🔒 **Bezpečné** - API klíče uloženy mimo zdrojový kód
- 🖼️ **Vlastní avatary** - Podpora pro vlastní obrázky postav
- 🗑️ **Vymazání historie** - Jednoduché resetování konverzace

### 🚀 Rychlý start

```bash
# 1. Naklonuj repozitář
git clone https://github.com/Briza5/AI_ASSISTANT
cd AI_ASSISTANT

# 2. Nainstaluj závislosti
pip install -r requirements.txt

# 3. Vytvoř .env soubor a přidej svůj API klíč
echo "GEMINI_API_KEY=tvuj_api_klic_zde" > .env

# 4. (Volitelné) Přidej obrázek einstein.png do složky

# 5. Spusť aplikaci
python main.py
```

Aplikace se automaticky otevře v prohlížeči na adrese `http://127.0.0.1:7860`

### 📦 Instalace

#### Předpoklady

- Python 3.8 nebo vyšší
- pip (správce balíčků Pythonu)
- Google Gemini API klíč ([získej zde](https://ai.google.dev/))

#### Krok za krokem

1. **Naklonuj repozitář**

2. **Vytvoř virtuální prostředí (doporučeno)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Nainstaluj závislosti**
```bash
pip install -r requirements.txt
```

Obsah `requirements.txt`:
```
langchain-google-genai
langchain-core
python-dotenv
gradio
```

4. **Nastav API klíč**

Vytvoř soubor `.env` v kořenovém adresáři:
```env
GEMINI_API_KEY=tvuj_api_klic_zde
```

> **⚠️ Důležité:** Soubor `.env` obsahuje citlivé informace. Nikdy ho nenahrávej na GitHub! Je automaticky ignorován v `.gitignore`.

5. **Přidej avatar (volitelné)**

Pokud chceš vlastní avatar pro Einsteina, přidej obrázek `einstein.png` do hlavní složky projektu.

### 💻 Použití

#### Základní spuštění

```bash
python main.py
```

#### Co se stane:
1. Program se spustí a inicializuje AI model
2. Vytvoří se webové rozhraní pomocí Gradio
3. Automaticky se otevře prohlížeč
4. Můžeš začít chatovat s Albertem Einsteinem!

#### Ovládání aplikace:
- **Psaní zprávy:** Napiš text do pole a stiskni Enter nebo klikni na ikonu odeslání
- **Vymazání historie:** Klikni na tlačítko "Vymazat historii"
- **Ukončení:** Zavři okno prohlížeče nebo stiskni Ctrl+C v terminálu

### ⚙️ Konfigurace

#### Změna AI modelu

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # nebo "gemini-2.5-pro" pro lepší kvalitu
    google_api_key=GEMINI_API_KEY,
    temperature=0.5  # 0.0 = konzervativní, 1.0 = velmi kreativní
)
```

**Dostupné modely:**
- `gemini-2.5-flash` - Rychlejší, vhodný pro běžné použití
- `gemini-2.5-pro` - Kvalitnější odpovědi, pomalejší

#### Změna osobnosti chatbota

Uprav `system_prompt` v `main.py`:

```python
system_prompt = """Jsi Marie Curie, průkopnice v oblasti radioaktivity.
Jsi nadšená vědkyní, která ráda vysvětluje složité vědecké koncepty.
Odpovídej s vášní a nadšením pro vědu."""
```

#### Nastavení délky odpovědí

```python
# V system_prompt:
"Odpověz maximálně ve 2-3 větách."  # Krátké odpovědi
"Odpověz podrobně a vyčerpávajícím způsobem."  # Dlouhé odpovědi
```

#### Úprava vzhledu

```python
# Změna tématu Gradio
page = gr.Blocks(
    title="Tvůj vlastní název",
    theme=gr.themes.Soft(),  # nebo Base(), Glass(), Monochrome()
)

# Změna variant tlačítka
clear = gr.Button("Vymazat", variant="primary")  # nebo "secondary", "stop"
```

#### Vlastní avatar

```python
chatbot = gr.Chatbot(
    type="messages",
    avatar_images=[None, 'cesta/k/tvemu/obrazku.png'],
    # None = výchozí avatar pro uživatele
    # Druhý parametr = avatar pro AI
)
```

### 📁 Struktura projektu

```
einstein-chatbot/
│
├── main.py                 # Hlavní soubor aplikace
├── .env                    # API klíče (NEVKLÁDEJ DO GITU!)
├── .gitignore              # Ignorované soubory pro Git
├── requirements.txt        # Python závislosti
├── README.md              # Tento soubor
├── einstein.png           # (Volitelné) Avatar Einsteina
└── venv/                  # (Volitelné) Virtuální prostředí
```

### 🔍 Jak to funguje

#### Architektura

```
┌─────────────┐
│  Uživatel   │
│ (Prohlížeč) │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│   Gradio UI      │
│   • Chatbot      │
│   • Textbox      │
│   • Button       │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐      ┌─────────────┐
│ LangChain Chain  │◄────►│  Historie   │
│  • Prompt        │      │ (konverzace)│
│  • LLM           │      └─────────────┘
│  • Parser        │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  Google Gemini   │
│      API         │
└──────────────────┘
```

#### Flow dat

1. **Uživatel napíše zprávu** → Gradio zachytí událost
2. **Konverze formátu** → Historie se převede z Gradio formátu do LangChain formátu
3. **Vytvoření promptu** → Systémový prompt + historie + nová zpráva
4. **Volání AI** → Odeslání požadavku na Google Gemini API
5. **Zpracování odpovědi** → Parsování a extrakce textu
6. **Aktualizace UI** → Zobrazení odpovědi v chatbotu
7. **Uložení do historie** → Pro kontext v dalších otázkách

#### Klíčové komponenty

**LangChain Chain:**
```python
chain = prompt | llm | StrOutputParser()
```
- Operátor `|` propojuje komponenty
- Data "protékají" zleva doprava

**Konverze formátu historie:**
```python
# Gradio formát (slovníky)
[{'role': 'user', 'content': 'Ahoj'}]

# ↓ Konverze ↓

# LangChain formát (objekty)
[HumanMessage(content='Ahoj')]
```

**Event handling:**
```python
msg.submit(chat, [msg, chatbot], [msg, chatbot])
# Když uživatel odešle zprávu → zavolá se funkce chat
```

### 🐛 Řešení problémů

#### Chyba: "GEMINI_API_KEY není nastaven"

**Řešení:**
1. Zkontroluj, že existuje soubor `.env` v kořenovém adresáři
2. Zkontroluj formát v `.env`:
```
GEMINI_API_KEY=tvuj_klic_zde
```
(bez mezer kolem znaku `=`)

#### Chyba: "ModuleNotFoundError"

**Řešení:**
```bash
pip install -r requirements.txt
```

#### Avatar se nezobrazuje

**Řešení:**
1. Ujisti se, že `einstein.png` existuje ve stejné složce jako `main.py`
2. Zkus použít absolutní cestu:
```python
avatar_images=[None, '/absolutni/cesta/k/einstein.png']
```
3. Nebo použij URL obrázku:
```python
avatar_images=[None, 'https://example.com/einstein.png']
```

#### Pomalé odpovědi

**Možná řešení:**
1. Změň model na `gemini-2.5-flash` (rychlejší)
2. Zkrať `system_prompt`
3. Omez délku historie:
```python
recent_hist = hist[-10:]  # Pouze posledních 10 zpráv
```

#### API chyba 429 (Rate Limit)

**Řešení:**
- Počkej několik sekund mezi požadavky
- Zkontroluj limity svého API klíče na [Google AI Studio](https://ai.google.dev/)
- Pro production použití zvaž placený plán

### 🤝 Přispívání

Příspěvky jsou vítány! Pokud máš nápady na vylepšení:

1. Forkni projekt
2. Vytvoř feature branch (`git checkout -b feature/NovyFeature`)
3. Commitni změny (`git commit -m 'Přidána nová funkce'`)
4. Pushni do branch (`git push origin feature/NovyFeature`)
5. Otevři Pull Request

#### Nápady na vylepšení:
- [ ] Podpora pro více jazykových modelů
- [ ] Export konverzace do PDF/TXT
- [ ] Výběr z více historických osobností
- [ ] Podpora pro obrázky v konverzaci
- [ ] Hlasové vstupy a výstupy
- [ ] Databáze pro dlouhodobé ukládání konverzací

### 📝 Licence

Tento projekt je licencován pod MIT licencí - viz soubor LICENSE pro detaily.



### 🙏 Poděkování

- Google za Google Gemini API
- LangChain tým za skvělý framework
- Gradio tým za jednoduchou tvorbu UI
- Albert Einstein za inspiraci! 🧠

### 📚 Další zdroje

- [LangChain dokumentace](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [Gradio dokumentace](https://www.gradio.app/docs)
- [Prompt engineering guide](https://www.promptingguide.ai/)

---

## 🇬🇧 ENGLISH VERSION

An interactive chatbot built on Google Gemini AI that simulates a conversation with the famous physicist Albert Einstein. The project uses LangChain for AI operations and Gradio to create a modern web interface.

### 📋 Table of Contents
- [Features](#-features-1)
- [Quick Start](#-quick-start-1)
- [Installation](#-installation-1)
- [Usage](#-usage-1)
- [Configuration](#️-configuration-1)
- [Project Structure](#-project-structure-1)
- [How It Works](#-how-it-works-1)
- [Troubleshooting](#-troubleshooting-1)
- [License](#-license-1)

### ✨ Features

- 🤖 **AI Powered** - Uses Google Gemini 2.5 Flash model
- 💬 **Conversational Memory** - Chatbot remembers entire conversation
- 🎨 **Modern UI** - Web interface created with Gradio
- 🎭 **Roleplay** - AI behaves and responds as Albert Einstein
- ⚡ **Fast Responses** - Optimized for quick interaction
- 🔒 **Secure** - API keys stored outside source code
- 🖼️ **Custom Avatars** - Support for custom character images
- 🗑️ **Clear History** - Easy conversation reset

### 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Briza5/AI_ASSISTANT
cd AI_ASSISTANT


# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file and add your API key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# 4. (Optional) Add einstein.png image to folder

# 5. Run the application
python main.py
```

The application will automatically open in your browser at `http://127.0.0.1:7860`

### 📦 Installation

#### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key ([get it here](https://ai.google.dev/))

#### Step by Step

1. **Clone the repository**

2. **Create virtual environment (recommended)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

`requirements.txt` contents:
```
langchain-google-genai
langchain-core
python-dotenv
gradio
```

4. **Set up API key**

Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_api_key_here
```

> **⚠️ Important:** The `.env` file contains sensitive information. Never upload it to GitHub! It's automatically ignored in `.gitignore`.

5. **Add avatar (optional)**

If you want a custom avatar for Einstein, add an image named `einstein.png` to the main project folder.

### 💻 Usage

#### Basic Launch

```bash
python main.py
```

#### What Happens:
1. Program starts and initializes AI model
2. Web interface is created using Gradio
3. Browser opens automatically
4. You can start chatting with Albert Einstein!

#### Application Controls:
- **Writing a message:** Type text in the field and press Enter or click the send icon
- **Clear history:** Click the "Vymazat historii" (Clear History) button
- **Exit:** Close the browser window or press Ctrl+C in terminal

### ⚙️ Configuration

#### Change AI Model

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # or "gemini-2.5-pro" for better quality
    google_api_key=GEMINI_API_KEY,
    temperature=0.5  # 0.0 = conservative, 1.0 = very creative
)
```

**Available models:**
- `gemini-2.5-flash` - Faster, suitable for general use
- `gemini-2.5-pro` - Better quality responses, slower

#### Change Chatbot Personality

Edit `system_prompt` in `main.py`:

```python
system_prompt = """You are Marie Curie, a pioneer in radioactivity.
You are an enthusiastic scientist who loves explaining complex scientific concepts.
Respond with passion and enthusiasm for science."""
```

#### Set Response Length

```python
# In system_prompt:
"Respond in 2-3 sentences maximum."  # Short responses
"Respond in detail and comprehensively."  # Long responses
```

#### Customize Appearance

```python
# Change Gradio theme
page = gr.Blocks(
    title="Your Custom Title",
    theme=gr.themes.Soft(),  # or Base(), Glass(), Monochrome()
)

# Change button variant
clear = gr.Button("Clear", variant="primary")  # or "secondary", "stop"
```

#### Custom Avatar

```python
chatbot = gr.Chatbot(
    type="messages",
    avatar_images=[None, 'path/to/your/image.png'],
    # None = default avatar for user
    # Second parameter = avatar for AI
)
```

### 📁 Project Structure

```
einstein-chatbot/
│
├── main.py                 # Main application file
├── .env                    # API keys (DON'T COMMIT TO GIT!)
├── .gitignore              # Ignored files for Git
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── einstein.png           # (Optional) Einstein's avatar
└── venv/                  # (Optional) Virtual environment
```

### 🔍 How It Works

#### Architecture

```
┌─────────────┐
│    User     │
│  (Browser)  │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│   Gradio UI      │
│   • Chatbot      │
│   • Textbox      │
│   • Button       │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐      ┌─────────────┐
│ LangChain Chain  │◄────►│   History   │
│  • Prompt        │      │(conversation)│
│  • LLM           │      └─────────────┘
│  • Parser        │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  Google Gemini   │
│      API         │
└──────────────────┘
```

#### Data Flow

1. **User writes message** → Gradio captures event
2. **Format conversion** → History converted from Gradio to LangChain format
3. **Prompt creation** → System prompt + history + new message
4. **AI call** → Request sent to Google Gemini API
5. **Response processing** → Parsing and text extraction
6. **UI update** → Display response in chatbot
7. **Save to history** → For context in future questions

#### Key Components

**LangChain Chain:**
```python
chain = prompt | llm | StrOutputParser()
```
- The `|` operator connects components
- Data "flows" from left to right

**History format conversion:**
```python
# Gradio format (dictionaries)
[{'role': 'user', 'content': 'Hello'}]

# ↓ Conversion ↓

# LangChain format (objects)
[HumanMessage(content='Hello')]
```

**Event handling:**
```python
msg.submit(chat, [msg, chatbot], [msg, chatbot])
# When user submits message → calls chat function
```

### 🐛 Troubleshooting

#### Error: "GEMINI_API_KEY is not set"

**Solution:**
1. Check that `.env` file exists in root directory
2. Check format in `.env`:
```
GEMINI_API_KEY=your_key_here
```
(no spaces around `=`)

#### Error: "ModuleNotFoundError"

**Solution:**
```bash
pip install -r requirements.txt
```

#### Avatar not displaying

**Solution:**
1. Make sure `einstein.png` exists in same folder as `main.py`
2. Try using absolute path:
```python
avatar_images=[None, '/absolute/path/to/einstein.png']
```
3. Or use image URL:
```python
avatar_images=[None, 'https://example.com/einstein.png']
```

#### Slow responses

**Possible solutions:**
1. Change model to `gemini-2.5-flash` (faster)
2. Shorten `system_prompt`
3. Limit history length:
```python
recent_hist = hist[-10:]  # Only last 10 messages
```

#### API error 429 (Rate Limit)

**Solution:**
- Wait a few seconds between requests
- Check your API key limits at [Google AI Studio](https://ai.google.dev/)
- For production use, consider a paid plan

### 🤝 Contributing

Contributions are welcome! If you have ideas for improvements:

1. Fork the project
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open Pull Request

#### Ideas for improvements:
- [ ] Support for multiple language models
- [ ] Export conversation to PDF/TXT
- [ ] Selection from multiple historical figures
- [ ] Support for images in conversation
- [ ] Voice input and output
- [ ] Database for long-term conversation storage

### 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.


### 🙏 Acknowledgments

- Google for Google Gemini API
- LangChain team for the excellent framework
- Gradio team for easy UI creation
- Albert Einstein for inspiration! 🧠

### 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [Gradio Documentation](https://www.gradio.app/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

⭐ If you like this project, give it a star on GitHub!

**Made with ❤️ and AI**
# 🤖 OpenRouter AI Personality Chatbot

An interactive AI chatbot built using **Python, Streamlit, LangChain, and OpenRouter**. It allows users to interact with an AI assistant through three different personalities: Angry, Funny, and Sad.

## 🚀 Live Demo

**Live App:** [Try the AI Personality Chatbot](https://ai-personality-chatbotversion01basic-vah45fhuu9blj6prk5encd.streamlit.app/)

**GitHub Repository:** [AI Personality Chatbot](https://github.com/Ayush1216-maker/AI-Personality-Chatbot_Version_01_basic)

## ✨ Features

- 😡 **Angry Mode:** Get bold, angry, and short-tempered responses.
- 😂 **Funny Mode:** Enjoy jokes, humor, and playful conversations.
- 😢 **Sad Mode:** Chat with an AI that responds in a gloomy and empathetic style.
- 💬 **Interactive Chat Interface:** Communicate with the AI through a user-friendly web application.
- 🧠 **LLM Integration:** Generate responses using a language model accessed through OpenRouter.
- 🔗 **LangChain Integration:** Use LangChain to interact with the chat model and manage messages.
- 🎨 **Custom UI:** Modern interface with themed cards, gradients, and personality selection.
- ☁️ **Cloud Deployment:** Access the chatbot online using Streamlit Community Cloud.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| LangChain Core | Chat message handling |
| LangChain OpenRouter | Integration with OpenRouter models |
| OpenRouter API | Access to the configured language model |
| python-dotenv | Load environment variables locally |
| Git and GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Cloud deployment |

## 📂 Project Structure

```text
AI-Personality-Chatbot/
├── UIchatbot.py       # Streamlit web application
├── chatbot.py         # Console-based chatbot
├── requirements.txt   # Python dependencies
├── .gitignore         # Excluded files and secrets
└── README.md          # Project documentation
```

## ⚙️ Installation and Setup

Follow these steps to run the chatbot on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/Ayush1216-maker/AI-Personality-Chatbot_Version_01_basic.git
```

### 2. Navigate to the project directory

```bash
cd AI-Personality-Chatbot_Version_01_basic
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the API key

Create a `.env` file in the project root directory and add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Get an API key from [OpenRouter](https://openrouter.ai/keys).

**Security:** Never commit your `.env` file or expose your API key in public repositories.

### 6. Run the Streamlit application

```bash
streamlit run UIchatbot.py
```

Open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## 🧠 How It Works

1. The user selects a personality: Angry, Funny, or Sad.
2. The selected personality guides the AI's response style.
3. The user enters a message in the chat interface.
4. LangChain sends the conversation to the configured model through OpenRouter.
5. The generated response appears in the Streamlit application.

## 🔐 Environment Configuration

The application uses the following environment variable:

| Variable | Description |
|---|---|
| `OPENROUTER_API_KEY` | Authenticates requests to the OpenRouter API |

For Streamlit Community Cloud, configure this variable in the application's **Settings → Secrets** section rather than committing it to GitHub.

## ☁️ Deployment

This project is deployed using Streamlit Community Cloud.

To deploy your own version:

1. Push the project to GitHub.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create a new app and select your repository.
4. Set the main file path to `UIchatbot.py`.
5. Add `OPENROUTER_API_KEY` in the app's Secrets settings.
6. Deploy the application.

## 🔮 Future Improvements

- Add more AI personalities.
- Support conversation history and chat export.
- Add model selection and customizable response parameters.
- Improve API error handling and usage feedback.
- Implement rate limiting to control public API usage.

## 👨‍💻 Author

**Ayush Kohli**

B.Tech in Computer Science and Engineering

- **GitHub:** [Ayush1216-maker](https://github.com/Ayush1216-maker)
- **Live Project:** [Open AI Personality Chatbot](https://ai-personality-chatbotversion01basic-vah45fhuu9blj6prk5encd.streamlit.app/)

## 📄 License

This project is available for learning and portfolio purposes. Add an open-source license if you want to specify the terms under which others may use, modify, or distribute your code.

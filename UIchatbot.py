import streamlit as st
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

st.set_page_config(page_title="OpenRouter AI Chatbot", page_icon="🤖", layout="centered")

# ---------- Modes (same prompts as the console version) ----------
MODES = {
    "angry": {
        "label": "Angry",
        "emoji": "😡",
        "prompt": "You are an angry AI agent.",
        "c1": "#ff416c",
        "c2": "#ff8a00",
        "glow": "255, 65, 108",
        "tagline": "Short fuse. Loud opinions.",
    },
    "funny": {
        "label": "Funny",
        "emoji": "😂",
        "prompt": "You are a funny AI agent.",
        "c1": "#f7971e",
        "c2": "#ffd200",
        "glow": "255, 190, 30",
        "tagline": "Jokes, puns and good vibes.",
    },
    "sad": {
        "label": "Sad",
        "emoji": "😢",
        "prompt": "You are a sad AI agent.",
        "c1": "#4776e6",
        "c2": "#8e54e9",
        "glow": "100, 110, 240",
        "tagline": "Gloomy, but still here for you.",
    },
}

# ---------- Session state ----------
if "mode" not in st.session_state:
    st.session_state.mode = None
if "message" not in st.session_state:
    st.session_state.message = []


def start_mode(key: str):
    st.session_state.mode = key
    st.session_state.message = [SystemMessage(content=MODES[key]["prompt"])]


def reset_mode():
    st.session_state.mode = None
    st.session_state.message = []


@st.cache_resource
def get_model():
    return ChatOpenRouter(
        model="recursive/flint-v1.0:free",
        temperature=0.8,
        max_tokens=1024,
        timeout=20000,
        max_retries=0,
    )


# ---------- Theme colours ----------
cur = MODES.get(st.session_state.mode)
C1 = cur["c1"] if cur else "#8b5cf6"
C2 = cur["c2"] if cur else "#ec4899"
GLOW = cur["glow"] if cur else "168, 85, 247"

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp, .stMarkdown, button, input, textarea {
    font-family: 'Poppins', sans-serif !important;
}

/* ---------- Animated dark background ---------- */
.stApp {
    background: linear-gradient(-45deg, #0b0b1a, #14102b, #0d1b2a, #1a0b2e);
    background-size: 400% 400%;
    animation: bgShift 18s ease infinite;
    color: #e8e8f5;
}
@keyframes bgShift {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.stApp::before, .stApp::after {
    content: "";
    position: fixed;
    width: 420px; height: 420px;
    border-radius: 50%;
    filter: blur(110px);
    opacity: 0.30;
    z-index: 0;
    pointer-events: none;
}
.stApp::before {background: __C1__; top: -120px; left: -120px; animation: float1 12s ease-in-out infinite;}
.stApp::after {background: __C2__; bottom: -140px; right: -120px; animation: float2 14s ease-in-out infinite;}
@keyframes float1 {0%,100% {transform: translate(0,0);} 50% {transform: translate(80px, 60px);}}
@keyframes float2 {0%,100% {transform: translate(0,0);} 50% {transform: translate(-80px, -60px);}}

header[data-testid="stHeader"] {background: transparent;}
#MainMenu, footer {visibility: hidden;}
.block-container {max-width: 860px; padding-top: 2rem; position: relative; z-index: 1;}

p, li, span, label, h1, h2, h3, h4, .stMarkdown {color: #e8e8f5;}

/* ---------- Hero ---------- */
.hero {
    position: relative;
    overflow: hidden;
    text-align: center;
    padding: 2.2rem 1.5rem 1.8rem 1.5rem;
    border-radius: 28px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    box-shadow: 0 0 60px rgba(__GLOW__, 0.25), inset 0 0 0 1px rgba(255,255,255,0.04);
    margin-bottom: 1.6rem;
}
.hero::before {
    content: "";
    position: absolute; inset: -2px;
    background: conic-gradient(from 0deg, __C1__, __C2__, __C1__);
    opacity: 0.10;
    animation: spin 10s linear infinite;
    z-index: 0;
}
@keyframes spin {to {transform: rotate(360deg);}}
.hero > * {position: relative; z-index: 1;}
.hero .logo {
    font-size: 3.4rem;
    display: inline-block;
    animation: bob 3s ease-in-out infinite;
    filter: drop-shadow(0 6px 18px rgba(__GLOW__, 0.7));
}
@keyframes bob {0%,100% {transform: translateY(0) rotate(-4deg);} 50% {transform: translateY(-10px) rotate(4deg);}}
.hero h1 {
    margin: 0.3rem 0 0 0;
    font-size: 2.5rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    background: linear-gradient(90deg, __C1__, __C2__, #ffffff, __C1__);
    background-size: 300% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 6s linear infinite;
}
@keyframes shine {to {background-position: 300% 0;}}
.hero p {margin: 0.4rem 0 0 0; color: #b8b8d6; font-size: 1.02rem;}

.badge {
    display: inline-block;
    margin-top: 1rem;
    padding: 0.4rem 1.1rem;
    border-radius: 999px;
    font-weight: 700;
    font-size: 0.9rem;
    color: #fff;
    background: linear-gradient(90deg, __C1__, __C2__);
    box-shadow: 0 0 22px rgba(__GLOW__, 0.65);
    animation: pulse 2.2s ease-in-out infinite;
}
@keyframes pulse {
    0%,100% {box-shadow: 0 0 14px rgba(__GLOW__, 0.45);}
    50% {box-shadow: 0 0 30px rgba(__GLOW__, 0.95);}
}

/* ---------- Mode cards ---------- */
.mode-card {
    text-align: center;
    padding: 1.6rem 0.8rem 1.2rem 0.8rem;
    border-radius: 22px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.14);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    margin-bottom: 0.7rem;
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    cursor: default;
}
.mode-card:hover {
    transform: translateY(-8px) scale(1.03);
}
.mode-card .emoji {font-size: 3.4rem; display: inline-block; transition: transform .3s ease;}
.mode-card:hover .emoji {transform: scale(1.25) rotate(-8deg);}
.mode-card .title {font-size: 1.2rem; font-weight: 700; margin-top: 0.4rem; color: #fff;}
.mode-card .tag {font-size: 0.82rem; color: #b8b8d6; margin-top: 0.2rem;}

.card-angry {box-shadow: 0 10px 32px rgba(255,65,108,0.22);}
.card-angry:hover {box-shadow: 0 16px 44px rgba(255,65,108,0.55); border-color: #ff416c;}
.card-funny {box-shadow: 0 10px 32px rgba(255,190,30,0.20);}
.card-funny:hover {box-shadow: 0 16px 44px rgba(255,190,30,0.55); border-color: #f7b71e;}
.card-sad {box-shadow: 0 10px 32px rgba(100,110,240,0.22);}
.card-sad:hover {box-shadow: 0 16px 44px rgba(100,110,240,0.55); border-color: #6f6ef0;}

/* ---------- Buttons ---------- */
.stButton > button {
    width: 100%;
    border: none;
    border-radius: 14px;
    padding: 0.6rem 1rem;
    font-weight: 700;
    color: #fff;
    background: linear-gradient(90deg, __C1__, __C2__);
    box-shadow: 0 6px 20px rgba(__GLOW__, 0.35);
    transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
}
.stButton > button:hover {
    transform: translateY(-2px);
    filter: brightness(1.12);
    box-shadow: 0 10px 28px rgba(__GLOW__, 0.65);
    color: #fff;
}
.stButton > button:active {transform: translateY(0) scale(0.98);}

/* Per-card button colours on the start screen */
div[data-testid="stColumn"]:nth-of-type(1) .stButton > button,
div[data-testid="column"]:nth-of-type(1) .stButton > button {
    background: linear-gradient(90deg, #ff416c, #ff8a00); box-shadow: 0 6px 20px rgba(255,65,108,0.40);
}
div[data-testid="stColumn"]:nth-of-type(2) .stButton > button,
div[data-testid="column"]:nth-of-type(2) .stButton > button {
    background: linear-gradient(90deg, #f7971e, #ffd200); box-shadow: 0 6px 20px rgba(255,190,30,0.40); color: #2a1f00;
}
div[data-testid="stColumn"]:nth-of-type(3) .stButton > button,
div[data-testid="column"]:nth-of-type(3) .stButton > button {
    background: linear-gradient(90deg, #4776e6, #8e54e9); box-shadow: 0 6px 20px rgba(100,110,240,0.40);
}

/* ---------- Chat bubbles ---------- */
[data-testid="stChatMessage"] {
    border-radius: 20px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.9rem;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.10);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    animation: pop .35s ease;
}
@keyframes pop {from {opacity: 0; transform: translateY(12px) scale(.98);} to {opacity: 1; transform: none;}}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    background: linear-gradient(135deg, rgba(__GLOW__, 0.35), rgba(255,255,255,0.06));
    border: 1px solid rgba(__GLOW__, 0.55);
    box-shadow: 0 6px 24px rgba(__GLOW__, 0.20);
}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
    border-left: 4px solid __C1__;
    box-shadow: 0 6px 24px rgba(0,0,0,0.25);
}
[data-testid="stChatMessage"] p {color: #f1f1fb; line-height: 1.65;}

/* ---------- Typing dots ---------- */
.dots span {
    display: inline-block; width: 9px; height: 9px; margin-right: 5px;
    border-radius: 50%;
    background: linear-gradient(90deg, __C1__, __C2__);
    animation: blink 1.2s infinite ease-in-out;
}
.dots span:nth-child(2) {animation-delay: .2s;}
.dots span:nth-child(3) {animation-delay: .4s;}
@keyframes blink {0%,80%,100% {transform: scale(.5); opacity: .4;} 40% {transform: scale(1.2); opacity: 1;}}

/* ---------- Chat input ---------- */
[data-testid="stChatInput"] {
    border-radius: 18px;
    background: rgba(255,255,255,0.07);
    border: 2px solid __C1__;
    box-shadow: 0 0 26px rgba(__GLOW__, 0.40);
}
[data-testid="stChatInput"] > div,
[data-testid="stChatInput"] div[data-baseweb="textarea"],
[data-testid="stChatInput"] div[data-baseweb="base-input"] {
    background: rgba(18, 18, 40, 0.95) !important;
    border-radius: 16px !important;
}
[data-testid="stChatInput"] textarea,
[data-testid="stChatInputTextArea"] {
    background: transparent !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    caret-color: #ffffff !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: #a9a9c8 !important;
    -webkit-text-fill-color: #a9a9c8 !important;
}
[data-testid="stBottom"], [data-testid="stBottom"] > div {background: transparent;}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background: rgba(12,12,28,0.85);
    backdrop-filter: blur(16px);
    border-right: 1px solid rgba(255,255,255,0.10);
}
.side-card {
    text-align: center;
    padding: 1.2rem 0.8rem;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(__GLOW__, 0.30), rgba(255,255,255,0.04));
    border: 1px solid rgba(__GLOW__, 0.55);
    box-shadow: 0 0 24px rgba(__GLOW__, 0.30);
    margin-bottom: 1rem;
}
.side-card .emoji {font-size: 3rem; display: inline-block; animation: bob 3s ease-in-out infinite;}
.side-card .name {font-weight: 700; font-size: 1.1rem; color: #fff;}
.side-card .tag {font-size: 0.8rem; color: #c3c3e0;}

hr {border-color: rgba(255,255,255,0.12);}
</style>
"""

CSS = (
    CSS.replace("__C1__", C1)
    .replace("__C2__", C2)
    .replace("__GLOW__", GLOW)
)
st.markdown(CSS, unsafe_allow_html=True)

# ---------- Mode selection screen ----------
if st.session_state.mode is None:
    st.markdown(
        """
        <div class="hero">
            <div class="logo">🤖</div>
            <h1>OpenRouter AI Chatbot</h1>
            <p>Pick a personality and start chatting ✨</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3, gap="medium")
    for col, (key, m) in zip(cols, MODES.items()):
        with col:
            st.markdown(
                f"""
                <div class="mode-card card-{key}">
                    <div class="emoji">{m['emoji']}</div>
                    <div class="title">{m['label']} Mode</div>
                    <div class="tag">{m['tagline']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.button(
                f"Choose {m['label']}",
                key=f"choose_{key}",
                use_container_width=True,
                on_click=start_mode,
                args=(key,),
            )
    st.stop()

# ---------- Chat screen ----------
mode = MODES[st.session_state.mode]
model = get_model()
message = st.session_state.message

with st.sidebar:
    st.markdown(
        f"""
        <div class="side-card">
            <div class="emoji">{mode['emoji']}</div>
            <div class="name">{mode['label']} Mode</div>
            <div class="tag">{mode['tagline']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.button("🔄 Change mode", use_container_width=True, on_click=reset_mode)

st.markdown(
    f"""
    <div class="hero">
        <div class="logo">{mode['emoji']}</div>
        <h1>OpenRouter AI Chatbot</h1>
        <p>Say something and let's chat!</p>
        <span class="badge">{mode['emoji']} {mode['label']} mode active</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# Render chat history (skip the system message)
for msg in message:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="🧑"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar=mode["emoji"]):
            st.markdown(msg.content)

prompt = st.chat_input("Type your message...")

if prompt and prompt.strip():
    prompt = prompt.strip()
    message.append(HumanMessage(content=prompt))

    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=mode["emoji"]):
        placeholder = st.empty()
        placeholder.markdown(
            '<div class="dots"><span></span><span></span><span></span></div>',
            unsafe_allow_html=True,
        )
        response_text = ""

        try:
            for chunk in model.stream(message):
                if isinstance(chunk.content, str):
                    text = chunk.content
                elif isinstance(chunk.content, list):
                    text = "".join(
                        block.get("text", "")
                        for block in chunk.content
                        if isinstance(block, dict) and block.get("type") == "text"
                    )
                else:
                    text = ""

                response_text += text
                if response_text:
                    placeholder.markdown(response_text + "▌")

            if response_text:
                placeholder.markdown(response_text)
                message.append(AIMessage(content=response_text))
            else:
                placeholder.markdown("_[The model returned no text.]_")
                message.pop()

        except Exception as e:
            message.pop()
            placeholder.error(f"Error: {e}")
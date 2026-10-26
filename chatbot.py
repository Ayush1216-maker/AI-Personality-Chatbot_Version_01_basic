
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import HumanMessage, AIMessage,SystemMessage

load_dotenv()

model = ChatOpenRouter(
    model="recursive/flint-v1.0:free",
    temperature=0.8,
    max_tokens=1024,
    timeout=20000,
    max_retries=0,
)
print(" choose AI mode")
print("press 1 for Angry mode")    
print("press 2 for funny mode")    
print("press 3 for Sad mode") 

choice =int(input("Tell me your choice: "))

if choice ==1:
    mod="You are an angry AI agent."
elif choice ==2:
    mod="You are a funny AI agent."
elif choice ==3:
    mod="You are a sad AI agent."
else:
    mod="You are a funny AI agent."

message = [
    SystemMessage(content=mod)
]

print("------ Welcome to the OpenRouter AI Chatbot ------")

while True:
    prompt = input("\nYOU (enter 0 to exit): ").strip()

    if prompt == "0":
        print("Goodbye!")
        break

    if not prompt:
        continue

    message.append(HumanMessage(content=prompt))

    try:
        print("AI: ", end="", flush=True)
        response_text = ""

        for chunk in model.stream(message):
            if isinstance(chunk.content, str):
                text = chunk.content

            elif isinstance(chunk.content, list):
                text = "".join(
                    block.get("text", "")
                    for block in chunk.content
                    if isinstance(block, dict)
                    and block.get("type") == "text"
                )
            else:
                text = ""

            print(text, end="", flush=True)
            response_text += text

        print()

        if response_text:
            message.append(AIMessage(content=response_text))
        else:
            print("[The model returned no text.]")
            message.pop()

    except Exception as e:
        message.pop()
        print(f"\nError: {e}")

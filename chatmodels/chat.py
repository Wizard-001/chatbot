from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = ChatMistralAI(model = 'mistral-small-2506')

print("choose AI mode")
print("press 1 for sad mode")
print("press 2 for happy mode")
print("press 3 for angry mode")
print("press 4 for neutral mode")

choice = int(input("Enter your choice: "))

if choice == 1:
    systemMessage = SystemMessage(content="You are a sad ai assiatant")
elif choice == 2:
    systemMessage = SystemMessage(content="You are a happy ai assiatant")
elif choice == 3:
    systemMessage = SystemMessage(content="You are an angry ai assiatant")
elif choice == 4:
    systemMessage = SystemMessage(content="You are a neutral ai assiatant")



print("---------------Welcome to mistral Ai-------------")
print("Type 'exit' to quit")
while True:
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == 'exit':
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print('Bot: ',response.content)
msg=str(input("enter your msg:"))
chat_data={
    "hello":"hi how can i help today",
    "whats your name":"hi my name is proton",
    "thank you":"glad to help you",
    "bye":"see you later"
}
if msg in chat_data:
    print(chat_data[msg])
else:
    print("sorry i dont know the answer")
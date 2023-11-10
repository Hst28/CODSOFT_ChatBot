import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you', ["I'm just a computer program, so I don't have feelings, but I'm here to help!"]],
    ['what is your name', ["You can call me SIGAI."]],
    ['introduce your self', ["I'm a chatbot created by Harsh."]],
    ['bye|goodbye', ['Goodbye!', 'See you later!','Goodbye! Feel free to come back if you have more questions.']],
    ['(.*)', ["I'm not sure I understand.", "Can you please rephrase that?"]],
]

chatbot = Chat(pairs, reflections)
def send_message():
    user_input = entry.get()
    if user_input.lower() == 'exit':
        chat_display.insert(tk.END, "Chatbot: Goodbye!\n")
        entry.delete(0, tk.END)
    else:
        response = chatbot.respond(user_input)
        chat_display.insert(tk.END, f"You: {user_input}\n")
        chat_display.insert(tk.END, f"Chatbot: {response}\n")
        entry.delete(0, tk.END)

window = tk.Tk()
window.title("Chatbot GUI")

chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=30)
chat_display.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

entry = tk.Entry(window, width=50)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()








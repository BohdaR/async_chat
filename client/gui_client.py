import json
import os
import socket
from tkinter import *


if os.path.exists('settings.json'):
    with open('settings.json', 'r') as file:
        data = json.load(file)
        user = data['user_name']


else:
    with open('settings.json', 'w', ) as file:
        data = {'user_name': input('Enter your name: ')}
        json.dump(data, file, indent=4, ensure_ascii=False)
        user = data['user_name']

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
client.send(user.encode())


def send_massage():
    recipient = recipient_field.get()
    massage_text = message_field.get()

    massage = f'{recipient} {massage_text}'
    message_field.delete(0, 'end')

    client.send(massage.encode())


root = Tk()

root.title('My app')
root['bg'] = '#8b00ff'
root.geometry('600x500')

frame = Frame(root, bg='white')
frame.grid(row=1, column=3)

recipient_field = Entry(frame)
recipient_field.grid(row=0, column=0)

message_field = Entry(frame)
message_field.grid(row=0, column=1)

send_btn = Button(frame, text='Some text', bg='blue', command=send_massage)
send_btn.grid(row=0, column=2)


if __name__ == '__main__':
    root.mainloop()

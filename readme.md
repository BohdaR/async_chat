# This is simple socket chat.

To run on Ubuntu you need to install the following packages.
```bash
sudo apt install python3, python3-tk
```
Then you need to start server.
```bash
python3 server/chat_server.py 
```
By default server is running at localhost:8000. You can use nc to test the server.

```bash
nc 127.0.0.1 8000
```
After starting nc, you need to specify the name without spaces in the first message, like the following below:
```bash
user@userPC:~$ nc 127.0.0.1 8000
Someone
```

In the terminal tab in which you started the server, you should see the following below:
```bash
user@userPC:~$ python3 server/chat_server.py 

[STARTED] - Server is running on 127.0.0.1:8000

[INFO] - Someone connected

[INFO] - Someone disconnected
```
You need to add another clients to send messages.
After that. You'll be able to send messages between connected clients.
To send a message to another client, you need to enter the username and message followed by a space.
```bash
user@userPC:~$ nc 127.0.0.1 8000
Someone
Someone2 Hello.
```
Someone2 will see it this way:
```bash
user@userPC:~$ nc 127.0.0.1 8000
Someone2
Someone > Hello.
```


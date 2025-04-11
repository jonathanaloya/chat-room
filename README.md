# Overview

This project is a simple real-time chat application that demonstrates basic network communication using Python. As a software engineer, I created this project to deepen my understanding of sockets, multithreading, and message broadcasting in a networked environment. The goal was to build a reliable and interactive communication tool that supports multiple users connecting to a central server.

The program uses a client-server architecture. The server listens for incoming client connections, and each client can send and receive messages in real time. Clients are asked to choose a nickname upon connecting, which is used to identify messages in the chat.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Networking chatroom tutorial](https://youtu.be/ahGN_czf8r4)

# Network Communication

This project uses a client/server architecture. A central server handles all connections, and clients connect to it to send and receive messages.

Protocol: TCP is used to ensure reliable communication.

Port: Communication happens over port 58000.

Message Format: Messages are sent as UTF-8 encoded strings. Each message includes the alias of the sender followed by their message (e.g., John: Hello everyone!).

The server also handles nickname registration at connection time and broadcasts system messages when users join or leave the chat.

# Development Environment

Programming Language: Python 

Libraries Used:

socket for network communication

threading for handling multiple clients simultaneously

The software was developed and tested using a basic Python environment. No external libraries are required beyond Python’s standard library.


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python.org](https://docs.python.org/3/howto/sockets.html)
* [Real Python](https://realpython.com/python-sockets/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Add timestamp to each message for better context

* Implement private messaging between users

* Create a graphical user interface (GUI) using tkinter or another Python GUI framework

* Add user authentication and message history logging

* Handle unexpected disconnections more gracefully and notify other users
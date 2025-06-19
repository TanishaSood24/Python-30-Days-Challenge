import requests
from bs4 import BeautifulSoup

# Step 1: Set the URL
url = "https://www.python.org"

# Step 2: Send HTTP GET request
response = requests.get(url)

# Step 3: Check the response status
if response.status_code == 200:
    print("✅ Request successful!")

    # Step 4: Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 5: Print page title
    print("🔹 Page Title:", soup.title.string.strip())

    # Step 6: Display first 300 characters of the page content
    print("\n🔹 First 300 characters of page content:")
    print(soup.prettify()[:300])
else:
    print("❌ Failed to fetch page. Status code:", response.status_code)
























# import requests
#
# # Step 1: Use a valid URL (example: Python's official website)
# url = "https://www.python.org"
#
# # Step 2: Make a GET request
# response = requests.get(url)
#
# # Step 3: Display the content
# print("Status Code:", response.status_code)  # Should be 200 if successful
# print("Webpage Content:\n")
# print(response.text)  # This prints the HTML content of the page

#
# ✅ First, Common Concepts Used in Both
# Term	Meaning
# socket	A Python module to create network connections.
# socket.socket()	Creates a socket object. Think of it as a phone.
# AF_INET	Tells Python you're using IPv4 addresses (like 127.0.0.1).
# SOCK_STREAM	Means you're using TCP (reliable, ordered communication).
# threading	Allows the program to run send and receive functions at the same time.
# recv()	Receives data from the other person.
# send()	Sends data to the other person.
# bind()	Binds the server to a specific IP and port.
# connect()	The client connects to a server at a given IP and port.
# flush=True	Immediately prints the prompt without waiting.
# sys.stdout.write(...)	Used to overwrite the input line and avoid message overlap.
# daemon=True	Ensures thread closes when the main program exits.
#
# 🖥️ Server Code (chat_server.py) — Line-by-Line Explanation
# python
# Copy
# Edit
# import socket
# import threading
# import sys
# Imports required libraries: socket for networking, threading for parallel tasks, sys for output formatting.
#
# python
# Copy
# Edit
# def receive_messages(client_socket):
# Defines a function to receive messages from the connected client.
#
# python
# Copy
# Edit
#     while True:
#         try:
#             message = client_socket.recv(1024).decode()
# Continuously receives 1024 bytes from the client, then decodes it from bytes to string.
#
# python
# Copy
# Edit
#             if message:
#                 sys.stdout.write("\r" + " " * 50 + "\r")
#                 print(f"Client: {message}")
#                 print("You: ", end="", flush=True)
# Clears the input line (\r), prints the received message, and brings back the input prompt.
#
# python
# Copy
# Edit
#         except:
#             break
# If any error occurs (e.g., client disconnects), break the loop.
#
# python
# Copy
# Edit
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.bind(('localhost', 5566))
# server_socket.listen(1)
# Creates the server socket.
#
# Enables port reuse (so you don’t get "port in use" errors).
#
# Binds the server to your machine (localhost) and port 5566.
#
# Starts listening for 1 client.
#
# python
# Copy
# Edit
# print("Server is waiting for a connection on port 5566...")
# client_socket, addr = server_socket.accept()
# Prints a waiting message.
#
# Accepts a connection from the client and returns a new socket client_socket for communication.
#
# python
# Copy
# Edit
# threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
# Starts a new thread that runs the receive_messages() function, so we can receive messages while sending them too.
#
# python
# Copy
# Edit
# while True:
#     msg = input("You: ")
#     client_socket.send(msg.encode())
# Main thread asks the server user for input and sends it to the client.
#
# 💻 Client Code (chat_client.py) — Similar Logic
# Only difference:
#
# python
# Copy
# Edit
# client_socket.connect(('localhost', 5566))
# Instead of bind() and listen(), the client connects to the server running on localhost and port 5566.
#
# Everything else — receive_messages(), input(), send(), and threading — works similarly.
#
# 📌 Summary Table
# Component	Server	Client
# Connection setup	bind(), listen(), accept()	connect()
# Send/Receive	send(), recv()	send(), recv()
# Threads	threading.Thread(...)	threading.Thread(...)
# Purpose	Waits for client, handles input	Connects to server, sends input
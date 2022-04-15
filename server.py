import random
import socket
import sys
from time import sleep


def server():
    host = "127.0.0.1"
    port = int(sys.argv[1])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    number_of_bots = 0
    bots = []
    print("Server initiated with: ")
    print("HOST: ", host)
    print("PORT: ", port)

    while number_of_bots < 4:
        print("Connect at least 4 bots.. " + str(4 - number_of_bots) + " more connections remaining..")
        print("Waiting for bots to connect...")
        connection, address = server_socket.accept()
        print("Connected to: " + str(address[0]) + " " + str(address[1]))
        bots.append(connection)
        number_of_bots += 1

    while True:
        activity_suggestion = input("Suggest an activity(Example: Code, Jump) or 'exit' to quit: ")
        if activity_suggestion == "exit":
            for bot in bots:
                bot.send("exit".encode())
                sleep(1)
            print("Connection to bots terminated")
            break
        message_options = ["Does anyone want to go {}?", "Who wants to {}!?", "{}?? LETS GO!", "Down for some {}?"]
        message = random.choice(message_options)
        message_to_client = activity_suggestion + " " + message.format(activity_suggestion + "ing")
        print(message_to_client.split(' ', 1)[1])  # removes activity-identifier-word
        for bot in bots:
            bot.send(message_to_client.encode())
            sleep(1)
            incoming_message = bot.recv(1024).decode()
            print(incoming_message)


if __name__ == "__main__":
    server()

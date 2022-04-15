import random
import socket
import sys


def john(a):
    positive = bool(random.getrandbits(1))
    positive_responses = ["Great stuff! I really like {}!", "{} is my favourite activity, lets go!",
                          "Absolutely, I really want to go {}", "Aww, I thought you would never ask! Lets start {}!"]
    negative_responses = ["What? Please I don't want to go {}", "No! Please god, NO! I hate {}", "Eww.. {}?!!"]
    if positive:
        response = "John: " + random.choice(positive_responses)
    else:
        response = "John: " + random.choice(negative_responses)

    return response.format(a + "ing")


def michael(a):
    positive = bool(random.getrandbits(1))
    positive_responses = ["Great stuff! I really like {}!", "{} is my favourite activity, lets go!",
                          "Absolutely, I really want to go {}", "Aww, I thought you would never ask! Lets start {}!"]
    negative_responses = ["What? Please I don't want to go {}", "No! Please god, NO! I hate {}", "Eww.. {}?!!"]
    if positive:
        response = "Michael: " + random.choice(positive_responses)
    else:
        response = "Michael: " + random.choice(negative_responses)

    return response.format(a + "ing")


def linda(a):
    positive = bool(random.getrandbits(1))
    positive_responses = ["Great stuff! I really like {}!", "{} is my favourite activity, lets go!",
                          "Absolutely, I really want to go {}", "Aww, I thought you would never ask! Lets start {}!"]
    negative_responses = ["What? Please I don't want to go {}", "No! Please god, NO! I hate {}", "Eww.. {}?!!"]
    if positive:
        response = "Linda: " + random.choice(positive_responses)
    else:
        response = "Linda: " + random.choice(negative_responses)

    return response.format(a + "ing")


def karen(a):
    positive = bool(random.getrandbits(1))
    positive_responses = ["Great stuff! I really like {}!", "{} is my favourite activity, lets go!",
                          "Absolutely, I really want to go {}", "Aww, I thought you would never ask! Lets start {}!"]
    negative_responses = ["What? Please I don't want to go {}", "No! Please god, NO! I hate {}", "Eww.. {}?!!"]
    if positive:
        response = "Karen: " + random.choice(positive_responses)
    else:
        response = "Karen: " + random.choice(negative_responses)

    return response.format(a + "ing")


def client():
    arguments = sys.argv
    host = arguments[1]
    port = int(arguments[2])
    bot = arguments[3]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to " + host + str(port) + " as " + bot)

    while True:
        raw_incoming_message = client_socket.recv(1024)
        decoded_incoming_message = raw_incoming_message.decode()
        incoming_message_identifier = decoded_incoming_message.split()[0]
        response = ""
        if incoming_message_identifier == "exit":
            print("You have exited the connection!")
            break
        else:
            suggestion = incoming_message_identifier
            match bot:
                case 'john':
                    response = john(suggestion)
                case "michael":
                    response = michael(suggestion)
                case "linda":
                    response = linda(suggestion)
                case "karen":
                    response = karen(suggestion)
            print(response)
            client_socket.send(response.encode())


if __name__ == "__main__":
    client()

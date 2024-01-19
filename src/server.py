import socket
from threading import Thread
from cards import cards
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 5555))
clients = []
server.listen(4)
game_start = False
print("listening for connection")

def process_client_messages(clnt):

    clients.append(clnt)
    clnt.sendall(f"id {len(clients)}".encode())

    dealt_cards = ""
    print(len(cards))
    for i in range(13):
        card = random.choice(list(cards.keys()))
        del cards[card]
        dealt_cards = dealt_cards + card + " "
    clnt.sendall(f"dealt_cards {dealt_cards}".encode())

    while True:
        try:
            data = clnt.recv(2 ** 11)
            reply = data.decode()
            if not data:
                break
            else:
                for client in clients:
                    if client != clnt:
                        client.sendall(bytes(reply, "utf-8"))
        except:
            break

    print(f"{clnt} disconnected")
    clients.remove(clnt)
    for i, client in enumerate(clients):
        client.sendall(f"id {i+1}".encode())
    clnt.close()

while True:
    try:
        clnt, addr = server.accept()
        ip = addr[0]
        print(f"Connected to {ip}")
        Thread(target=process_client_messages, args=(clnt,)).start()
    except ConnectionAbortedError:
        break
    
print("Couldn't establish connection")

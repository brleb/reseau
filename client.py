#!/usr/bin/python3

from grid import *
from macro import *

import sys
import socket
import select
import pickle

def handle(tmp, server) :

    code = tmp[0]

    if (code == WELCOME) :
        print("Bienvenue sur le jeu du morpion version aveugle.")

    if (code == START) :
        print("En attente d'un adversaire !")

    if (code == PLAY) :
        grille = tmp[1]
        grille.display()
        print("Quelle case voulez-vous jouer ?")
        print("Entrez un entier allant de 0 à 8")
        caseAJouer = input()
        server.send(bytes(str(caseAJouer).encode('utf')))
        print("Vous avez joué la case " + caseAJouer)

    if (code == ERROR) :
        print("Cette case a déjà été jouée, elle a été révélée.")

    if (code == GRID) :
        grille = tmp[1]
        grille.display()

    if (code == WIN) :
        print("Vous avez gagné.")

    if (code == LOSE) :
        print("Vous avez perdu.")

    if (code == DRAW) :
        print("Egalité.")

    if (code == END) :
        print("Parti terminée.")

host = "::1"
port = int(sys.argv[1])

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0, None)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((host, port))
s.setblocking(True)
print("Connexion au port " + str(7777))

while True :
    clients, _ , _ = select.select([s], [], [])
    for sock in clients :
        msg = sock.recv(1024)
        tmp = pickle.loads(msg)
        handle(tmp, sock)

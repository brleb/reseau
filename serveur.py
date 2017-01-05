#!/usr/bin/python3

import socket
import select
import threading
import sys
import pickle
import time

from macro import *
from main import main
from grid import *

listeSocket = []
listeJoueur = []
listeSpec   = []

serverSocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0, None)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(('', 7777))
serverSocket.listen(1)
listeSocket.append(serverSocket)

nbJoueur = 0

print("Lancement du serveur sur le port 7777")
print("En attente de joueurs")
while(1):
    clients, _ , _ = select.select(listeSocket, [], [])
    for i in clients:
        if (i == serverSocket):
            new_socket, adresse = serverSocket.accept()
            listeSocket.append(new_socket)
            nbJoueur = nbJoueur + 1
            print("Clients connectés : " + str(nbJoueur))

        if (len(listeJoueur) < 2) :
            listeJoueur.append(new_socket)

        if (len(listeJoueur) > 2) :
            listeSpec.append(new_socket)

        if (len(listeJoueur) == 2) :
            print("La partie va commencer")
            main(listeJoueur)
            time.sleep(1)
            serverSocket.close()

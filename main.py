#!/usr/bin/python3

from grid import *
from macro import *

def main(listeJoueur):

    grids = [grid(), grid(), grid()]
    current_player = J1

    for i in listeJoueur :
        i.send(MSG_START)

    while grids[0].gameOver() == -1 :

        if current_player == J1 :
            caseAJouer = -1
            while caseAJouer <0 or caseAJouer >=NB_CELLS:
                tosend = pickle.dumps([PLAY, grids[current_player]])
                listeJoueur[current_player-1].send(tosend)
                caseAJouer = int(listeJoueur[J1-1].recv(1024))

        if current_player == J2 :
            caseAJouer = -1
            while caseAJouer <0 or caseAJouer >=NB_CELLS:
                tosend = pickle.dumps([PLAY, grids[current_player]])
                listeJoueur[current_player-1].send(tosend)
                caseAJouer = int(listeJoueur[J2-1].recv(1024))

        if (grids[0].cells[caseAJouer] != EMPTY):
            grids[current_player].cells[caseAJouer] = grids[0].cells[caseAJouer]
            listeJoueur[current_player-1].send(MSG_ERROR)

        else:
            grids[current_player].cells[caseAJouer] = current_player
            grids[0].play(current_player, caseAJouer)
            current_player = current_player%2+1

    gagnant = grids[0].gameOver()

    if (gagnant == J1) :
        listeJoueur[J1-1].send(MSG_WIN)
        listeJoueur[J2-1].send(MSG_LOSE)

    if (gagnant == J2) :
        listeJoueur[J1-1].send(MSG_LOSE)
        listeJoueur[J2-1].send(MSG_WIN)

    if (gagnant == EMPTY) :
        listeJoueur[J1-1].send(MSG_DRAW)
        listeJoueur[J2-1].send(MSG_DRAW)

    for i in listeJoueur :
        tosend = pickle.dumps([GRID, grids[0]])
        i.send(tosend)

    for i in listeJoueur :
         i.send(MSG_END)

#!/usr/bin/python3

import pickle
#Pour chaque code un message est attribué dans le client
WELCOME =   10
START   =   11
PLAY    =   12
GRID    =   13
WIN     =   14
LOSE    =   15
DRAW    =   16
ERROR   =   17
END     =   20

MSG_WELCOME = pickle.dumps([WELCOME, None])
MSG_START   = pickle.dumps([START, None])
MSG_WIN     = pickle.dumps([WIN, None])
MSG_LOSE    = pickle.dumps([LOSE, None])
MSG_DRAW    = pickle.dumps([DRAW, None])
MSG_ERROR   = pickle.dumps([ERROR, None])
MSG_END     = pickle.dumps([END, None])

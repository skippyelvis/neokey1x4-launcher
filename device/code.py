import board
import busio
import time
import usb_cdc
from neokey1x4 import NeoKey1x4

nk = NeoKey1x4(busio.I2C(board.SCL1, board.SDA1))
cols = [(0,0,125), (0,125,125), (125,0,125), (125,125,0)]

def whichkeys(nk):
    yes, no = [], []
    for i in range(4):
        if nk[i]:
            yes.append(i)
        else:
            no.append(i)
    return yes, no

def send(yes):
    if len(yes) == 0:
        return
    c = ",".join([str(y) for y in yes]) + "\n"
    usb_cdc.data.write(bytes(c, "utf-8"))

def light(nk, yes, no):
    for y in yes:
        nk.pixels[y] = cols[y]
    for n in no:
        nk.pixels[n] = (0,0,0)


while True:
    yes, no = whichkeys(nk)
    send(yes)
    light(nk, yes, no)


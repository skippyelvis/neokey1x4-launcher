import serial
import subprocess
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-a', type=str, default='/dev/ttyACM1', help='serial addr')
args = parser.parse_args()

s = serial.Serial(args.a)

keymap = {
    "0":   "kitty",
    "0,1": "kitty nvim",
    "0,2": "kitty ranger",
    "0,3": "lockscreen.sh",
    "1":   "google-chrome-stable",
    "1,2": "google-chrome-stable https://outlook.office.com/mail/",
    "1,3": "google-chrome-stable youtube.com",
    "2":   "thunar",
    "2,3": "qtile cmd-obj -o window -f kill",
    "3":   "kitty cmatrix"
}

def callcmd(cmd):
    cmd = cmd.decode().strip()
    cmd = keymap[cmd]
    subprocess.Popen(cmd.split(" "), cwd="/home/homieja/", start_new_session=True)

while True:
    s.reset_input_buffer()
    line = s.readline()
    callcmd(line)
    time.sleep(.25)

from time import sleep
import sys
import uselect

poll = uselect.poll()
poll.register(sys.stdin, uselect.POLLIN)

def getCommand():
    if poll.poll(10):
        return sys.stdin.readline().strip()

while True:
    command = getCommand()

    if command == "START":
        for i in range(11):
            command = getCommand()
            if command == "STOP":
                break
            print(i)
            sleep(1)

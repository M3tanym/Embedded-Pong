import pygame
from pygame.locals import *

import shared

import threading
import queue

class AI(threading.Thread):
    def __init__(self, q):
        shared.systemMessage("Starting AI")
        threading.Thread.__init__(self)
        self.q = q
        self.eventConfig = {}
        self.running = True

    def run(self):
        try:
            # Any init items here
            while self.running:
                opCode = ""
                try:
                    q_item = self.q.get(False)
                    s = q_item
                    opCode = s[0:2]
                except Exception: pass

                if opCode == "ex":
                    print("Stopping AI")
                    self.running = False
                    self.q.task_done()

                # MAIN LOOP CODE HERE

        except Exception as e:
            shared.systemMessage(str(e), True)
            shared.exitProgram()


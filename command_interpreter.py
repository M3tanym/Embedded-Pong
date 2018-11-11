import shared

import threading
import queue
import re
import requests
import json

class CommandInterpreter(threading.Thread):
    def __init__(self, q):
        shared.systemMessage("Starting command_interpreter")
        threading.Thread.__init__(self)
        self.q = q
        self.eventConfig = {}
        self.running = True


    def run(self):
        try:
            while self.running:
                q_item = self.q.get()
                s = q_item
                opCode = s[0:2]

                if opCode == "ex":
                    print("Stopping command_interpreter")
                    self.running = False
                    self.q.task_done()
                    shared.exitProgram()

                elif opCode == "te":
                    shared.systemMessage("Hello World!")
                    self.q.task_done()

                else:
                    if not (opCode == ""):
                        shared.systemMessage("Unknown command \"" + opCode + "\"")
                    self.q.task_done()

        except Exception as e:
            shared.systemMessage(str(e), True)
            shared.exitProgram()

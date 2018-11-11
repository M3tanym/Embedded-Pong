import shared

import threading
import queue
import re

class ConsoleInput(threading.Thread):
    def __init__(self):
        shared.systemMessage("Starting console_input")
        threading.Thread.__init__(self)
        self.running = True

    def run(self):
        while self.running:
            s = input("Pong > ")
            shared.q_command_interpreter.put(s)

class ConsoleOutput(threading.Thread):
    def __init__(self, q):
        shared.systemMessage("Starting console_output")
        threading.Thread.__init__(self)
        self.q = q
        self.running = True

    def run(self):
        while self.running:
            q_item = self.q.get()
            if q_item.startswith("ex"):
                print("Stopping console_output")
                self.running = False
            else:
                print(q_item)
            self.q.task_done()


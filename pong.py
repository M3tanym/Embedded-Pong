import pygame
from pygame.locals import *

import shared

import threading
import queue

class Pong(threading.Thread):
    def __init__(self, q):
        shared.systemMessage("Starting pong")
        threading.Thread.__init__(self)
        self.q = q
        self.eventConfig = {}
        self.running = True

    def run(self):
        try:
            pygame.init()
            FPS = 30
            fpsClock = pygame.time.Clock()

            display = pygame.display.set_mode((600, 300), 0, 32)
            pygame.display.set_caption('Pong')

            BLACK = (0, 0, 0)
            WHITE = (255, 255, 255)

            ball = pygame.image.load('cat-face.png')
            ball = pygame.transform.scale(ball, (30, 30))

            ballx = 285
            bally = 135

            paddle1 = (10, 115, 15, 70)
            paddle2 = (575, 115, 15, 70)

            while self.running:
                opCode = ""
                try:
                    q_item = self.q.get(False)
                    s = q_item
                    opCode = s[0:2]
                except Exception: pass

                if opCode == "ex":
                    print("Stopping command_interpreter")
                    self.running = False
                    self.q.task_done()

                display.fill(BLACK)

                display.blit(ball, (ballx, bally))

                pygame.draw.rect(display, WHITE, paddle1, 0)
                pygame.draw.rect(display, WHITE, paddle2, 0)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        shared.exitProgram()

                pygame.display.update()
                fpsClock.tick(FPS)

        except Exception as e:
            shared.systemMessage(str(e), True)
            shared.exitProgram()


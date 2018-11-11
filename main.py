import shared
import console
import command_interpreter

import pong
import ai
import player

import sys
import traceback
import time

if __name__ == "__main__":
    try:
        shared.systemMessage("Started!")

        # Console output thread
        thread_console_output = console.ConsoleOutput(shared.q_console_output)
        thread_console_output.start()

         # Command interpreter thread
        thread_command_interpreter = command_interpreter.CommandInterpreter(shared.q_command_interpreter)
        thread_command_interpreter.start()

        # Console input thread
        thread_console_input = console.ConsoleInput()
        thread_console_input.daemon = True
        thread_console_input.start()

        # Pong thread
        thread_pong = pong.Pong(shared.q_pong)
        thread_pong.start()

        # AI thread
        thread_ai = ai.AI(shared.q_ai)
        thread_ai.start()

        # Player thread
        thread_player = player.Player(shared.q_player)
        thread_player.start()

        # PROGRAM RUNS HERE TILL EXIT

        # wait for all threads to be stopped with their various exit signals
        # (except for threads which are daemonic and will be killed by sys.exit)
        thread_console_output.join()
        thread_command_interpreter.join()
        sys.exit()

    except Exception as e:
        print("Main handler exception!")
        print("Error: " + str(e))
        sys.exit()

import queue
import time

q_console_output = queue.Queue()
q_command_interpreter = queue.Queue()
q_pong = queue.Queue()
q_ai = queue.Queue()
q_player = queue.Queue()

def exitProgram():
    q_console_output.put("ex")
    q_command_interpreter.put("ex")
    q_pong.put("ex")
    q_ai.put("ex")
    q_player.put("ex")

def manageError(errType, errMsg, isFatal=True):
    errorMessage = errType + ": " + str(errMsg)
    if (isFatal):
        errorMessage = "FATAL: " + errorMessage
    systemMessage(errorMessage, True)
    if(isFatal): # quit the thread and exit the program
        systemMessage("\n\n=====EXITING!=====\n\n")
        time.sleep(1.0)
        exitProgram()

def systemMessage(outMsg, isError=False):
    # update console, log, and web status textbox
    if (isError):
        outMsg = "Error: " + outMsg
    else:
        outMsg = "Info: " + outMsg
    q_console_output.put_nowait(outMsg)


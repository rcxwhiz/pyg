from FileExecution import security

# these are the strings to get prepended and appended to the source code
prepend_1 = r"""
# EXIT SCRIPT ###################################
import os as EXECUTION_OS
import sys as EXECUTION_SYS
import time as EXECUTION_TIME
import threading as EXECUTION_THREADING
def ILLEGAL_FUNCTION_(*args):
    print('Tried to use an illegal function!')
"""

if len(security.function_blacklist) > 0:
    prepend_2 = f'{", ".join(security.function_blacklist)} = ILLEGAL_FUNCTION'
else:
    prepend_2 = ''

prepend_3 = """
def KILL_PROGRAM_():
    timer = TIME BEFORE KILL HERE
    EXECUTION_TIME.sleep(timer)
    print(f'\n[GRADER] Program killed after {timer} seconds')
    EXECUTION_SYS.stdout.close()
    EXECUTION_OS._exit(0)
kill_thread = EXECUTION_THREADING.Thread(target=KILL_PROGRAM_)
kill_thread.start()
EXECUTION_OS.chdir(EXECUTION_OS.path.dirname(EXECUTION_SYS.argv[0]))
# ###############################################
"""

prepend = prepend_1 + prepend_2 + prepend_3

append = r"""


# EXIT SCRIPT ###################################
EXECUTION_SYS.stdout.close()
EXECUTION_OS._exit(0)
# ###############################################"""

# these are the strings to get prepended and appended to the source code
prepend = r"""
# EXIT SCRIPT ###################################
import os as EXECUTION_OS
import sys as EXECUTION_SYS
import time as EXECUTION_TIME
import threading as EXECUTION_THREADING
def kill_prog():
    timer = TIME BEFORE KILL HERE
    EXECUTION_TIME.sleep(timer)
    print(f'\n[GRADER] Program killed after {timer} seconds')
    EXECUTION_SYS.stdout.close()
    EXECUTION_OS._exit(0)
kill_thread = EXECUTION_THREADING.Thread(target=kill_prog)
kill_thread.start()
EXECUTION_OS.chdir(EXECUTION_OS.path.dirname(EXECUTION_SYS.argv[0]))
# ###############################################

"""

append = r"""


# EXIT SCRIPT ###################################
EXECUTION_SYS.stdout.close()
EXECUTION_OS._exit(0)
# ###############################################"""

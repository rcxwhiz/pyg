prepend = r"""
# EXIT SCRIPT ###################################
import os
import sys
import time
import threading
killed = True
def kill_prog():
    timer = TIME BEFORE KILL HERE
    time.sleep(timer)
    if killed:
        print(f'\n[GRADER] Program killed after {timer} seconds')
    sys.stdout.close()
    os._exit(0)
kill_thread = threading.Thread(target=kill_prog)
kill_thread.start()
os.chdir(os.path.dirname(sys.argv[0]))
# ###############################################

"""

append = r"""


# EXIT SCRIPT ###################################
sys.stdout.close()
os._exit(0)
# ###############################################"""

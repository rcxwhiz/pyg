prepend = r"""
# EXIT SCRIPT ###################################
import os
import sys
import time
import threading
killed = True
def kill_prog():
    time.sleep(TIME BEFORE KILL HERE)
    if killed:
        print('\n[GRADER] Program killed after being unresponsive')
    os._exit(0)
kill_thread = threading.Thread(target=kill_prog)
kill_thread.start()
os.chdir(os.path.dirname(sys.argv[0]))
# ###############################################

"""

append = r"""


# EXIT SCRIPT ###################################
killed = False
# ###############################################"""

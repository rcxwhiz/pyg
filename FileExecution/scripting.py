prepend = r"""
# EXIT SCRIPT ###################################
import os
import sys
import time
import threading
def kill_prog():
    time.sleep(TIME BEFORE KILL HERE)
    print('\n[GRADER] - Program killed after being unresponsive')
    os._exit(2)
kill_thread = threading.Thread(target=kill_prog)
kill_thread.start()
os.chdir(os.path.dirname(sys.argv[0]))
# ###############################################
"""

append = r"""


# EXIT SCRIPT ###################################
time.sleep(0.2)
os._exit(1)
# ###############################################"""

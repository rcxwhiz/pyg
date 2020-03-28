# EXIT SCRIPT ###################################
import os
import sys
import threading
import time


def kill_prog():
    time.sleep(1)
    print('\n[GRADER] Program killed after being unresponsive')
    os._exit(0)


kill_thread = threading.Thread(target=kill_prog)
kill_thread.start()
os.chdir(os.path.dirname(sys.argv[0]))
# ###############################################


print('part 1')
print('part 2')
print('PART a')
print('42')
print('partc')
print([[42] * 42] * 42)
print('done')

# EXIT SCRIPT ###################################
os._exit(0)
# ###############################################

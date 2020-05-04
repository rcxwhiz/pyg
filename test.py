# EXIT SCRIPT ###################################
import inspect as EXECUTION_INSPECT_
import os as EXECUTION_OS_
import sys as EXECUTION_SYS_
import threading as EXECUTION_THREADING_
import time as EXECUTION_TIME_


def ILLEGAL_FUNCTION_(*args):
    stack_spot = EXECUTION_INSPECT_.stack()[-1]
    print(f'Illegal function called on line {stack_spot.lineno}: {stack_spot.code_context[0]}')


input, open = ILLEGAL_FUNCTION_


def KILL_PROGRAM_():
    EXECUTION_TIME_.sleep(1)
    print('')
    print(f'[GRADER] Program killed after 1 seconds')
    EXECUTION_SYS_.stdout.close()
    EXECUTION_OS_._exit(0)


kill_thread = EXECUTION_THREADING_.Thread(target=KILL_PROGRAM_)
EXECUTION_OS_.chdir(EXECUTION_OS_.path.dirname(EXECUTION_SYS_.argv[0]))
kill_thread.start()
# ###############################################
import numpy as np

print('Part 1')

print(np.pi * 2)

# EXIT SCRIPT ###################################
EXECUTION_SYS_.stdout.close()
EXECUTION_OS_._exit(0)
# ###############################################

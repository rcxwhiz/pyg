import sys

import Config as cfg

# these are the strings to get prepended and appended to the source code
prepend = r"""
# EXIT SCRIPT ###################################
import inspect as EXECUTION_INSPECT_
import os as EXECUTION_OS_
import sys as EXECUTION_SYS_
import time as EXECUTION_TIME_
import threading as EXECUTION_THREADING_
def ILLEGAL_FUNCTION_(*args):
    stack_spot = EXECUTION_INSPECT_.stack()[-1]
    print(f'Illegal function called on line {stack_spot.lineno}: {stack_spot.code_context[0]}')
"""

for function in cfg.function_blacklist:
    prepend += f'{function} = ILLEGAL_FUNCTION_'

timer = cfg.max_program_time
if timer == 0:
    timer = sys.maxsize

prepend += f"""
def KILL_PROGRAM_():
    EXECUTION_TIME_.sleep({timer})
    print('')
    print(f'[GRADER] Program killed after {timer} seconds')
    EXECUTION_SYS_.stdout.close()
    EXECUTION_OS_._exit(0)
kill_thread = EXECUTION_THREADING_.Thread(target=KILL_PROGRAM_)
EXECUTION_OS_.chdir(EXECUTION_OS_.path.dirname(EXECUTION_SYS_.argv[0]))
kill_thread.start()
# ###############################################
"""

append = r"""


# EXIT SCRIPT ###################################
EXECUTION_SYS_.stdout.close()
EXECUTION_OS_._exit(0)
# ###############################################"""

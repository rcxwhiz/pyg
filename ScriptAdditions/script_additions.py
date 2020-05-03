import sys

import Config as cfg

# these are the strings to get prepended and appended to the source code
prepend_1 = r"""
# EXIT SCRIPT ###################################
import inspect as EXECUTION_INSPECT_
import os as EXECUTION_OS_
import sys as EXECUTION_SYS_
import time as EXECUTION_TIME_
import threading as EXECUTION_THREADING_
def ILLEGAL_FUNCTION__(*args):
    stack_spot = EXECUTION_INSPECT_.stack()[-1]
    print(f'Illegal function called on line {stack_spot.lineno}: {stack_spot.code_context[0]}')
"""

if len(cfg.function_blacklist) > 0:
    prepend_2 = f'{", ".join(cfg.function_blacklist)} = ILLEGAL_FUNCTION_'
else:
    prepend_2 = ''

timer = cfg.max_program_time
if timer == 0:
    timer = sys.maxsize

prepend_3 = f"""
def KILL_PROGRAM_():
    EXECUTION_TIME_.sleep({timer})
    print(f'\n[GRADER] Program killed after {timer} seconds')
    EXECUTION_SYS_.stdout.close()
    EXECUTION_OS_._exit(0)
kill_thread = EXECUTION_THREADING_.Thread(target=KILL_PROGRAM_)
EXECUTION_OS_.chdir(EXECUTION_OS_.path.dirname(EXECUTION_SYS_.argv[0]))
kill_thread.start()
# ###############################################
"""

prepend = prepend_1 + prepend_2 + prepend_3

append = r"""


# EXIT SCRIPT ###################################
EXECUTION_SYS_.stdout.close()
EXECUTION_OS_._exit(0)
# ###############################################"""

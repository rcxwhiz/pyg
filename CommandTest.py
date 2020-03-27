import subprocess
import threading

temp_script_name = r'C:\Users\josh-laptop\PycharmProjects\sag\test-program-location\HW 31\key-source\butts.py'


def func(script_name):
    result_string = subprocess.check_output(['python', script_name], stderr=subprocess.STDOUT).decode('utf-8')
    print(result_string)
    input()


print('Test:')
my_thread = threading.Thread(target=func, args=(temp_script_name,))
my_thread.start()

"""
BIG NOTE: It works totally fine without shell when normal or in function
When in a thread it still works without shell
Everything seems to be working fine up until this point without shell
"""

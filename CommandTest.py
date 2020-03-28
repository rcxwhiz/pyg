import subprocess
import threading

temp_script_name = r'C:\Users\josh-laptop\PycharmProjects\sag\test-program-location\HW 31\key-source\butts.py'


def func(script_name, shelltf):
    result_string = subprocess.check_output(['python', script_name], stderr=subprocess.STDOUT, shell=shelltf).decode(
        'utf-8')
    print(result_string)


"""
Literally all of these test are working in all cases so that kind of sucks
"""

input('Test 1. Press enter to continue')
print(subprocess.check_output(['python', temp_script_name], stderr=subprocess.STDOUT).decode('utf-8'))

input('Test 2. Press enter to continue')
print(subprocess.check_output(['python', temp_script_name], stderr=subprocess.STDOUT, shell=True).decode('utf-8'))

input('Test 3. Press enter to continue')
func(temp_script_name, False)

input('Test 4. Press enter to continue')
func(temp_script_name, True)

input('Test 5. Press enter to continue')
my_thread = threading.Thread(target=func, args=(temp_script_name, False))
my_thread.start()
my_thread.join()

input('Test 6. Press enter to continue')
my_thread = threading.Thread(target=func, args=(temp_script_name, True))
my_thread.start()
my_thread.join()

input('Finished tests. Press enter to exit')

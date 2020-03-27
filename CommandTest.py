import subprocess

temp_script_name = r'C:\Users\josh-laptop\PycharmProjects\sag\test-program-location\HW 31\key-source\butts.py'
result_string = subprocess.check_output(['python', temp_script_name], stderr=subprocess.STDOUT).decode('utf-8')

print('Test:\n', result_string)
input()

import inspect


def illegal_function(*args):
    print('Illegal function called')
    print('args:', *args)
    print(inspect.stack()[-1].lineno)
    print(inspect.stack()[-1].code_context)


input = illegal_function

if True:
    dude = input('help')

print('done')

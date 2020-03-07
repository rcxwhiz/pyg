def input_num_range(ran):
    answer = -1
    while answer < ran[0] or answer > ran[1]:
        try:
            answer = int(input('\rOption: '))
        except ValueError:
            continue
    return answer

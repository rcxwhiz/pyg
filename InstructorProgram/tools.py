def input_num_range(low, high):
    answer = -1
    while answer < low or answer > high:
        try:
            answer = int(input('\rOption: '))
        except ValueError:
            continue
    return answer

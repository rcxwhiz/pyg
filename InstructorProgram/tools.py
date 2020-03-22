def input_num_range(low, high, message='Option: '):
    answer = -100
    while answer < low or answer > high:
        try:
            answer = int(input(message))
        except ValueError:
            continue
    return answer

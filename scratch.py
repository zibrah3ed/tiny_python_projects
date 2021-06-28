def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    dec_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decoded = []
    for char in roman:
        decoded.append(dec_dict[char])

    for index, elem in enumerate(decoded):

        if index + 1 < len(decoded) and index - 1 >= 0:
            curr_el = str(elem)
            next_el = str(decoded[index + 1])

            print(curr_el, next_el)

solution('XXI')

solution('XIVVVVVVVV')
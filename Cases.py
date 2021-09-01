
def rule(rule_num):
    bin_of_num = f'{rule_num:08b}'
    pos = 7

    rule_set = {
        '000': 0,
        '001': 0,
        '010': 0,
        '011': 0,
        '100': 0,
        '101': 0,
        '110': 0,
        '111': 0,
    }

    for char in str(bin_of_num):
        key = f'{pos:03b}'
        rule_set.update({key: int(char)})
        pos -= 1

    return rule_set
with open("input.txt", "r") as f:
    strings = f.readlines()

ref = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

strings = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
    "sevenine",  # corner case 1, 79
    "67mcmfive1sixonefive"] # corner case 2, two "five"


total = 0
for s_t_r in strings:
    s_t_r = s_t_r.strip()
    digits = []
    for c in range(len(s_t_r)):
        p_s_t_r = s_t_r[c:]
        rpl = [p_s_t_r.find(str_digit) for str_digit in ref]
        min = len(p_s_t_r)
        for d in range(len(rpl)):
            if 0 <= rpl[d] <= min:
                min = rpl[d]
                digit = d + 1 
        native_digit = [d for d in range(len(p_s_t_r)) if p_s_t_r[d].isdigit()]
        if native_digit and min != len(p_s_t_r):
            digits += [digit] if min < native_digit[0] else p_s_t_r[native_digit[0]]
        elif native_digit and min == len(p_s_t_r):
            digits += p_s_t_r[native_digit[0]]
        elif len(native_digit) == 0 and min != len(p_s_t_r):
            digits += [digit]
        
    cali = int(str(digits[0]) + str(digits[-1]))
    total += cali

print(total)

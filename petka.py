import re
def find_patterns(input_string):
    search_regs = [r'(\.)((?!com|org|ru|net|gov| |\d|").)',
                   r'([^\d]\.)(\d)',
                   r'(%)([^:;,.?!" ])',
                   r'([!?])([^" ])',
                   r'([:,])([^\d ])',
                   r'([^\d][:,])(\d)',
                   r'([);])([^ ])']
    search_regs = list(map(re.compile, search_regs))
    replace_string = r'\1 \2'
    correct_string = input_string
    for search_reg in search_regs:
        correct_string = re.sub(search_reg, replace_string, correct_string)
    return correct_string


# Если после знаков ",.?!%):;" нет пробела, вставить его, но есть исключения:
# 1. Если после "." или ","  или ":"  идет цифра и до них цифра, то вставлять не надо (это число или отношение)
# 2. Если после ".?!%" идут простые двойные кавычки ("),  то вставлять не надо (это цитата)
# 3. Если после "%" идут знаки препинания (:;,.?!),  то вставлять не надо
# 4. Если после "." идут com или org или ru или net или gov,  то вставлять не надо

if __name__ == '__main__':
    strings = ['"Apple."', "Apple.ru", "Apple.coc"
               "a.0", "a,0", "a:0",
               "0.0", "0,0", "0:0",
               "0.a", "0,a", "0:a",
               "56%,k", "56%k",
               "It works!Yaay. Hoho.",
               "a.a. a",
               '''Why1:1''']
    for s in strings:
        print(s, "->", find_patterns(s))
        print(s == find_patterns(s))
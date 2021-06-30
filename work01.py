import random

INIT_STRING = 'ABCDEFGHIJKLMNOPQISTUVWXYZ1234567890'
INIT_STRING_LENGTH = len(INIT_STRING) - 1
CODE_LENGTH = 20
CODE_NUM = 200


def get_activation_code():
    code = ''
    for i in range(CODE_LENGTH):
        num = random.randint(0, INIT_STRING_LENGTH)
        code += INIT_STRING[num]
        if (i + 1) % 5 == 0 and i + 1 != CODE_LENGTH:
            code += '-'
    return code


CodeList = []
for i in range(CODE_NUM):
    CodeList.append(get_activation_code())

print(CodeList)

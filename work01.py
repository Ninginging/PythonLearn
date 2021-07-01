import random

INIT_STRING = 'ABCDEFGHIJKLMNOPQISTUVWXYZ1234567890'
INIT_STRING_LENGTH = len(INIT_STRING) - 1
CODE_LENGTH = 20
CODE_NUM = 200


def get_activation_code(length, num):
    code_list = []

    def get_code():
        code = ''
        for __i in range(length):
            __num = random.randint(0, INIT_STRING_LENGTH)
            code += INIT_STRING[num]  # 字符串拼接实现激活码生成
            if (__i + 1) % 5 == 0 and __i + 1 != CODE_LENGTH:
                code += '-'
        return code

    for i in range(num):
        code_list.append(get_code())
    return code_list


Code_List = get_activation_code(CODE_LENGTH, CODE_NUM)
# print(Code_List)

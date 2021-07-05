PEO_NUM = 12
KILL_NUM = 5
Peo_list = list(range(1, PEO_NUM))
kill_list = []  # 初始化玩家编号列表和击杀顺序列表


# normal_way
def get_kill(peo_list, kill_num_set):
    __killed_num = []
    for i in range(-1, len(peo_list)):
        if kill_num_set % len(peo_list) == i + 1:
            if i == -1:
                __killed_num = peo_list[-1]
                del peo_list[i]
                break
            else:
                __killed_num = peo_list[i]
                del peo_list[i]
                peo_list = peo_list[i:] + peo_list[0:i]
                break

    return [__killed_num, peo_list]


while len(Peo_list) != 1:
    [killed_num, Peo_list] = get_kill(Peo_list, KILL_NUM)
    # print(killed_num, Peo_list)     # 调试用
    kill_list.append(killed_num)

print('生成击杀的顺序列表为:%s\n最后存活的玩家编号是：%s' % (kill_list, Peo_list[0]))

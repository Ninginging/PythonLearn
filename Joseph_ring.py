PEO_NUM = 11
KILL_NUM = 3
Peo_list = list(range(0, 11))
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


# recursive way
# 当有n-1个人的时候，编号为i的人对应着上一轮编号为(m+i)%n的人
# 假设此轮编号为x(n-1)的人最终会留下来,因为编号为x(n-1)的人肯定对应着上一轮的x(n),所以有递推式 x(n)=(m+x(n-1))%n
# def get_kill_rec(n, m):  # 总共有n个人,编号为m的人出列,
#     if n == 1:
#         return 0
#     else:
#         return (m + get_kill_rec(n - 1, m)) % n
#
#
# print('最后存活的玩家编号是：%s' % get_kill_rec(PEO_NUM, KILL_NUM))
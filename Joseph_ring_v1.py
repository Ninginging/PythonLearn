class Player:
    def __init__(self, name, std_id, gender):
        self.name = name
        self.std_id = std_id
        self.gender = gender


# 实例化对象
zzc = Player('zzc', '2020****', '男')
sky = Player('sky', '2020****', '男')
csb = Player('csb', '2020****', '男')
yyj = Player('yyj', '2020****', '男')
lq = Player('lq', '2020****', '女')
wyk = Player('wyk', '2020****', '男')
hht = Player('hht', '2020****', '男')
wf = Player('wf', '2020****', '男')
cn = Player('cn', '2020****', '男')

group = [zzc, sky, csb, yyj, lq, wyk, hht, wf, cn]


# use the f to traversal the container
def joseph_traversal(container, step, start_ele):
    assert type(step) == int, '输入错误'
    start_index = container.index(start_ele)
    index_list = list(range(len(container)))  # 创建输入容器的索引列表，只针对索引进行操作
    used_index_list = []  # 暂存已经遍历过的索引值
    results = []  # 返回的遍历之后的结果
    pos = 0     # 改为位置 pos

    while len(used_index_list) != len(index_list):
        if start_index > len(index_list) - 1:
            start_index = 0
        if not (index_list[start_index] in used_index_list):
            pos += 1
            # print('当前i是', start_index)
            if pos == step:
                used_index_list.append(start_index)  # 更新已遍历列表
                results.append(container[start_index])  # 将容器的对应值存入结果列表
                # print(used_index)
                pos = 0
        start_index += 1

    return results


for i in range(len(group)):
    print(joseph_traversal(group, 4, lq)[i].name)

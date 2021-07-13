import random

INIT_STRING = 'ABCDEFGHIJKLMNOPQISTUVWXYZabcdefghijklmnopqrstuvwxyz'
INIT_NUM = '01234567890'
INIT_GENDER = ('男', '女')
GROUP_SIZE =11


class Player:
    def __init__(self):
        self.name = self.get_name()
        self.std_id = self.get_id()
        self.gender = self.get_gender()

    def get_name(self, size=5):
        name = ''
        for i in range(size):
            name += random.choice(INIT_STRING)
        return name

    def get_id(self, size=12):
        std_id = ''
        for i in range(size):
            std_id += random.choice(INIT_NUM)
        return std_id

    def get_gender(self):
        gender = random.choice(INIT_GENDER)
        return gender


group = []
for i in range(GROUP_SIZE):
    locals()['player' + str(i)] = Player()      # 批量化生成实例对象
    group.append(locals()['player' + str(i)])   # 将对象存入列表


class Joseph(list):
    def __init__(self, container, step=1, start_pos=0,):     # 初始化,输入可索引的容器,步长,起始元素的编号位置
        self.container = container
        self.step = step
        self.start_pos = start_pos

    def traversal(self):    # 约瑟夫遍历方法,返回按照初始化参数遍历之后的容器
        assert type(self.step) == int and self.step != 0, '步长输入错误'
        assert self.start_pos <= len(self.container), '起始元素不在容器当中'

        index_list = list(range(len(self.container)))  # 创建输入容器的索引列表，只针对索引进行操作
        start_pos = self.start_pos
        length_container = len(index_list)
        used_index_list = []  # 暂存已经遍历过的索引值
        results = []          # 返回的遍历之后的结果
        pos = 0

        while len(used_index_list) != length_container:
            if start_pos > len(index_list) - 1:
                start_pos = 0
            if not (index_list[start_pos] in used_index_list):
                pos += 1
                # print('当前i是', start_index) # 测试用
                if pos == self.step:
                    used_index_list.append(start_pos)          # 更新已遍历列表
                    results.append(self.container[start_pos])  # 将容器的对应值存入结果列表
                    # print(used_index)        # 测试用
                    pos = 0
            start_pos += 1

        return results


if __name__ == "__main__":
    group_name, group_name_new = [], []
    for i in range(GROUP_SIZE):
        group_name.append(group[i].name)
        group_name_new.append(Joseph(group, 4).traversal()[i].name)
    print('初始容器顺序为：%s\n遍历之后的结果是：%s' % (group_name, group_name_new))

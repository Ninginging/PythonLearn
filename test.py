import random


class Turtel:
    def __init__(self, name):
        self.name = name
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)  # 乌龟位置初始化

    def move(self):
        dirsel = random.randint(0, 1)
        eachmove = random.sample([-2, -1, 1, 2], 1)

        def one_move(__step):
            if dirsel:
                self.x += __step
            else:
                self.y += __step

        one_move(eachmove[0])
        if self.x <= 0 or self.y <= 0:
            step = abs(eachmove[0])
            one_move(step)
        elif self.x >= 10 or self.y >= 10:
            step = -abs(eachmove[0])
            one_move(step)
        position = [self.x, self.y]
        return position
        # print('Turtel%s的位置是:' % self.name, self.x, self.y)


class Fish:
    def __init__(self, name):
        self.name = name
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)  # 鱼位置初始化

    def move(self):
        dirsel = random.randint(0, 1)
        eachmove = random.sample([-1, 1], 1)

        def one_move(__step):
            if dirsel:
                self.x += __step
            else:
                self.y += __step

        one_move(eachmove[0])
        if self.x <= 0 or self.y <= 0:
            step = abs(eachmove[0])
            one_move(step)
        elif self.x >= 10 or self.y >= 10:
            step = -abs(eachmove[0])
            one_move(step)
        position = [self.x, self.y]
        return position

        # print('Fish%s的位置是:' % self.name, self.x, self.y)


strength = 100
turtel = Turtel(Turtel)
fish_eat, fish_num = 0, []
fish_pos = dict.fromkeys(range(10))

for i in range(1, 11):
    fish_num.append(i)
    locals()['fish' + str(i)] = Fish(i)  # 批量化实例化对象的方法！！！

while strength > 0 and fish_num != []:
    turtel_pos = turtel.move()
    for i in fish_num:
        fish_pos[i - 1] = locals()['fish' + str(i)].move()
        if turtel_pos == fish_pos[i - 1]:
            fish_num.remove(i)
            fish_eat += 1
            print('吃掉鱼的坐标是%s' % turtel_pos + ',已经吃鱼的数量是%s' % fish_eat)
            print(fish_pos[i - 1])
    strength -= 1

import copy
import queue


class Node:
    def __init__(self, structure, terminal, g):
        self.structure = structure
        self.terminal = terminal # возможно, это не понадобится
        self.g = g
        self.n = len(structure)


    def null_adress_def(self): #определяет адресс нуля
        for s in range(n):
            if 0 in self.structure[s]:
                r = self.structure[s].index(0)
                break
        self.s = s
        self.r = r
        return [self.s, self.r]


    def f_def(self):
        self.f = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.structure[i][j] != self.terminal[i][j]:
                    self.f += 1
        return self.f

    def g_get(self):
        return self.g

    def h_get(self):
        return self.g + self.f_def()

    def potomoks(self):
        self.s = self.null_adress_def()[0]
        self.r = self.null_adress_def()[1]
        list_of_potomoks = []
        if 0 <= self.s - 1:
            potomok1 = copy.deepcopy(self.structure)
            potomok1[self.s][self.r], potomok1[self.s - 1][self.r] = potomok1[self.s - 1][self.r], potomok1[self.s][self.r]
            list_of_potomoks.append(potomok1)
        if self.s + 1 < self.n:
            potomok2 = copy.deepcopy(self.structure)
            potomok2[self.s+1][self.r], potomok2[self.s][self.r] = potomok2[self.s][self.r], potomok2[self.s+1][self.r]
            list_of_potomoks.append(potomok2)
        if 0 <= self.r - 1:
            potomok3 = copy.deepcopy(self.structure)
            potomok3[self.s][self.r-1], potomok3[self.s][self.r] = potomok3[self.s][self.r], potomok3[self.s][self.r-1]
            list_of_potomoks.append(potomok3)
        if self.r + 1 < self.n:
            potomok4 = copy.deepcopy(self.structure)
            potomok4[self.s][self.r + 1], potomok4[self.s][self.r] = potomok4[self.s][self.r], potomok4[self.s][self.r + 1]
            list_of_potomoks.append(potomok4)
        return(list_of_potomoks)

    def up_g(self):
        self.g += 1


    def is_terminal(self):
        if self.structure == self.terminal:
            return True


# записываем исходную матрицу
quest = [[3, 1], [0, 2]]
n = len(quest)
# создаем конечную матрицу
terminal = [[0 for i in range(n)] for j in range(n)]
for i in range(n ** 2 - 1):
    terminal[i // n][i % n] = i + 1
#создаем закрытый список
closed = []
set_of_h = []
open_dict = dict()
current_node = Node(quest, terminal, 0)
set_of_h.append(current_node.h_get())
open_dict[current_node] = [current_node.h_get()]
while len(open_dict) != 0:
    minimum_h = min(set_of_h)
    for key, value in open_dict:
        if value == minimum_h:
            current_node = key
            break
   # print('Текущий', current_node.structure)
   #  print('положение нуля', current_node.null_adress_def())
    if current_node.is_terminal():
        print('YES')
        break
    else:
        if current_node.structure not in closed:
            print('NO')
            del open_dict[current_node]
            closed.append(current_node.structure)
            g = current_node.g_get() + 1
            for i in current_node.potomoks():
              #  print('потомки',current_node.potomoks())
                potomok = Node(i, terminal, g)
                if i not in closed:
                    open_dict[potomok] = potomok.h_get()
        else:
            del open_dict[current_node]
print(closed)




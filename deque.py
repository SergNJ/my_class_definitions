class Deque():
    def __init__(self, name: str=''):
        self.__dq = []
        self.__name = name

    def __repr__(self):
        return self.__name + ':  rear-> ' + ','.join(self.__dq) + ' <-front'

    def get_all(self):
        return self.__dq

    def length(self):
        return len(self.__dq)

    def add_front(self, val):
        self.__dq.append(val)

    def add_rear(self, val):
        self.__dq.insert(0, val)

    def pop_front(self):
        return self.__dq.pop()

    def pop_rear(self):
        return self.__dq.pop(0)

    def pop_ends(self):
        self.__dq.pop()
        self.__dq.pop(0)

    def peek_front(self):
        return self.__dq[-1]

    def peek_rear(self):
        return self.__dq[0]

    def copy_rear(self, pos):
        return self.__dq[:pos]

    def empty(self):
        return self.__dq == []

    def ends_match(self):
        return self.__dq[0] == self.__dq[-1]

    def move_ends(self, destination_dq):
        destination_dq.add_front(self.__dq.pop())
        destination_dq.add_rear(self.__dq.pop(0))

    def find(self, val):
        return self.__dq.index(val) if val in self.__dq else None

    def find_all(self, val):
        return [pos for pos, item in enumerate(self.__dq) if item == val]

    def get_str(self, separator):
        return separator.join(self.__dq)

    def clear(self):
        self.__dq = []


dq = Deque('Test')
print(dq)
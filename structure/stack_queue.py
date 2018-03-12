class Stack(object):
    """栈"""

    def __init__(self):
        self._list = []  # 尾部栈顶,操作顺序表尾部O(1)

    def push(self, item):
        """入栈到栈顶"""
        self._list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self._list.pop()

    def peek(self):
        """返回栈顶元素不弹出"""
        if self._list:
            return self._list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self._list == []

    def size(self):
        """返回栈元素个数"""
        return len(self._list)


class Queue(object):
    """队列"""

    def __init__(self):
        self._list = []

    def enqueue(self, item):
        """入队"""
        self._list.append(item)

    def dequeue(self):
        """出队"""
        if self._list:
            return self._list.pop(0)
        else:
            return None

    def is_empty(self):
        """判断队列是否为空"""
        return self._list == []

    def size(self):
        """返回队列元素大小"""
        return len(self._list)


class DoubleQueue(object):
    """双端队列"""

    def __init__(self):
        self._list = []

    def add_front(self, item):
        """头入队"""
        self._list.insert(0, item)

    def add_real(self, item):
        """尾入队"""
        self._list.append(item)

    def pop_front(self):
        """头出队"""
        if self._list:
            return self._list.pop(0)
        else:
            return None

    def pop_real(self):
        """头出队"""
        if self._list:
            return self._list.pop()
        else:
            return None

    def is_empty(self):
        """判断队列是否为空"""
        return self._list == []

    def size(self):
        """返回队列元素大小"""
        return len(self._list)

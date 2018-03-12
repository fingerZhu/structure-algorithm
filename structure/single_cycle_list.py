from structure.single_list import SingleList, SingleNode


class SingleCycleNode(SingleNode):
    """单向循环链表节点"""

    def __repr__(self):
        return str(self.elem) + "(单向循环链表节点：后(" + str(self.next.elem if self.next else None) + "))"


class SingleCycleList(SingleList):
    """单向循环链表"""

    def __init__(self, node=None):
        SingleList.__init__(self, node)
        if node:
            node.next = self._head

    def length(self):
        """单向循环链表长度"""
        if self.is_empty():
            return 0
        else:
            cur = self._head
            count = 0
            while cur.next != self._head:
                cur = cur.next
                count += 1
            count += 1  # 尾节点+1
            return count

    def traverse(self):
        """单向循环遍历链表"""
        print("-------单向循环链表遍历S--------")
        if self.is_empty():
            return
        else:
            cur = self._head
            while cur.next != self._head:
                print(cur, end=", ")
                cur = cur.next
            print(cur, end=", ")  # 退出循环，打印尾节点
        print("\n-------单向循环链表遍历E--------")

    def add(self, item):
        """单向循环链表头部添加元素"""
        node = SingleCycleNode(item)
        if self.is_empty():
            self._head = node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            cur.next = self._head = node

    def append(self, item):
        """单向循环链表尾部添加元素"""
        node = SingleCycleNode(item)
        if self.is_empty():
            self._head = node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next, node.next = node, self._head

    def insert(self, pos, item):
        """单向循环链表指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count < pos - 1:
                pre = pre.next
                count += 1
            node = SingleCycleNode(item)
            node.next, pre.next = pre.next, node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        pre = None
        cur = self._head
        while cur.next != self._head:
            if cur.elem == item:
                if cur == self._head:  # 头结点
                    temp = self._head
                    while temp.next != self._head:
                        temp = temp.next
                    temp.next = self._head = cur.next
                else:  # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:  # 尾节点
            if cur == self._head:  # 只有一个节点
                self._head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """查找元素是否存在"""
        if self.is_empty():
            return False
        else:
            cur = self._head
            while cur.next != self._head:
                if cur.elem == item:
                    return True
                cur = cur.next
            if cur.elem == item:
                return True
            return False

    def reverse(self):
        """单向循环链表逆序"""
        leng = self.length()
        if leng <= 1:
            return
        last = None
        while leng > 1:
            pre = None
            cur = self._head
            while cur.next != self._head:
                pre, cur = cur, cur.next
            if not last:
                last = cur
            cur.next, pre.next = pre, self._head
            leng -= 1
        self._head = pre.next = last

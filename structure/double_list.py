from structure.single_list import SingleList, SingleNode


class DoubleNode(SingleNode):
    """双向链表节点"""

    def __init__(self, elem):
        SingleNode.__init__(self, elem)
        self.pre = None

    def __repr__(self):
        return str(self.elem) + "(双向链表节点：前(" + str(self.pre.elem if self.pre else None) + "),后(" + str(self.next.elem if self.next else None) + "))"


class DoubleList(SingleList):
    """双向链表"""

    def traverse(self):
        """双向链表遍历"""
        print("-------双向链表遍历S--------")
        cur = self._head
        while cur:
            print(cur, end=", ")
            cur = cur.next
        print("\n-------双向链表遍历E--------")

    def add(self, item):
        """链表头部添加元素"""
        node = DoubleNode(item)
        node.next = self._head
        self._head = node
        if node.next:
            node.next.pre = node

    def append(self, item):
        """链表尾部添加元素"""
        node = DoubleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next, node.pre = node, cur

    def insert(self, pos, item):
        """链表指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < pos - 1:
                cur = cur.next
                count += 1
            node = DoubleNode(item)
            node.next, node.pre = cur.next, cur
            cur.next = node
            node.next.pre = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        while cur:
            if cur.elem == item:
                if cur == self._head:  # 头节点
                    self._head = cur.next
                    if cur.next:  # 不止一个节点
                        cur.next.pre = None
                elif not cur.next:  # 尾节点
                    cur.pre.next = None
                    cur.pre = None
                else:
                    cur.pre.next = cur.next
                    cur.next.pre = cur.pre
                break
            cur = cur.next

    def reverse(self):
        """双向链表逆序"""
        if self.length() <= 1:
            return
        cur = self._head
        while cur.next:
            temp = cur.next
            cur.next, cur.pre = cur.pre, cur.next
            cur = temp
        cur.next = cur.pre
        cur.pre = None
        self._head = cur

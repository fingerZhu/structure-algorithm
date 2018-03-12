class SingleNode(object):
    """单向链表节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None

    def __repr__(self):
        return str(self.elem) + "(单向链表节点：后(" + str(self.next.elem if self.next else None) + "))"


class SingleList(object):
    """单向链表"""

    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        cur = self._head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count

    def traverse(self):
        """单向链表遍历"""
        print("-------单向链表遍历S--------")
        cur = self._head
        while cur:
            print(cur, end=", ")
            cur = cur.next
        print("\n-------单向链表遍历E--------")

    def add(self, item):
        """链表头部添加元素"""
        node = SingleNode(item)
        node.next, self._head = self._head, node

    def append(self, item):
        """链表尾部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """链表指定位置添加元素"""
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
            node = SingleNode(item)
            node.next, pre.next = pre.next, node

    def remove(self, item):
        """删除节点"""
        pre = self._head
        if pre.elem == item:  # 头结点
            self._head = pre.next
        else:
            while pre.next:
                if pre.next.elem == item:
                    pre.next = pre.next.next
                    break
                pre = pre.next

    def search(self, item):
        """查找元素是否存在"""
        cur = self._head
        while cur:
            if cur.elem == item:
                return True
            cur = cur.next
        return False

    def reverse(self):
        leng = self.length()
        if leng <= 1:
            return
        last = None
        while leng > 1:
            pre = None
            cur = self._head
            while cur.next:
                pre, cur = cur, cur.next
            if not last:
                last = cur
            cur.next, pre.next = pre, None
            leng -= 1
        self._head = last

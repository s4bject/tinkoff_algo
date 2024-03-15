class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class F3:
    def __init__(self):
        self.root = None

    def add(self, i):
        self.root = self._insert(self.root, i)

    def _insert(self, node, i):
        if node is None:
            return TreeNode(i)

        if i < node.value:
            node.left = self._insert(node.left, i)
        elif i > node.value:
            node.right = self._insert(node.right, i)

        return node

    def next(self, i):
        result = -1
        node = self.root

        while node:
            if i <= node.value:
                result = node.value
                node = node.left
            elif i > node.value:
                node = node.right

        return result

n = int(input())
custom = F3()
operstack = []
for _ in range(n):
    operation, i = input().split()
    i = int(i)
    if operation == '+':
        if operstack and operstack[-1] == '?':
            custom.add((i+result) % 10**9)
        else:
            custom.add(i)
    elif operation == '?':
        result = custom.next(i)
        print(result)
    operstack.append(operation)
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(arr, 2 * v + 1, tl, tm)
            self.build(arr, 2 * v + 2, tm + 1, tr)
            self.tree[v] = self.tree[2 * v + 1] + self.tree[2 * v + 2]

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2 * v + 1, tl, tm, pos, new_val)
            else:
                self.update(2 * v + 2, tm + 1, tr, pos, new_val)
            self.tree[v] = self.tree[2 * v + 1] + self.tree[2 * v + 2]

    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        left_sum = self.query(2 * v + 1, tl, tm, l, min(r, tm))
        right_sum = self.query(2 * v + 2, tm + 1, tr, max(l, tm + 1), r)
        return left_sum + right_sum

n, m = map(int, input().split())
arr = list(map(int, input().split()))

segment_tree = SegmentTree(arr)

for _ in range(m):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        index, value = operation[1], operation[2]
        segment_tree.update(0, 0, n - 1, index, value)
    elif operation[0] == 2:
        left, right = operation[1], operation[2] - 1
        result = segment_tree.query(0, 0, n - 1, left, right)
        print(result)

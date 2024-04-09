class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [None] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = (arr[tl], 1)
        else:
            tm = (tl + tr) // 2
            self.build(arr, 2 * v + 1, tl, tm)
            self.build(arr, 2 * v + 2, tm + 1, tr)
            left_min, left_count = self.tree[2 * v + 1]
            right_min, right_count = self.tree[2 * v + 2]
            if left_min < right_min:
                self.tree[v] = (left_min, left_count)
            elif left_min > right_min:
                self.tree[v] = (right_min, right_count)
            else:
                self.tree[v] = (left_min, left_count + right_count)

    def query(self, v, tl, tr, l, r):
        if l > r:
            return (float('inf'), 0)
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        left_result = self.query(2 * v + 1, tl, tm, l, min(r, tm))
        right_result = self.query(2 * v + 2, tm + 1, tr, max(l, tm + 1), r)
        left_min, left_count = left_result
        right_min, right_count = right_result
        if left_min < right_min:
            return (left_min, left_count)
        elif left_min > right_min:
            return (right_min, right_count)
        else:
            return (left_min, left_count + right_count)

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = (new_val, 1)
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2 * v + 1, tl, tm, pos, new_val)
            else:
                self.update(2 * v + 2, tm + 1, tr, pos, new_val)
            left_min, left_count = self.tree[2 * v + 1]
            right_min, right_count = self.tree[2 * v + 2]
            if left_min < right_min:
                self.tree[v] = (left_min, left_count)
            elif left_min > right_min:
                self.tree[v] = (right_min, right_count)
            else:
                self.tree[v] = (left_min, left_count + right_count)

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
        print(result[0], result[1])

class SegmentTree:

  def __init__(self, n):
    self.n = n
    self.tree_sum = [0] * (4 * n)
    self.tree_sq = [0] * (4 * n)
    self.lazy = [0] * (4 * n)
    self.MOD = 10**9 + 7

  def _apply(self, node, l, r, val):
    # (v + val)^2 = v^2 + 2*v*val + val^2
    length = r - l + 1
    self.tree_sq[node] = (
        self.tree_sq[node]
        + 2 * val * self.tree_sum[node]
        + val * val * length
    ) % self.MOD
    self.tree_sum[node] = (
        self.tree_sum[node] + val * length
    ) % self.MOD
    self.lazy[node] = (self.lazy[node] + val) % self.MOD

  def _push(self, node, l, r):
    if self.lazy[node] != 0:
      mid = (l + r) // 2
      self._apply(2 * node, l, mid, self.lazy[node])
      self._apply(2 * node + 1, mid + 1, r, self.lazy[node])
      self.lazy[node] = 0

  def update(self, node, l, r, ql, qr, val):
    if ql <= l and r <= qr:
      self._apply(node, l, r, val)
      return
    self._push(node, l, r)
    mid = (l + r) // 2
    if ql <= mid:
      self.update(2 * node, l, mid, ql, qr, val)
    if qr > mid:
      self.update(2 * node + 1, mid + 1, r, ql, qr, val)
    self.tree_sum[node] = (
        self.tree_sum[2 * node] + self.tree_sum[2 * node + 1]
    ) % self.MOD
    self.tree_sq[node] = (
        self.tree_sq[2 * node] + self.tree_sq[2 * node + 1]
    ) % self.MOD

  def query_sq_sum(self):
    return self.tree_sq[1]


class Solution:

  def sumCounts(self, nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    st = SegmentTree(n)
    last_occurrence = {}
    total_sum = 0

    for j in range(n):
      val = nums[j]
      prev_idx = last_occurrence.get(val, -1)
      # Update range [prev_idx + 1, j] by adding 1
      st.update(1, 0, n - 1, prev_idx + 1, j, 1)
      last_occurrence[val] = j

      # Add the sum of squares of all subarrays ending at index j
      total_sum = (total_sum + st.query_sq_sum()) % MOD

    return total_sum
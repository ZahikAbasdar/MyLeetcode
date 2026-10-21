class Solution:

  def minOperations(self, s: str) -> int:
    # 1. If already sorted, 0 operations needed
    if s == "".join(sorted(s)):
      return 0

    # 2. If length is 2, since we can only sort a proper substring (length < len(s)),
    # we can only sort substrings of length 1, which do nothing.
    # Hence, impossible if not already sorted.
    if len(s) == 2:
      return -1

    min_char = min(s)
    max_char = max(s)

    # 3. If the minimum character is at the beginning (and not spanning the whole string)
    # OR the maximum character is at the end (and not spanning the whole string),
    # we can achieve it in 1 operation.
    if s[0] == min_char or s[-1] == max_char:
      return 1

    # 4. If the string contains any elements that are neither min_char nor max_char,
    # or if we can position them via proper prefixes/suffixes, it typically takes 3 operations,
    # but let's check the classic case structure:
    # If the first character is the unique maximum and the last character is the unique minimum,
    # it takes 3 operations. Otherwise, 2 operations.
    # More generally:
    # Check if a proper prefix contains a min_char or a proper suffix contains a max_char.
    has_min_in_proper_prefix = min_char in s[:-1]
    has_max_in_proper_suffix = max_char in s[1:]

    if not has_min_in_proper_prefix and not has_max_in_proper_suffix:
      return 3

    return 2
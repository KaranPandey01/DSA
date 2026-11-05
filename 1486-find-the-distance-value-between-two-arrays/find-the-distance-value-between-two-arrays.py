class Solution:
  def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    ans = 0

    import bisect

    for x in arr1:
      # Find the insertion point for x - d in arr2
      idx = bisect.bisect_left(arr2, x - d)
      # Check if the element at idx is within [x - d, x + d]
      if idx < len(arr2) and abs(arr2[idx] - x) <= d:
        continue
      # Check the previous element as well
      if idx > 0 and abs(arr2[idx - 1] - x) <= d:
        continue
      ans += 1

    return ans

## Use Sliding window technique with two pointers
import math

def smallest_subarray_with_given_sum(s, arr):
  # TODO: Write your code here
  start_ptr = 0
  subarray_size = math.inf
  inner_sum = arr[0]

  for end_ptr in range(1, len(arr)):
    inner_sum += arr[end_ptr]

    while inner_sum >= s:
      subarray_size = min(subarray_size, end_ptr-start_ptr+1)
      inner_sum -= arr[start_ptr]
      start_ptr += 1

  if subarray_size == math.inf:
    subarray_size = -1
  #if subarray_size == math.inf: pass else: subarray_size = -1
  return subarray_size

### LIST-1

# 1. first_last6
def first_last6(nums):
   if nums[0] == 6 or nums[-1] == 6:
     return True
   else:
     return False

# 2. same_first_last
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  else:
    return False

# 3. make_pi
def make_pi():
  pi_list = [3, 1, 4]
  return pi_list

# 4. common_end
def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  else:
    return False

# 5. sum3
def sum3(nums):
  return sum(nums)

# 6. rotate_left3
def rotate_left3(nums):
  return nums[1:] + nums[:1]

# 7. reverse3
def reverse3(nums):
  return nums[2:] + nums[1:2] + nums[:1:]

# 8. max_end3
def max_end3(nums):
  if nums[0] > nums[2]:
    return nums[0:1] + nums[0:1] + nums[0:1]
  else:
    return nums[2:] + nums[2:] + nums[2:]

# 9. sum2
def sum2(nums):
  return sum(nums[0:2])

# 10. middle_way
def middle_way(a, b):
  return a[1:2] + b[1:2]

# 11. make_ends
def make_ends(nums):
  return nums[0:1] + nums[-1:]

# 12. has23
def has23(nums):
  return 2 in nums or 3 in nums

#############################################
#############################################

### LIST-2

# 1. count_Evens
def count_evens(nums):
  evens = 0
  for num in nums:
    if num % 2 == 0:
      evens += 1
  return evens

# 2. big_diff
def big_diff(nums):
  return max(nums) - min(nums)

# 3. centered_average
def centered_average(nums):
  center_length = len(nums) - 2
  center_sum = sum(nums) - max(nums) - min(nums)
  return center_sum / center_length

# 4. sum13
def sum13(nums):
  if len(nums) == 0:
    return 0
  for i in range(len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i + 1 < len(nums):
        nums[i + 1] = 0
  return sum(nums)

# 5. has22
def has_22(nums: List[int]) -> bool:
    valid = False
    for i in range(len(nums) - 1):
        if nums[i] == 2:
            if nums[i+1] == 2:
                valid = True
                return valid
            else:
                valid = False
    return valid

# 6. lucky_13
def lucky_13(nums: List[int]) -> bool:
    return 1 not in nums and 3 not in nums

# 7. sum_28
def sum_28(nums: List[int]) -> bool:
    total = 0
    for i in range(len(nums)):
        if nums[i] == 2:
            total += 2
    return total == 8

# 8. more_14
def more_14(nums: List[int]) -> bool:
    ones = 0
    fours = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            ones += 1
        elif nums[i] == 4:
            fours += 1
    return ones > fours

# 9. only_14
def only_14(nums: List[int]) -> bool:
    for i in range(len(nums)):
        if nums[i] != 1 and nums[i] != 4:
            return False
    return True

# 10. no_14
def no_14(nums: List[int]) -> bool:
    return 1 not in nums or 4 not in nums


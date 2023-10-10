#Longest Consecutive Subsequence
def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        if n - 1 not in numSet:
            length = 0
            while n + length in numSet:
                length += 1
            longest = max(longest, length)
    return longest

print(longestConsecutive([1,9,3,4,2,20]))

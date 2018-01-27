from django.test import TestCase

# Create your tests here.

def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    lenl = len(nums)
    l = 0
    sumn = 0
    res = lenl + 1
    r = -1
    while (l < lenl):
        if sumn < s and r + 1 < lenl:
            r += 1
            sumn += nums[r]
        else:
            sumn -= nums[l]
            l += 1
        if sumn>=s:
            res = min(res, r - l + 1)
    if res == lenl + 1:
        return -1

    return res


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    strlen = len(s)
    l = 0
    r = 1
    subl = 0
    maxsubstr = ''
    while (l < strlen and r <= strlen):
        substr = s[l:r - 1]
        mark = s[r-1]
        if mark in substr:
            l += substr.index(mark) + 1
        else:
            r += 1
        substr = s[l:r -1]
        if len(substr) > subl:
            maxsubstr = s[l:r -1]
            subl = len(substr)

    return maxsubstr

t= 'cbc'
print(lengthOfLongestSubstring(t))
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

def bracket_match(bracket_string):
    tmp = []
    res = 0
    for i in bracket_string:
        if i == '(':
            tmp.append(i)
        elif i == ')' and len(tmp)!=0:
            tmp.pop()
        else:
            res +=1
    return res+len(tmp)



def solution(t):
    ind = []
    res = []
    deep = 10
    # ind 相当于一个hash table 记录当前路径下的index,初始化为0
    # res 用来存储结果并返回
    for i in range(deep):
        ind.append(0)
    #先暂时设置了最大深度是10，可变
    prev_len = 10
    for s in t:
        ss = s.split(' ');
        tmp_len = len(ss[0])
        ind[tmp_len-1]+=1
        tem = ''
        if tmp_len<prev_len:
            for i in range(tmp_len, prev_len):
                ind[i]=0
        prev_len = tmp_len
        for i in range(len(ss[0])):
            tem+=(str(ind[i])+'.')
        tem = tem[0:len(tem)-1]
        res+=[{"hn":tem, "title": ss[1]}]

    return res

t = ["# a", "## b", "## c", "### d", "# d", "## e", "### f", "## g"]
rest = [{"hn": "1", "title": "a"},
{"hn": "1.1", "title": "b"},
{"hn": "1.2", "title": "c"},
{"hn": "1.2.1", "title": "d"},
{"hn": "2", "title": "e"}]
aa = solution(t)
print(aa)
# for i in range(len(aa)):
#     assert(rest[i]['hn']==aa[i]['hn'] and rest[i]['title']==aa[i]['title'])
# def addDigits(num):
#
#     # 数根dr(n)=1+((n-1)mod 9)
#     res = 1 + ((num -1)%9)
#     return res
#
# assert(addDigits(38)==2)

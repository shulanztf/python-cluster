"""
力扣刷题
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
https://blog.csdn.net/qq_42570457/article/details/84348339
(python)给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的两个整数
"""


# 1、使用最容易理解的遍历数组进行查找
# 算法复杂度分析：时间复杂度：O(n^2)，空间复杂度：O(1)
def solution(nums, target):
    # print(nums,target)
    # 如果列表长度小于2，则直接结束
    if len(nums) < 2:
        return
    # 两次循环列表，分别对列表中的所有可能的数字进行相加
    # 循环两次列表对应的时间复杂度为O(n²)
    result = []
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append([i, j])
                # return [i,j]
    return result


nums = [2, 7, 11, 15, 1, 8]
target = 9
print(solution(nums, target))


# 2、使用哈希表，通过以空间换取速度的方式，我们可以将查找时间从 O(n)降低到 O(1)。在python中列表字典的即为哈希类型
# 算法复杂度分析：时间复杂度：O(n)，空间复杂度：O(n)
def solution2(nums, target):
    # print(nums,target)
    # 新建立一个空字典用来保存数值及其在列表中对应的索引
    dict1 = {}
    result = []
    # 遍历一遍列表对应的时间复杂度为O(n)
    for i in range(0, len(nums)):
        # 相减得到另一个数值
        num = target - nums[i]
        # 如果另一个数值不在字典中，则将第一个数值及其的索引报错在字典中
        # 因为在字典中查找的时间复杂度为O(1)，因此总时间复杂度为O(n)
        if num not in dict1:
            dict1[nums[i]] = i
        # 如果在字典中则返回
        else:
            # return [dict1[num],i]
            result.append([dict1[num], i])
    return result


print(solution2(nums, target))

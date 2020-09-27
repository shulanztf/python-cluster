"""
leetCode4. 寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
https://zhuanlan.zhihu.com/p/143240662    leetcode4. 寻找两个正序数组的中位数
"""
from typing import List


class Solution:
    """
    1：暴力解法
    也是归并排序的组合部分。
    这个时候我们先不要求解出本题的时间复杂度为：O(log(m+n))
    中位数：最中间的那个数（该数的左右个数相同）
    既然给出了两个正序数组，我们可以将这两个正序数组合成为一个正序的数组
    判断合成后的数组的长度为奇数还是偶数，进而求出中位数
    时间复杂度：O(m+n)，空间复杂度：O(m+n)
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = nums1 + nums2
        ans.sort()
        n = len(ans)
        if n % 2 == 0:
            print(ans[n // 2], ans[(n // 2) - 1])
            return float((ans[n // 2] + ans[(n // 2) - 1]) / 2)
        else:
            print(n // 2)
            return float(ans[n // 2])

    """
    方法二：二分查找递归
    """

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        # 找到nums1和nums2固定范围内的第t小的数，left1、right1、left2、right2为nums1和nums2的范围。
        def find(left1, right1, left2, right2, t):
            if left1 > right1:  # 此时其中一个数组已经无用，返回另一个数组的第t即可
                return nums2[left2 + t - 1]
            elif left2 > right2:  # 此时其中一个数组已经无用，返回另一个数组的第t即可
                return nums1[left1 + t - 1]

            if t == 1:  # 两数组都存在的递归结束条件，找最小的一个数
                return min(nums1[left1], nums2[left2])
            numm = t // 2  # 二分，向下取整，最多为t的一半
            # 处理其中一个数组范围不足numm的情况，length表示判断之后丢弃的数的个数
            length1 = min(numm, right1 - left1 + 1)
            length2 = min(numm, right2 - left2 + 1)
            # 判断left+length-1的两个元素大小，调整两个数组的范围以及第几小元素，进行递归
            if nums1[left1 + length1 - 1] <= nums2[left2 + length2 - 1]:
                return find(left1 + length1, right1, left2, right2, t - length1)
            else:
                return find(left1, right1, left2 + length2, right2, t - length2)

        m = len(nums1)
        n = len(nums2)
        # 初始判断，处理其中有一个为空的情况
        if m == 0:
            if n % 2 == 0:
                return float((nums2[n // 2] + nums2[(n // 2) - 1]) / 2)
            else:
                return float(nums2[n // 2])
        if n == 0:
            if m % 2 == 0:
                return float((nums1[m // 2] + nums1[(m // 2) - 1]) / 2)
            else:
                return float(nums1[m // 2])
        # ans = 0.0
        # 分两种情况讨论返回
        if (m + n) % 2 == 1: # 长度为奇数时
            k = (m + n + 1) // 2 # k向上取整
            ans = float(find(0, m - 1, 0, n - 1, k))
        else: # 长度为偶数时
            k = (m + n) // 2
            ans = (float(find(0, m - 1, 0, n - 1, k)) + float(find(0, m - 1, 0, n - 1, k + 1))) / 2
        return ans


nums1 = [1, 3]
nums2 = [2]
so = Solution()
# print(so.findMedianSortedArrays(nums1, nums2))
# print(so.findMedianSortedArrays1(nums1, nums2))

# nums3 = [1, 2]
# nums4 = [3, 4]
# print(so.findMedianSortedArrays1(nums3, nums4))

nums5 = [1,3,5,7,9]
nums6 = [2,4,6,8]
print(so.findMedianSortedArrays1(nums5, nums6))

# nums7 = [1,3,5,7,9,10,11]
# nums8 = [2,4,6,8]
# print(so.findMedianSortedArrays1(nums7, nums8))

# nums9 = [1,3,5,7]
# nums10 = [2,4,6,8]
# print(so.findMedianSortedArrays1(nums9, nums10))
# nums11 = [1,3,5,7,9,10]
# nums12 = [2,4,6,8]
# print(so.findMedianSortedArrays1(nums11, nums12))


# **1.**

------

## **中文版**
### [**两数之和**](https://leetcode-cn.com/problems/two-sum/)

- **难度：** 简单
- **标签：** 数组、哈希表
- **相似题目：** [*三数之和*](https://leetcode-cn.com/problems/3sum/)、[*四数之和*](https://leetcode-cn.com/problems/4sum/)、[*两数之和 II - 输入有序数组*](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)、[*两数之和 III - 数据结构设计*](https://leetcode-cn.com/problems/two-sum-iii-data-structure-design/)、[*和为K的子数组*](https://leetcode-cn.com/problems/subarray-sum-equals-k/)、[*两数之和 IV - 输入 BST*](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/)、[*小于 K 的两数之和*](https://leetcode-cn.com/problems/two-sum-less-than-k/)


### **题目：**

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。

 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

  

 **示例:**

 给定 nums = \[2, 7, 11, 15\], target = 9 因为 nums\[**0**\] + nums\[**1**\] = 2 + 7 = 9 所以返回 \[**0, 1**\]  


------


## **English**
### [**Two Sum**](https://leetcode-cn.com/problems/two-sum/)

- **Difficulty:** Easy
- **Topic Tag:** Array; Hash Table
- **Similar Questions:** [*3Sum*](https://leetcode-cn.com/problems/3sum/); [*4Sum*](https://leetcode-cn.com/problems/4sum/); [*Two Sum II - Input array is sorted*](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/); [*Two Sum III - Data structure design*](https://leetcode-cn.com/problems/two-sum-iii-data-structure-design/); [*Subarray Sum Equals K*](https://leetcode-cn.com/problems/subarray-sum-equals-k/); [*Two Sum IV - Input is a BST*](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/); [*Two Sum Less Than K*](https://leetcode-cn.com/problems/two-sum-less-than-k/)

### **Content**

Given an array of integers nums and an integer target, return *indices of the two numbers such that they add up to target*.

 You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

 You can return the answer in any order.

  

 **Example 1:**

  **Input:** nums = \[2,7,11,15\], target = 9 **Output:** \[0,1\] **Output:** Because nums\[0\] + nums\[1\] == 9, we return \[0, 1\].  **Example 2:**

  **Input:** nums = \[3,2,4\], target = 6 **Output:** \[1,2\]  **Example 3:**

  **Input:** nums = \[3,3\], target = 6 **Output:** \[0,1\]   

 **Constraints:**

 
 * 2 <= nums.length <= 105
 * -109 <= nums\[i\] <= 109
 * -109 <= target <= 109
 * **Only one valid answer exists.**
 
 


------


- **来源：** 力扣（LeetCode）
- **链接：** [两数之和](https://leetcode-cn.com/problems/two-sum/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [i for i in enumerate(nums)]
        nums.sort(key = lambda x: x[1])
        l = len(nums) - 1
        nmax = nums[-1][1]
        for i in range(l):
            ni = nums[i][1]
            if i > 0 and ni == pre:
                continue
            t = target - ni
            if t > nmax:
                pre = ni
                continue
            j = l
            while j > i:
                if t == nums[j][1]:
                    return [nums[i][0], nums[j][0]]
                j -= 1
            pre = ni
```



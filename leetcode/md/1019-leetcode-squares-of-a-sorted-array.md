# **1019.**

------

## **中文版**
### [**有序数组的平方**](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)

- **难度：** 简单
- **标签：** 数组、双指针
- **相似题目：** [*合并两个有序数组*](https://leetcode-cn.com/problems/merge-sorted-array/)、[*有序转化数组*](https://leetcode-cn.com/problems/sort-transformed-array/)


### **题目：**

给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

  

 **示例 1：**

 **输入：**\[-4,-1,0,3,10\] **输出：**\[0,1,9,16,100\]  **示例 2：**

 **输入：**\[-7,-3,2,3,11\] **输出：**\[4,9,9,49,121\]   

 **提示：**

 
 2. 1 <= A.length <= 10000
 4. -10000 <= A\[i\] <= 10000
 6. A 已按非递减顺序排序。
 
 


------


## **English**
### [**Squares of a Sorted Array**](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)

- **Difficulty:** Easy
- **Topic Tag:** Array; Two Pointers
- **Similar Questions:** [*Merge Sorted Array*](https://leetcode-cn.com/problems/merge-sorted-array/); [*Sort Transformed Array*](https://leetcode-cn.com/problems/sort-transformed-array/)

### **Content**

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

  

  **Example 1:**

  **Input:** \[-4,-1,0,3,10\] **Output:** \[0,1,9,16,100\]   **Example 2:**

  **Input:** \[-7,-3,2,3,11\] **Output:** \[4,9,9,49,121\]   

 **Note:**

 
 2. 1 <= A.length <= 10000
 4. -10000 <= A\[i\] <= 10000
 6. A is sorted in non-decreasing order.
 
  


------


- **来源：** 力扣（LeetCode）
- **链接：** [有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # 内存
#         A.sort(key=abs)
#         for i in range(len(A)):
#             A[i] = A[i] ** 2
#         return A
        i, j = 0, len(A) - 1
        left, right = A[i]**2, A[j]**2
        ans, end = [], right
        while i < j:
            if left > right:
                ans.append(left)
                i += 1
                left = A[i]**2
                end = right
            else:
                ans.append(right)
                j -= 1
                right = A[j]**2
                end = left
        ans.append(end)
        ans.reverse()
        return ans



solution = Solution()
inp = []

```



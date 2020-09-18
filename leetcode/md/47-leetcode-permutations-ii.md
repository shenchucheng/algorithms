# **47.**

------

## **中文版**
### [**全排列 II**](https://leetcode-cn.com/problems/permutations-ii/)

- **难度：** 中等
- **标签：** 回溯算法
- **相似题目：** [*下一个排列*](https://leetcode-cn.com/problems/next-permutation/)、[*全排列*](https://leetcode-cn.com/problems/permutations/)、[*回文排列 II*](https://leetcode-cn.com/problems/palindrome-permutation-ii/)、[*正方形数组的数目*](https://leetcode-cn.com/problems/number-of-squareful-arrays/)


### **题目：**

给定一个可包含重复数字的序列，返回所有不重复的全排列。

 **示例:**

 **输入:** \[1,1,2\] **输出:** \[ \[1,1,2\], \[1,2,1\], \[2,1,1\] \] 


------


## **English**
### [**Permutations II**](https://leetcode-cn.com/problems/permutations-ii/)

- **Difficulty:** Medium
- **Topic Tag:** Backtracking
- **Similar Questions:** [*Next Permutation*](https://leetcode-cn.com/problems/next-permutation/); [*Permutations*](https://leetcode-cn.com/problems/permutations/); [*Palindrome Permutation II*](https://leetcode-cn.com/problems/palindrome-permutation-ii/); [*Number of Squareful Arrays*](https://leetcode-cn.com/problems/number-of-squareful-arrays/)

### **Content**

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

 **Example:**

  **Input:** \[1,1,2\] **Output:** \[ \[1,1,2\], \[1,2,1\], \[2,1,1\] \]  


------


- **来源：** 力扣（LeetCode）
- **链接：** [全排列 II](https://leetcode-cn.com/problems/permutations-ii/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def wrap(*num):
            if len(nums) == 1:
                ans.append(list(num) + nums)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                v = nums.pop(i)
                wrap(*num, v)
                nums.insert(i, v)
        wrap()
        return ans



solution = Solution()
inp = [1,1,2]
solution.permuteUnique(inp)

```




    [[1, 1, 2], [1, 2, 1], [2, 1, 1]]



![image.png](attachment:aee1022f-ea66-45fe-94cb-e327213905fd.png)


```python

```

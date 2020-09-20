# **78.**

------

## **中文版**
### [**子集**](https://leetcode-cn.com/problems/subsets/)

- **难度：** 中等
- **标签：** 位运算、数组、回溯算法
- **相似题目：** [*子集 II*](https://leetcode-cn.com/problems/subsets-ii/)、[*列举单词的全部缩写*](https://leetcode-cn.com/problems/generalized-abbreviation/)、[*字母大小写全排列*](https://leetcode-cn.com/problems/letter-case-permutation/)


### **题目：**

给定一组**不含重复元素**的整数数组 *nums*，返回该数组所有可能的子集（幂集）。

 **说明：**解集不能包含重复的子集。

 **示例:**

 **输入:** nums = \[1,2,3\] **输出:** \[ \[3\], \[1\], \[2\], \[1,2,3\], \[1,3\], \[2,3\], \[1,2\], \[\] \] 


------


## **English**
### [**Subsets**](https://leetcode-cn.com/problems/subsets/)

- **Difficulty:** Medium
- **Topic Tag:** Bit Manipulation; Array; Backtracking
- **Similar Questions:** [*Subsets II*](https://leetcode-cn.com/problems/subsets-ii/); [*Generalized Abbreviation*](https://leetcode-cn.com/problems/generalized-abbreviation/); [*Letter Case Permutation*](https://leetcode-cn.com/problems/letter-case-permutation/)

### **Content**

Given a set of **distinct** integers, *nums*, return all possible subsets (the power set).

 **Note:** The solution set must not contain duplicate subsets.

 **Example:**

  **Input:** nums = \[1,2,3\] **Output:** \[ \[3\], \[1\], \[2\], \[1,2,3\], \[1,3\], \[2,3\], \[1,2\], \[\] \] 


------


- **来源：** 力扣（LeetCode）
- **链接：** [子集](https://leetcode-cn.com/problems/subsets/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def wrap(nums):
            if nums:
                ret = []
                n = nums.pop()
                for i in wrap(nums):
                    ret.append(i)
                    ret.append([n]+i)
                print(n, ret)
                return ret
                
            return [[]]                
            
        return wrap(nums)



solution = Solution()
inp = []
solution.subsets(inp)

```




    [[]]



![image.png](attachment:b84a6770-34a5-41ca-96ee-cb624e8ae1be.png)

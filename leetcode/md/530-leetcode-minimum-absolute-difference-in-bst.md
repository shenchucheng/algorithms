# **530.**

------

## **中文版**
### [**二叉搜索树的最小绝对差**](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/)

- **难度：** 简单
- **标签：** 树
- **相似题目：** [*数组中的 k-diff 数对*](https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/)


### **题目：**

给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

  

 **示例：**

 **输入：** 1 \ 3 / 2 **输出：** 1 **解释：** 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。   

 **提示：**

 
 * 树中至少有 2 个节点。
 * 本题与 783 <https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/> 相同
 
 


------


## **English**
### [**Minimum Absolute Difference in BST**](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/)

- **Difficulty:** Easy
- **Topic Tag:** Tree
- **Similar Questions:** [*K-diff Pairs in an Array*](https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/)

### **Content**

Given a binary search tree with non-negative values, find the minimum \[absolute difference\](https://en.wikipedia.org/wiki/Absolute_difference) between values of any two nodes.

 **Example:**

  **Input:** 1 \ 3 / 2 **Output:** 1 **Explanation:** The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).   

 **Note:**

 
 * There are at least two nodes in this BST.
 * This question is the same as 783: <https://leetcode.com/problems/minimum-distance-between-bst-nodes/>
 
 


------


- **来源：** 力扣（LeetCode）
- **链接：** [二叉搜索树的最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        pre, mini = -1, -1
        def wrap(root):
            if not root:
                return
            wrap(root.left)
            val = root.val
            nonlocal pre, mini
            if pre == -1:
                pass
            elif mini >= 0:
                mini = min(mini, val - pre)
            else:
                mini = val - pre 
            pre = val 
            wrap(root.right)
        wrap(root)
        return mini

solution = Solution()
inp = []

```



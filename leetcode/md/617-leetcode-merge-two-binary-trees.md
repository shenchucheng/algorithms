# **617.**

------

## **中文版**
### [**合并二叉树**](https://leetcode-cn.com/problems/merge-two-binary-trees/)

- **难度：** 简单
- **标签：** 树
- **相似题目：** 


### **题目：**

给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则**不为** NULL 的节点将直接作为新二叉树的节点。

 **示例 1:**

  **输入:** Tree 1 Tree 2 1 2 / \ / \ 3 2 1 3 / \ \ 5 4 7 **输出:** 合并后的树: 3 / \ 4 5 / \ \ 5 4 7  **注意:** 合并必须从两个树的根节点开始。

 


------


## **English**
### [**Merge Two Binary Trees**](https://leetcode-cn.com/problems/merge-two-binary-trees/)

- **Difficulty:** Easy
- **Topic Tag:** Tree
- **Similar Questions:** 

### **Content**

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

 You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

 **Example 1:**

  **Input:** Tree 1 Tree 2 1 2 / \ / \ 3 2 1 3 / \ \ 5 4 7 **Output:** Merged tree: 3 / \ 4 5 / \ \ 5 4 7   

 **Note:** The merging process must start from the root nodes of both trees.

 


------


- **来源：** 力扣（LeetCode）
- **链接：** [合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees/)
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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def merge(t1, t2):
            if t1 and t2:
                t3 = TreeNode(t1.val + t2.val)
                t3.left = merge(t1.left, t2.left)
                t3.right = merge(t1.right, t2.right)
                return t3 
            return t1 or t2 
        return merge(t1, t2)


solution = Solution()
inp = []

```



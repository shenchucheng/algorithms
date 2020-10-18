# **113.**

------

## **中文版**
### [**路径总和 II**](https://leetcode-cn.com/problems/path-sum-ii/)

- **难度：** 中等
- **标签：** 树、深度优先搜索
- **相似题目：** [*路径总和*](https://leetcode-cn.com/problems/path-sum/)、[*二叉树的所有路径*](https://leetcode-cn.com/problems/binary-tree-paths/)、[*路径总和 III*](https://leetcode-cn.com/problems/path-sum-iii/)、[*路径和 IV*](https://leetcode-cn.com/problems/path-sum-iv/)


### **题目：**

给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

 **说明:** 叶子节点是指没有子节点的节点。

 **示例:**  
 给定如下二叉树，以及目标和 sum = 22，

  **5** / \ **4** **8** / / \ **11** 13 **4** / \ / \ 7 **2** **5** 1  返回:

 \[ \[5,4,11,2\], \[5,8,4,5\] \]  


------


## **English**
### [**Path Sum II**](https://leetcode-cn.com/problems/path-sum-ii/)

- **Difficulty:** Medium
- **Topic Tag:** Tree; Depth-first Search
- **Similar Questions:** [*Path Sum*](https://leetcode-cn.com/problems/path-sum/); [*Binary Tree Paths*](https://leetcode-cn.com/problems/binary-tree-paths/); [*Path Sum III*](https://leetcode-cn.com/problems/path-sum-iii/); [*Path Sum IV*](https://leetcode-cn.com/problems/path-sum-iv/)

### **Content**

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

 **Note:** A leaf is a node with no children.

 **Example:**

 Given the below binary tree and sum = 22,

  **5** **/ \** **4 8** **/** / **\** **11** 13 **4** / **\** **/** \ 7 **2** **5** 1  Return:

  \[ \[5,4,11,2\], \[5,8,4,5\] \]  


------


- **来源：** 力扣（LeetCode）
- **链接：** [路径总和 II](https://leetcode-cn.com/problems/path-sum-ii/)
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
    def pathSum(self, root: TreeNode, _sum: int) -> List[List[int]]:
        nums = []
        def wrap(root, target):
            if not root:
                return
            if root.val == target:
                if not (root.left or root.right):
                    ans.append(nums+[root.val])
            val = root.val
            nums.append(val)
            wrap(root.left, target-val)
            wrap(root.right, target-val)
            nums.pop()
        ans = []
        wrap(root, _sum)
        return ans




solution = Solution()
inp = []

```



# **102.**

------

## **中文版**
### [**二叉树的层序遍历**](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

- **难度：** 中等
- **标签：** 树、广度优先搜索
- **相似题目：** [*二叉树的锯齿形层次遍历*](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)、[*二叉树的层次遍历 II*](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)、[*二叉树的最小深度*](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)、[*二叉树的垂直遍历*](https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal/)、[*二叉树的层平均值*](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/)、[*N叉树的层序遍历*](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)、[*二叉树的堂兄弟节点*](https://leetcode-cn.com/problems/cousins-in-binary-tree/)


### **题目：**

给你一个二叉树，请你返回其按 **层序遍历** 得到的节点值。 （即逐层地，从左到右访问所有节点）。

  

 **示例：**  
 二叉树：\[3,9,20,null,null,15,7\],
```
  3
 / \ 
9  20 
  / \ 
15   7  
```
  返回其层次遍历结果：

 \[ \[3\], \[9,20\], \[15,7\] \]  


------


## **English**
### [**Binary Tree Level Order Traversal**](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

- **Difficulty:** Medium
- **Topic Tag:** Tree; Breadth-first Search
- **Similar Questions:** [*Binary Tree Zigzag Level Order Traversal*](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/); [*Binary Tree Level Order Traversal II*](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/); [*Minimum Depth of Binary Tree*](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/); [*Binary Tree Vertical Order Traversal*](https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal/); [*Average of Levels in Binary Tree*](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/); [*N-ary Tree Level Order Traversal*](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/); [*Cousins in Binary Tree*](https://leetcode-cn.com/problems/cousins-in-binary-tree/)

### **Content**

Given a binary tree, return the *level order* traversal of its nodes' values. (ie, from left to right, level by level).

  For example:  
 Given binary tree \[3,9,20,null,null,15,7\],  
  3 / \ 9 20 / \ 15 7  

  return its level order traversal as:  
  \[ \[3\], \[9,20\], \[15,7\] \]  




------


- **来源：** 力扣（LeetCode）
- **链接：** [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        pass 
```



# **94.**

------

## **中文版**
### [**二叉树的中序遍历**](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

- **难度：** 中等
- **标签：** 栈、树、哈希表
- **相似题目：** [*验证二叉搜索树*](https://leetcode-cn.com/problems/validate-binary-search-tree/)、[*二叉树的前序遍历*](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)、[*二叉树的后序遍历*](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)、[*二叉搜索树迭代器*](https://leetcode-cn.com/problems/binary-search-tree-iterator/)、[*二叉搜索树中第K小的元素*](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/)、[*最接近的二叉搜索树值 II*](https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii/)、[*二叉搜索树中的顺序后继*](https://leetcode-cn.com/problems/inorder-successor-in-bst/)、[*将二叉搜索树转化为排序的双向链表*](https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)、[*二叉搜索树节点最小距离*](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/)


### **题目：**

给定一个二叉树，返回它的*中序* 遍历。

 **示例:**

 **输入:** \[1,null,2,3\] 1 \ 2 / 3 **输出:** \[1,3,2\] **进阶:** 递归算法很简单，你可以通过迭代算法完成吗？

 


------


## **English**
### [**Binary Tree Inorder Traversal**](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

- **Difficulty:** Medium
- **Topic Tag:** Stack; Tree; Hash Table
- **Similar Questions:** [*Validate Binary Search Tree*](https://leetcode-cn.com/problems/validate-binary-search-tree/); [*Binary Tree Preorder Traversal*](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/); [*Binary Tree Postorder Traversal*](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/); [*Binary Search Tree Iterator*](https://leetcode-cn.com/problems/binary-search-tree-iterator/); [*Kth Smallest Element in a BST*](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/); [*Closest Binary Search Tree Value II*](https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii/); [*Inorder Successor in BST*](https://leetcode-cn.com/problems/inorder-successor-in-bst/); [*Convert Binary Search Tree to Sorted Doubly Linked List*](https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/); [*Minimum Distance Between BST Nodes*](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/)

### **Content**

Given a binary tree, return the *inorder* traversal of its nodes' values.

 **Example:**

  **Input:** \[1,null,2,3\] 1 \ 2 / 3 **Output:** \[1,3,2\] **Follow up:** Recursive solution is trivial, could you do it iteratively?

 


------


- **来源：** 力扣（LeetCode）
- **链接：** [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        # 递归 38%
        def wrap(root):
            if root.left:
                wrap(root.left)
            ans.append(root.val)
            if root.right:
                wrap(root.right)
        # wrap(root) 以下是迭代 96.63%
        notuse = []
        while root or len(notuse) :
            while root:
                notuse.append(root)
                root = root.left
            root = notuse.pop()
            ans.append(root.val)
            root = root.right
        return ans 
```



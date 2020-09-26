# **106.**

------

## **中文版**
### [**从中序与后序遍历序列构造二叉树**](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

- **难度：** 中等
- **标签：** 树、深度优先搜索、数组
- **相似题目：** [*从前序与中序遍历序列构造二叉树*](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)


### **题目：**

根据一棵树的中序遍历与后序遍历构造二叉树。

 **注意:**  
 你可以假设树中没有重复的元素。

 例如，给出

 中序遍历 inorder = \[9,3,15,20,7\] 后序遍历 postorder = \[9,15,7,20,3\] 返回如下的二叉树：

  3 / \ 9 20 / \ 15 7  


------


## **English**
### [**Construct Binary Tree from Inorder and Postorder Traversal**](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

- **Difficulty:** Medium
- **Topic Tag:** Tree; Depth-first Search; Array
- **Similar Questions:** [*Construct Binary Tree from Preorder and Inorder Traversal*](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

### **Content**

Given inorder and postorder traversal of a tree, construct the binary tree.

 **Note:**  
 You may assume that duplicates do not exist in the tree.

 For example, given

  inorder = \[9,3,15,20,7\] postorder = \[9,15,7,20,3\] Return the following binary tree:

  3 / \ 9 20 / \ 15 7  


------


- **来源：** 力扣（LeetCode）
- **链接：** [从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def dfs(in_l, in_r, post_l, post_r):
            if post_l < post_r:
                return None
            inorder_root = Hash[postorder[post_l]]

            root = TreeNode(postorder[post_l])
            subtree_size = in_r - inorder_root
            root.right = dfs(inorder_root+1, in_r, post_l-1, post_l-subtree_size)
            root.left = dfs(in_l, inorder_root-1, post_l-subtree_size-1, post_r)
            return root

        Hash = {key:value for value, key in enumerate(inorder)}
        return dfs(0, len(inorder)-1, len(postorder)-1, 0)




solution = Solution()
inp = []

```

[参考链接](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/di-gui-jian-shu-by-yi-wen-statistics/)

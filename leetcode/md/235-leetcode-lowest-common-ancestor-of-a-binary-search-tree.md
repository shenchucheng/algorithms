# **235.**

------

## **中文版**
### [**二叉搜索树的最近公共祖先**](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

- **难度：** 简单
- **标签：** 树
- **相似题目：** [*二叉树的最近公共祖先*](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)、[*最小公共区域*](https://leetcode-cn.com/problems/smallest-common-region/)


### **题目：**

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

 \[百度百科\](https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin)中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

 例如，给定如下二叉搜索树: root = \[6,2,8,0,4,7,9,null,null,3,5\]

 !\[\](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png)

  

 **示例 1:**

 **输入:** root = \[6,2,8,0,4,7,9,null,null,3,5\], p = 2, q = 8 **输出:** 6 **解释:** 节点 2 和节点 8 的最近公共祖先是 6。  **示例 2:**

 **输入:** root = \[6,2,8,0,4,7,9,null,null,3,5\], p = 2, q = 4 **输出:** 2 **解释:** 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。  

 **说明:**

 
 * 所有节点的值都是唯一的。
 * p、q 为不同节点且均存在于给定的二叉搜索树中。
 
 


------


## **English**
### [**Lowest Common Ancestor of a Binary Search Tree**](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

- **Difficulty:** Easy
- **Topic Tag:** Tree
- **Similar Questions:** [*Lowest Common Ancestor of a Binary Tree*](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/); [*Smallest Common Region*](https://leetcode-cn.com/problems/smallest-common-region/)

### **Content**

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

 According to the \[definition of LCA on Wikipedia\](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

 Given binary search tree: root = \[6,2,8,0,4,7,9,null,null,3,5\]

 !\[\](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)  

 **Example 1:**

  **Input:** root = \[6,2,8,0,4,7,9,null,null,3,5\], p = 2, q = 8 **Output:** 6 **Explanation:** The LCA of nodes 2 and 8 is 6.  **Example 2:**

  **Input:** root = \[6,2,8,0,4,7,9,null,null,3,5\], p = 2, q = 4 **Output:** 2 **Explanation:** The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.   

 **Constraints:**

 
 * All of the nodes' values will be unique.
 * p and q are different and both values will exist in the BST.
 
 


------


- **来源：** 力扣（LeetCode）
- **链接：** [二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            q, p = p, q
        p, q = p.val, q.val
        def wrap(root):
            r = root.val
            if p <= r <= q:
                return root
            if r < p:
                return wrap(root.right)
            return wrap(root.left)
        return wrap(root)



solution = Solution()
inp = []

```

![image.png](attachment:9d7d80d7-8b34-42f6-a660-1203e515f8eb.png)

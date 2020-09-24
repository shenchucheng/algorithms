# **501.**

------

## **中文版**
### [**二叉搜索树中的众数**](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/)

- **难度：** 简单
- **标签：** 树
- **相似题目：** [*验证二叉搜索树*](https://leetcode-cn.com/problems/validate-binary-search-tree/)


### **题目：**

给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

 假定 BST 有如下定义：

 
 * 结点左子树中所含结点的值小于等于当前结点的值
 * 结点右子树中所含结点的值大于等于当前结点的值
 * 左子树和右子树都是二叉搜索树
 
 例如：  
 给定 BST \[1,null,2,2\],

  1 \ 2 / 2  返回\[2\].

 **提示**：如果众数超过1个，不需考虑输出顺序

 **进阶：**你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

 


------


## **English**
### [**Find Mode in Binary Search Tree**](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/)

- **Difficulty:** Easy
- **Topic Tag:** Tree
- **Similar Questions:** [*Validate Binary Search Tree*](https://leetcode-cn.com/problems/validate-binary-search-tree/)

### **Content**

Given a binary search tree (BST) with duplicates, find all the \[mode(s)\](https://en.wikipedia.org/wiki/Mode_(statistics)) (the most frequently occurred element) in the given BST.

 Assume a BST is defined as follows:

 
 * The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
 * The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
 * Both the left and right subtrees must also be binary search trees.
 
  

 For example:  
 Given BST \[1,null,2,2\],

  1 \ 2 / 2   

 return \[2\].

 **Note:** If a tree has more than one mode, you can return them in any order.

 **Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

 


------


- **来源：** 力扣（LeetCode）
- **链接：** [二叉搜索树中的众数](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans, cnum, ctimes, mtimes = [], None, 0, 0
        def wrap2(val):
            nonlocal ans, cnum, ctimes, mtimes
            if val == cnum:
                ctimes += 1
            else:
                cnum = val
                ctimes = 1
            if ctimes == mtimes:
                ans.append(cnum)
            elif ctimes > mtimes:
                ans = [val]
                mtimes = ctimes

        def wrap(root):
            if not root:
                return
            wrap(root.left)
            wrap2(root.val)
            wrap(root.right)
        wrap(root)
        return ans




solution = Solution()
inp = []

```



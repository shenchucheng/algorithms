# **226.**

------

## **中文版**
### [**翻转二叉树**](https://leetcode-cn.com/problems/invert-binary-tree/)

- **难度：** 简单
- **标签：** 树
- **相似题目：** 


### **题目：**

翻转一棵二叉树。

 **示例：**

 输入：

  4 / \ 2 7 / \ / \ 1 3 6 9 输出：

  4 / \ 7 2 / \ / \ 9 6 3 1 **备注:**  
 这个问题是受到 \[Max Howell\](https://twitter.com/mxcl) 的 \[原问题\](https://twitter.com/mxcl/status/608682016205344768) 启发的 ：

 
> 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。 


------


## **English**
### [**Invert Binary Tree**](https://leetcode-cn.com/problems/invert-binary-tree/)

- **Difficulty:** Easy
- **Topic Tag:** Tree
- **Similar Questions:** 

### **Content**

Invert a binary tree.

 **Example:**

 Input:

  4 / \ 2 7 / \ / \ 1 3 6 9 Output:

  4 / \ 7 2 / \ / \ 9 6 3 1 **Trivia:**  
 This problem was inspired by \[this original tweet\](https://twitter.com/mxcl/status/608682016205344768) by \[Max Howell\](https://twitter.com/mxcl):

 
> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off. 


------


- **来源：** 力扣（LeetCode）
- **链接：** [翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def reverse(root):
            if root:
                root.right, root.left = root.left,root.right
                reverse(root.left)
                reverse(root.right)
        reverse(root)
        return root             
```



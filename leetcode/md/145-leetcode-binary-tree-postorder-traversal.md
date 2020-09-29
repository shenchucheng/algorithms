# **145.**

------

## **中文版**
### [**二叉树的后序遍历**](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)

- **难度：** 中等
- **标签：** 栈、树
- **相似题目：** [*二叉树的中序遍历*](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)、[*N叉树的后序遍历*](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)


### **题目：**

给定一个二叉树，返回它的 *后序* 遍历。

 **示例:**

 **输入:** \[1,null,2,3\] 1 \ 2 / 3 **输出:** \[3,2,1\] **进阶:** 递归算法很简单，你可以通过迭代算法完成吗？

 


------


## **English**
### [**Binary Tree Postorder Traversal**](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)

- **Difficulty:** Medium
- **Topic Tag:** Stack; Tree
- **Similar Questions:** [*Binary Tree Inorder Traversal*](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/); [*N-ary Tree Postorder Traversal*](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)

### **Content**

Given the root of a binary tree, return *the postorder traversal of its nodes' values*.

  

 **Example 1:**

 !\[\](https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg)  **Input:** root = \[1,null,2,3\] **Output:** \[3,2,1\]  **Example 2:**

  **Input:** root = \[\] **Output:** \[\]  **Example 3:**

  **Input:** root = \[1\] **Output:** \[1\]  **Example 4:**

 !\[\](https://assets.leetcode.com/uploads/2020/08/28/pre3.jpg)  **Input:** root = \[1,2\] **Output:** \[2,1\]  **Example 5:**

 !\[\](https://assets.leetcode.com/uploads/2020/08/28/pre2.jpg)  **Input:** root = \[1,null,2\] **Output:** \[2,1\]   

 **Constraints:**

 
 * The number of the nodes in the tree is in the range \[0, 100\].
 * -100 <= Node.val <= 100
 
  

 **Follow up:**

 Recursive solution is trivial, could you do it iteratively?

  

 


------


- **来源：** 力扣（LeetCode）
- **链接：** [二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []   # 用来存储后序遍历节点的值
        stack = []  
        node = root
        while stack or node:
            while node:
                stack.append(node)  # 第一次入栈的是根节点
                #判断当前节点的左子树是否存在，若存在则持续左下行，若不存在就转向右子树
                node = node.left if node.left is not None else node.right
            #循环结束说明走到了叶子节点，没有左右子树了，该叶子节点即为当前栈顶元素，应该访问了
            node = stack.pop() # 取出栈顶元素进行访问
            res.append(node.val) # 将栈顶元素也即当前节点的值添加进res
            # （下面的stack[-1]是执行完上面那句取出栈顶元素后的栈顶元素）
            if stack and stack[-1].left == node: #若栈不为空且当前节点是栈顶元素的左节点
                node = stack[-1].right   ## 则转向遍历右节点
            else:
                node = None  # 没有左子树或右子树，强迫退栈
        return res        




solution = Solution()
inp = []

```



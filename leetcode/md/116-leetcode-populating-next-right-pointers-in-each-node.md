# **116.**

------

## **中文版**
### [**填充每个节点的下一个右侧节点指针**](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)

- **难度：** 中等
- **标签：** 树、深度优先搜索
- **相似题目：** [*填充每个节点的下一个右侧节点指针 II*](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)、[*二叉树的右视图*](https://leetcode-cn.com/problems/binary-tree-right-side-view/)


### **题目：**

给定一个**完美二叉树**，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

 struct Node { int val; Node *left; Node *right; Node *next; } 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

 初始状态下，所有 next 指针都被设置为 NULL。

  

 **示例：**

 !\[\](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/116_sample.png)

 **输入：**{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1} **输出：**{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1} **解释：**给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。   

 **提示：**

 
 * 你只能使用常量级额外空间。
 * 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 
 


------


## **English**
### [**Populating Next Right Pointers in Each Node**](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)

- **Difficulty:** Medium
- **Topic Tag:** Tree; Depth-first Search
- **Similar Questions:** [*Populating Next Right Pointers in Each Node II*](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/); [*Binary Tree Right Side View*](https://leetcode-cn.com/problems/binary-tree-right-side-view/)

### **Content**

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

  struct Node { int val; Node *left; Node *right; Node *next; }  Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

 Initially, all next pointers are set to NULL.

  

 **Follow up:**

 
 * You may only use constant extra space.
 * Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 
  

 **Example 1:**

 !\[\](https://assets.leetcode.com/uploads/2019/02/14/116_sample.png)

  **Input:** root = \[1,2,3,4,5,6,7\] **Output:** \[1,#,2,3,#,4,5,6,7,#\] **Explanation:** Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.   

 **Constraints:**

 
 * The number of nodes in the given tree is less than 4096.
 * -1000 <= node.val <= 1000
 
 


------


- **来源：** 力扣（LeetCode）
- **链接：** [填充每个节点的下一个右侧节点指针](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        root.next = None
        index = root
        while 1:
            head = index.left
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                    head = head.next
                else:
                    head.right.next = None
                    index = index.left
        return root
    
solution = Solution()
inp = []

```



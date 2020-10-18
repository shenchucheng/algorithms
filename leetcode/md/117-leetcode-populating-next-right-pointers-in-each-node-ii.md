# **117.**

------

## **中文版**
### [**填充每个节点的下一个右侧节点指针 II**](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)

- **难度：** 中等
- **标签：** 树、深度优先搜索
- **相似题目：** [*填充每个节点的下一个右侧节点指针*](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)


### **题目：**

给定一个二叉树

 struct Node { int val; Node *left; Node *right; Node *next; } 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

 初始状态下，所有 next 指针都被设置为 NULL。

  

 **进阶：**

 
 * 你只能使用常量级额外空间。
 * 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 
  

 **示例：**

 !\[\](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/117_sample.png)

 **输入**：root = \[1,2,3,4,5,null,7\] **输出：**\[1,#,2,3,#,4,5,7,#\] **解释：**给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。  

 **提示：**

 
 * 树中的节点数小于 6000
 * -100 <= node.val <= 100
 
  

 
 
 


------


## **English**
### [**Populating Next Right Pointers in Each Node II**](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)

- **Difficulty:** Medium
- **Topic Tag:** Tree; Depth-first Search
- **Similar Questions:** [*Populating Next Right Pointers in Each Node*](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)

### **Content**

Given a binary tree

  struct Node { int val; Node *left; Node *right; Node *next; }  Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

 Initially, all next pointers are set to NULL.

  

 **Follow up:**

 
 * You may only use constant extra space.
 * Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 
  

 **Example 1:**

 !\[\](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)

  **Input:** root = \[1,2,3,4,5,null,7\] **Output:** \[1,#,2,3,#,4,5,7,#\] **Explanation:** Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.   

 **Constraints:**

 
 * The number of nodes in the given tree is less than 6000.
 * -100 <= node.val <= 100
 
 


------


- **来源：** 力扣（LeetCode）
- **链接：** [填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)
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
    def connect(self, root):
        if not root:
            return root
        root.next = None
        start = root 
        while start:
            paths = gen(start)
            start = start1 = next(paths)
            if start:
                while start1:
                    nextNode = next(paths)
                    start1.next = nextNode
                    start1 = nextNode
            else:
                break
        return root

def gen(root: None):
    while 1:
        if root.left:
            yield root.left
        if root.right:
            yield root.right
        if root.next:
            root = root.next
        else:
            yield None
        




solution = Solution()
inp = []

```

![image.png](attachment:152ee32b-a761-4c02-a18c-242a1f395690.png)

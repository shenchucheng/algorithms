# **24.**

------

## **中文版**
### [**两两交换链表中的节点**](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

- **难度：** 中等
- **标签：** 链表
- **相似题目：** [*K 个一组翻转链表*](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)


### **题目：**

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

 **你不能只是单纯的改变节点内部的值**，而是需要实际的进行节点交换。

  

 **示例:**

 给定 1->2->3->4, 你应该返回 2->1->4->3.  


------


## **English**
### [**Swap Nodes in Pairs**](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

- **Difficulty:** Medium
- **Topic Tag:** Linked List
- **Similar Questions:** [*Reverse Nodes in k-Group*](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)

### **Content**

Given a linked list, swap every two adjacent nodes and return its head.

 You may **not** modify the values in the list's nodes. Only nodes itself may be changed.

  

 **Example 1:**

 !\[\](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)  **Input:** head = \[1,2,3,4\] **Output:** \[2,1,4,3\]  **Example 2:**

  **Input:** head = \[\] **Output:** \[\]  **Example 3:**

  **Input:** head = \[1\] **Output:** \[1\]   

 **Constraints:**

 
 * The number of nodes in the list is in the range \[0, 100\].
 * 0 <= Node.val <= 100
 
 


------


- **来源：** 力扣（LeetCode）
- **链接：** [两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def wrap(head):
            if head and head.next:
                temp = head.next.next
                head, head.next = head.next, head
                head.next.next = wrap(temp)
            return head
        return wrap(head)


solution = Solution()
inp = []

```



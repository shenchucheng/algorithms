# **19.**

------

## **中文版**
### [**删除链表的倒数第N个节点**](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

- **难度：** 中等
- **标签：** 链表、双指针
- **相似题目：** 


### **题目：**

给定一个链表，删除链表的倒数第 *n* 个节点，并且返回链表的头结点。

 **示例：**

 给定一个链表: **1->2->3->4->5**, 和 ***n* = 2**. 当删除了倒数第二个节点后，链表变为 **1->2->3->5**.  **说明：**

 给定的 *n* 保证是有效的。

 **进阶：**

 你能尝试使用一趟扫描实现吗？

 


------


## **English**
### [**Remove Nth Node From End of List**](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

- **Difficulty:** Medium
- **Topic Tag:** Linked List; Two Pointers
- **Similar Questions:** 

### **Content**

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 **Follow up:** Could you do this in one pass?

  

 **Example 1:**

 !\[\](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)  **Input:** head = \[1,2,3,4,5\], n = 2 **Output:** \[1,2,3,5\]  **Example 2:**

  **Input:** head = \[1\], n = 1 **Output:** \[\]  **Example 3:**

  **Input:** head = \[1,2\], n = 1 **Output:** \[1\]   

 **Constraints:**

 
 * The number of nodes in the list is sz.
 * 1 <= sz <= 30
 * 0 <= Node.val <= 100
 * 1 <= n <= sz
 
 


------


- **来源：** 力扣（LeetCode）
- **链接：** [删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(next=head)
        head1 = head2 = pre
        for i in range(n):
            head2 = head2.next
        while head2.next:
            head2 = head2.next
            head1 = head1.next
        head1.next = head1.next.next
        return pre.next

solution = Solution()
inp = []

```



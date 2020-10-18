# **141.**

------

## **中文版**
### [**环形链表**](https://leetcode-cn.com/problems/linked-list-cycle/)

- **难度：** 简单
- **标签：** 链表、双指针
- **相似题目：** [*环形链表 II*](https://leetcode-cn.com/problems/linked-list-cycle-ii/)、[*快乐数*](https://leetcode-cn.com/problems/happy-number/)


### **题目：**

给定一个链表，判断链表中是否有环。

 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。**注意：pos 不作为参数进行传递**，仅仅是为了标识链表的实际情况。

 如果链表中存在环，则返回 true 。 否则，返回 false 。

  

 **进阶：**

 你能用 *O(1)*（即，常量）内存解决此问题吗？

  

 **示例 1：**

 !\[\](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

 **输入：**head = \[3,2,0,-4\], pos = 1 **输出：**true **解释：**链表中有一个环，其尾部连接到第二个节点。  **示例 2：**

 !\[\](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

 **输入：**head = \[1,2\], pos = 0 **输出：**true **解释：**链表中有一个环，其尾部连接到第一个节点。  **示例 3：**

 !\[\](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

 **输入：**head = \[1\], pos = -1 **输出：**false **解释：**链表中没有环。   

 **提示：**

 
 * 链表中节点的数目范围是 \[0, 104\]
 * -105 <= Node.val <= 105
 * pos 为 -1 或者链表中的一个 **有效索引** 。
 
 


------


## **English**
### [**Linked List Cycle**](https://leetcode-cn.com/problems/linked-list-cycle/)

- **Difficulty:** Easy
- **Topic Tag:** Linked List; Two Pointers
- **Similar Questions:** [*Linked List Cycle II*](https://leetcode-cn.com/problems/linked-list-cycle-ii/); [*Happy Number*](https://leetcode-cn.com/problems/happy-number/)

### **Content**

Given head, the head of a linked list, determine if the linked list has a cycle in it.

 There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. **Note that pos is not passed as a parameter**.

 Return true *if there is a cycle in the linked list*. Otherwise, return false.

 **Follow up:**

 Can you solve it using O(1) (i.e. constant) memory?

  

 **Example 1:**

 !\[\](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)  **Input:** head = \[3,2,0,-4\], pos = 1 **Output:** true **Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).  **Example 2:**

 !\[\](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)  **Input:** head = \[1,2\], pos = 0 **Output:** true **Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.  **Example 3:**

 !\[\](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)  **Input:** head = \[1\], pos = -1 **Output:** false **Explanation:** There is no cycle in the linked list.   

 **Constraints:**

 
 * The number of the nodes in the list is in the range \[0, 104\].
 * -105 <= Node.val <= 105
 * pos is -1 or a **valid index** in the linked-list.
 
 


------


- **来源：** 力扣（LeetCode）
- **链接：** [环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head:
            slow = head
            fast = head.next
        else:
            return False
        while fast != slow:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return False
        return True
        




solution = Solution()
inp = []

```

![image.png](attachment:86b69950-fa80-49c7-9a2f-0d3a5b86ff56.png)

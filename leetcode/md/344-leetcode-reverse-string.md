# **344.**

------

## **中文版**
### [**反转字符串**](https://leetcode-cn.com/problems/reverse-string/)

- **难度：** 简单
- **标签：** 双指针、字符串
- **相似题目：** [*反转字符串中的元音字母*](https://leetcode-cn.com/problems/reverse-vowels-of-a-string/)、[*反转字符串 II*](https://leetcode-cn.com/problems/reverse-string-ii/)


### **题目：**

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char\[\] 的形式给出。

 不要给另外的数组分配额外的空间，你必须**\[原地\](https://baike.baidu.com/item/原地算法)修改输入数组**、使用 O(1) 的额外空间解决这一问题。

 你可以假设数组中的所有字符都是 \[ASCII\](https://baike.baidu.com/item/ASCII) 码表中的可打印字符。

  

 **示例 1：**

 **输入：**\["h","e","l","l","o"\] **输出：**\["o","l","l","e","h"\]  **示例 2：**

 **输入：**\["H","a","n","n","a","h"\] **输出：**\["h","a","n","n","a","H"\] 


------


## **English**
### [**Reverse String**](https://leetcode-cn.com/problems/reverse-string/)

- **Difficulty:** Easy
- **Topic Tag:** Two Pointers; String
- **Similar Questions:** [*Reverse Vowels of a String*](https://leetcode-cn.com/problems/reverse-vowels-of-a-string/); [*Reverse String II*](https://leetcode-cn.com/problems/reverse-string-ii/)

### **Content**

Write a function that reverses a string. The input string is given as an array of characters char\[\].

 Do not allocate extra space for another array, you must do this by **modifying the input array \[in-place\](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

 You may assume all the characters consist of \[printable ascii characters\](https://en.wikipedia.org/wiki/ASCII#Printable_characters).

  

  **Example 1:**

  **Input:** \["h","e","l","l","o"\] **Output:** \["o","l","l","e","h"\]   **Example 2:**

  **Input:** \["H","a","n","n","a","h"\] **Output:** \["h","a","n","n","a","H"\]    


------


- **来源：** 力扣（LeetCode）
- **链接：** [反转字符串](https://leetcode-cn.com/problems/reverse-string/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 方法一
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
        # 方法二
        l = len(s) - 1
        for i in range((l+1)//2):
            s[i], s[l-i] = s[l-i], s[i]


solution = Solution()
inp = []

```



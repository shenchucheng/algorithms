# **874.**

------

## **中文版**
### [**比较含退格的字符串**](https://leetcode-cn.com/problems/backspace-string-compare/)

- **难度：** 简单
- **标签：** 栈、双指针
- **相似题目：** 


### **题目：**

给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

 **注意：**如果对空文本输入退格字符，文本继续为空。

  

 **示例 1：**

 **输入：**S = "ab#c", T = "ad#c" **输出：**true **解释：**S 和 T 都会变成 “ac”。  **示例 2：**

 **输入：**S = "ab##", T = "c#d#" **输出：**true **解释：**S 和 T 都会变成 “”。  **示例 3：**

 **输入：**S = "a##c", T = "#a#c" **输出：**true **解释：**S 和 T 都会变成 “c”。  **示例 4：**

 **输入：**S = "a#c", T = "b" **输出：**false **解释：**S 会变成 “c”，但 T 仍然是 “b”。  

 **提示：**

 
 2. 1 <= S.length <= 200
 4. 1 <= T.length <= 200
 6. S 和 T 只含有小写字母以及字符 '#'。
 
  

 **进阶：**

 
 * 你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
 
  

 


------


## **English**
### [**Backspace String Compare**](https://leetcode-cn.com/problems/backspace-string-compare/)

- **Difficulty:** Easy
- **Topic Tag:** Stack; Two Pointers
- **Similar Questions:** 

### **Content**

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

 Note that after backspacing an empty text, the text will continue empty.

  **Example 1:**

  **Input:** S = "ab#c", T = "ad#c" **Output:** true **Explanation**: Both S and T become "ac".   **Example 2:**

  **Input:** S = "ab##", T = "c#d#" **Output:** true **Explanation**: Both S and T become "".   **Example 3:**

  **Input:** S = "a##c", T = "#a#c" **Output:** true **Explanation**: Both S and T become "c".   **Example 4:**

  **Input:** S = "a#c", T = "b" **Output:** false **Explanation**: S becomes "c" while T becomes "b".  **Note**:

 
 * 1 <= S.length <= 200
 * 1 <= T.length <= 200
 * S and T only contain lowercase letters and '#' characters.
 
 **Follow up:**

 
 * Can you solve it in O(N) time and O(1) space?
 
     


------


- **来源：** 力扣（LeetCode）
- **链接：** [比较含退格的字符串](https://leetcode-cn.com/problems/backspace-string-compare/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # s = t = ''
        # for i in S:
        #     if i == '#':
        #         s = s[:-1]
        #     else:
        #         s += i
        # for i in T:
        #     if i == '#':
        #         t = t[:-1]
        #     else:
        #         t += i
        # return s == t
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        
        return True




solution = Solution()
inp = []

```



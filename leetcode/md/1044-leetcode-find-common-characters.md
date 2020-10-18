# **1044.**

------

## **中文版**
### [**查找常用字符**](https://leetcode-cn.com/problems/find-common-characters/)

- **难度：** 简单
- **标签：** 数组、哈希表
- **相似题目：** [*两个数组的交集 II*](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)


### **题目：**

给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（**包括重复字符**）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

 你可以按任意顺序返回答案。

  

 **示例 1：**

 **输入：**\["bella","label","roller"\] **输出：**\["e","l","l"\]  **示例 2：**

 **输入：**\["cool","lock","cook"\] **输出：**\["c","o"\]   

 **提示：**

 
 2. 1 <= A.length <= 100
 4. 1 <= A\[i\].length <= 100
 6. A\[i\]\[j\] 是小写字母
 
 


------


## **English**
### [**Find Common Characters**](https://leetcode-cn.com/problems/find-common-characters/)

- **Difficulty:** Easy
- **Topic Tag:** Array; Hash Table
- **Similar Questions:** [*Intersection of Two Arrays II*](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)

### **Content**

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list **(including duplicates)**. For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

 You may return the answer in any order.

  

  **Example 1:**

  **Input:** \["bella","label","roller"\] **Output:** \["e","l","l"\]   **Example 2:**

  **Input:** \["cool","lock","cook"\] **Output:** \["c","o"\]   

 **Note:**

 
 2. 1 <= A.length <= 100
 4. 1 <= A\[i\].length <= 100
 6. A\[i\]\[j\] is a lowercase letter
 
  


------


- **来源：** 力扣（LeetCode）
- **链接：** [查找常用字符](https://leetcode-cn.com/problems/find-common-characters/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        empd = {}
        for i in A[0]:
            try:
                tempd[i][0] += 1
            except:
                tempd[i] = [1,0]
        for i in A[1:]:
            for j in i:
                try:
                    tempd[j][1] += 1
                except:
                    continue
            for k, v in list(tempd.items()):
                if v[1]:
                    v = [min(v), 0]
                    tempd[k] = v
                else:
                    tempd.pop(k)
        l = []
        for k, v in tempd.items():
            l = l + list(k*v[0])
        return l
solution = Solution()
inp = []

```



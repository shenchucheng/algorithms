# **79.**

------

## **中文版**
### [**单词搜索**](https://leetcode-cn.com/problems/word-search/)

- **难度：** 中等
- **标签：** 数组、回溯算法
- **相似题目：** [*单词搜索 II*](https://leetcode-cn.com/problems/word-search-ii/)


### **题目：**

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

  

 **示例:**

 board = \[ \['A','B','C','E'\], \['S','F','C','S'\], \['A','D','E','E'\] \] 给定 word = "**ABCCED**", 返回 **true** 给定 word = "**SEE**", 返回 **true** 给定 word = "**ABCB**", 返回 **false**  

 **提示：**

 
 * board 和 word 中只包含大写和小写英文字母。
 * 1 <= board.length <= 200
 * 1 <= board\[i\].length <= 200
 * 1 <= word.length <= 10^3
 
 


------


## **English**
### [**Word Search**](https://leetcode-cn.com/problems/word-search/)

- **Difficulty:** Medium
- **Topic Tag:** Array; Backtracking
- **Similar Questions:** [*Word Search II*](https://leetcode-cn.com/problems/word-search-ii/)

### **Content**

Given a 2D board and a word, find if the word exists in the grid.

 The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

 **Example:**

  board = \[ \['A','B','C','E'\], \['S','F','C','S'\], \['A','D','E','E'\] \] Given word = "**ABCCED**", return **true**. Given word = "**SEE**", return **true**. Given word = "**ABCB**", return **false**.   

 **Constraints:**

 
 * board and word consists only of lowercase and uppercase English letters.
 * 1 <= board.length <= 200
 * 1 <= board\[i\].length <= 200
 * 1 <= word.length <= 10^3
 
 


------


- **来源：** 力扣（LeetCode）
- **链接：** [单词搜索](https://leetcode-cn.com/problems/word-search/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l1 = len(board)
        l2 = len(board[0])
        l = len(word)
        if l1*l2 < l:
            return False
        isin = {i: 0 for i in range(l1)}

        def isuse(i, j):
            return 1 << j & isin[i]

        def search(i, j, k):
            if isuse(i, j) or board[i][j] != word[k]:
                return 
            k += 1
            if k == l:
                return True
            isin[i] += 1 << j
            if j + 1 < l2:
                if search(i, j+1, k):
                    return True
            if j - 1 >= 0:
                if search(i, j-1, k):
                    return True
            if i - 1 >= 0:
                if search(i-1, j, k):
                    return True
            if i + 1 < l1:
                if search(i+1, j, k):
                    return True
            isin[i] -= 1 << j

        for i in range(l1):
            for j in range(l2):
                if search(i, j, 0):
                    return True
        return False
a = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCE"
a.exist(board, word)
```

- 利用位运算存储数字是否使用过
- 或者将使用过的格子替换成#
- 70.01%


# **685.**

------

## **中文版**
### [**冗余连接 II**](https://leetcode-cn.com/problems/redundant-connection-ii/)

- **难度：** 复杂
- **标签：** 树、深度优先搜索、并查集、图
- **相似题目：** [*冗余连接*](https://leetcode-cn.com/problems/redundant-connection/)


### **题目：**

在本问题中，有根树指满足以下条件的**有向**图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。

 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

 结果图是一个以边组成的二维数组。 每一个边 的元素是一对 \[u, v\]，用以表示**有向**图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。

 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

 **示例 1:**

 **输入:** \[\[1,2\], \[1,3\], \[2,3\]\] **输出:** \[2,3\] **解释:** 给定的有向图如下: 1 / \ v v 2-->3  **示例 2:**

 **输入:** \[\[1,2\], \[2,3\], \[3,4\], \[4,1\], \[1,5\]\] **输出:** \[4,1\] **解释:** 给定的有向图如下: 5 <- 1 -> 2 ^ | | v 4 <- 3  **注意:**

 
 * 二维数组大小的在3到1000范围内。
 * 二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。
 
 


------


## **English**
### [**Redundant Connection II**](https://leetcode-cn.com/problems/redundant-connection-ii/)

- **Difficulty:** Hard
- **Topic Tag:** Tree; Depth-first Search; Union Find; Graph
- **Similar Questions:** [*Redundant Connection*](https://leetcode-cn.com/problems/redundant-connection/)

### **Content**

 In this problem, a rooted tree is a **directed** graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents. 

 The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed. 

 The resulting graph is given as a 2D-array of edges. Each element of edges is a pair \[u, v\] that represents a **directed** edge connecting nodes u and v, where u is a parent of child v. 

 Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. 

**Example 1:**  
  **Input:** \[\[1,2\], \[1,3\], \[2,3\]\] **Output:** \[2,3\] **Explanation:** The given directed graph will be like this: 1 / \ v v 2-->3  

 **Example 2:**  
  **Input:** \[\[1,2\], \[2,3\], \[3,4\], \[4,1\], \[1,5\]\] **Output:** \[4,1\] **Explanation:** The given directed graph will be like this: 5 <- 1 -> 2 ^ | | v 4 <- 3  

 **Note:**  
 - The size of the input 2D-array will be between 3 and 1000.
 - Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
 




------


- **来源：** 力扣（LeetCode）
- **链接：** [冗余连接 II](https://leetcode-cn.com/problems/redundant-connection-ii/)
- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
from typing import List, Dict, Tuple
class UnionFind:
    def __init__(self, n):
        self.ancestor = list(range(n))
    
    def union(self, index1: int, index2: int):
        self.ancestor[self.find(index1)] = self.find(index2)
    
    def find(self, index: int) -> int:
        if self.ancestor[index] != index:
            self.ancestor[index] = self.find(self.ancestor[index])
        return self.ancestor[index]

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        nodesCount = len(edges)
        uf = UnionFind(nodesCount + 1)
        parent = list(range(nodesCount + 1))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if uf.find(node1) == uf.find(node2):
                    cycle = i
                else:
                    uf.union(node1, node2)

        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]

inp =  [[1,2], [2,3], [3,4], [4,1], [1,5]]
a = Solution()
a.findRedundantDirectedConnection(inp)
```




    [4, 1]




```python
a.findRedundantDirectedConnection([[1,2], [1,3], [2,3]])
```




    [2, 3]



- 抄的官方作业
- 学习差并集

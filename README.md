# Raw Breadth-first Search Algorithm 😷🔎

Raw implementation of Breadth-First Search with the use of a stack as the underlying data structure

Instead of using the `deque` library, I decided to make my own breadth-first search with the use of the stack. Still works as normal, however, my Stack may vist more or even less nodes at an uncertain rate. 

Each function in the Stack data structure takes `O(1)` complexity. 

The Breadth-First Search Algorithm takes the same amount of average time of `O(N)`. 

More Info 

`test.py` are test inputs. 
`Tree.py` is the underlying Tree Data structure for the algorithm.

*To add more test inputs, initialize a `TreeNode(value)` node, and add a child to another `TreeNode` using `TreeNode1.add_child(TreeNode2)`* 

Made in Python 🐍

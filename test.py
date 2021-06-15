from Tree import TreeNode 
from bfs import bfs
### Test Inputs ###
test = TreeNode(1)
test2 = TreeNode(2)
test3 = TreeNode(3)
test4 = TreeNode(4)
test5 = TreeNode(5)
test6 = TreeNode(6)
test7 = TreeNode(7)

test.add_child(test2)
test.add_child(test3)
test2.add_child(test4)
test2.add_child(test5)
test3.add_child(test6)
test3.add_child(test7)
########################


goal_path = bfs(test, 5)

if goal_path == None:
    print("No path found! ")
else:
    print('-'*24)
    print("Path found! ")
    for node in goal_path:
        print(node.value)
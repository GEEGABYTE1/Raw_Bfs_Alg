#from collections import deque 
from Stack import Stack

def bfs(root_node, goal_value):
    path_queue = Stack()
    initial_path = [root_node]
    path_queue.push(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print("Searching node with value {}".format(current_node.value))
        if current_node.value == goal_value:
            return current_path 
        
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.push(new_path)

    return None 
# from binary_tree import BinaryTree
# from typing import Union

# def leaves(tree: Union[BinaryTree, None]) -> int: 
#     '''
#     Compute the total number of interesting leaf nodes. 
#     You must only traverse through the tree once. 

#     Arguments:
#         tree: a binary tree with integer values

#     Returns:
#         The total number of interesting leaf nodes 
#     '''
#     # TODO: Write your solution here
#     def dfs(node: Union[BinaryTree, None], current_sum: int, depth: int) -> int:
#         if node == None:
#             return 0
        
#         if node.left is None and node.right is None:
#             if current_sum < depth:
#                 return 1
#             else:
#                 return 0
        
#         new_sum = current_sum + node.value
#         left_count = dfs(node.left, new_sum, depth + 1)
#         right_count = dfs(node.right, new_sum, depth + 1)
#         return left_count + right_count

#     return dfs(tree, 0, 0)

# def mk_node(val: int,
#             left: Union[BinaryTree, None],
#             right: Union[BinaryTree, None]) -> BinaryTree:
#     """
#     Create a binary tree node, given the node number, value,
#     left child, and right child.
#     """
#     t = BinaryTree(val)
#     t.add_left(left)
#     t.add_right(right)
#     return t

# def mk_sample_tree() -> BinaryTree:
#     '''
#     Make the sample tree from the problem statement.

#     Returns:
#         The root node of the sample tree
#     '''
#     return mk_node(-1,
#                mk_node(15,
#                    mk_node(20, None,None),
#                    mk_node(-13, mk_node(7,None,None),None)),
#                mk_node(10,None, None))

# print(leaves(mk_sample_tree()))

from binary_tree import BinaryTree
from typing import Union

def leaves(tree: Union[BinaryTree, None]) -> int: 
    '''
    Compute the total number of interesting leaf nodes. 
    You must only traverse through the tree once. 

    Arguments:
        tree: a binary tree with integer values

    Returns:
        The total number of interesting leaf nodes 
    '''
    # TODO: Write your solution here
    def dfs(node: Union[BinaryTree, None], current_sum: int, depth: int) -> int:
        if node == None:
            return 0
        
        if node.left == None and node.right == None:
            if current_sum < depth:
                return 1
            else:
                return 0
            
        new_sum = current_sum + node.value
        left_count = dfs(node.left, new_sum, depth + 1)
        right_count = dfs(node.right, new_sum, depth + 1)

        return left_count + right_count
    
    return dfs(tree, 0, 0)

def mk_node(val: int,
            left: Union[BinaryTree, None],
            right: Union[BinaryTree, None]) -> BinaryTree:
    """
    Create a binary tree node, given the node number, value,
    left child, and right child.
    """
    t = BinaryTree(val)
    t.add_left(left)
    t.add_right(right)
    return t

def mk_sample_tree() -> BinaryTree:
    '''
    Make the sample tree from the problem statement.

    Returns:
        The root node of the sample tree
    '''
    return mk_node(-1,
               mk_node(15,
                   mk_node(20, None,None),
                   mk_node(-13, mk_node(7,None,None),None)),
               mk_node(10,None, None))

print(leaves(mk_sample_tree()))
# from binary_tree import BinaryTree
# from typing import Union


# def tree_sum(tree: Union[BinaryTree, None], ceiling: int) -> int:
#     '''
#     Compute the sum of all the values in the tree, up to the given
#     ceiling (short-circuiting the traversal of the tree is we hit
#     that ceiling)

#     Arguments:
#         tree: a binary tree with integer values
#         ceiling: the maximum value for the sum of values

#     Returns:
#         The sum of all the values in the tree or, if that sum
#         is greater than the ceiling value, return the ceiling
#         value.
#     '''
#     # TODO: Write your solution here
#     def dfs(node: Union[BinaryTree, None], current_sum: int) -> int:
#         if node == None:
#             return current_sum
        
#         current_sum += node.value

#         if current_sum >= ceiling:
#             return ceiling #short circuit
        
#         left_sum = dfs(node.left, current_sum)
#         if left_sum >= ceiling:
#             return ceiling
#         right_sum = dfs(node.right, left_sum)
#         if right_sum >= ceiling:
#             return ceiling
        
#         return right_sum

#     return dfs(tree, 0)


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
#     return mk_node(10,
#                mk_node(5,
#                    None,
#                    mk_node(15,
#                            mk_node(5, None, None),
#                            mk_node(10, None, None))),
#                mk_node(20,
#                    mk_node(5, None, None),
#                    mk_node(5,
#                            mk_node(15, None, None),
#                            None)))

# tree = mk_sample_tree()
# print(tree_sum(tree, 200))
# print(tree_sum(tree, 40))

from binary_tree import BinaryTree
from typing import Union


def tree_sum(tree: Union[BinaryTree, None], ceiling: int) -> int:
    '''
    Compute the sum of all the values in the tree, up to the given
    ceiling (short-circuiting the traversal of the tree is we hit
    that ceiling)

    Arguments:
        tree: a binary tree with integer values
        ceiling: the maximum value for the sum of values

    Returns:
        The sum of all the values in the tree or, if that sum
        is greater than the ceiling value, return the ceiling
        value.
    '''
    # TODO: Write your solution here
    def dfs(node: Union[BinaryTree, None], current_val: int) -> int:
        if node == None:
            return current_val # short circuit
        
        current_val += node.value

        if current_val >= ceiling:
            return ceiling
        
        left_sum = dfs(node.left, current_val)
        if left_sum >= ceiling:
            return ceiling
        right_sum = dfs(node.right, left_sum)
        if right_sum >= ceiling:
            return ceiling
        
        return right_sum
    
    return dfs(tree, 0)


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
    return mk_node(10,
               mk_node(5,
                   None,
                   mk_node(15,
                           mk_node(5, None, None),
                           mk_node(10, None, None))),
               mk_node(20,
                   mk_node(5, None, None),
                   mk_node(5,
                           mk_node(15, None, None),
                           None)))

tree = mk_sample_tree()
print(tree_sum(tree, 200))
print(tree_sum(tree, 40))
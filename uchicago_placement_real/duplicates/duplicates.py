from binary_tree import BinaryTree


def duplicates(tree: BinaryTree | None) -> int: 
    '''
    Compute the total number of paths from the *root* node to a *leaf* node 
    where two (or more) nodes in the path have the same integer value. 

    Args:
        tree: a binary tree with integer values

    Returns: The total number of paths from the *root* node to a *leaf* node 
    where two (or more) nodes in the path have the same integer value. 
    '''
    # TODO: Write your solution here
    def dfs(node: BinaryTree | None, visited: set[int], has_dup: bool) -> int:
        if node == None:
            return 0
        
        if node.value in visited:
            is_dup = True
        else:
            is_dup = False
        
        visited.add(node.value)

        if has_dup or is_dup:
            has_dup = True
        else:
            has_dup = False

        if node.left == None and node.right == None:
            if has_dup:
                dup_count = 1
            else:
                dup_count = 0
        else:
            next_visited_l = visited.copy()
            left_count = dfs(node.left, next_visited_l, has_dup)
            next_visited_r = visited.copy()
            right_count = dfs(node.right, next_visited_r, has_dup)
            dup_count = left_count + right_count

        return dup_count    
        
    return dfs(tree, set(), False)


# The functions below are for testing purposes only and should not be called
# from the duplicates() function

def mk_node(val: int,
            left: BinaryTree | None,
            right: BinaryTree | None) -> BinaryTree:
    """
    Create a binary tree node, given the integer value,
    left child, and right child.

    Args:
        val: the integer value of the new node 
        left: the left branch of the new node 
        right: the right branch of the new node 

    Returns: A new binary tree node with the given value, left child, and right child.  
    """
    t = BinaryTree(val)
    t.left = left
    t.right = right
    return t


def mk_sample_tree() -> BinaryTree:
    '''
    Generates sample tree from the problem statement.

    Args: None 
 
    Returns: the sample tree from the problem statements. 
    '''
    return mk_node(10,
               mk_node(5,
                   mk_node(10, None,None),
                   mk_node(4, None,None)),
               mk_node(8,
                   mk_node(6,None, mk_node(8,None,None)),
                   mk_node(7, None,None)))
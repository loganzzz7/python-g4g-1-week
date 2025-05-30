# def expand(lb: int, ub: int, skip: list[int]) -> list[int]:
#     """
#     Create a list of integers from a lower bound to an upper bound,
#         inclusive on both sides, excluding any value that is a divisor
#         of a value in list of values to skip.

#     Inputs:
#         lb [int]: lower bound
#         ub [int]: upper bound
#         skip list[int]: list of multiples to skip

#     Returns list[int]: List of integers from lb to ub (inclusive)
#         except for any integer that is a divisor of a value in skip.
#     """
#     assert lb >= 2
#     assert lb <= ub

#     # TODO: Implement this function.
#     result = []

#     while lb <= ub:
#         can_append = True
#         for val in skip:
#             if val % lb == 0:
#                 can_append = False
#                 break # exit immediately if any lb is divisor of val

#         if can_append == True:
#             result.append(lb)
        
#         lb = lb + 1
#     return result

# print(expand(2, 8, [10, 77]))
# print(expand(7, 17, [60, 16]))

def expand(lb: int, ub: int, skip: list[int]) -> list[int]:
    """
    Create a list of integers from a lower bound to an upper bound,
        inclusive on both sides, excluding any value that is a divisor
        of a value in list of values to skip.

    Inputs:
        lb [int]: lower bound
        ub [int]: upper bound
        skip list[int]: list of multiples to skip

    Returns list[int]: List of integers from lb to ub (inclusive)
        except for any integer that is a divisor of a value in skip.
    """
    assert lb >= 2
    assert lb <= ub

    # TODO: Implement this function.
    result = []

    while lb <= ub:
        can_append = True
        for val in skip:
            if val % lb == 0:
                can_append = False
                break

        if can_append == True:
            result.append(lb)
        lb = lb + 1
    return result

print(expand(2, 8, [10, 77]))
print(expand(7, 17, [60, 16]))


def total_wasted_space(shipments: list[int], bin_size: int) -> int:
    '''
    This function takes a list of integers, representing the number of items
    in each shipment, and a bin size, and computes the total wasted
    space across all shipments.

    Arguments:
        shipments: a list of integers
        bin_size: the capacity of each bin (all bins have the same capacity)

    Returns:
        The total wasted space across all shipments.
    '''

    # Your code here
    # Return is included to verify the test code.
    total_wasted_space = 0

    for shipment in shipments:
        left_over = shipment % bin_size
        if left_over != 0:
            individual_wasted_space = bin_size - left_over
            total_wasted_space = total_wasted_space + individual_wasted_space
    return total_wasted_space

print(total_wasted_space([23, 31, 108, 46], 10))
# 7 + 9 + 2 + 4 = 22 Correct!
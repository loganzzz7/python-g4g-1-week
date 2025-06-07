def roadtrip(vehicle_ranges: list[int], route: list[int]) -> list[int]:
    """
    Simulate multiple vehicles on a road trip, determining how many
    destinations vehicles can reach given fuel capacity
    and a given route.

    Parameters:
        vehicle_ranges: A list of integers representing the number of
                        kilometers each vehicle can travel.
        route: A list of integers representing the distance to each 
               sequential destination.

    Returns:
        A list of integers indicating how many stops each vehicle was able to
        make without refueling.
    """
    result = []
    for vehicle_range in vehicle_ranges:
        stops = 0
        for val in route:
            if vehicle_range >= val:
                vehicle_range -= val
                stops += 1
            else:
                break # stop if cant go another dest
        result.append(stops)
    return result

# # e.g. 1
# print(roadtrip([50], [10, 20, 10, 30]))
# # e.g. 2
# print(roadtrip([30, 100], [10, 20, 10, 30]))
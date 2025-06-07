def bikeshare(capacity: tuple[int, int], num_bikes: tuple[int, int], 
              checkouts: list[str]) -> int:
    """
    Given an initial state at the downtown and university stations and a list 
    of students who arrive to check out a bike, model and simulate a bikeshare 
    system with two stations. 

    Args:
        capacity: the capacity of the downtown and university 
            stations, in that order
        num_bikes: the initial number of bikes at the downtown 
            and university stations, in that order
        checkouts: students who arrive to check out a bike 

    Returns: The number of unhappy students.
    """

    # TODO: Implement this function.
    # checkout first then return
    # unhappy if cant checkout or wait to ret
    unhappy_cnt = 0
    num_d = num_bikes[0]
    num_u = num_bikes[1]
    cap_d = capacity[0]
    cap_u = capacity[1]

    bike_trans = []

    wait_d = 0
    wait_u = 0

    for time in range(len(checkouts)):
        # checkout logic
        for checkout in checkouts[time]:
            if checkout == "D":
                # checking out from downtown
                if num_d > 0:
                    num_d -= 1
                    # goes to uni
                    bike_trans.append([3, "U"])
                else: # unhappy checkout
                    unhappy_cnt += 1
            elif checkout == "U":
                # checking out from uni
                if num_u > 0:
                    num_u -= 1
                    # goes to dtn
                    bike_trans.append([3, "D"])
                else: # unhappy checkout
                    unhappy_cnt += 1

        # ret logic
        moving_bike = []
        for time_left, dest in bike_trans:
            if time_left > 0:
                moving_bike.append([time_left, dest])
            else:
                if dest == "D":
                    if num_d == cap_d:
                        # unhappy ret
                        unhappy_cnt += 1
                        wait_d += 1
                    else:
                        num_d += 1
                elif dest == "U":
                    if num_u == cap_u:
                        # unhappy ret
                        unhappy_cnt += 1
                        wait_u += 1
                    else:
                        num_u += 1
        bike_trans = moving_bike # rmv ret bike
        for bike in bike_trans: # dec time on bike till ret
            bike[0] -= 1

        # if waiting and has empty spot now
        while wait_d > 0 and num_d < cap_d:
            wait_d -= 1
            num_d += 1
        while wait_u > 0 and num_u < cap_u:
            wait_u -= 1
            num_u += 1

    return unhappy_cnt

# # e.g. 1
# print(bikeshare((2, 2), (2, 2), ["D", "D", "", ""]))
# # e.g. 2
# print(bikeshare((2, 3), (2, 2), ["U", "", "U", "U", "D"]))
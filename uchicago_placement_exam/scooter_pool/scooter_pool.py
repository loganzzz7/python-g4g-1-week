# from location import Location
# from scooter import Scooter

# class ScooterPool:
#     """
#     A class for representing a pool of scooters and their current locations.
#     """

#     _scooters: dict[str, Scooter] # _ = this is protected

#     def __init__(self):
#         """
#         Construct an instance of ScooterPool
#         """
#         # TODO: complete this constructor
#         # pass
#         self._scooters = {}


#     def add_scooter(self, sid: str, x: int, y: int) -> bool:
#         """
#         Add a scooter to the pool

#         Inputs:
#           sid: the unique identifier for this scooter
#           x: the initial x coordinate for the scooter
#           y: the initial y coordinate for the scooter           

#         Returns: True, if the scooter ID does not already appear in the pool
#           and False, otherwise.
#         """
#         # TODO: complete this method
#         if sid not in self._scooters:
#             self._scooters[sid] = Scooter(sid, x, y)
#             return True
#         return False

#     def num_scooters_in_range(self, loc: Location, dist: int) -> int:
#         """
#         Count the number of scooters where the distance
#         between the scooter and a specified location (loc) is
#         strictly less than dist.

#         Inputs:
#           loc: the specified location
#           dist: the maximum allowed distance from the specified location

#         Returns: the number of scooters where the distance between
#           the scooter's location and the specified location is
#           strictly less than dist.
#         """
#         # TODO: complete this method
#         num_s = 0
#         for scooter in self._scooters.values():
#             if dist > scooter.distance_between(loc):
#                 num_s += 1
#         return num_s

#     def __str__(self) -> str:
#         # optional method
#         if not self._scooters:
#             return "There are no scooters in pool"
#         else:
#             result = []
#             for scooter in self._scooters.values():
#                 result.append(str(scooter))
#         return " ".join(result)
    
# pool = ScooterPool()
# pool.add_scooter("A1", 2, 3)
# pool.add_scooter("B2", 4, 5)
# print(pool)

from location import Location
from scooter import Scooter

class ScooterPool:
    """
    A class for representing a pool of scooters and their current locations.
    """

    _scooters: dict[str, Scooter] # _ = this is protected

    def __init__(self):
        """
        Construct an instance of ScooterPool
        """
        # TODO: complete this constructor
        # pass
        self._scooters = {}


    def add_scooter(self, sid: str, x: int, y: int) -> bool:
        """
        Add a scooter to the pool

        Inputs:
          sid: the unique identifier for this scooter
          x: the initial x coordinate for the scooter
          y: the initial y coordinate for the scooter           

        Returns: True, if the scooter ID does not already appear in the pool
          and False, otherwise.
        """
        # TODO: complete this method
        if sid not in self._scooters:
            self._scooters[sid] = Scooter(sid, x, y)
            return True
        
        return False


    def num_scooters_in_range(self, loc: Location, dist: int) -> int:
        """
        Count the number of scooters where the distance
        between the scooter and a specified location (loc) is
        strictly less than dist.

        Inputs:
          loc: the specified location
          dist: the maximum allowed distance from the specified location

        Returns: the number of scooters where the distance between
          the scooter's location and the specified location is
          strictly less than dist.
        """
        # TODO: complete this method
        num_s = 0
        for scooter in self._scooters.values():
            if scooter.distance_between(loc) < dist:
                num_s += 1

        return num_s


    def __str__(self) -> str:
        # optional method
        if not self._scooters:
            return "There are no scooters in pool"
        else:
            result = []
            for scooter in self._scooters.values():
                result.append(str(scooter))
        return " ".join(result)
    
pool = ScooterPool()
pool.add_scooter("A1", 2, 3)
pool.add_scooter("B2", 4, 5)
print(pool)
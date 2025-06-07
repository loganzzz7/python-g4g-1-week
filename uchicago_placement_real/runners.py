class Runner:
  """
  A class to represent a runner and store their finishing times.
  """
  def __init__(self, name: str):
      """
      Args:
          name (string): Name of the runner        
      """
      self.name = name
      self.__finishing_times: list[int] = []

  def add_time(self, time: int) -> None:
      """
      Args: 
          time (int): Time (in seconds) for finishing a marathon for this
          runner
      """
      self.__finishing_times.append(time)


  def best_time(self) -> int:
      """
      Returns the best time for the runner.
      Returns:
          (int): Best finishing time for this runner
      """
      
      # TODO: Implement this method
      if self.__finishing_times == []: # if not parti
          return -1
      return min(self.__finishing_times)

  def worst_time(self) -> int:
      """
      Returns the worst time for the runner.
      Returns:
          (int): Worst finishing time for this runner
      """
      # TODO: Implement this method
      if self.__finishing_times == []: # if not parti
          return -1
      return max(self.__finishing_times)

  def average_pace(self) -> float:
      """
      Returns the average pace for the runner.
      Returns:
          (float): Average number of seconds per mile for this runner
      """
      MARATHON_MILES = 26.2
      
      # TODO: Implement this method
      sum_times = 0
      num_mara = 0

      if self.__finishing_times == []: # if not parti
          return -1

      for finishing_time in self.__finishing_times:
          sum_times += finishing_time
          num_mara += 1
      average_pace = sum_times / (num_mara * MARATHON_MILES)
      return average_pace


class Marathon:
  """
  A class to represent a marathon and store a list of participating runners.
  """

  def __init__(self, name: str):
      """
      Args:
          name (string): Name of the Marathon
      """
      self.name = name
      self.__runners: list[Runner] = []

  def register(self, runner_name: str, times: list[int]) -> None:
      """
      Add a runner to the Marathon.
      Args:
          runner_name (string): name of the runner to be added
          times List(int): A list of finishing times
      Returns:
          None
      """
      # TODO Implement this method
      # create Runner obj and add to list
      runner = Runner(runner_name)
      for time in times:
          runner.add_time(time)
      self.__runners.append(runner)
      return None

  def top_seed(self) -> str:
      """
      Returns the  name of the top runner based on their best time.
      Returns:
          str - The name of the top runner based on their best time
      """
      assert len(self.__runners) > 0

      # TODO Implement this method
      top_runner = self.__runners[0]
      best_time = top_runner.best_time()

      for runner in self.__runners:
          runner_best = runner.best_time()
          if runner_best != -1 and runner_best < best_time: # if not time best is -1
              best_time = runner_best
              top_runner = runner

      return top_runner.name

  def pace_bracket(self, min_pace: float, max_pace: float) -> list[Runner]:
      """
      Returns the runners whose avg_pace falls within the given range.
      Args:
          min_pace (float): Minimum avg. seconds per mile 
          max_pace (float): Maximum avg. seconds per mile
      Retruns:
          List[Runner]: A list of runners whose average pace falls within
          min_pace and max_pace
      """
      # TODO Implement this method
      pace_bracket = []
      for runner in self.__runners:
          if runner.average_pace() != -1 and runner.average_pace() >= min_pace and runner.average_pace() <= max_pace: # inclusive
              pace_bracket.append(runner) # append runner objs!
      return pace_bracket
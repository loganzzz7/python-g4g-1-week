from line_item import LineItem

class Order:
  def __init__(self, tax_rate):
      """Class for representing an Order
      
      Parameters:
          tax_rate: the sales tax rate
      """
      self.__tax_rate = tax_rate
      self.__items = []

  def add_line_item(self, item: LineItem) -> None:
      """Add a LineItem to the Order
      
      Parameters:
          item: the item to add
      """
      self.__items.append(item)
      return None

  def total_cost(self) -> float:
      """Calculate the total cost of the order
      
      Returns:
          The total cost of the order in dollars
      """
      total_cost = 0
      for item in self.__items:
         total_cost += item.line_cost()
      total_cost_with_tax = total_cost + (total_cost * self.__tax_rate / 100)
      return total_cost_with_tax
  
order = Order(12.5)
order.add_line_item(LineItem("Apple", 1.0, 5))   # $5
order.add_line_item(LineItem("Orange", 2.0, 3))  # $6
print(order.total_cost())  # 11 + (11 * 0.125) = 12.375
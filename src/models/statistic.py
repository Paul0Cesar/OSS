class Statistic:
  total_time: int
  turn_arround: float
  total_process: int
  pagination_rate: float
  page_fault: float
  ram_use: float  
  swap_use: float
  page_found: float

  def __init__(self, 
                 turn_arround: float = 0.0, 
                 pagination_rate: float = 0.0, 
                 page_fault: float = 0.0, 
                 ram_use: float = 0.0, 
                 swap_use: float = 0.0, 
                 page_found: float = 0.0):
    self.turn_arround = turn_arround
    self.pagination_rate = pagination_rate
    self.page_fault = page_fault
    self.ram_use = ram_use
    self.swap_use = swap_use
    self.page_found = page_found

  def calcPaginationRate(self):
    self.pagination_rate=self.page_fault/(self.page_fault+self.page_found)
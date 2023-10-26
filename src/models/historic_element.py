from src.models.pcb import PCB

class HistoricElement:
    time: int
    process: PCB
    page_found: bool

    def __init__(self, time:int, pc:PCB):
      self.time = time
      self.process= pc
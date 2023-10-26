from typing import List
from src.models.page import Page
from src.models.pcb import PCB

class FIFO():
  def __init__(self) -> None:
    pass

  def selectNext(self, pgList: List[Page] = [], pcList: List[PCB] = []):
    if(pgList):
      return min(pgList, key=lambda x: x.lastTimeOnRam)
    elif(pcList):
      return min(pcList, key=lambda x: x.creation_time)

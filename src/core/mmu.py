from typing import List
from src.models.page import Page
from src.models.pcb import PCB
from src.utils.default_ordered_dict import DefaultOrderedDict
from src.core.fifo import FIFO

class MMU:
  ram_memory: List[Page]
  swap_memory: List[Page]
  pages_memory: List[Page]
  #pages_requisition: DefaultOrderedDict[PCB, List[Page]]
  max_ram_pages : int

  def __init__(self):
    self.pages_requisition = DefaultOrderedDict(list)
    self.pages_memory = []
    self.swap_memory = []
    self.ram_memory = []
    self.max_ram_pages = 6

  def createPage(self, pages: List[Page]):
    self.swap_memory.extend(pages)
    self.pages_memory.extend(pages)

  def start(self):
    self.swap_memory = self.pages_memory.copy();

  def verifyAndRequestPages(self, pc: PCB):
    pages_in_swap = []
    for p in pc.pages:
      if not p in self.ram_memory:
        pages_in_swap.append(p)
        self.pages_requisition[pc].append(p)
    if(pages_in_swap):
      return False
    else:
      return True

  def getPolityc():
    return FIFO()

  def execDMA(self, time: int):
    if(self.pages_requisition):
      pc = list(self.pages_requisition.keys())[0]
      p = self.pages_requisition[pc][0]

      if(len(self.ram_memory) >= self.max_ram_pages):
        politic = FIFO()
        pg= politic.selectNext(self.ram_memory)
        self.swap_memory.append(pg)
        self.ram_memory[self.ram_memory.index(pg)] = p
        print(" [-] - ", pg.name, " saiu e ", p.name, " entrou na ram")
      else:
        self.ram_memory.append(p)

      p.lastTimeOnRam = time
      self.pages_requisition[pc].pop(0)
      self.swap_memory.remove(p)

      if(not self.pages_requisition[pc]):
        pc.readyToExecute = True
        self.pages_requisition.pop(pc)
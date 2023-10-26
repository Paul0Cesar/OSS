from typing import List
from src.models.page import Page
from src.models.pcb import PCB
from src.models.statistic import Statistic
from src.models.historic_element import HistoricElement
from src.utils.default_ordered_dict import DefaultOrderedDict
from src.core.fifo import FIFO
from copy import copy

class MMU:
  ram_memory: List[Page]
  swap_memory: List[Page]
  pages_memory: List[Page]
  pages_requisition: DefaultOrderedDict[PCB, List[Page]]
  max_ram_pages : int
  max_swap_pages : int
  statistic: Statistic

  def __init__(self, statistic: Statistic=Statistic(), max_ram_page: int=6, max_swap_page: int=18):
    self.statistic = Statistic()
    self.pages_requisition = DefaultOrderedDict(list)
    self.pages_memory = []
    self.swap_memory = []
    self.ram_memory = []
    self.max_ram_pages = max_ram_page
    self.max_swap_pages = max_swap_page

  def createPage(self, pages: List[Page]):
    self.swap_memory.extend(pages)
    self.pages_memory.extend(pages)
    self.statistic.swap_use = len(self.pages_memory.copy)/self.max_swap_pages;

  def start(self):
    self.swap_memory = self.pages_memory.copy();

  def verifyAndRequestPages(self, pc: PCB):
    pages_in_swap = []
    for p in pc.pages:
      if not p in self.ram_memory:
        pages_in_swap.append(p)
        self.statistic.page_fault+=1
        self.pages_requisition[pc].append(p)
      else:
        self.statistic.page_found+=1
    
    self.statistic.calcPaginationRate()
    if(pages_in_swap):
      return False
    else:
      return True

  def getPolityc():
    return FIFO()

  def execDMA(self, time: int, historic: List[HistoricElement]):
    if(self.pages_requisition):
      pc = list(self.pages_requisition.keys())[0]
      p = self.pages_requisition[pc][0]
      historicElement = HistoricElement(time=time)

      if(len(self.ram_memory) >= self.max_ram_pages):
        politic = FIFO()
        pg= politic.selectNext(self.ram_memory)
        self.swap_memory.append(pg)

        historicElement.swap_out = pg
        historicElement.swap_in = p
        
        self.ram_memory[self.ram_memory.index(pg)] = p
        print(" [-] - ", pg.name, " saiu e ", p.name, " entrou na ram")
      else:
        historicElement.swap_in = p
        self.ram_memory.append(p)

      p.lastTimeOnRam = time
      self.pages_requisition[pc].pop(0)
      self.swap_memory.remove(p)
      
      if(not self.pages_requisition[pc]):
        historicElement.process_to_execution = pc
        
        pc.readyToExecute = True
        self.pages_requisition.pop(pc)

      print(len(self.ram_memory))
      self.statistic.ram_use=len(self.ram_memory)/self.max_ram_pages
      historicElement.statistic = copy(self.statistic)
      historic.append(historicElement)
  ram_memory: List[Page]
  swap_memory: List[Page]
  pages_memory: List[Page]
  # pages_requisition: DefaultOrderedDict[PCB, List[Page]]
  max_ram_pages : int
  statistic: Statistic


  def __init__(self):
    self.statistic = Statistic()
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

  def execDMA(self, time: int, historic: List[HistoricElement]):
    if(self.pages_requisition):
      pc = list(self.pages_requisition.keys())[0]
      p = self.pages_requisition[pc][0]
      historicElement = HistoricElement(time=time)

      if(len(self.ram_memory) >= self.max_ram_pages):
        politic = FIFO()
        pg= politic.selectNext(self.ram_memory)
        self.swap_memory.append(pg)

        historicElement.swap_out = pg
        historicElement.swap_in = p
        
        self.ram_memory[self.ram_memory.index(pg)] = p
        print(" [-] - ", pg.name, " saiu e ", p.name, " entrou na ram")
      else:
        historicElement.swap_in = p

        self.ram_memory.append(p)

      p.lastTimeOnRam = time
      self.pages_requisition[pc].pop(0)
      self.swap_memory.remove(p)
      
      if(not self.pages_requisition[pc]):
        historicElement.process_to_execution = p
        
        pc.readyToExecute = True
        self.pages_requisition.pop(pc)

      historic.append(historicElement)
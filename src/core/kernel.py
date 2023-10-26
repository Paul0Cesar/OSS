from typing import List
from src.models.pcb import PCB
from src.core.mmu import MMU
from src.models.historic_element import HistoricElement
import math

class Kernel:
  execution_list:List[PCB] = []
  waiting_list:List[PCB] = []
  finshed_list: List[PCB] = []
  time: int
  mmu: MMU

  def __init__(self,historic, interval: int):
    self.historic=historic
    self.interval=interval
    self.execution_list = []
    self.awaiting_list = []
    self.time = 0
    self.mmu = MMU()

  def verifyWaitingList(self):
    for p in [pc for pc in self.waiting_list if pc.readyToExecute]:
      self.execution_list.append(p)
      self.waiting_list.remove(p)

  def add_PCB(self, pcb: PCB):
    self.execution_list.append(pcb)
    self.mmu.createPage(pcb.pages) 

  def execute(self):
    while(self.execution_list or self.waiting_list):
      if(self.execution_list): #Se tiver algum processo a ser executado
        pc = min(self.execution_list, key=lambda x: x.creation_time)
        pc_i = self.execution_list.index(pc)

        if(self.mmu.verifyAndRequestPages(pc)): #Se pc tem as paginas na memoria
          interations = math.ceil(pc.restant_time/self.interval)
          print("[*] - Interations: ",interations)
          for i in range(0, interations):
            self.historic.put(HistoricElement(time=self.time, pc=pc))
            self.time += self.interval
            print("[*] - Execute pc: ", pc.name)
          self.execution_list.remove(pc)
        else: #Se não tiver coloca em espera
          pc.readyToExecute = False
          self.waiting_list.append(pc)
          self.execution_list.remove(pc)

      self.verifyWaitingList()
      self.mmu.execDMA(self.time)
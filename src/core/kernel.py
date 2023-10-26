from typing import List
from src.models.pcb import PCB
from src.models.statistic import Statistic
from src.core.mmu import MMU
from src.models.historic_element import HistoricElement
import math
from copy import copy


class Kernel:
    execution_list: List[PCB] = []
    waiting_list: List[PCB] = []
    finshed_list: List[PCB] = []
    time: int
    mmu: MMU
    statistic: Statistic

    def __init__(self,historic, interval: int):
        self.historic = historic
        self.interval = interval
        self.execution_list = []
        self.awaiting_list = []
        self.time = 0
        self.mmu = MMU()

    def verifyWaitingList(self):
        for p in [pc for pc in self.waiting_list if pc.readyToExecute]:
            self.execution_list.append(p)
            self.waiting_list.remove(p)

    def get_all_memory_ram(self):
        return self.mmu.pages_memory.copy()        

    def add_PCB(self, pcb: PCB):
        self.execution_list.append(pcb)
        self.historic.put(HistoricElement(
            time=self.time, process_to_execution=pcb))
        self.mmu.createPage(pcb.pages)

    def clear(self):
        self.execution_list.clear()
        self.awaiting_list.clear()
        self.finshed_list.clear()
        #self.mmu.clear()

    def execute(self):
        while (self.execution_list or self.waiting_list):
            historicElement = HistoricElement(time=self.time)

            if (self.execution_list):  # Se tiver algum processo a ser executado
                pc = min(self.execution_list, key=lambda x: x.creation_time)
                pc_i = self.execution_list.index(pc)

                #historicElement.process_in_execution = pc
                self.historic.put(HistoricElement(
                    time=self.time, process_in_execution=pc))

                if (self.mmu.verifyAndRequestPages(pc)):  # Se pc tem as paginas na memoria
                    interations = math.ceil(pc.restant_time/self.interval)
                    print("[*] - Interations: ", interations)

                    for i in range(0, interations):
                        self.historic.put(HistoricElement(
                            time=self.time, process_in_execution=pc, statistic=copy(self.mmu.statistic)))
                        self.time += self.interval
                        print("[*] - Execute pc: ", pc.name)

                    self.finshed_list.append(pc)
                    self.execution_list.remove(pc)
                    pc.final_time = self.time
                    historicElement.process_to_finish = pc
                    historicElement.duration = interations * self.interval

                else:  # Se não tiver coloca em espera
                    historicElement.page_fault = True
                    historicElement.process_to_await = pc

                    pc.readyToExecute = False
                    self.waiting_list.append(pc)
                    self.execution_list.remove(pc)

            historicElement.statistic = copy(self.mmu.statistic)
            self.historic.put(historicElement)
            self.verifyWaitingList()
            self.mmu.execDMA(self.time, self.historic)

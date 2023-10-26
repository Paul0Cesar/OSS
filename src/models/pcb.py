from src.models.page import Page
from typing import List

class PCB:
    PID: int
    name: str
    icon: str
    creation_time: int
    restant_time: int
    total_time: int
    priority: int
    final_time: int
    readyToExecute: bool
    pages: List[Page]

    def __init__(self, PID:int,icon: str, name: str, creation_time: int,
                              total_time: int, priority: int = 0,
                              pages: List[Page] = []):

        self.PID = PID
        self.name = name
        self.icon=icon
        self.creation_time = creation_time
        self.total_time = total_time
        self.priority = priority
        self.restant_time = total_time
        self.pages = pages

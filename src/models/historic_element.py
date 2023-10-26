from src.models.pcb import PCB

class HistoricElement:
    time: int
    duration: int
    process_in_execution: PCB or None
    process_to_await: PCB or None
    process_to_execution: PCB or None
    process_to_finish: PCB or None
    page_fault: bool
    swap_in: Page or None
    swap_out: Page or None

    def __init__(self, 
                 time: int = 0, 
                 duration: int = 0,
                 process_in_execution = None, 
                 process_to_await = None, 
                 process_to_execution = None, 
                 process_to_finish = None, 
                 page_fault: bool = False, 
                 swap_in = None, 
                 swap_out = None):
        self.time = time
        self.duration = duration
        self.process_in_execution = process_in_execution
        self.process_to_await = process_to_await
        self.process_to_execution = process_to_execution
        self.process_to_finish = process_to_finish
        self.page_fault = page_fault
        self.swap_in = swap_in
        self.swap_out = swap_out

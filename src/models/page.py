class Page:
  name: str
  inMemory: bool
  lastAcess: int
  lastTimeOnRam: int

  def __init__(self, name):
    self.name = name
    self.inMemory = False
    self.lastAcess = 0
    self.lastTimeOnRam = 0
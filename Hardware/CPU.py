from all_memory import AllMemory
from F1 import F1
from F2 import F2
from F3 import F3
from CD_BR import CD, BR

class CPU:
    def __init__(self) -> None:
        self.memory = AllMemory()
        self.f1 = F1(self.memory)
        self.f2 = F2(self.memory)
        self.f3 = F3(self.memory)
        self.CD = CD(self.memory)
        self.BR = BR(self.memory)

    def clock(self):
        pass

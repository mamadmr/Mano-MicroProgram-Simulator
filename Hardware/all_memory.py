from memory import Memory
from register import Register


class AllMemory:
    def __init__(self) -> None:
        self.main_memory = Memory(16, 11)
        self.control_memory = Memory(20, 7)

        self.AR = Register(11)
        self.PC = Register(11)

        self.DR = Register(16)
        self.AC = Register(16)

        self.CAR = Register(7)
        self.SBR = Register(7)

        self.reset_flag()
    
    def reset_flag(self):
        self.AR : Register
        self.AR.reset_flag()
        self.PC.reset_flag()
        self.DR.reset_flag()
        self.AC.reset_flag()
        self.CAR.reset_flag()
        self.SBR.reset_flag()
        self.main_memory.reset_flags()
        self.control_memory.reset_flags()

    def check_flags(self):
        self.AR_flag.check_flag()
        self.PC_flag.check_flag()
        self.DR_flag.check_flag()
        self.AC_flag.check_flag()
        self.CAR_flag.check_flag()
        self.SBR_flag.check_flag()
        self.main_memory.check_flags()
        self.control_memory.check_flags()
    

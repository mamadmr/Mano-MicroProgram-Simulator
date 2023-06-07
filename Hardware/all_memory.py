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

        # I will use the flag to check if the register is used or not in the single clock cycle
        self.flag = dict()
        self.reset_flag()
    
    def reset_flag(self):
        self.flag["main_memory_flag"] = [0] * 2 ** 11
        self.flag["control_memory_flag"] = [0] * 2 ** 7
        self.flag["AR_flag"] = 0
        self.flag["PC_flag"] = 0
        self.flag["DR_flag"] = 0
        self.flag["AC_flag"] = 0
        self.flag["CAR_flag"] = 0
        self.flag["SBR_flag"] = 0

if __name__ == "__main__":
    pass
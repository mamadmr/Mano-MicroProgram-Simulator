from all_memory import AllMemory

class F1:
    def __init__(self, memory: AllMemory) -> None:
        self.memory = memory
        self.opt = ['000', '001', '010', '011', '100', '101', '110', '111']
        self.asm = ['NOP', 'ADD', 'CLRAC', 'INCAC', 'DRTAC', 'DRTAR','PCTAR', 'WRITE']
        self.func = [self.isz_000, self.isz_001, self.isz_010, self.isz_011, self.isz_100, self.isz_101, self.isz_110, self.isz_111]
    
    def instruction(self, inst):
        for i in range(len(self.opt)):
            if inst == self.opt[i]:
                self.func[i]()
                break
            elif inst == self.asm[i]:
                self.func[i]()
                break
    
    def isz_000():
        pass

    def isz_001(self):
        # AC <- AC + DR
        self.memory.AC.write(self.memory.AC.read_dec()+ self.memory.DR.read_dec(), "d")
        self.memory.flag["AC_flag"] += 1

    def isz_010(self):
        # AC <- 0
        self.memory.AC.write("0b0000000000000000", "b")
        self.memory.flag["AC_flag"] += 1

    def isz_011(self):
        # AC <- AC + 1
        self.memory.AC.write(self.memory.AC.read_dec()+1, "d")
        self.memory.flag["AC_flag"] += 1

    def isz_100(self):
        # AC <- DR
        self.memory.AC.write(self.memory.DR.read_dec(), "d")
        self.memory.flag["AC_flag"] += 1

    def isz_101(self):
        # AR <- DR[10:0]
        self.memory.AR.write(self.memory.DR.read_binary()[-10:], "b")
        self.memory.flag["AR_flag"] += 1

    def isz_110(self):
        # AR <- PC
        self.memory.AR.write(self.memory.PC.read_binary(), "b")
        self.memory.flag["AR_flag"] += 1

    def isz_111(self):
        # M[AR] <- DR
        self.memory.main_memory.write(self.memory.AR.read_dec(), self.memory.DR.read_binary(), "b")
        self.memory.flag["main_memory_flag"][self.memory.AR.read_dec()] += 1


if __name__ == "__main__":
    mem = AllMemory()
    A = F1(mem)
    B = F1(mem)

    A.instruction("001")
    A.instruction("001")
    B.instruction("001")
    B.instruction("001")
    print(mem.flag['AC_flag'])
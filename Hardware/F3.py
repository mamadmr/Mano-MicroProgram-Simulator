from all_memory import AllMemory

class F3:
    def __init__(self, memory: AllMemory) -> None:
        self.memory = memory
        self.opt = ['000', '001', '010', '011', '100', '101', '110', '111']
        self.asm = ['NOP', 'XOR', 'COM', 'SHL', 'SHR', 'INCPC','ARTPC', 'RES']
        self.func = [self.isz_000, self.isz_001, self.isz_010, self.isz_011, self.isz_100, self.isz_101, self.isz_110, self.isz_111]
    
    def instruction(self, inst):
        for i in range(len(self.opt)):
            if inst == self.opt[i]:
                self.func[i]()
                break
            elif inst == self.asm[i]:
                self.func[i]()
                break

    def isz_000(self):
        pass

    def isz_001(self):
        # AC <- AC XOR DR
        self.memory.AC.write(self.memory.AC.read_dec() ^ self.memory.DR.read_dec(), "d")
        self.memory.flag["AC_flag"] += 1

    def isz_010(self):
        # AC <- ~AC
        self.memory.AC.write(~self.memory.AC.read_dec(), "d")
        self.memory.flag["AC_flag"] += 1

    def isz_011(self):
        # AC <- AC << 1
        self.memory.AC.write(self.memory.AC.read_dec() << 1, "d")
        self.memory.flag["AC_flag"] += 1

    def isz_100(self):
        # AC <- AC >> 1
        self.memory.AC.write(self.memory.AC.read_dec() >> 1, "d")
        self.memory.flag["AC_flag"] += 1

    def isz_101(self):
        # PC <- PC + 1
        self.memory.PC.write(self.memory.PC.read_dec()+1, "d")
        self.memory.flag["PC_flag"] += 1

    def isz_110(self):
        # PC <- AR
        self.memory.PC.write(self.memory.AR.read_dec(), "d")
        self.memory.flag["PC_flag"] += 1

    def isz_111(self):
        pass
from all_memory import AllMemory

class F1:
    def __init__(self, memory: AllMemory) -> None:
        """
        F1 is the first functional unit of the CPU. It is responsible for the following instructions:
        000: NOP
        001: ADD (AC <- AC + DR)
        010: CLRAC (AC <- 0)
        011: INCAC (AC <- AC + 1)
        100: DRTAC (AC <- DR) 
        101: DRTAR (AR <- DR[10:0])
        110: PCTAR (AR <- PC)
        111: WRITE (M[AR] <- DR)
        """
        self.memory = memory
        self.opt = ['000', '001', '010', '011', '100', '101', '110', '111']
        self.asm = ['NOP', 'ADD', 'CLRAC', 'INCAC', 'DRTAC', 'DRTAR','PCTAR', 'WRITE']
        self.func = [self.isz_000, self.isz_001, self.isz_010, self.isz_011, self.isz_100, self.isz_101, self.isz_110, self.isz_111]
    
    def instruction(self, inst: str):
        for i in range(len(self.opt)):
            if inst == self.opt[i]:
                # If the instruction matches an op code, call the corresponding function
                self.func[i]()
                break
            elif inst == self.asm[i]:
                # If the instruction matches an assembly instruction, call the corresponding function
                self.func[i]()
                break
    
    def isz_000():
        pass

    def isz_001(self):
        # AC <- AC + DR
        self.memory.AC.write(self.memory.AC.read_dec()+ self.memory.DR.read_dec(), "d")

    def isz_010(self):
        # AC <- 0
        self.memory.AC.write("0b0", "b")

    def isz_011(self):
        # AC <- AC + 1
        self.memory.AC.write(self.memory.AC.read_dec()+1, "d")

    def isz_100(self):
        # AC <- DR
        self.memory.AC.write(self.memory.DR.read_dec(), "d")

    def isz_101(self):
        # AR <- DR[10:0]
        # the indexing in the book is right to leftbut in str it is left to right
        # the write data in bainary should have '0b' in the begining
        self.memory.AR.write('0b'+self.memory.DR.read_binary()[-11:], "b")

    def isz_110(self):
        # AR <- PC
        self.memory.AR.write(self.memory.PC.read_binary(), "b")

    def isz_111(self):
        # M[AR] <- DR
        self.memory.main_memory.write(self.memory.AR.read_dec(), self.memory.DR.read_binary(), "b")

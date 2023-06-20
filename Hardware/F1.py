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
    
    def isz_000(self):
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

if __name__ == '__main__':
    # Initialize a new AllMemory object and a new F1 object
    mem = AllMemory()
    f1 = F1(mem)

    # Test the NOP instruction
    f1.instruction('000')
    assert mem.AC.read_dec() == 0

    # Test the ADD instruction
    mem.AC.write(10, "d")
    mem.DR.write(3, "d")
    f1.instruction('001')
    assert mem.AC.read_dec() == 13

    # Test the CLRAC instruction
    mem.AC.write(10, "d")
    f1.instruction('010')
    assert mem.AC.read_dec() == 0

    # Test the INCAC instruction
    mem.AC.write(10, "d")
    f1.instruction('011')
    assert mem.AC.read_dec() == 11

    # Test the DRTAC instruction
    mem.DR.write(42, "d")
    f1.instruction('100')
    assert mem.AC.read_dec() == 42

    # Test the DRTAR instruction
    mem.DR.write("0b01110111", "b")
    f1.instruction('101')
    assert mem.AR.read_binary() == "0b00001110111"

    # Test the PCTAR instruction
    mem.PC.write(10, "d")
    f1.instruction('110')
    assert mem.AR.read_dec() == 10

    # Test the WRITE instruction
    mem.DR.write(10, "d")
    mem.AR.write(5, "d")
    f1.instruction('111')
    assert mem.main_memory.read(5, 'd') == 10

    print("All tests passed!")
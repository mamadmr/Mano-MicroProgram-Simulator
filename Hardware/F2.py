from all_memory import AllMemory

class F2:
    def __init__(self, memory: AllMemory) -> None:
        self.memory = memory
        self.opt = ['000', '001', '010', '011', '100', '101', '110', '111']
        self.asm = ['NOP', 'SUB', 'OR', 'AND', 'READ', 'ACTDR','INCDR', 'PCTDR']
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
        #AC <- AC - DR
        self.memory.AC.write(self.memory.AC.read_dec() - self.memory.DR.read_dec(), "d")

    def isz_010(self):
        #AC <- AC | DR
        self.memory.AC.write(self.memory.AC.read_dec() | self.memory.DR.read_dec(), "d")

    def isz_011(self):
        #AC <- AC & DR
        self.memory.AC.write(self.memory.AC.read_dec() & self.memory.DR.read_dec(), "d")

    def isz_100(self):
        #DR <- M[AR]
        self.memory.DR.write(self.memory.main_memory.read(self.memory.AR.read_dec(), 'd'), "d")

    def isz_101(self):
        #DR <- AC
        self.memory.DR.write(self.memory.AC.read_dec(), "d")

    def isz_110(self):
        #DR <- DR + 1
        self.memory.DR.write(self.memory.DR.read_dec() + 1, "d")

    def isz_111(self):
        #DR[10:0] <- PC
        self.memory.DR.assign_bits(self.memory.PC.read_binary(), 0, 10)


if __name__ == '__main__':
    # Initialize a new AllMemory object and a new F2 object
    mem = AllMemory()
    f2 = F2(mem)

    # Test the NOP instruction
    f2.instruction('000')
    assert mem.AC.read_dec() == 0

    # Test the SUB instruction
    mem.AC.write(10, "d")
    mem.DR.write(3, "d")
    f2.instruction('001')
    assert mem.AC.read_dec() == 7

    # Test the OR instruction
    mem.AC.write("0b1010", "b")
    mem.DR.write("0b1100", "b")
    f2.instruction('010')
    assert mem.AC.read_binary() == "0b0000000000001110"

    # Test the AND instruction
    mem.AC.write("0b1010", "b")
    mem.DR.write("0b1100", "b")
    f2.instruction('011')
    assert mem.AC.read_dec() == 0b1000

    # Test the READ instruction
    mem.main_memory.write(5, 42 ,'d')
    mem.AR.write(5, "d")
    f2.instruction('100')
    assert mem.DR.read_dec() == 42

    # Test the ACTDR instruction
    mem.AC.write(10, "d")
    f2.instruction('101')
    assert mem.DR.read_dec() == 10

    # Test the INCDR instruction
    mem.DR.write(5, "d")
    f2.instruction('110')
    assert mem.DR.read_dec() == 6

    # Test the PCTDR instruction
    mem.PC.write("0b01010101010", "b")
    f2.instruction('111')
    assert mem.DR.read_binary()[-11:] == "01010101010"

    print("All tests passed!")
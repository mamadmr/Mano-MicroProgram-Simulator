from all_memory import AllMemory

class F3:
    def __init__(self, memory: AllMemory) -> None:
        self.memory = memory
        self.opt = ['000', '001', '010', '011', '100', '101', '110', '111']
        self.asm = ['NOP', 'XOR', 'COM', 'SHL', 'SHR', 'INCPC','ARTPC', 'HAL']
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

    def isz_010(self):
        # AC <- ~AC
        ans = '0b'
        for i in self.memory.AC.read_binary()[2:]:
            ans += '0' if i == '1' else '1'
        self.memory.AC.write(ans, "b")

    def isz_011(self):
        # AC <- AC << 1
        self.memory.AC.write(self.memory.AC.read_dec() << 1, "d")

    def isz_100(self):
        # AC <- AC >> 1
        self.memory.AC.write(self.memory.AC.read_dec() >> 1, "d")

    def isz_101(self):
        # PC <- PC + 1
        self.memory.PC.write(self.memory.PC.read_dec()+1, "d")

    def isz_110(self):
        # PC <- AR
        self.memory.PC.write(self.memory.AR.read_dec(), "d")

    def isz_111(self):
        # HALT
        print("---------------halt--------------------")
        raise("halt")


if __name__ == "__main__":
    mem = AllMemory()
    f3 = F3(mem)


    # test the XOR instruction
    mem.AC.write('0b1010', "b")
    mem.DR.write('0b1100', "b")
    f3.instruction('001')
    assert mem.AC.read_binary() == '0b0000000000000110'


    # test the COM instruction
    mem.AC.write('0b1010', "b")
    f3.instruction('010')
    assert mem.AC.read_binary() == '0b1111111111110101'

    # test the SHL instruction
    mem.AC.write('0b1010', "b")
    f3.instruction('011')
    assert mem.AC.read_binary() == '0b0000000000010100'

    # test the SHR instruction
    mem.AC.write('0b1010', "b")
    f3.instruction('100')
    assert mem.AC.read_binary() == '0b0000000000000101'

    # test the INCP instruction
    mem.PC.write('0b1010', "b")
    f3.instruction('101')
    assert mem.PC.read_binary() == '0b00000001011'

    # test the ARTPC instruction
    mem.AR.write('0b1010', "b")
    f3.instruction('110')
    assert mem.PC.read_binary() == '0b00000001010' 

    print("F3.py: All tests passed!")
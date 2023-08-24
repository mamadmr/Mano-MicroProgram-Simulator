from all_memory import AllMemory

class CD:
    def __init__(self, mem: AllMemory) -> None:
        self.mem = mem
        self.CD_opt = ['00', '01', '10', '11']
        self.CD_asm = ['U', 'I', 'S', 'Z']
        self.CD_func = [self.U, self.I, self.S, self.Z]

    def insruction(self, CD: str):
        # CD is a 2 bit binary string 
        # CD is the condition for the BR instruction
        for i in range(len(self.CD_opt)):
            if CD == self.CD_opt[i]:
                return self.CD_func[i]()


    def U(self):
        # The U condition is always set to 1
        return True

    def I(self):
        # The I bit is set to 1 if the leftmost bit of the DR register is 1
        return self.mem.DR.read_binary()[2] == '1'

    def S(self):
        # The S bit is set to 1 if the leftmost bit of the AC register is 1
        return self.mem.AC.read_binary()[2] == '1'

    def Z(self):
        # The Z bit is set to 1 if the AC register is equal to 0
        return self.mem.AC.read_dec(0) == 0
    

class BR:
    def __init__(self, mem: AllMemory) -> None:
        self.mem = mem
        self.opt = ['00', '01', '10', '11']
        self.asm = ['JMP', 'CALL', 'RET', 'MAP']
        self.func = [self.JMP, self.CALL, self.RET, self.MAP]

    def insruction(self, BR: str):
        for i in range(len(self.opt)):
            if BR == self.opt[i]:
                return self.func[i]()
    
    def AD(self):
        # read the last 7 bits of the control memory (next address)
        return self.mem.control_memory.read(self.mem.CAR.read_dec(), 'b')[-7:]

    def JMP(self):
        # CAR <- AD
        self.mem.CAR.write('0b'+self.AD(), "b")
    
    def CALL(self):
        # CAR <- AD, SBR <- CAR + 1
        self.mem.SBR.write(self.mem.CAR.read_dec() + 1, "d")
        self.mem.CAR.write('0b'+self.AD(), "b")

    def RET(self):
        # CAR <- SBR
        self.mem.CAR.write(self.mem.SBR.read_dec(), "d")
    
    def MAP(self):
        # CAR[0,1,6] = 0, CAR[5:2] = DR[14:11]
        opt = '0b0' + self.mem.DR.read_binary()[2:][1:5]+'00'
        self.mem.CAR.write(opt, "b")


if __name__ == "__main__":
    mem = AllMemory()

    # Test CD
    cd = CD(mem)
    mem.DR.write("0b1000000000000000", "b")
    assert cd.insruction('01') == True

    mem.DR.write("0b0000000000000000", "b")
    assert cd.insruction('01') == False

    mem.AC.write("0b1000000000000000", "b")
    assert cd.insruction('10') == True

    mem.AC.write("0b0000000000000000", "b")
    assert cd.insruction('10') == False

    mem.AC.write("0b0000000000000000", "b")
    assert cd.insruction('11') == True

    mem.AC.write("0b0000000000000001", "b")
    assert cd.insruction('11') == False

    # Test BR

    br = BR(mem)


    mem.CAR.write("0b0000000", "b")
    mem.control_memory.write(0, '0b10100111001010111000', 'b')

    br.insruction('00')
    assert mem.CAR.read_binary() == "0b0111000"

    mem.CAR.write("0b0000000", "b")
    br.insruction('01')
    assert mem.CAR.read_binary() == "0b0111000"
    assert mem.SBR.read_binary() == "0b0000001"

    br.insruction('10')
    assert mem.CAR.read_binary() == "0b0000001"

    mem.DR.write("0b1011011101111010", "b")
    br.insruction('11')
    assert mem.CAR.read_binary() == "0b0011000"

    print("All tests passed!")


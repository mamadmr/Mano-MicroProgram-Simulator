from all_memory import AllMemory
from F1 import F1
from F2 import F2
from F3 import F3
from CD_BR import CD, BR
from register import Register
import copy

class CPU:
    def __init__(self, memory=AllMemory()) -> None:
        self.memory = memory
        self.f1_memory = copy.deepcopy(memory)
        self.f2_memory = copy.deepcopy(memory)
        self.f3_memory = copy.deepcopy(memory)
        self.BR_memory = copy.deepcopy(memory)
        self.CD_memory = copy.deepcopy(memory)

        self.f1 = F1(self.f1_memory)
        self.f2 = F2(self.f2_memory)
        self.f3 = F3(self.f3_memory)
        self.CD = CD(self.CD_memory)
        self.BR = BR(self.BR_memory)
    
    def update_reg(self, reg: Register, reg1: Register, reg2: Register, reg3: Register, reg4: Register, reg5:Register):
        if reg.read_dec() != reg1.read_dec():
            reg.write(reg1.read_dec(), "d")
        elif reg.read_dec() != reg2.read_dec():
            reg.write(reg2.read_dec(), "d")
        elif reg.read_dec() != reg3.read_dec():
            reg.write(reg3.read_dec(), "d")
        elif reg.read_dec() != reg4.read_dec():
            reg.write(reg4.read_dec(), "d")
        elif reg.read_dec() != reg5.read_dec():
            reg.write(reg5.read_dec(), "d")

    def update(self):
        self.update_reg(self.memory.AC, self.f1_memory.AC, self.f2_memory.AC, self.f3_memory.AC, self.BR_memory.AC, self.CD_memory.AC)
        self.update_reg(self.memory.DR, self.f1_memory.DR, self.f2_memory.DR, self.f3_memory.DR, self.BR_memory.DR, self.CD_memory.DR)
        self.update_reg(self.memory.AR, self.f1_memory.AR, self.f2_memory.AR, self.f3_memory.AR, self.BR_memory.AR, self.CD_memory.AR)
        self.update_reg(self.memory.PC, self.f1_memory.PC, self.f2_memory.PC, self.f3_memory.PC, self.BR_memory.PC, self.CD_memory.PC)
        self.update_reg(self.memory.CAR, self.f1_memory.CAR, self.f2_memory.CAR, self.f3_memory.CAR, self.BR_memory.CAR, self.CD_memory.CAR)
        self.update_reg(self.memory.SBR, self.f1_memory.SBR, self.f2_memory.SBR, self.f3_memory.SBR, self.BR_memory.SBR, self.CD_memory.SBR)
        for i in range(0, 128):
            self.update_reg(self.memory.control_memory.memory[i], self.f1_memory.control_memory.memory[i], self.f2_memory.control_memory.memory[i], self.f3_memory.control_memory.memory[i], self.BR_memory.control_memory.memory[i], self.CD_memory.control_memory.memory[i])
        for i in range(0, 2048):
            self.update_reg(self.memory.main_memory.memory[i], self.f1_memory.main_memory.memory[i], self.f2_memory.main_memory.memory[i], self.f3_memory.main_memory.memory[i], self.BR_memory.main_memory.memory[i], self.CD_memory.main_memory.memory[i])
    def clock(self):
        self.memory.reset_flag()
        self.f1_memory = copy.deepcopy(self.memory)
        self.f2_memory = copy.deepcopy(self.memory)
        self.f3_memory = copy.deepcopy(self.memory)
        self.BR_memory = copy.deepcopy(self.memory)
        self.CD_memory = copy.deepcopy(self.memory)

        self.f1.memory = self.f1_memory
        self.f2.memory = self.f2_memory
        self.f3.memory = self.f3_memory
        self.CD.mem = self.CD_memory
        self.BR.mem = self.BR_memory

        opt = self.memory.control_memory.read(self.memory.CAR.read_dec(), 'b')[2:]
        self.f1.instruction(opt[0:3])
        self.f2.instruction(opt[3:6])
        self.f3.instruction(opt[6:9])
        if self.CD.insruction(opt[9:11]):
            self.BR.insruction(opt[11:13])
        else:
            self.BR_memory.CAR.write(self.BR_memory.CAR.read_dec() + 1, "d")
        self.update()
        if self.memory.check_flags():
            raise("Error in CPU, Write in the same space twice in the same clock cycle")
    def print_reg(self):
        print('AC:', self.memory.AC.read_dec())
        print('DR:', self.memory.DR.read_binary())
        print('AR:', self.memory.AR.read_binary())
        print('PC:', self.memory.PC.read_dec())
        print('CAR:', self.memory.CAR.read_dec())
        print('SBR:', self.memory.SBR.read_dec())
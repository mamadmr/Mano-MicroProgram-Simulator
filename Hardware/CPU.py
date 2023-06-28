from all_memory import AllMemory
from F1 import F1
from F2 import F2
from F3 import F3
from CD_BR import CD, BR
import json

class CPU:
    def __init__(self, memory=AllMemory()) -> None:
        self.memory = memory
        self.f1 = F1(self.memory)
        self.f2 = F2(self.memory)
        self.f3 = F3(self.memory)
        self.CD = CD(self.memory)
        self.BR = BR(self.memory)
        self.memory = memory

    def make_json(self):
        ans = dict()
        ans['AC'] = [self.memory.AC.read_dec(), self.memory.AC.read_binary(), self.memory.AC.read_hex()]
        ans['DR'] = [self.memory.DR.read_dec(), self.memory.DR.read_binary(), self.memory.DR.read_hex()]
        ans['AR'] = [self.memory.AR.read_dec(), self.memory.AR.read_binary(), self.memory.AR.read_hex()]
        ans['PC'] = [self.memory.PC.read_dec(), self.memory.PC.read_binary(), self.memory.PC.read_hex()]
        ans['CAR'] = [self.memory.CAR.read_dec(), self.memory.CAR.read_binary(), self.memory.CAR.read_hex()]
        ans['SBR'] = [self.memory.SBR.read_dec(), self.memory.SBR.read_binary(), self.memory.SBR.read_hex()]
        ans['main'] = []
        ans['micro'] = []
        for i in self.memory.main_memory.iter():
            ans['main'].append([i.read_dec(), i.read_binary(), i.read_hex()])
        
        for i in self.memory.control_memory.iter():
            ans['micro'].append([i.read_dec(), i.read_binary(), i.read_hex()])
        
        return  json.dumps(ans)

    def json_to_memory(self, file):
        # convert jason to memory
        # convert json to dictionary
        file = json.loads(file)
        return file
        #temp = AllMemory()
        
    def clock(self):
        self.memory.reset_flag()
        opt = self.memory.control_memory.read(self.memory.CAR.read_dec(), 'b')[2:]
        self.f1.instruction(opt[0:3])
        self.f2.instruction(opt[3:6])
        self.f3.instruction(opt[6:9])
        if self.CD.insruction(opt[9:11]):
            self.BR.insruction(opt[11:13])
        else:
            self.memory.CAR.write(self.memory.CAR.read_dec() + 1, "d")
        if self.memory.check_flags():
            raise("Error in CPU, Write in the same space twice in the same clock cycle")

    def print_reg(self):
        print('AC:', self.memory.AC.read_dec())
        print('DR:', self.memory.DR.read_binary())
        print('AR:', self.memory.AR.read_binary())
        print('PC:', self.memory.PC.read_dec())
        print('CAR:', self.memory.CAR.read_dec())
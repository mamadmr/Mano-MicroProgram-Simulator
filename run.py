import os 
import sys

add2 = os.getcwd() + '/Hardware'
add1 = os.getcwd() + '/Assembler'
sys.path.append(add1)
sys.path.append(add2)


import all_memory as memory
import mainprogram as assembler
import CPU as cpu

def load(micro_code, main_code):
    micro, main = assembler.assembler(micro_code, main_code)
    mem = memory.AllMemory()
    for i in micro:
        bin, address = i.split('-')
        mem.control_memory.write(int(address), '0b'+bin, 'b')
    
    for j in main:
        bin, address = j.split('-')
        mem.main_memory.write(int(address), '0b'+bin, 'b')
    
    mem.CAR.write(64, 'd')
    mem.PC.write(0, 'd')
    return cpu.CPU(mem)






if __name__ == "__main__":
    micro_code = """ORG 0
    ADD: NOP I CALL INDRCT
        READ U JMP NEXT
        ADD U JMP FETCH
    ORG 4
    BRANCH: NOP S JMP OVER
            NOP U JMP FETCH
    OVER:   NOP I CALL INDRCT
            ARTPC U JMP FETCH
    ORG 8
    STORE: NOP I CALL INDRCT
           ACTOR U JMP NEXT 
           WRITE U JMP FETCH
    ORG 12
    EXCHANGE:   NOP              I CALL INDRCT
                READ             U JMP NEXT
                ACTDR, DRTAC     U JMP NEXT
                WRITE            U JMP FETCH
    ORG 64 
    FETCH: PCTAR U JMP NEXT
           READ, INCPC U JMP NEXT
           DRTAR U JMP MAP
    INDRCT: READ U JMP NEXT
            DRTAR U RET"""
    

    main_code = """ORG 0
        ADD DEC1000
        ADD DEC1000 
        ADD DEC1000 
        STORE DEC100
        STORE HEXFF
        STORE BIN1111
    ORG 1000
    A1: DEC20
    A2: DEC30
    A3: DEC40
    """

    computer = load(micro_code, main_code)
    computer.print_reg()
    for i in range(50):
        print('--------------')
        computer.clock()
        computer.print_reg()
    
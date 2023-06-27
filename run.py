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
    ORG 16
    HAL: HAL U JMP
    ORG 64 
    FETCH: PCTAR U JMP NEXT
           READ, INCPC U JMP NEXT
           DRTAR U JMP MAP
    INDRCT: READ U JMP NEXT
            DRTAR U RET"""
    

    main_code = """ORG 0
        ADD A1 I
        ADD A2 
        ADD A3 
        STORE DEC100
        STORE HEXFF
        STORE BIN1111
        HAL DEC100
    ORG 1000
    A1: DEC1001
    A2: DEC30
    A3: DEC40
    """
    micro, main = assembler.assembler(micro_code, main_code)

    computer = load(micro_code, main_code)
    computer.print_reg()
    for i in range(50):
        print(i)
        print('--------------')
        computer.clock()
        computer.print_reg()
    



    """
    
00000000001011000011-0
00010000000000000010-1
00100000000001000000-2
00000000010000000110-4
00000000000001000000-5
00000000001011000011-6
00000011000001000000-7
00000000001011000011-8
00000000000000001010-9
11100000000001000000-10
00000000001011000011-12
00010000000000001110-13
10010100000000001111-14
11100000000001000000-15
11000000000001000001-64
00010010100001000010-65
10100000000110000000-66
00010000000001000100-67
10100000000100000000-68
--------------------
0000001111101000-0
0000001111101000-1
0000001111101000-2
0001000001100100-3
0001000011111111-4
0001000000001111-5
0000000000010100-1000
0000000000011110-1001
0000000000101000-1002
    
    
    """
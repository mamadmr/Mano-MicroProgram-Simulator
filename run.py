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


# command line to control simulator 
# >clock num                           done
# >clock next command                  done    
# >run                                 done
# >memory address                      done
# >registers                           done
# >write address value                 done
# >load mircro file_address            done
# >load main file_address              done 
# >assemble                            done
# >quit                                done
# >help
# >codes                               done

def show_code(micro_bin, main_bin):
    print("micro code")
    for i in micro_bin:
        i = i.split('-')
        print(i[1], i[0])
    print('--------------------------------------------------')
    print("main code")
    for i in main_bin:
        i = i.split('-')
        print(i[1], i[0])
    print('--------------------------------------------------')

def main():
    micro = None
    main = None
    micro_bin = None
    main_bin = None
    computer = None

    while True:
        print("****************************************************")
        inp = input(">>> ").split()
        if inp[0] == 'quit':
            break
        elif inp[0] == "write":
            try:
                computer.memory.main_memory.write(int(inp[1]), int(inp[2]), 'd')
            except:
                print("syntax error")
        elif inp[0] == "load":
            if inp[1] == 'main':
                try:
                    with open(inp[2], 'r') as f:
                        main = str(f.read())
                    print(main)
                except:
                    print("file not found")

            elif inp[1] == 'micro':
                try:
                    with open(inp[2], 'r') as f:
                        micro = str(f.read())
                    print(micro)
                except:
                    print("file not found")
            else:
                print("syntax error") 
        elif inp[0] == 'assemble':
            micro_bin, main_bin = assembler.assembler(micro, main)
            computer = load(micro, main)
            show_code(micro_bin, main_bin)
        elif inp[0] == 'clock':
            computer.clock()
            if inp[1] == 'next':
                while computer.memory.CAR.read_dec() != 64:
                    computer.clock()
            else:
                try:
                    for _ in range(int(inp[1])):
                        computer.clock()
                except:
                    print("syntax error")
        
        elif inp[0] == 'register':
            computer.print_reg()
        
        elif inp[0] == 'memory':
            print(computer.memory.main_memory.read(int(inp[1]), 'd'))
            try:
                pass
            except:
                print("syntax error")
        elif inp[0] == 'codes':
            show_code(micro_bin, main_bin)
        elif inp[0] == 'run':
            try:
                while True:
                    computer.clock()
            except:
                pass
        else:
            print("command not found")

if __name__ == "__main__":
    main()

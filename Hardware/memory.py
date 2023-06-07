from register import *

class Memory:
    def __init__(self, block_size, address_size) -> None:
        self.memory = []
        for i in range(2**address_size):
            self.memory.append(Register(block_size, "0"*block_size))

    def read(self,address, type):
        if type == "b":
            return self.memory[address].read_binary()
        elif type == 'd':
            return self.memory[address].read_dec()
        elif type == 'h':
            return self.memory[address].read_hex()

    def write(self,address,value, type):
        self.memory[address].write(value,type)

if __name__ == "__main__":
    A = Memory(16, 10)
    A.write(0,"0b1111111111111111","b")
    print(A.read(0,"b"))
    print(A.read(0,"d"))
    print(A.read(0,"h"))
    A.write(1,"0b11","b")
    A.write(2,"0b110","b")
    A.write(3, A.read(1,"d")+A.read(2,"d"),"d")
    print(A.read(3,"b"))
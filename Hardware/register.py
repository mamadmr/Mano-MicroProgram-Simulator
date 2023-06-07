from math import ceil


class Register:
    def __init__(self,number_of_bits =16 ,initial_value="") -> None:
        self.number_of_bits = number_of_bits
        self._reg_value = initial_value
    
    @property
    def _reg_value(self):
        return self._value
    
    @_reg_value.setter
    def _reg_value(self,value):
        self._value = self.normalize(value,self.number_of_bits)

    def normalize(self, value, number_of_bits):
        if len(value) <= number_of_bits:
            # add zeros to the left side
            value = "0"*(number_of_bits-len(value)) + value
        elif len(value) > number_of_bits:
            # just save the less valuable bits
            value = value[-number_of_bits:]
        return value

    def write(self,value, type):
        # type can be b, h, d for binary, hex, decimal
        # the value should be in correct format 
        # for example if type is b, value should be like "0b1010"
        # if type is h, value should be like "0xaf10"
        # if type is d, value should be like 10 

        if type == "b":
            self._reg_value = value[2:]
        elif type == 'd':
            self._reg_value = bin(int(value))[2:]
        elif type == 'h':
            self._reg_value = bin(int(value,16))[2:]

    def read_binary(self) -> str:
        # return the binary value of the register
        return '0b' + self._reg_value

    def read_hex(self) -> str:
        # return the hex value of the register
        output = hex(int(self._reg_value,2))[2:]
        len_out = ceil(self.number_of_bits/4)
        if len(output) < len_out:
            output = "0"*(len_out-len(output)) + output
        return output 

    def read_dec(self) -> int:
        # return the decimal value of the register
        return int(self._reg_value,2)



if __name__ == "__main__":
    A = Register(13,"1111111111")
    print(A.read_binary())
    print(A.read_hex())
    print(A.read_dec())
    A.write("0xaf", 'h')
    print(A.read_binary())
    print(A.read_hex())
    A.write("0b1010", 'b')
    print(A.read_binary())
    print(A.read_hex())
    A.write(15, 'd')
    print(A.read_binary())
    print(A.read_hex())
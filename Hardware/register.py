class register:
    def __init__(self,number_of_bits =16 ,initial_value="") -> None:
        self.value = initial_value
        self.number_of_bits = number_of_bits

        if len(self.value) <= number_of_bits:
            # add zeros to the left side
            self.value = "0"*(number_of_bits-len(self.value)) + self.value
        elif len(self.value) > number_of_bits:
            # just save the less valuable bits
            self.value = self.value[-number_of_bits:]

    def read_binary(self) -> str:
        # return the binary value of the register
        return '0b' + self.value

    def read_hex(self) -> str:
        # return the hex value of the register
        return hex(int(self.value,2))

    def read_dec(self) -> int:
        # return the decimal value of the register
        return int(self.value,2)



if __name__ == "__main__":
    A = register(16,"10000")
    print(A.read_binary())
    print(A.read_hex())
    print(A.read_dec())
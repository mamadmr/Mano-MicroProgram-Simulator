from math import ceil


class Register:
    def __init__(self, number_of_bits: int = 16, initial_value: str = "") -> None:
        """
        A class representing a register.

        :param number_of_bits: The number of bits in the register. The register should have a fixed size.
        :param initial_value: The initial binary value of the register with a '0b' prefix.

        The most significant bit is the leftmost bit. We assume the indexing is from right to left, just like in the Mano book (mirrored of the Python indexing). We don't save '0b' as a prefix of the value in the register, but you have to use the standard format for writing the initial_value.
        """

        # Check for valid input
        initial_value = self.check_bainary_format(initial_value)

        self.number_of_bits = number_of_bits
        self._reg_value = initial_value
    
    def test_bits(self, value: str) -> bool:
        """
        Test if all the bits in the value are either 0 or 1.

        :return: True if the binary value contains only 0's and 1's, False otherwise.
        """
        for bit in value:
            if bit != '0' and bit != '1':
                return False
        return True

    def check_bainary_format(self, value: str) -> str:
        """
        Check if the value is in binary format and return the value without '0b' prefix.

        :param value: The value to check.
        :return: The value without '0b' prefix.
        """
        if value[:2] != '0b':
            raise Exception("The value should be in binary format with '0b' prefix")
        
        # remove the '0b' prefix
        value = value[2:]

        if self.test_bits(value) == False:
            raise Exception("The value should be in binary format consisting of 0s and 1s")
        
        return value

    @property
    def _reg_value(self):
        """
        Get the value of the register.

        :return: The value of the register.

        it's a private method. 
        so the return value doesn't have '0b' prefix.
        """
        return self._value
    
    @_reg_value.setter
    def _reg_value(self, value: str):
        """
        Set the value of the register.

        :param value: The new value of the register.

        this is a private method.
        so you here assume that the value doesn't have '0b' prefix.
        """
        self._value = self.normalize(value)

    def assign_bits(self, value: str, start: int, end: int):
        """
        Assign the value to the bits from start to end (inclusive).

        :param value: The value to assign.
        :param start: The starting bit position.
        :param end: The ending bit position.

        the value should be in binary format with '0b' prefix.

        the indexing is from right to left just like the mano book.
        """

        # Check for valid input
        value = self.check_bainary_format(value)

        if end - start + 1 != len(value):
            # The length of the value should be equal to end-start+1
            raise Exception("The length of the value should be equal to end-start+1")
        if end >= self.number_of_bits:
            # The end should be less than the number of bits
            raise Exception("The end should be less than the number of bits")
        if start < 0:
            # The start should be positive
            raise Exception("The start should be positive")
        if start > end:
            # The start should be less than or equal to end
            raise Exception("The start should be less than or equal to end")
        
        # make the indexing from left to right just like the python indexing 
        # because the indexing of the input is from right to left just like the mano book 
        end = self.number_of_bits - start - 1
        start = self.number_of_bits - end - 1

        # Assign the value to the specified bits
        self._reg_value = self._reg_value[:start] + value + self._reg_value[end + 1:]

    def normalize(self, value: str):
        """
        Normalize the value to the specified number of bits.

        :param value: The value to normalize.
        :return: The normalized value.
        """
        if len(value) <= self.number_of_bits:
            # Add zeros to the left side
            value = "0" * (self.number_of_bits - len(value)) + value
        elif len(value) > self.number_of_bits:
            # Save the less valuable bits
            value = value[-self.number_of_bits:]
        return value

    def write(self, value: str, type: str):
        """
        Write the value to the register.

        :param value: The value to write. should have correct prefix.
            '0b' for binary, '0h' for hexadecimal
        :param type: The type of the value (b for binary, h for hex, d for decimal).
        """
        # Check the type of the value and convert it to binary
        if type == "b":
            # If the type is binary
            # Check for valid input
            value = self.check_bainary_format(value)
            self._reg_value = value

        elif type == 'd':
            # If the type is decimal, convert the value to binary
            self._reg_value = bin(int(value))[2:]
        elif type == 'h':
            # If the type is hex, convert the value to binary
            # remove the prefix "0h"
            self._reg_value = bin(int(value, 16))[2:]

    def read_binary(self) -> str:
        """
        Get the binary value of the register.

        :return: The binary value of the register.
        """
        # Add the prefix "0b" to the binary value
        return '0b' + self._reg_value

    def read_hex(self) -> str:
        """
        Get the hexadecimal value of the register.

        :return: The hexadecimal value of the register.
        """
        # Convert the binary value to hexadecimal
        output = hex(int(self._reg_value, 2))[2:]

        # Add leading zeros if necessary
        len_out = ceil(self.number_of_bits / 4)
        if len(output) < len_out:
            output = "0" * (len_out - len(output)) + output

        # Add the prefix "0h" to the hexadecimal value
        return '0h' + output 

    def read_dec(self) -> int:
        """
        Get the decimal value of the register.

        :return: The decimal value of the register.
        """
        # Convert the binary value to decimal
        return int(self._reg_value, 2)


if __name__ == '__main__':
    # Create a new register with 8 bits and an initial value of 0
    reg = Register(8, '0b00000000')

    # Test the assign_bits method
    reg.assign_bits('0b101', 2, 4)
    assert reg.read_binary() == '0b00010100'

    # Test the write method with a binary value
    reg.write('0b1100', 'b')
    assert reg.read_binary() == '0b00001100'

    # Test the write method with a hexadecimal value
    reg.write('0x3f', 'h')
    assert reg.read_binary() == '0b00111111'

    # Test the write method with a decimal value
    reg.write(128, 'd')
    assert reg.read_binary() == '0b10000000'

    # Test the read_binary method
    assert reg.read_binary() == '0b10000000'

    # Test the read_hex method
    assert reg.read_hex() == '0h80'

    # Test the read_dec method
    assert reg.read_dec() == 128

    # Test the normalize method with a value that is too long
    assert reg.normalize('101010101010101010101010101010101') == '01010101'

    # Test the normalize method with a value that is too short
    assert reg.normalize('101') == '00000101'

    # Test the normalize method with a value that is the correct length
    assert reg.normalize('0b10101010') == '10101010'


    reg.write('0b0', 'b')
    # Test the assign_bits method with a valid range
    reg.assign_bits('0b101', 2, 4)
    assert reg.read_binary() == '0b00010100'

    try:
        # Test the assign_bits method with a range that is too long
        reg.assign_bits('0b10101010', 2, 6)
    except:
        pass
    try:
        # Test the assign_bits method with a range that is too short
        reg.assign_bits('0b1', 2, 4)
    except:
        pass
    try:
        # Test the assign_bits method with a range that is out of bounds
        reg.assign_bits('0b101', 8, 10)
    except:
        pass
    try:
        # Test the assign_bits method with a value that is too long
        reg.assign_bits('0b101010101010101010101010101010101', 2, 10)
    except:
        pass
    try:
        # Test the assign_bits method with a value that is too short
        reg.assign_bits('0b1', 2, 10)
    except:
        pass

    print("All tests passed!")
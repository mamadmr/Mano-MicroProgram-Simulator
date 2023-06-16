from register import Register

class Memory:
    def __init__(self, block_size: int, address_size: int) -> None:
        """
        Initialize a new Memory object.

        :param block_size: The size of each block in bits.
        :param address_size: The size of the address space in bits. the number of the blocks is 2^address_size.

        This method creates a new Memory object with an address space of 2^address_size blocks, each with a size of block_size bits. The memory is initialized with all blocks set to 0.
        """
        # Create an empty list to hold the memory blocks
        self.memory = []

        # Initialize each block in the memory with a new Register object
        for i in range(2**address_size):
            self.memory.append(Register(block_size))

    def read(self, address: int, type: str):
        """
        Read a value from the memory at the given address.

        :param address: The address of the memory block to read.
        :param type: The type of value to read. This should be one of 'b' (binary), 'd' (decimal), or 'h' (hexadecimal).

        This method reads a value from the memory at the given address and returns it in the specified format. If the type is 'b', the value is returned as a binary string. If the type is 'd', the value is returned as a decimal integer. If the type is 'h', the value is returned as a hexadecimal string.
        """
        # Check if the address is within the bounds of the memory
        self._check_address(address)

        if type == "b":
            # Read the value as a binary string
            return self.memory[address].read_binary()
        elif type == 'd':
            # Read the value as a decimal integer
            return self.memory[address].read_dec()
        elif type == 'h':
            # Read the value as a hexadecimal string
            return self.memory[address].read_hex()

    def write(self, address: int, value: str, type: str):
        """
        Write a value to the memory at the given address.

        :param address: The address of the memory block to write to.
        :param value: The value to write to the memory block.
        :param type: The type of value to write. This should be one of 'b' (binary), 'd' (decimal), or 'h' (hexadecimal).

        This method writes a value to the memory at the given address. The value should be in the specified format. If the type is 'b', the value should be a binary string. If the type is 'd', the value should be a decimal integer. If the type is 'h', the value should be a hexadecimal string.
        """
        # Check if the address is within the bounds of the memory
        self._check_address(address)
        # Write the value to the memory block at the given address
        self.memory[address].write(value, type)

    def _check_address(self, address: int):
        """
        Check if the given address is within the bounds of the memory.

        :param address: The address to check.

        :raises IndexError: If the address is out of bounds.

        :return: None.
        """
        # Check if the address is greater than or equal to 0 and less than the length of the memory
        if address < 0 or address >= len(self.memory):
            # If the address is out of bounds, raise an IndexError
            raise IndexError("Address out of bounds")
    
    def reset_flags(self):
        """
        Reset the flag for all memory blocks.

        This method resets the flag for all memory blocks in the memory. The flag is used to indicate whether the memory block has been accessed or not.
        """
        # Loop through all memory blocks and reset their flags
        for i in self.memory:
            i.reset_flag()
    
    def check_flags(self):
        """
        Check if any memory blocks have been accessed.

        :return: True if any memory blocks have been accessed, False otherwise.
        """
        # Loop through all memory blocks and check if any have been accessed
        for i in self.memory:
            if i.check_flag():
                # If a memory block has been accessed, return True
                return True
        # If no memory blocks have been accessed, return False
        return False

if __name__ == "__main__":
    # Test the initialization of a new Memory object
    mem = Memory(8, 3)
    assert mem.read(0, "b") == "0b00000000"

    # Test writing and reading a binary value
    mem.write(1, "0b10101010", "b")
    assert mem.read(1, "b") == "0b10101010"

    # Test writing and reading a decimal value
    mem.write(2, 255, "d")
    assert mem.read(2, "d") == 255

    # Test writing and reading a hexadecimal value
    mem.write(3, "0xFF", "h")
    assert mem.read(3, "h") == "0xff"

    # Test writing and reading a binary value with a decimal address
    mem.write(4, "0b11110000", "b")
    assert mem.read(4, "b") == "0b11110000"

    # Test writing and reading a decimal value with a hexadecimal address
    mem.write(5, 42, "d")
    assert mem.read(0x05, "d") == 42

    # Test writing and reading a hexadecimal value with a binary address
    mem.write(6, "0x1A", "h")
    assert mem.read(6, "h") == "0x1a"

    # check that an IndexError is raised when trying to read from an out of bounds address
    try:
        mem.read(8, "b")
    except:
        pass
    
    print("All tests passed!")
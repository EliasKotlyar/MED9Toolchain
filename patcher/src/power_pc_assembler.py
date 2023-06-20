class PowerPCAssembler:
    def __init__(self):
        self.instructions = []

    def generate_b_instruction(self, target_address):
        opcode = 0x48000002
        offset = (target_address - 4) & 0x03FFFFFC
        instruction = opcode | offset

        # Convert the instruction to a byte array
        instruction_bytes = instruction.to_bytes(4, byteorder='big')

        return instruction_bytes

    def generate_bl_instruction(self, function_address):
        opcode = 0x48000000
        offset = (function_address - 4) & 0x03FFFFFC
        instruction = opcode | offset

        # Convert the instruction to a byte array
        instruction_bytes = instruction.to_bytes(4, byteorder='big')

        return instruction_bytes

    def assemble_from_list(self, lines: []):
        bytecode = bytearray()
        for line in lines:
            parts = line.replace(",", " ").strip().split(' ')
            opcode = parts[0]
            operands = parts[1:]

            if opcode == 'b':
                address = int(operands[0], 16)
                bytecode += self.generate_b_instruction(address)

            elif opcode == 'bl':
                address = int(operands[0], 16)
                bytecode += self.generate_bl_instruction(address)


            else:
                raise ValueError("Opcode '" + opcode + "' not found!")
            # Add more opcode handlers as needed...

        return bytecode.hex().upper()

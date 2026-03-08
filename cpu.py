class CPU:
    def __init__(self, memory):
        # Registers
        self.registers = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0
        }

        # Program counter
        self.PC = 0

        # Memory reference
        self.memory = memory

        # Running state
        self.running = True


    def fetch(self):
        instruction = self.memory[self.PC]
        self.PC += 1
        return instruction


    def execute(self, instruction):
        parts = instruction.split()
        op = parts[0]

        if op == "MOV":
            reg = parts[1]
            val = int(parts[2])
            self.registers[reg] = val

        elif op == "ADD":
            reg1 = parts[1]
            reg2 = parts[2]
            self.registers[reg1] += self.registers[reg2]

        elif op == "SUB":
            reg1 = parts[1]
            reg2 = parts[2]
            self.registers[reg1] -= self.registers[reg2]

        elif op == "PRINT":
            reg = parts[1]
            print(self.registers[reg])

        elif op == "HLT":
            self.running = False

        else:
            print("Unknown instruction:", instruction)


    def run(self):
        while self.running:
            instruction = self.fetch()
            self.execute(instruction)

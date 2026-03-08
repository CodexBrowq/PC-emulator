import requests

class CPU:
    def __init__(self, program):
        self.registers = {"A": 0, "B": 0, "C": 0, "D": 0}
        self.PC = 0
        self.program = program
        self.running = True

    def fetch(self):
        instr = self.program[self.PC]
        self.PC += 1
        return instr

    def execute(self, instr):
        parts = instr.split()
        op = parts[0]

        if op == "MOV":
            reg, val = parts[1], int(parts[2])
            self.registers[reg] = val

        elif op == "ADD":
            reg1, reg2 = parts[1], parts[2]
            self.registers[reg1] += self.registers[reg2]

        elif op == "SUB":
            reg1, reg2 = parts[1], parts[2]
            self.registers[reg1] -= self.registers[reg2]

        elif op == "PRINT":
            reg = parts[1]
            print(self.registers[reg])

        elif op == "GET":
            reg, url = parts[1], parts[2]
            try:
                response = requests.get(url)
                self.registers[reg] = len(response.text)  # zapisujemy długość strony
            except:
                self.registers[reg] = -1  # błąd pobierania

        elif op == "INPUT":
            reg, prompt = parts[1], " ".join(parts[2:])
            val = input(prompt + " ")
            try:
                self.registers[reg] = int(val)
            except:
                self.registers[reg] = val  # jeśli nie liczba, zapisujemy tekst

        elif op == "HLT":
            self.running = False

        else:
            print("Nieznana instrukcja:", instr)

    def run(self):
        while self.running:
            instr = self.fetch()
            self.execute(instr)

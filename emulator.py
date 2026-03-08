from cpu import CPU

program = [
    "MOV A 5",
    "MOV B 10",
    "ADD A B",
    "PRINT A",
    "HLT"
]

cpu = CPU(program)
cpu.run()

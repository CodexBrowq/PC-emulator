from cpu import CPU

with open("program.asm") as f:
    program = [line.strip() for line in f if line.strip()]

cpu = CPU(program)
cpu.run()

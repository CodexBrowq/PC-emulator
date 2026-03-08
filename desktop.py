from cpu import CPU

def load_program(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

def mini_desktop():
    print("=== Witaj w Mini Pulpicie Emulatora ===")
    cpu = None

    while True:
        command = input(">>> ").strip()

        if command.upper() == "EXIT":
            print("Zamykanie Mini Pulpitu...")
            break

        elif command.upper().startswith("RUN"):
            parts = command.split()
            if len(parts) < 2:
                print("Użycie: RUN <nazwa_programu.asm>")
                continue
            filename = parts[1]
            try:
                program = load_program(filename)
                cpu = CPU(program)
                cpu.run()
            except FileNotFoundError:
                print(f"Nie znaleziono pliku {filename}")

        elif command.upper() == "REG":
            if cpu:
                print(cpu.registers)
            else:
                print("CPU nie jest uruchomiony")

        else:
            print("Nieznane polecenie. Dostępne: RUN, REG, EXIT")

if __name__ == "__main__":
    mini_desktop()

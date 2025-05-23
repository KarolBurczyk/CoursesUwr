# W moim rozwiązaniu przechodzę po sekwencji cyfr biorąc po n naraz (gdzie n jest podane jako wejściowe) i sprawdzam ile najwięcej jedynek mogę z tej
# sekwencji wykorzystać. Na koniec prosto podliczam ile cyfr muszę w sumie zmienić i zwracam wynik.

def count_gaps(sequence, gap):
    maks = 0
    for i in range(len(sequence)-gap+1):
        if maks < sequence[i:i+gap].count("1"):
            maks = sequence[i:i+gap].count("1")
    return sequence.count("1") - maks + (gap - maks)


def main(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    results = []
    for line in lines:
        parts = line.strip().split()
        sequence, gap = parts[0], int(parts[1])
        result = count_gaps(sequence, gap)
        results.append(str(result))
    
    with open(output_file, 'w') as f:
        f.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main("zad4_input.txt", "zad4_output.txt")
def read_numbers(filepath):
    total = 0
    count = 0

    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                try:
                    num = int(line)
                    total += num
                    count += 1
                except ValueError:
                    print(f"Skipping invalid line: '{line}'")

    except FileNotFoundError:
        print(f"File '{filepath}' \n not found.")
        return

    if count > 0:
        average = total / count
        print(f"Total: {total}")
        print(f"Count: {count}")
        print(f"Average: {average:.2f}")
    else:
        print("No valid numbers found.")

if __name__ == "__main__": ## code here runs only when the script is run directly
    file_path = r"D:\DOWNLOAD\PYTHON\Python30DaysChallenge\Day_10(Exception Handling).txt"
    read_numbers(file_path)




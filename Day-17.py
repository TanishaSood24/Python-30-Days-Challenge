class ManagedTextFile:
    def __init__(self, name, mode="r"):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print("Opening file for reading...")
        self.f = open(self.name, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("File read complete. Closing now.")
        self.f.close()


with ManagedTextFile("Day_10(Exception Handling).txt") as file:
    for line in file:
        print(line.strip())



        







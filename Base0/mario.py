#for i in range(3):
#    print("\n#", end="")

#for i in range(4):
#    print("?", end="")

def main():
    print_square(3)
    print_row(4)
    print_column(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
        
def print_row(width):
    print("?" * width)

def print_column(height):
    for _ in range(height):
        print("#")

main()


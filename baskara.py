import math
matrix = [1,3,-9]

def baskara(matrix):
    minus_b = matrix[1] * -1
    ecuation = (minus_b**2) - (4 * matrix[0] * matrix[2])
    divider = matrix[0] * 2
    if ecuation < 0:
        print("No root found")
        return
    roots = [ (minus_b + math.sqrt(ecuation)) / divider, (minus_b - math.sqrt(ecuation)) / divider]
    print(roots)
    return roots

def main():
    roots = baskara(matrix)


if __name__ == "__main__":
    main()


from SuperMatrix import SuperMatrix as SM
def main():
    matrix = SM([
        [1,-3,2,-3],
        [5,6,-1,13],
        [4,-1,3,8],
        ])
    print(matrix.cramer_method())


if __name__ == "__main__":
    main()


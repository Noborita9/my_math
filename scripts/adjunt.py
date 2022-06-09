matrix = [
        [1,2,3],
        [1,2,3],
        [1,2,3],
        ]
def get_stats(matrix):
    stats = {
            "size" : {
                "length": len(matrix[0]),
                "height": len(matrix)
                },
            "method": None
            }
    if stats["size"]["length"] == 3 and stats["size"]["height"] == 3:
        stats["method"] = "sarrus"
    return stats


def get_adjunt(matrix):
    stats = get_stats(matrix)
    print(f"doing method {stats['method']}")


def main():
    get_adjunt(matrix)


if __name__ == "__main__":
    main()

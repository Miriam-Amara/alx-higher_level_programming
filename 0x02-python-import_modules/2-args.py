#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    else:
        for n in range(len(argv) - 1):
            if n == 0:
                if len(argv) == 2:
                    print(f"{len(argv) - 1} argument:")
                else:
                    print(f"{len(argv) -1 } arguments:")
            print(f"{n + 1}: {argv[n + 1]}")

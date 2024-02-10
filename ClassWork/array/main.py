def find_smallest_integer(N, D):
    N_str = str(N)
    D_str = str(D)

    while D_str in N_str:
        N += 1
        N_str = str(N)

    return N

def main():
    T = int(input())
    results = []

    for _ in range(T):
        N, D = map(int, input().split())
        result = find_smallest_integer(N, D)
        results.append(result)

    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()

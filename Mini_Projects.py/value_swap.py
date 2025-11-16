def main():
    values = [12, 16, 5, 8, 6, 21]
    sorted_values = sorted(values)
    i = 0
    j = len(sorted_values) // 2
    while i < len(sorted_values) // 2:
        swap(sorted_values, i, j )
        i += 1
        j += 1
    print(sorted_values)


def swap(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp

main()
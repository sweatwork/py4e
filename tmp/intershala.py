def is_part_of_series(lst):
    for n in lst:
        if n == 0 or n == 1:
            continue
        s = 2 * lst(n-1) - 2 * lst(n-2)
        if n != s:
            print("Not all the numbers belong to the series.")


num_list = [0, 1, -3, 8, 9]
is_part_of_series(num_list)

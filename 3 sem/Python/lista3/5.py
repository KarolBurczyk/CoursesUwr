# aglorytm Kadane poszerzony o zapisywanie indeksów i oraz j opisujących początek i koniec podciągu 

def max_sub_list_sum_2(my_list):
    local_max = total_max = my_list[0]
    local_max_id = total_max_id = (0, 0)
    for i in range(1, len(my_list)):
        if my_list[i] > local_max + my_list[i]:
            local_max = my_list[i]
            local_max_id = (i, i)
        else:
            local_max += my_list[i]
            local_max_id = (local_max_id[0], i)
        if local_max > total_max:
            total_max = local_max
            total_max_id = local_max_id
    return total_max_id


print(max_sub_list_sum_2([4, -10, 3, 29, -3, 12, -5, 4]))
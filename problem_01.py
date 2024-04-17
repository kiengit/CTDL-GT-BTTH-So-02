def find_max_sliding_window(num_list, k):
    result = []
    n = len(num_list)
    for i in range(n - k + 1):
        window = num_list[i:i+k]
        result.append(max(window))
    return result

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(find_max_sliding_window(num_list, k))

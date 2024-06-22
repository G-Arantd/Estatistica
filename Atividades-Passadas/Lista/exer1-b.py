from statistics import mode, median

num_list = [1, 1, 3, 2, 3, 5, 4, 5, 3, 3, 2, 2, 1, 1]

num_list.sort()

median_list = median(num_list)

moda_list = mode(num_list)

aven_list = sum(num_list)/len(num_list)

print(f"Média: {aven_list}")
print(f"Moda: {moda_list}")
print(f"Mediana: {median_list}")
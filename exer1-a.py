from statistics import mode, median

num_list = [46, 44, 49, 45, 44, 48, 50, 42, 47]

num_list.sort()

median_list = median(num_list)

moda_list = mode(num_list)

aven_list = sum(num_list)/len(num_list)

print(f"Média: {aven_list}")
print(f"Moda: {moda_list}")
print(f"Mediana: {median_list}")
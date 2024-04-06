from statistics import mode, median

num_list = [67, 68, 74, 67, 68, 84, 75, 80, 75, 84, 75, 73, 67, 74, 78, 77, 75, 80, 74, 77, 85, 85, 68, 74, 72, 73, 71, 73, 71, 85, 68, 84, 80, 77, 78, 75, 71, 72, 73, 84]

num_list.sort()

median_list = median(num_list)

moda_list = mode(num_list)

aven_list = sum(num_list)/len(num_list)

print(f"Média: {aven_list}")
print(f"Moda: {moda_list}")
print(f"Mediana: {median_list}")
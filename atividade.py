from math import sqrt

def InRol(l):
    l.sort()
    
    return l

def average(l):
    
    list_sum = sum(l)
    list_num_itens = len(l)
    
    result = list_sum/list_num_itens
    
    return result

def countItemsInList(l):
    
    count_number = {}
    
    for number in l:
        if number in count_number:
            count_number[number] += 1
        else:
            count_number[number] = 1

    return count_number

def varianceList(l):

    list_result = []
    
    qtd_l = countItemsInList(InRol(l))

    aven = average(InRol(l))

    for num in qtd_l.keys():
        
        list_result.append(qtd_l.get(num)*((num-aven)**2))
        
    sum_list = sum(list_result)

    result = sum_list/len(l)

    return result

def varianceListTwo(l_c, fi):
    
    l = []
    
    for i in range(len(l_c)):
        
        point_aven = (l_c[i][0] + l_c[i][1]) / 2
        
        l = fi[i] * point_aven
        
    sum_list = sum(l)
    sum_fi = sum(fi)
    
    result = sum_list/sum_fi
    
    return result
        
        

def standardDeviation(l):
    
    v = varianceList(l)
    
    return sqrt(v)

def coefficientOfVariation(l):
    
    std = standardDeviation(l)
    mean = average(l)
    
    print(mean)
    
    if mean == 0:
        return "Divisão por zero!"
    else:
        return (std / mean) * 100
    
l = [32, 19, 20, 20, 19, 21, 21, 25, 26, 19, 21, 27, 22, 26, 19]

classe = [ [0, 4], [4, 8], [8, 12], [12, 16], [16, 20] ]
fi = 2, 6, 8, 3, 1
    
variancia = varianceList(l)
desvio_padrao = standardDeviation(l)
coeficiente_variacao = coefficientOfVariation(l)

print (f"Variancia: {variancia}")
print(f"Desvio padrão: {desvio_padrao}")
print(f"Coeficiente de variação: {coeficiente_variacao:.2f}%")

result = varianceListTwo(classe, fi)
print(result)
from statistics import median

def point_aven(lc):

    result = []

    for i in range (0, len(lc)):
        calc = (lc[i][0] + lc[i][1])/2

        result.append(calc)

        calc = ""

    return result

def mult_point_aven(pm, fi):

    result = []

    for i in range(0, len(pm)):
        calc = (pm[i]*fi[i])

        result.append(calc)

        calc = ""

    return result

def average(lm, fi):

    sum_lm = sum(lm)
    sum_fi = sum(fi)

    if sum_fi != 0:
        result = sum_lm/sum_fi
    else:
        result = "Error"

    return result

def median_list(pm, fi):

    result = []

    for i in range(0, len(pm)):
        for y in range (0, fi[i]):
            result.append(pm[i])

    result = median(result)

    return result

classes = [(151, 158), (159, 166), (167, 174), (175, 182), (183, 190)]
freq = [ 5, 12, 18, 27, 8]

result_point_aven = point_aven(classes)

result_mult_point_aven = mult_point_aven(result_point_aven, freq)

result_aven = average(result_mult_point_aven, freq)

result_median = median_list(result_point_aven, freq)

print(result_median)
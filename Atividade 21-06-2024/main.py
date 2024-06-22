import pandas as pd

def multiply_column(xi_list, yi_list):

    xi_yi_list = [x * y for x, y in zip(xi_list, yi_list)]
    
    return xi_yi_list


def calc_exp(xi_list):

    xi_two_list = []
    calc = 0

    for x in xi_list:

        calc = x*x
        xi_two_list.append(calc)

    return xi_two_list

def sum_list(ls):
    sum = 0

    for l in ls:
        sum += l

    return sum

data = "ex-1.csv"

df = pd.read_csv(data)

df_num_row = len(df)

xi_list = df["Xi"].tolist()
yi_list = df["Yi"].tolist()

df["Xi * Yi"] = multiply_column(xi_list, yi_list)

df["X²"] = calc_exp(xi_list)

print(df)

xi_yi_list = df["Xi * Yi"].tolist()
xi_two = df["X²"].tolist()

sum_xi_yi = sum_list(xi_yi_list)
sum_xi = sum_list(xi_list)
sum_yi = sum_list(yi_list)
sum_xi_two = sum_list(xi_two)

sum_xi_list = sum_list(xi_list)

line_one = (df_num_row*sum_xi_yi) - (sum_xi*sum_yi)
line_two = (df_num_row*sum_xi_two) - (sum_xi_list*sum_xi_list)

print(line_one/line_two)
import pandas

# pip install pandas

data = pandas.read_csv('records_dict.csv')
print(data)
#     name branch  year  cgpa
# 0  radek    coe     3     0

data = pandas.read_csv('records_discount.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  radek    coe     3     0
#    sku  exp_date   price
# 0    1     today   200.0
# 1    2     today   100.0
# 2    3  tomorrow    50.0
# 3    4     today   200.0
# 4    5     today  1200.0
# 5    6     today    25.5
print(data.columns)  # Index(['sku', 'exp_date', 'price'], dtype='str')

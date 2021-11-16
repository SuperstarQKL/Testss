long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

# {
#     'name': 'Variopartner SICAV',
#     'lei': '529900LPCSV88817QH61',
#     'sub_fund': [{
#         'title': 'TARENO GLOBAL WATER SOLUTIONS FUND',
#         'isin': ['LU2001709034', 'LU2057889995', 'LU2001709547']
#     }, {
#         'title': 'TARENO FIXED INCOME FUND',
#         'isin': ['LU1299722972']
#     }, {
#         'title': 'TARENO GLOBAL EQUITY FUND',
#         'isin': ['LU1299721909', 'LU1299722113', 'LU1299722030']
#     }, {
#         'title': 'MIV GLOBAL MEDTECH FUND',
#         'isin': ['LU0329630999', 'LU0329630130']
#     }]
# }
list1 = long_text.split('\n')
length = len(list1)
dict1 = {}
sub_fund = []
i = 0
x = 0
j = 0
for i in range(j, length):
    dict1["name"] = list1[1]
    if list1[i][:2].isdigit():
        dict1["len"] = list1[i]
        x += 1
        continue
    if x > 0:
        sf = []
        dict2 = {}
        n = 1
        for j in range(i, length):
            if n == 2 and list1[j][2:6].isdigit() is False:
                dict2['isin'] = sf
                sub_fund.append(dict2)
                sf = []
                dict2 = {}
                n = 1
            if list1[j][:1].isdigit():
                dict2['title'] = list1[j]
                n += 1
            elif list1[j][2:6].isdigit() is True:
                sf.append(list1[j])

    if i == 3:
        break
    i += 1
dict1['sub_fund'] = sub_fund
print(dict1)
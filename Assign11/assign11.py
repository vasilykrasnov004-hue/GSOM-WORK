import numpy as np

income = np.array([
    [100, 110, 120, 130, 140, 150, 160, 170, 180, 190], # dep 1
    [200, 210, 220, 230, 240, 250, 260, 270, 280, 290], # dep 2
    [150000, 160000, 170000, 180000, 190000, 200000, 210000, 220000, 230000, 240000]  # dep 3
])

print('2.1 Gross Income')
print(income)

net_income = income * 0.7

print("2.2 Net Income")
print(net_income)


recalculated_net = net_income.copy()

recalculated_net[:, 4:7] = income[:, 4:7] * 0.6

print("2.3 Recalculated Net Income")
print(recalculated_net)

q2_data = recalculated_net[:, 3:6]

print("2.4 Second Quarter Data")
print(q2_data)
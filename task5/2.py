import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('C:/Users/danya/Downloads/populations.txt')
year, hares, lynxes, carrots = data.T
print(data)

plt.axes([0.2, 0.1, 0.5, 0.8])

plt.plot(year, hares, year, lynxes, year, carrots)

plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.15, 0.5))

plt.show()

print('Среднее:', np.round(np.mean(data[:, 1:]), 2))
print('Стандартная девиация:', np.round(np.std(data[:, 1:]), 2))

print('Максимум кроликов:', int(*data[np.argmax(data[:, 1:2], 0), 0]))
print('Максимум рысей:', int(*data[np.argmax(data[:, 2:3], 0), 0]))
print('Максимум морковок:', int(*data[np.argmax(data[:, 3:4], 0), 0]))

letters = np.array(['Hare', 'Lynx', 'Carrot'])
print(np.stack((year, letters[np.argmax(data[:, 1:], 1)]), 1))

print('Популяция больше 50000:', year[np.any(data[:, 1:] > 50000, 1)])

print('Топ 2 года с самой низкой популяцией:')
print(year[np.argsort(data[:, 1:], 0)[:2]])

hares_grade = np.gradient(hares, 1.0)
print('Разница (кролики и рыси):', np.corrcoef(hares_grade, lynxes)[0, 1])
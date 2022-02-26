import pandas
from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

data = pandas.read_csv('iphone_price.csv')
# print(data.head())

# plt.scatter(data['version'],data['price'])
# plt.show()

# from sklearn
model = LinearRegression()
model.fit(data[['version']],data[['price']])
print(model.predict([[13]]))
print('hey')
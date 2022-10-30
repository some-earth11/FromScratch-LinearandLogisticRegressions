import pandas as pd
import matplotlib.pyplot as plt

raw_data = pd.read_csv("Fuel.csv")
data = raw_data[['FUELCONSUMPTION_COMB_MPG','CO2EMISSIONS'].copy()]

def loss_function(m ,b, points):
    total_error = 0
    for i in range(points):
        x = data.iloc[i].FUELCONSUMPTION_COMB_MPG
        y = data.iloc[i].CO2EMISSIONS
        total_error += (y - (m * x + b))**2
    total_error / float(len(points))
    print(total_error)


# plt.scatter(data.FUELCONSUMPTION_COMB_MPG, data.CO2EMISSIONS)
# plt.show()


# Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd

data = pd.read_csv("sample_data/california_housing_train.csv")

max_households = data[data["population"] == data["population"].min()]['households'].max()
print(f"Максимальная households в зоне минимального значения population = {max_households}")
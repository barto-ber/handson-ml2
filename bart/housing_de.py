import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv
pd.options.display.width = 0
pd.options.display.max_rows = None
pd.options.display.precision = 1


def read_housing():
    dtypes = {
        "regio1": "category",
        "firingTypes": "category",
        "heatingType": "category",
        "petsAllowed": "category",
        "typeOfFlat": "category"
    }
    data = read_csv("immo_data.csv", dtype=dtypes)
    return data

def drop_columns():
    data = read_housing()
    less_columns = ["telekomTvOffer", "serviceCharge", "telekomHybridUploadSpeed", "newlyConst", "picturecount", "pricetrend",
                    "geo_bln", "yearConstructedRange", "interiorQual", "street", "baseRentRange", "thermalChar", "regio2",
                    "description", "facilities", "energyEfficiencyClass", "electricityBasePrice", "electricityKwhPrice",
                    "telekomUploadSpeed", "noParkSpaces", "garden",
                    "balcony", "hasKitchen", "cellar", "lift"]
    data.drop(less_columns, inplace=True, axis=1)
    data = data[data['totalRent'] < 3000]
    data = data[data['baseRent'] < 3000]
    data = data[data['noRooms'] < 8]
    data = data[data['floor'] <= 20]
    data = data[data['numberOfFloors'] <= 20]
    data = data[data['heatingCosts'] <= 500]
    data = data[data['livingSpace'] <= 500]
    data = data[data['yearConstructed'] <= 2020]
    data = data[data['yearConstructed'] >= 1850]
    data = data[data['lastRefurbish'] >= 2020]
    return data


def check_data():
    data = drop_columns()
    print(data.head())
    print(data.info())
    print(data.describe())
    # print("Lets see PLZ:\n", data['hasKitchen'].value_counts())
    print("Check Values:\n", data[data['floor'] >= 20])

check_data()

def data_histogram():
    data = drop_columns()
    data.hist(bins=50)
    plt.show()

data_histogram()
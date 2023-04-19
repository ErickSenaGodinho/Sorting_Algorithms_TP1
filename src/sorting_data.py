import os
import pandas as pd

file_name = "./src/resources/sorting_data.csv"


def load_data():
    if not os.path.isfile(file_name):
        data = {
            "sorting algorithm name": [],
            "type": [],
            "size": [],
            "time": [],
            "comp": [],
            "swaps": [],
        }
        return data

    df = pd.read_csv(file_name)
    return df.to_dict("list")


def save_data(sort_algorithm_name, type_, size, time, comp, swaps):
    data = load_data()
    data.get("sorting algorithm name").append(sort_algorithm_name)
    data.get("type").append(type_)
    data.get("size").append(size)
    data.get("time").append(time)
    data.get("comp").append(comp)
    data.get("swaps").append(swaps)

    df = pd.DataFrame(data)

    df.to_csv(file_name, index=False)

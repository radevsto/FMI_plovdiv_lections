import pandas


def dict_to_csv(dict_info):
    pandas.DataFrame.from_dict(dict_info, orient="index").to_csv("paragraph_info_csv.csv", sep="|")

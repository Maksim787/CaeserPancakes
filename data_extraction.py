"""
Положить все rar файлы в rar_data_folder: "1_april.rar", "1_febr.rar", "1_march.rar", "1_may.rar", "1_ost.rar"
1. Данные по всем покупкам будут в purchases_file
2. Данные по всем поставками будут в supplies_file
"""

import os
import pandas as pd
import rarfile

from tqdm import tqdm

rar_data_folder = "data/rar"
purchases_file = "data/purchases.csv"
supplies_file = "data/supplies.csv"

purchases_rar = ["1_april.rar",
                 "1_febr.rar",
                 "1_march.rar",
                 "1_may.rar"]
supplies_rar = "1_ost.rar"


def read_rar(file):
    with rarfile.RarFile(f"{rar_data_folder}/{file}") as rar_file:
        assert len(rar_file.namelist()) == 1
        with rar_file.open(rar_file.namelist()[0]) as f:
            return pd.read_csv(f, sep=";")


def extract_data():
    if not os.path.exists(purchases_file):
        for file in tqdm(purchases_rar):
            read_rar(file).to_csv(purchases_file, mode="a", header=not os.path.exists(purchases_file), index=False)
    if not os.path.exists(supplies_file):
        read_rar(supplies_rar).to_csv(supplies_file, index=False)


if __name__ == "__main__":
    extract_data()

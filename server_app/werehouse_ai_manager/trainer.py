import os
import csv

path_empty = "train_data/empty"
path_full = "train_data/full"
path_half_full = "train_data/half-full"
path_not_organized = "train_data/not-organized"

try:
    fill_list = os.listdir(path_full)

    for f in fill_list:
        print(f)

except OSError:
    print(f'Błąd podczas odczytywania zawartości katalogu: {path_full}')

try:
    with open ("names.csv",'w',newline='') as csv_wr:
        writer = csv.writer(csv_wr)
        writer.writerows(fill_list)
    print("Zapisano do pliku")

except IOError:
    print(f'Błąd podczas zapisywania danych do pliku')
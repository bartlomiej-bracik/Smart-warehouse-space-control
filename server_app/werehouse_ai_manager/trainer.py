import os
import csv
import image_analyzer as ia
import learning_utils as lu
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import datasets
import cv2
import numpy as np

path_empty = "train_data/empty"
path_full = "train_data/full"
path_half_full = "train_data/half-full"
path_not_organized = "train_data/not-organized"

features_data = []
flatten_image_data=[]

def createDatasetfromImages():

    fill_names_empty = get_fill_name(path_empty)
    fill_names_full = get_fill_name(path_full)
    fill_names_half_full = get_fill_name(path_half_full)
    fill_names_not_organized = get_fill_name(path_not_organized)

    features_data = []
    flatten_image_data = []
    getFeaturesbyAnalyzer(fill_names_empty,path_empty)
    getFeaturesbyAnalyzer(fill_names_full,path_full)
    getFeaturesbyAnalyzer(fill_names_half_full,path_half_full)
    #getFeaturesbyAnalyzer(fill_names_not_organized,path_not_organized)

    getFlatenImageData(fill_names_empty, path_empty)
    getFlatenImageData(fill_names_full, path_full)
    getFlatenImageData(fill_names_half_full, path_half_full)


    writeDataSet()
    #writeDataSetFlatten()
    print(flatten_image_data)

def getFeaturesbyAnalyzer(fill_names,path):
    for f in fill_names:
        analyzer = ia.analyzer(path+"/" + str(f))
        features = lu.Feature(analyzer, 0, 0)
        d = features.getFeature()
        d = d + [path.replace("train_data/","")]
       # print(d)
        features_data.append(d)

def getFlatenImageData(fill_names,path):
    for f in fill_names:
        p = path+"/" + str(f)
        d = flattenImg(p)
        d1 = [d , [path.replace("train_data/","")]]
        print(d1)
        flatten_image_data.append(d1)

def get_fill_name(path):
    try:
        fill_list = os.listdir(path)
    except OSError:
        print(f'Błąd podczas odczytywania zawartości katalogu: {path_full}')
    return fill_list

def writeDataSet():
    try:
        with open("features_dataset.csv", 'w', newline='') as csv_wr:
            writer = csv.writer(csv_wr)
            for row in features_data:
                writer.writerow(row)
        print("Zapisano do pliku")

    except IOError:
        print(f'Błąd podczas zapisywania danych do pliku')

def writeDataSetFlatten():
    try:
        with open("flatten_dataset.csv", 'w', newline='') as csv_wr1:
            writer = csv.writer(csv_wr1)
            for row in flatten_image_data:
                writer.writerow(row)
        print("Zapisano do pliku")

    except IOError:
        print(f'Błąd podczas zapisywania danych do pliku')




def flattenImg(path):
    image = cv2.imread(path)
    return image.flatten()

import os
import numpy as np
from skimage import io, color, feature, transform
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def lerning():
    # Ścieżka do folderu zawierającego obrazy, gdzie nazwa folderu to nazwa klasy
    folder_path = "train_data/"

    # Inicjalizacja listy do przechowywania obrazów i etykiet
    images = []
    labels = []

    # Przejście przez foldery (każdy folder to klasa)
    for class_folder in os.listdir(folder_path):
        class_path = os.path.join(folder_path, class_folder)
        if os.path.isdir(class_path):
            # Przejście przez pliki wewnątrz foldera klasy
            for filename in os.listdir(class_path):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    # Wczytaj obraz
                    image = io.imread(os.path.join(class_path, filename))
                    # Przetwarzanie obrazu (opcjonalne, w zależności od potrzeb)
                    image = transform.resize(image, (100, 100))
                    image = color.rgb2gray(image)
                    image = feature.hog(image)
                    # Dodaj obraz i etykietę do list
                    images.append(image)
                    labels.append(class_folder)

    # Konwertowanie list na tablice numpy
    X = np.array(images)
    y = np.array(labels)

    # Zakodowanie etykiet za pomocą LabelEncoder
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Podziel dane na zbiór treningowy i testowy
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    # Stwórz model SVM
    clf = svm.SVC(kernel='linear')

    # Trenuj model na danych treningowych
    clf.fit(X_train, y_train)

    # Dokładność modelu na danych testowych
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Dokładność: {accuracy}')
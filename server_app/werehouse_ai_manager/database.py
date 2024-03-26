
def writeRecortToDatabase(textToWrite):
    with open ('data_historic.txt', 'a') as plik:
        plik.writelines(f"TextToWrite  \n")

def readRecordsFromDatabase():
    print("Wyświetl dane")




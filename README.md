# Smart-warehouse-space-control

Projekt jest prototypem systemu odpowiedzialnego za załadunek oraz rozładunek magazynu buforowego. Określanie stanu magazynu odbywa sięprzy użyciu algorytmów sztucznej inteligencji. Projekt został zaimplementowany w jezyku Python wraz z biblotekami Flask, OpenCV oraz scit-learn.
Aplikacja mobilna na urządzenie z systemem Android jest odpowiedzialna za przesyłanie pomiarów w postaci obrazu oraz za 

## Spis treści

- [Instalacja](#instalacja)
- [Użycie](#użycie)


## Instalacja


1. Pobierz repozytorium w ZIP

2. Przejdz  w cmd do katalogu ...\Smart-warehouse-space-control\server_app\werehouse_ai_manager

3. Stwórz wirtualne środowisko:

    ```bash
    python -m venv venv
    ```

4. Aktywuj wirtualne środowisko:

    - Dla systemu Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - Dla systemu Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

5. Zainstaluj zależności:

    ```bash
    pip install -r requirements.txt
    ```

## Użycie

Po instalacji należy uruchomić projekt za pomocą:

```bash
    python app.py
```


Nastepnie należy otworzyć strone z lokalnego adresu.Strona umożliwia przesyłanie zdjecia ( będącego pomiarem w prototypowym magazynie) do analizy obrazu. Serwer zwraca raport stworzony przez AI.

![Widok strony](https://github.com/bartlomiej-bracik/Smart-warehouse-space-control/blob/main/description/web.JPG)

Folder ...\Smart-warehouse-space-control\mobile  uruchamia się za pomocą programu Android Studio. Aplikacja pozwala na wykonywanie pomiarów oraz otrzymywanie raportu AI.


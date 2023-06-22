import os
import glob
import sys

def zmien_nazwy(sciezka, nowa_nazwa):
    pliki = glob.glob(os.path.join(sciezka, '*'))

    pliki.sort()

    for indeks, stary_plik in enumerate(pliki):
        nazwa, rozszerzenie = os.path.splitext(stary_plik)
        nowa_nazwa_pliku = nowa_nazwa + str(indeks) + rozszerzenie
        nazwa_sciezki_pliku = os.path.join(sciezka, nowa_nazwa_pliku)
        os.rename(stary_plik, nazwa_sciezki_pliku)
        print(f'Zmieniono nazwę pliku "{stary_plik}" na "{nowa_nazwa_pliku}"')

sciezka = "C:\Users\Mateusz\PycharmProjects\bomberman-final-project-po2\resources\assets\character1\Front\PNG Sequences\Walk\\"
nazwa = "character1_walk_down_"

zmien_nazwy(sciezka, nazwa)
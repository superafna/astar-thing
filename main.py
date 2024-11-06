import numpy as np
from packages.a_star import a_star_search


def test():
    """
    fixed test.
    """
    grid = np.stack([
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ])

    # Define the source and destination
    src = (8, 0)
    dest = (0, 0)

    # Run the A* search algorithm
    a_star_search(grid, src, dest)


def main():
    for _ in range(100):
        test()


if __name__ == "__main__":
    main()

"""
V datoteki a_star.py je pythonovska implementacija algoritma A*, z uporabo knjižnjice numpy.
Vasa naloga je, da poskrbite da funkcija a_star_search() deluje brez napak, ali pa vsaj čim vec napak odpravite.
Funkcija a_star_search() sprejme tabelo kot dvo-dimenzionalni numpy array, in dve tocki kot tupla intov.
(lahko tudi od zacetka napisete novo kodo za implementacijo A*, ampak morate uporabiti tudi numpy, 
sicer je prelahko vse skopirati s spleta :p)

Komentarji opisujejo delovanje brez napak, torej ce gre kaj v kljub njim, je verjetno napaka.
Funkcije v a_star.py imajo lahko eno po napako, ali pa sploh nobene.
Ena napaka lahko obsega eno ali več zaporednih vrstic.
Dovoljena je prosta uporaba kakršnihkoli orodij, spletni brskalnik ipd. (tudi chatGPT, ampak tega sicer ne bi predlagal)
dataclass Cell je pravilen, konstanta DIRECTIONS tudi.

Vso srečo!
"""

# Varianz berechnen bra

werte = [10.320, 18.430, 15.240, 12.490, 21.310, 17.310, 18.100, 25.560, 7.440, 16.370]

def varianz_berechnen(liste: list):
    if len(liste) == 0:
        return "Liste ist leer.."
    mittelwert = sum(liste) / len(liste)
    ausgabe = (1/len(liste)) * sum([(i - mittelwert)**2 for i in liste])

    return ausgabe

varianz_berechnen(werte)

def stani(varianz):
    return varianz ** 0.5

stani(varianz_berechnen(werte))

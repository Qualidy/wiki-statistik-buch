# Ergänzungen zum Buch "Statistik Schritt für Schritt"

!!! tip "Schneller Navigieren"

    ++p++ oder ++comma++ : Zur vorherigen Seite gehen (**P**revious)
    
    ++n++ oder ++period++ : Zur nächsten Seite gehen (**N**ext)


Unittest:

* leere Argumente (z.B. leere Liste, 0, usw.)
* fast leere/minimale Argumente (z.B. Listen mit nur einem Element, 1)
* Normalfälle (z.B. mode([1,3,2,1]), alle Einträge negativ, positive und negative Einträge)
* Extremfälle (z.B. alles gleich)
* Unschönste Fälle (z.B. mit maximaler Laufzeit sort([5,4,3,2,1]))
* Fehlerfälle, wenn die Fehler auch im Code geworfen werden können und sollten.
* Performance-Tests (sollten aber nicht zu lange dauern. Unittest sollten weiterhin in wenigen ms fertig sein. Z.B.: [1] * 10**6 + [2] * 10**6)
* Alle Zweige im Code sollten getestet werden. (nicht zwingend erforderlich ist es, alle Variationen durchzugehen, aber man muss jede Codezeile in jedem Test mindestens einmal durchgeführt haben)

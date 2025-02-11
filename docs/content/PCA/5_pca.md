# PCA

Wir haben nun alle theoretsichen Bausteine für PCA zusammengestellt.

!!! formel "Zusammenfassung der Herleitung von PCA"

    Gegeben sei ein Datensatz $X \in \mathbb{R}^{N\times D}$ mit $D$ Merkmalen und $N$ Ausprägungen.

    $X$ soll auf $D$ neue Merkmale $pc_1, \cdots , pc_D$ übertragen werden, wobei diese neuen Merkmale
    nach ihrer Varianz geordnet sind sind, d.h. $var(pc_1) \geq var(pc_2) \geq \cdots \geq var(pc_D)$.

    Dazu werden die Daten zuerste in die Mitte des Koordinatensystems mit der Rechnung $Y := X - \bar{X}$ verschoben.

    Dann wird die Kovarianzmatrix $S$ von $Y$ berechnet.

    Berechne dann die Eigenwerte von $S$ und sortiere diese der Größe nach, sodass $var(\lambda_1) \geq \cdots \geq var(\lambda_d)$ ist ($d \leq D$).

    Bereche zu jedem Eigenwert die normierten Eigenvektoren $(v_1, \cdots, v_d)$.

    Da $S$ symetrisch ist, stehen die Eigenvektoren senkrecht aufeinander, sodass man $Y$ einfach auf diese projizieren kann
    und so die neuen Merkmale erhält.


{{ task(file="tasks/pca/pca/full.yaml") }}
{{ task(file="tasks/pca/pca/implement_pca.yaml") }}
{{ task(file="tasks/pca/pca/sklearn_implementation.yaml") }}

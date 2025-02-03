# Lagrange

## Zwischenstand der PCA Herleitung

Wir haben uns bereits damit auseinandergesetzt, wie man einen Datensazt \( X \in \mathbb{R}^{N \times D} \) 
mit \( N \) Beobachtungen und \( D \) Merkmalen auf einen Vektor $v$ und auf eine Hyperebene projizieren kann.

Wir haben auch gesehen, wie man die Varianz des neuen Merkmals $k := pr_v(X)$ bestimmen kann, indem man die
Kovarianzmatrix $S$ von $X$ verwendet: $var(k) = \frac{1}{|v|^4} v^t S v$.

Diese Formel hat aber noch ein gewisse Problematik, die wir durch die nächsten Übungsaufgaben erkennen wollen.

# TODO: Rechenaufgaben: Datensatz auf Vektor projizieren, Cov.matr. des Datensatzes ausrechnen. neue varianz bestimmen. Dabei insbes. skalierungen des gleichen vektors benutzen.

Wir stellen also fest, dass der Faktor $\frac{1}{|v|^4}$ in $var(k)$ dafür sorgt, dass wir $var(k)$ minimieren
können, indem wir ein $v$ wählen mit möglichst kleinem $v$. Das kann aber kein sinnvolles Vorgehen sein.

Daher müssen wir eine **weitere Bedingung** hinzufügen, nämlich dass $v$ ein Einheitsvektor ist (d.h. es gilt
$|v| = 1$).

**Wir suchen also $v\in \mathbb{R}^D$, sodass $v^t S v$ minimal ist, während gleichzeitig die Nebenbedingung
$|v| = 1$ gilt.**

Um so einen Extrempunkt einer Funktion zu finden, während gleichzeitig eine Nebenbedingung erfüllt werden soll,
eignet sich die sog. *Lagrange-Methode*.

## Lagrange-Methode

![Erklärung für die Lagrange-Methode von studyflix](https://studyflix.de/wirtschaft/lagrange-ansatz-83)

{{ task("tasks/pca/lagrange/R1.yaml") }}
{{ task("tasks/pca/lagrange/R2.yaml") }}
{{ task("tasks/pca/lagrange/R3.yaml") }}
{{ task("tasks/pca/lagrange/R4.yaml") }}

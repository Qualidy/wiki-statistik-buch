# Lagrange

## Zwischenstand der PCA Herleitung

Wir haben uns bereits damit auseinandergesetzt, wie man einen Datensazt \( X \in \mathbb{R}^{N \times D} \) 
mit \( N \) Beobachtungen und \( D \) Merkmalen auf einen Vektor $v$ und auf eine Hyperebene projizieren kann.

Wir haben auch gesehen, wie man die Varianz des neuen Merkmals $k := pr_v(X)$ bestimmen kann, indem man die
Kovarianzmatrix $S$ von $X$ verwendet: $var(k) = \frac{1}{|v|^4} v^t S v$.

Diese Formel hat aber noch ein gewisse Problematik, die wir durch die nächsten Übungsaufgaben erkennen wollen.

{{ task("tasks/pca/lagrange/different_variances.yaml") }}

!!! beispiel

    <iframe src="https://www.geogebra.org/calculator/jh6bq8v7?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

Wir stellen also fest, dass der Faktor $\frac{1}{|v|^4}$ in $var(k)$ dafür sorgt, dass wir $var(k)$ minimieren
können, indem wir ein $v$ wählen mit möglichst großem $|v|$. Das kann aber kein sinnvolles Vorgehen sein.

Daher müssen wir eine **weitere Bedingung** hinzufügen, nämlich dass $v$ ein Einheitsvektor ist (d.h. es gilt
$|v| = 1$).

**Wir suchen also $v\in \mathbb{R}^D$, sodass $v^t S v$ minimal ist, während gleichzeitig die Nebenbedingung
$|v| = 1$ gilt.**

Um so einen Extrempunkt einer Funktion zu finden, während gleichzeitig eine Nebenbedingung erfüllt werden soll,
eignet sich die sog. *Lagrange-Methode*.

## Lagrange-Methode

[Erklärung für die Lagrange-Methode von studyflix](https://studyflix.de/wirtschaft/lagrange-ansatz-83)

!!! formel "Lagrange-Methode"

    Gegegeben sei eine Funktion $f$, deren Extremwerte $x\in \mathbb{R}^D$ gesucht werden.
    Diese Extremwerte sollen aber auch gleichzeitig eine Bedingung $g(x)=0$ erfüllen. Diese lässt sich finden,
    indem die Extremstellen von 

    $$
    L(x,\lambda) = f(x) + \lambda g(x)
    $$

    gefunden werden. Man beachte, dass $x$ mehrdimensional sein kann. Sollte es mehrere Bedingungen geben,
    können diese, mit weitern Faktoren der Funktion $L$ hinzugefügt werden.

    Das finden des Extremstellen von $L$ erfolgt durch das gleichsetzten der partiellen Ableitungen von 
    $L$ mit $0$.

!!! beispiel "Beispiel für Lagrange"

    Gesucht sind die Extrema der Funktion $f(x,y) = x+2y$ unter den Nebenbedingung $1 = x^2+y^2$.

    <iframe src="https://www.geogebra.org/calculator/tdp25khh?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

    **Aufstellen der Lagrange-Funktion**

    \[
    L(x, y, \lambda) = x + 2y + \lambda (1 - x^2 - y^2).
    \]
    
    **Berechnung der Ableitungen**
    
    Wir bestimmen die Ableitungen nach \( x \), \( y \) und \( \lambda \):
    
    \[
    \frac{\partial L}{\partial x} = 1 - 2\lambda x = 0
    \]
    
    \[
    \frac{\partial L}{\partial y} = 2 - 2\lambda y = 0
    \]
    
    \[
    \frac{\partial L}{\partial \lambda} = 1 - x^2 - y^2 = 0.
    \]
    
    **Lösen des Gleichungssystems**
    
    Aus der ersten Gleichung folgt:
    
    \[
    1 = 2\lambda x \Rightarrow \lambda = \frac{1}{2x}.
    \]
    
    Aus der zweiten Gleichung:
    
    \[
    2 = 2\lambda y \Rightarrow \lambda = \frac{1}{y}.
    \]
    
    Setzen wir beide Gleichungen gleich:
    
    \[
    \frac{1}{2x} = \frac{1}{y} \Rightarrow y = 2x.
    \]
    
    Setzen wir dies in die Nebenbedingung ein:
    
    \[
    1 = x^2 + (2x)^2
    \]
    
    \[
    1 = x^2 + 4x^2 = 5x^2
    \]
    
    \[
    x^2 = \frac{1}{5}, \quad x = \pm \frac{1}{\sqrt{5}}.
    \]
    
    Daraus folgt:
    
    \[
    y = 2x = \pm \frac{2}{\sqrt{5}}.
    \]
    
    **Werte der Zielfunktion**
    
    Die Funktionswerte an den kritischen Punkten:
    
    \[
    f\left(\frac{1}{\sqrt{5}}, \frac{2}{\sqrt{5}}\right) = \frac{1}{\sqrt{5}} + 2 \cdot \frac{2}{\sqrt{5}} = \frac{5}{\sqrt{5}} = \sqrt{5}.
    \]
    
    \[
    f\left(-\frac{1}{\sqrt{5}}, -\frac{2}{\sqrt{5}}\right) = -\frac{1}{\sqrt{5}} - 2 \cdot \frac{2}{\sqrt{5}} = -\frac{5}{\sqrt{5}} = -\sqrt{5}.
    \]
    
    **Ergebnis**
    Das Maximum von \( f(x,y) \) ist \( \sqrt{5} \) bei \( \left(\frac{1}{\sqrt{5}}, \frac{2}{\sqrt{5}}\right) \).
    Das Minimum von \( f(x,y) \) ist \( -\sqrt{5} \) bei \( \left(-\frac{1}{\sqrt{5}}, -\frac{2}{\sqrt{5}}\right) \).

!!! info

    Wir untersuchen hier nur, **ob** ein Extremwert vorliegt. Ob dieser dann ein Hoch- oder Tiefpunkt ist, 
    lässt sich nur unter Bestimmung der zweiten Ableitungen und dem Aufstellen und Untersuchen der Hesse-Matrix
    feststellen. Dies ist aber für uns im Rahmen von PCA nicht relevant und wird daher gekonnt ignoriert.

{{ task("tasks/pca/lagrange/R1.yaml") }}
{{ task("tasks/pca/lagrange/R2.yaml") }}
{{ task("tasks/pca/lagrange/R3.yaml") }}
{{ task("tasks/pca/lagrange/R4.yaml") }}

## Verwendung von Lagrange für die Herleitung von PCA

Wenn wir nun die Lagrange-Methode verwenden wollen, um PCA herzuleiten, müssen wir uns zunächst klar machen,
dass 

$$
v^t S v
$$

die Zielfunktion und 

$$
|v| = 1 = v^t v
$$

die Nebenbedingung ist.

Das heißt wir müssen die partielle Ableitung von

$$
L(v, \lambda) = v^t S v + \lambda (1 - v^t v)
$$

bilden.

### Ableitung von $x^tAx$

{{ task("tasks/pca/lagrange/matrix_mult_2d.yaml") }}

{{ task("tasks/pca/lagrange/matrix_mult_3d.yaml") }}

Ziel: Ableitung von $\frac{\partial x^t A x}{\partial x} = 2Ax$

Wir können nun also Lagrange ausführen. Wir leiten 

$$
L(v, \lambda) = v^t S v + \lambda (1 - v^t v)
$$

nach $v$ ab und setzen den Term gleich $0$: 

$$
\frac{\partial L(v,\lambda)}{\partial v} = 2Sv + 2\lambda v = 0
$$

Wir können den Term umstellen zu:

\begin{align}
                &2Sv - 2\lambda v = 0 \\
\Leftrightarrow &Sv - \lambda v = 0 \\
\Leftrightarrow &Sv = \lambda v \\
\Leftrightarrow &v^t S v = \lambda v^t v \overset{|v|=1}{=} \lambda
\end{align}

Wir sehen also in der letzten Zeile, dass unsere ursprüngliche Funktion $v^t S v$ gleich $\lambda$ ist.
Das heißt um $v^t S v$ zu maximieren, heißt $\lambda$ zu maximieren.

Aber $\lambda$ ist doch bloß irgendeine beliebige, reelle Zahl, oder? Kann sie nicht beliebig groß werden?
Nein, denn die vorletzte Gleichung
$Sv = \lambda v$ bedeutet, dass $\lambda$ zusätzlich noch ein **Eigenwert** sein muss. Und von diesen
gibt es nur eine endliche Anzahl, wie wir im folgenden Kapitel sehen werden. 

Das heißt, wir können unseren gesuchten Varianz-maximierenden Projektionsvektor $v$ finden, indem wir den
größten Eigenwert $\lambda$ von $S$ finden. What a crazy turn of events!

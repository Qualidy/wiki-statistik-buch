# Projektion

## Projektion auf einen Vektor

Wir müssen uns zunächst klar machen, was eine Projektion auf einen Vektor bedeutet.

<iframe src="https://www.geogebra.org/calculator/mhnxsjsr?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

!!! formel "Aufgespannter Vektorraum"

    Sei $v \in \mathbb{R}^D$ ein Vektor. Dann ist 

    $$
    \langle v \rangle := \{ kv | k \in \mathbb{R} \}
    $$

    der von $v$ aufgespannte Vektorraum. Man spricht $\langle v \rangle$ aus als "Der Aufspann von $v$" oder
    "Der von $v$ aufgespannte Vektorraum".

    Einen solchen aufgespannten Vektorraum kannst du dir als eine (eindimensionale) Linie in einem Raum vorstellen.

{{ task("tasks/pca/projektion/projektionsraum_bestimmen.yaml") }}

!!! formel "Senkrecht stehen"

    Seien $v$ und $w$ zwei Vektoren gleicher Größe. Dann ist $v$ senkrecht auf $w$ (geschrieben $v \perp w$) genau dann wenn
    $v^tw=0$ ist. Oft wird $v^tw$ als $v\cdot w$ notiert. 

{{ task("tasks/pca/projektion/senkrechte_vektoren_berechnen.yaml") }}

!!! formel "Projektionsfunktion"

    Sei $v \in \mathbb{R}^D$ ein Vektor, auf den projeziert werden soll.

    Dann sei $pr_v : \mathbb{R}^D \to \langle v \rangle : w \mapsto kv$, wobei ein $d\in \mathbb{R}^D$ existiert,
    mit $w = kv + d$ und $d \perp v$ (das heißt $d$ steht senkrecht auf $v$).

    <iframe src="https://www.geogebra.org/calculator/psst9sn4?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

Die Projektionsfunktion ist derzeit noch **sehr unbefriedigend**, da sie keine Rechenvorschrift angibt, wie
man auf $k$ kommt.

!!! formel "Rechenvorschrift der Projektionsfunktion"

    Sei $v \in \mathbb{R}^D$ ein Vektor. Dann ist

    $$pr_v(w) = \frac{w^tv}{|v|^2} v$$

    Das in der Definition noch nicht näher bestimmte $k$ ist also $\frac{w^tv}{|v|^2}$.

    Ist $|v|=1$ (ein sog. Einheitsvektor), so gilt sogar:

    $$pr_v(w) = v^twv$$

{{ task("tasks/pca/projektion/projektionen_berechnen.yaml") }}

Wiekann ich einen Vektor normieren?

Warum funktioniert diese Rechenregel? Betrachten wir dazu die folgende Herleitung:

!!! tip "Herleitung"
    
    Sei $v\in \mathbb{R}^D\setminus {0}$ ein Vektor, auf den $w\in \mathbb{R}^D$ projiziert werden soll.
    
    Zunächst normieren wir $v$ zu $u := \frac{v}{|v|}$. Das heißt $|u| = 1$.
    
    Wir suchen nun ein $k \in \mathbb{R}$ mit $ku + d = w$ und dabei ist $d \in \mathbb{R}^D$ so, dass $d \perp v, u$ ist.
    
    Da $d \perp u$ und damit auch $d \perp ku$ ist, gilt:
    
    $$
    0 = d^t(ku)
    $$
    
    Da $ku + d = w$ gilt $d = w - ku$:
    
    $$
    0 = (w-ku)^t(ku) = (w^t-ku^t)(ku) = w^tku - ku^tku = kw^tu - k^2u^tu
    $$
    
    Da $|u| = 1$ ist, gilt $u^tu=1$. Also:
    
    $$
    0 = kw^tu-k^2 = k(w^tu-k)
    $$
    
    Nun gibt es zwei Fälle, warum die Gleichung $0$ ergibt.
    
    **1. Fall:** Ist $k=0$, so bedeutet das nach $w = ku + d = 0u + d = d$, dass $w = d\perp u$ ist. $w$ steht also senkrecht
    auf $u$ bzw. $v$ und wird daher auf $0$ projeziert.
    
    **2. Fall:** Ist $k\neq 0$, so muss $w^tu-k = 0$ sein. Dann können wir die Gleichung umstellen zu:
    
    $$
    w^tu = k
    $$
    
    Damit haben wir auch unser gesuchtes $k$ gefunden.
    
    Wir können also sagen, dass $pr_v(w)=ku= w ^t u u$ gilt. Wir können dies auch noch umschreiben nach $v$:
    
    $$
    pr_v(w) = \frac{w^t v v}{|v|^2}
    $$

{{ task("tasks/pca/projektion/beweis_für_einheitsvektoren_projektion.yaml") }}

### Programmierung

{{ task("tasks/pca/projektion/programm_unitmaker.yaml") }}
{{ task("tasks/pca/projektion/programm_perpendicular.yaml") }}
{{ task("tasks/pca/projektion/programm_projector.yaml") }}

## Projektion auf einen Hyperraum

!!! formel "Hyperebene"
    
    Eine **Hyperebene** ist ein Raum, der eine Dimension kleiner ist, als mein Hauptraum.

!!! beispiel

    Wenn der Hauptraum der 3-dimensionale Raum ist, dann ist ein Hyperraum eine Ebene, die unendlich groß ist und 
    durch den Nullpunkt geht. Diese Ebene muss nicht auf einer der Achsen liegen, sondern kann auch "quer"
    im Raum sein. Das wichtige ist, dass man sich auf dieser Ebene nurnoch in zwei verschiedene Richtungen bewegen kann,
    während man im 3d-Raum noch drei orthogonale Richtungsvektoren hatte.

    Wenn der Hauptraum ein 2d-Koordinatensystem ist, dann ist jede Linie, die durch den Nullpunkt geht eine Hyperebene.
    
Jeder Hyperraum hat einen Normalenvektor, der senkrecht auf den Raum steht. Dieser ist nützlich, um alle 
Punkte aus dem großen Raum auf den Hyperraum herunter zu projizieren.

<iframe src="https://www.geogebra.org/calculator/aejercma?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

!!! formel "Normalenvektor"
    
    a
    

# TODO: Normalenvektor

{{ task("tasks/pca/projektion/projektion_auf_ebene.yaml") }}

# TODO: Übungsaufgabe Projektion auf Hyperebene (2,3,4 dim.)

{{ task("tasks/pca/projektion/projektion_auf_ebene_programmieren.yaml") }}



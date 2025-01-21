# Hypergeometrische Verteilung

## 1. Was ist das für eine Verteilung und wozu dient sie?

- Ähnelt der Binomialverteilung, jedoch mit Stichprobenziehungen **OHNE** Zurücklegen
- Wird verwendet, wenn die Wahrscheinlichkeit für einen Treffer oder Nicht-Treffer von der vorherigen Ziehung abhängt, da die Gesamtpopulation endlich ist und sich mit jeder Ziehung reduziert

## 2. Herleitung anhand eines Beispiels

!!! Beispiel
    ### Gegeben:
    Insgesamt 6 Kugeln in der Urne.

    - Es gibt 2 rote Kugeln.
    - Es gibt 4 blaue Kugeln.

    ### Aufgabe:

    Es werden 3 Kugeln ohne Zurücklegen gezogen.
    Dabei soll genau 1 rote Kugel gezogen werden. Wie groß ist die Wahrscheinlichkeit?

    ![alt text](<handmade_prob.jpeg>)
   

    ### Ansatz

    !!! Formel

        $$ 
        \begin{align}
            P(\text{x rote Kugel ziehen}) &= \frac{\text{Anzahl der zutreffenden Kombinationen}}{\text{Anzahl aller Kombinationen }}  \\& =\frac{\text{(Kombinationen für x rote Kugeln)}  \cdot \text{(Kombinationen für $n-x$ nicht-rote (blaue) Kugeln)}}{\text{ Kombinationen für n Kugeln}}
        \end{align}
        $$

    ### Berechnung:
    
    ### 1. Anzahl aller Kombinationen
    
    Erinnere daran, wie du die Anzahl der Kombinationen berechnest, aus k Objekte aus einer Menge von n Objekten auswählen kannst. (ohne Zurücklegen, ohne Beachtung der Reihenfolge)  
    $\rightarrow$ Formel des Binomialkoeffizienten: (siehe F.1.2.8, Seite 107 im Buch) 
    
    $$
    \binom{n}{k} = \frac{n!}{k!(n-k)!}
    $$
    
    Daraus ergeben sich insgesamt
    
    $$\binom{6}{3} =  \frac{6!}{3!(6-3)!} = 20 $$
    
    Möglichkeiten, 3 Kugeln zu ziehen.

    ---

    ### 2. Anzahl aller zutreffenden Kombinationen
    
    Nun zeigen wir alle möglichen Kombinationen der **3 gezogenen Kugeln** mit genau **1 roter Kugel**.

    ### Tabellarisch:
    
    | Kombinations-Nr. | Rote Kugeln (1 von 2) | Blaue Kugeln (2 von 4) |
    | ---------------- | --------------------- | ---------------------- |
    | 1                | {R1}                  | {B1, B2}               |
    | 2                | {R1}                  | {B1, B3}               |
    | 3                | {R1}                  | {B1, B4}               |
    | 4                | {R1}                  | {B2, B3}               |
    | 5                | {R1}                  | {B2, B4}               |
    | 6                | {R1}                  | {B3, B4}               |
    | 7                | {R2}                  | {B1, B2}               |
    | 8                | {R2}                  | {B1, B3}               |
    | 9                | {R2}                  | {B1, B4}               |
    | 10               | {R2}                  | {B2, B3}               |
    | 11               | {R2}                  | {B2, B4}               |
    | 12               | {R2}                  | {B3, B4}               |

    **Anzahl der zutreffenden Kombinationen**: 12

    ---

    ### Oder Anzahl der zutreffenden Kombinationen rechnerisch dargestellt:
    
    #### 1. **Es gibt 2 Kombinationen für die 1 rote Kugel** (R1 oder R2):
    
    $$\binom{2}{1} =  \frac{2!}{1!(2-1)!} = 2 $$

    #### 2. **Es gibt 6 Kombinationen für die 2 blauen Kugeln** (B1, B2, B3, B4): 
    
    $$ \binom{4}{2} = 6 $$
    
    Diese Anzahl entspricht der Berechnung: 
    
    $$ \text{(Kombinationen für x rote Kugeln)} \cdot \text{ (Kombinationen für $n-x$ nicht-rote (blaue) Kugeln)} = 2 \cdot 6 = 12 $$

    ---

    ### 3. Wahrscheinlich berechnen:
    
    $$ P(\text{Eine rote Kugel ziehen}) = \frac{\text{Anzahl der zutreffenden Kombinationen}}{\text{Anzahl aller Kombinationen }} = \frac{12}{20} $$
    
    Oder allgemeiner ausgedrückt:
    
    $$
    \begin{align*}
    P(X = x) &= \frac{\binom{M}{x} \cdot \binom{N - M}{n - x}}{\binom{N}{n}}
    \end{align*}
    $$
    
    mit

    - **X**: Die Zufallsvariable für gezogene rote Kugeln
    - **N = 6**: Insgesamt 6 Kugeln in der Urne.
    - **M= 2**: Es gibt 2 rote Kugeln.
    - **N - M = 4**: Es gibt 4 blaue Kugeln.
    - **n = 3**: Es werden 3 Kugeln ohne Zurücklegen gezogen.
    - **x = 1**: Es sollen genau 1 rote Kugel gezogen werden.


!!! formel "Formeln der hypergeometrischen Verteilung"

**Wahrscheinlichkeitsfunktion:**
    
    $$
    \begin{equation}
    f_h(x \mid N; M; n) = P(X = x) = \begin{cases}
    \frac{\binom{M}{x} \cdot \binom{N - M}{n - x}}{\binom{N}{n}} & \text{für } x = 0, 1, 2, \dots, n \\
    0 & \text{sonst}
    \end{cases}
    \end{equation}
    $$
    
    mit

    - **X**: Die Zufallsvariable der interessierenden Eigenschaft
    - **N**: Zahl aller Elemente in der Gesamtheit
    - **M**: Zahl der Elemente (von der Gesamtheit), die die interessierende Eigenschaft tragen
    - **N - M**: Zahl der Elemente (von der Gesamtheit), die **nicht** die interessierende Eigenschaft tragen
    - **n**: Zahl der Elemente, die gewählt werden
    - **x**: Zahl der Elemente mit der interessierenden Eigenschaft in dieser Auswahl

!!! beispiel "Zusammengefasst für das Beispiel"
    
    **Anzahl der Möglichkeiten, 1 rote Kugel zu ziehen:**
    
    Wähle genau 1 rote Kugel aus den **M = 2** roten Kugeln:
    
    $$ 
    \begin{equation}
    \binom{M}{x} = \binom{2}{1} = 2
    \end{equation}
    $$
    
    **Anzahl der Möglichkeiten, die restlichen 2 blauen Kugeln zu ziehen:**
    
    Wähle 2 blaue Kugeln aus den **N - M = 4** blauen Kugeln:
    
    $$ 
    \begin{equation}
    \binom{N - M}{n - x} = \binom{4}{2} = 6 
    \end{equation}
    $$
    
    **Gesamtanzahl der möglichen Ziehungen von 3 Kugeln aus 6:**
    
    Ziehe 3 Kugeln aus den **N = 6** Kugeln:
    
    $$
    \begin{equation}
    \binom{N}{n} = \binom{6}{3} = 20
    \end{equation}
    $$
    

    **Setze die Werte in die Formel ein:**
    
    $$
    \begin{equation}
    P(X = 0) = \frac{\binom{2}{0} \cdot \binom{4}{3}}{\binom{6}{3}} = \frac{1 \cdot 4}{20} = \frac{4}{20} = 0.2
    \end{equation}
    $$
    
    $$
    \begin{equation}
    P(X = 1) = \frac{\binom{2}{1} \cdot \binom{4}{2}}{\binom{6}{3}} = \frac{2 \cdot 6}{20} = \frac{12}{20} = 0.6
    \end{equation}
    $$
    
    $$
    \begin{equation}
    P(X = 2) = \frac{\binom{2}{2} \cdot \binom{4}{1}}{\binom{6}{3}} = \frac{1 \cdot 4}{20} = \frac{4}{20} = 0.2
    \end{equation}
    $$

{{ task(
question="Was ist die Wahrscheinlichkeit für $P(X = 3)$?",
) }}

$x$ kann dabei natürlich höchstens so groß sein wie der kleinere der beiden Werte  $\min(n, M)$. 

![alt text](<Bildschirmfoto 2025-01-20 um 13.48.46.png>)

!!! formel "Verteilungsfunktion"
    
    $$
    \begin{equation}
    F_h(x \mid N; M; n) = P(X \leq x) = 
    \begin{cases}
    0 & \text{für } x < 0, \\
    \sum_{k=0}^{x} \frac{\binom{M}{k} \cdot \binom{N - M}{n - k}}{\binom{N}{n}} & \text{für } x = 0, 1, 2, \dots, n\\
    1 & \text{für } x > n.
    \end{cases}
    \end{equation}
    $$

![alt text](<Bildschirmfoto 2025-01-20 um 13.48.29.png>)


!!! formel Erwartungswert
    Für die hypergeometrisch verteilte Zufallsvariable $X_h$ ist der Erwartungswert: 
    
    $$ E[X_h] = n \cdot \frac{M}{N} $$ 

!!! formel Varianz
    Für die hypergeometrisch verteilte Zufallsvariable $X_h$ ist der Erwartungswert: 
    
    $$ var(X_h)= E[(X_h - E[X_h])^2] = n \cdot \frac{M}{N} \cdot \left(1-\frac{M}{N}\right) \cdot \frac{N-n}{N-1}$$ 

## Fragen

{{ task(
title="Freitext Frage 1",
question="""Wie unterscheidet sich die hypergeometrische Verteilung von der Binomialverteilung?""",
solution="""Hypergeometrische Verteilung: Ziehen ohne Zurücklegen, die Wahrscheinlichkeiten ändern sich nach jeder Ziehung.

Binomialverteilung: Ziehen mit Zurücklegen, die Wahrscheinlichkeiten bleiben konstant.""",
) }}

{{ task(
title="Freitext Frage 2",
question="""Was bedeuten die Parameter $N$, $M$, $n$ und $x$ in der hypergeometrischen Verteilung $f_h(x \mid N; M; n)$?""",
solution="""$N$: Gesamtanzahl der Elemente in der Grundgesamtheit.

$M$: Anzahl der Erfolgsfälle in der Grundgesamtheit.

$n$: Anzahl der gezogenen Elemente (Stichprobengröße).

$x$: Anzahl der Erfolgsfälle in der Stichprobe.""",
) }}

{{ task(
title="Freitext Frage 3",
question="""In welchen realen Szenarien findet die hypergeometrische Verteilung Anwendung?""",
solution="""Ziehen von Karten ohne Zurücklegen.

Qualitätskontrolle, bei der Bauteile auf Fehler untersucht werden.

Auswahl von Teams oder Gruppen mit bestimmten Merkmalen (z. B. Männer/Frauen).

Gewinnchancen bei Losen oder Tombolas.""",
) }}

{{ task(
title="Freitext Frage 4",
question="""Ziehen von Karten: 

In einem Kartenspiel gibt es 52 Karten, darunter 13 Herz-Karten. Du spielst ein Spiel, bei dem du zufällig 5 Karten aus dem Stapel ziehst, ohne sie zurückzulegen.

a) Wie groß ist die Wahrscheinlichkeit, dass du genau 2 Herz-Karten in deiner Hand hast?

b) Wie groß ist die Wahrscheinlichkeit, dass du höchstens 2 Herz-Karten in deiner Hand hast?

c) (zusätzliche Herausforderung):Wie groß ist die Wahrscheinlichkeit, dass du mindestens 3 Herz-Karten in deiner Hand hast?""",
solution="""""",
) }}

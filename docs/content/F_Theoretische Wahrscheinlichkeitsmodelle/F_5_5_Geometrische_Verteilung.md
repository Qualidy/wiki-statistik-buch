# Geometrische Verteilung

Die geometrische Verteilung ist eine diskrete Wahrscheinlichkeitsverteilung, die modelliert, wie viele Bernoulli-Versuche benötigt werden, um einen Erfolg zu erzielen. Ein Bernoulli-Versuch ist ein Experiment mit zwei möglichen Ergebnissen: **Erfolg** (mit Wahrscheinlichkeit \(p\)) oder **Misserfolg** (mit Wahrscheinlichkeit \(1-p\)).

### Definition

Die geometrische Verteilung gibt die Wahrscheinlichkeit an, dass der erste Erfolg im \(k\)-ten Versuch eintritt. Die Wahrscheinlichkeit wird wie folgt berechnet:

!!! formel Wahrscheinlichkeitsfunktion

    \[
    f(k|p) = P(X = k) = (1-p)^{k-1} \cdot p
    \]

    \[
    f_g(x|\Theta) = \begin{cases}
                    (1-\Theta)^{x-1} \cdot \Theta & \text{für } x \in \mathbb{N} \\
                    0 & \text{für } sonst.
                \end{cases}
    \]

    Hierbei gilt:

    - \(X\): Anzahl der Versuche bis zum ersten Erfolg (eine Zufallsvariable).
    - \(k\): Anzahl der benötigten Versuche (\(k = 1, 2, 3, \dots\)).
    - \(p\): Wahrscheinlichkeit eines Erfolgs bei einem einzelnen Versuch (\(0 < p \leq 1\)).

## Eigenschaften

!!! formel "1. **Erwartungswert (Mittelwert):**"

    \[
    \mathbb{E}[X] = \frac{1}{p}
    \]
!!! formel "2. **Varianz:**"

    \[
    \text{Var}(X) = \frac{1-p}{p^2}
    \]

!!! formel "3. **Gedächtnislosigkeit:**"

    Die geometrische Verteilung ist gedächtnislos. Das bedeutet, dass die Wahrscheinlichkeit für einen Erfolg unabhängig davon ist, wie viele Misserfolge bereits eingetreten sind:

    \[
    P(X > n + k \mid X > n) = P(X > k)
    \]


!!! beispiel Beispiel

    Angenommen, die Wahrscheinlichkeit eines Erfolgs bei einem einzelnen Versuch beträgt \(p = 0,125\) (12.5 %). Die Wahrscheinlichkeit, dass der erste Erfolg im dritten Versuch eintritt, ist:
    
    \[
    P(X = 3) = (1-0,125)^{3-1} \cdot 0,125 = 0,875^2 \cdot 0,125 = 0.095703125
    \]
    
    <div style="display: flex;">
        <img src="https://www.crashkurs-statistik.de/wp-content/uploads/2016/01/verteilungen-geometrische-verteilung-dichte.png" alt="Geometrische Verteilung Dichte">
        <img src="https://www.crashkurs-statistik.de/wp-content/uploads/2016/01/verteilungen-geometrische-verteilung-verteilungsfunktion.png" alt="Geometrische Verteilung Verteilungsfunktion" style="margin-right: 10px;">
    </div>


!!! note Anwendungen
    Die geometrische Verteilung wird häufig in Szenarien verwendet, bei denen ein Ereignis durch wiederholte Versuche erzielt werden soll, wie z. B.:

    - Analyse von wiederholten Versuchen in Glücksspielen
    - Bestimmung sich wiederholdender gleich bleibender Ereignisse bis zum eintreffen des ersten Erfolgs

## Fragen

### Multiple Choice Aufgaben(Kopfrechnen)

{{ task(
title="MC-Frage 1",
question="""Was beschreibt die geometrische Verteilung?

A) Die Anzahl der Erfolge bis zum ersten Misserfolg.

B) Die Anzahl der Erfolge in einer festen Anzahl von Versuchen.

C) Die Anzahl der Misserfolge bis zum ersten Erfolg.

D) Die Anzahl der Misserfolge in einer festen Anzahl von Versuchen.
""",
solution="C",
) }}

{{ task(
title="MC-Frage 2",
question="""Welche der folgenden Formeln beschreibt die Wahrscheinlichkeit \( P(X = k) \) für eine geometrische Verteilung mit Erfolgswahrscheinlichkeit \( p \)?

A) \( P(X = k) = (1-p)^{k-1} p \)

B) \( P(X = k) = p^k (1-p) \)

C) \( P(X = k) = (1-p)^k p \)

D) \( P(X = k) = p (1-p)^{k-1} \)""",
solution="""A""",
) }}

{{ task(
title="MC-Frage 3",
question="""Gegeben ist eine geometrische Verteilung mit Erfolgswahrscheinlichkeit \( p = 0.5 \). Berechne die Wahrscheinlichkeit, dass der erste Erfolg im 2. Versuch eintritt.
A) 0.25

B) 0.5

C) 0.75

D) 0.125
""",
solution="A",
) }}

{{ task(
title="MC-Frage 4",
question="""Berechne den Erwartungswert \( E(X) \) einer geometrischen Verteilung mit Erfolgswahrscheinlichkeit \( p = 0.2 \).
A) 4

B) 5

C) 6

D) 7""",
solution="B",
) }}

{{ task(
title="MC-Frage 5",
question="""Eine geometrische Verteilung hat eine Erfolgswahrscheinlichkeit von \( p = 0.2 \). Was ist die Wahrscheinlichkeit, dass der erste Erfolg im 3. Versuch eintritt?

A) 0.140625

B) 0.1875

C) 0.128

D) 0.421875"""
,
solution="C",
) }}


### Freitext Fragen
{{ task(
title="Freitext-Frage 1",
question="""1. Ist die Geometrische Verteilung diskret oder kontinuierlich?""",
solution="Diskret.",
)}}

{{ task(
title="Freitext-Frage 2",
question="""2. Wie verändert sich die Erfolgswahrscheinlichkeit im Verlauf der Versuche?""",
solution="Sie bleibt konstant.",
)}}

{{ task(
title="Freitext-Frage 3",
question="""3. Wie lautet die Formel für den Erwartungswert der GV?""",
solution="$$E(X) = \frac{1}{p}$$",
)}}

{{ task(
title="Freitext-Frage 4",
question="""4. Welche Schwierigkeiten könnten in einer realen Anwendung auftreten, wenn die Annahmen der geometrischen Verteilung verletzt werden?""",
solution="Variierende Erfolgswahrscheinlichkeiten.",
)}}

{{ task(
title="Freitext-Frage 5",
question="""5. Wie lautet die Wahrscheinlichkeitsfunktion der GV?""",
solution="""$$
    f_g(x|\Theta) = \begin{cases}
                    (1-\Theta)^{x-1} \cdot \Theta & \text{für } x \in \mathbb{N} \\
                    0 & \text{für } sonst.
                \end{cases}
    $$""",
)}}

{{ task(
title="Freitext-Frage 6",
question="""6. Wie lautet die Formel der Verteilungsfunktion der GV?""",
solution="""$$
    F_g(x|\Theta) = \begin{cases}
                    0 & \text{für } x<1 \\
                    1-(1-\Theta)^x & \text{für } x \in \mathbb{N}
                \end{cases}
    $$""",
)}}


### Rechenfragen (Python ist benötigt)
{{ task(
title="Rechenfragen 1",
question="""Berechne die Varianz eines gleichmäßig verteilten 20-seitigen Würfels.""",
solution="380",
)}}



{{ task(
title="Rechenfragen 2",
question="""Lottospiel: Du möchtest endlich reich werden und beschließt, ab sofort Lotto zu spielen. Dabei nimmst du dir vor, aufzuhören, sobald du gewonnen hast. Auf dem Lottoschein steht, dass die Wahrscheinlichkeit für einen Gewinn bei 1:1000 liegt. Wie oft musst du spielen, um mit mindestens 50 prozentiger Wahrscheinlichkeit einmal gewonnen zu haben?""",
solution="693",
)}}


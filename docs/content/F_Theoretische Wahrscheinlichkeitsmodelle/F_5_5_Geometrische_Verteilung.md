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
question="""""",
solution="",
) }}

{{ task(
title="MC-Frage 5",
question="""""",
solution="",
) }}


!!! question "4. **Eine geometrische Verteilung hat eine Erfolgswahrscheinlichkeit von \( p = 0.2 \). Was ist die Wahrscheinlichkeit, dass der erste Erfolg im 3. Versuch eintritt?**"

    - A) 0.140625

    - B) 0.1875

    - C) 0.128

    - D) 0.421875

    <details>

    <summary>Lösung</summary>

    C

    </details>

!!! question "5. **Berechne den Erwartungswert \( E(X) \) einer geometrischen Verteilung mit Erfolgswahrscheinlichkeit \( p = 0.2 \).**"

    - A) 4

    - B) 5

    - C) 6

    - D) 7

    <details>

    <summary>Lösung</summary>

    B

    </details>



### Freitext Fragen

!!! question 1. Ist die Geometrische Verteilung diskret oder kontinuierlich?
    <input type="text" id="lname" name="lname" placeholder="Antwort" style=" padding: 10px 15px; font-size: 14px; border: 1px solid #ccc; border-radius: 5px; box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); transition: border-color 0.3s, box-shadow 0.3s; outline: none; " onfocus="this.style.borderColor='#007BFF'; this.style.boxShadow='0 0 5px rgba(0, 123, 255, 0.5)';" onblur="this.style.borderColor='#ccc'; this.style.boxShadow='inset 0 1px 3px rgba(0, 0, 0, 0.1)';"><br></br>
    <details>
    <summary>Lösung</summary>
    Diskret.
    </details>

!!! question  2. Wie verändert sich die Erfolgswahrscheinlichkeit im Verlauf der Versuche?
    <input type="text" id="lname" name="lname" placeholder="Antwort" style=" padding: 10px 15px; font-size: 14px; border: 1px solid #ccc; border-radius: 5px; box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); transition: border-color 0.3s, box-shadow 0.3s; outline: none; " onfocus="this.style.borderColor='#007BFF'; this.style.boxShadow='0 0 5px rgba(0, 123, 255, 0.5)';" onblur="this.style.borderColor='#ccc'; this.style.boxShadow='inset 0 1px 3px rgba(0, 0, 0, 0.1)';"><br></br>

    <details>

    <summary>Lösung</summary>
    Sie bleibt konstant.
    </details>
!!! question 3. Wie lautet die Formel für den Erwartungswert der GV?
    <input type="text" id="lname" name="lname" placeholder="Antwort" style=" padding: 10px 15px; font-size: 14px; border: 1px solid #ccc; border-radius: 5px; box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); transition: border-color 0.3s, box-shadow 0.3s; outline: none; " onfocus="this.style.borderColor='#007BFF'; this.style.boxShadow='0 0 5px rgba(0, 123, 255, 0.5)';" onblur="this.style.borderColor='#ccc'; this.style.boxShadow='inset 0 1px 3px rgba(0, 0, 0, 0.1)';"><br></br>
    <details>

    <summary>Lösung</summary>

    $$E(X) = \frac{1}{p}$$

    </details>



!!! question 4. Welche Schwierigkeiten könnten in einer realen Anwendung auftreten, wenn die Annahmen der geometrischen Verteilung verletzt werden?
    <input type="text" id="lname" name="lname" placeholder="Antwort" style=" padding: 10px 15px; font-size: 14px; border: 1px solid #ccc; border-radius: 5px; box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); transition: border-color 0.3s, box-shadow 0.3s; outline: none; " onfocus="this.style.borderColor='#007BFF'; this.style.boxShadow='0 0 5px rgba(0, 123, 255, 0.5)';" onblur="this.style.borderColor='#ccc'; this.style.boxShadow='inset 0 1px 3px rgba(0, 0, 0, 0.1)';"><br></br>
    <details>

    <summary>Lösung</summary>
    Variierende Erfolgswahrscheinlichkeiten.
    </details>

!!! question 5. Wie lautet die Wahrscheinlichkeitsfunktion der GV?
    <input type="text" id="lname" name="lname" placeholder="Antwort" style=" padding: 10px 15px; font-size: 14px; border: 1px solid #ccc; border-radius: 5px; box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); transition: border-color 0.3s, box-shadow 0.3s; outline: none; " onfocus="this.style.borderColor='#007BFF'; this.style.boxShadow='0 0 5px rgba(0, 123, 255, 0.5)';" onblur="this.style.borderColor='#ccc'; this.style.boxShadow='inset 0 1px 3px rgba(0, 0, 0, 0.1)';"><br></br>
    <details>

    <summary>Lösung</summary>

    $$
    f_g(x|\Theta) = \begin{cases}
                    (1-\Theta)^{x-1} \cdot \Theta & \text{für } x \in \mathbb{N} \\
                    0 & \text{für } sonst.
                \end{cases}
    $$

    </details>

!!! question 6. Wie lautet die Formel der Verteilungsfunktion der GV?
    <input type="text" id="lname" name="lname" placeholder="Antwort" style=" padding: 10px 15px; font-size: 14px; border: 1px solid #ccc; border-radius: 5px; box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); transition: border-color 0.3s, box-shadow 0.3s; outline: none; " onfocus="this.style.borderColor='#007BFF'; this.style.boxShadow='0 0 5px rgba(0, 123, 255, 0.5)';" onblur="this.style.borderColor='#ccc'; this.style.boxShadow='inset 0 1px 3px rgba(0, 0, 0, 0.1)';"><br></br>
    <details>

    <summary>Lösung</summary>

    $$
    F_g(x|\Theta) = \begin{cases}
                    0 & \text{für } x<1 \\
                    1-(1-\Theta)^x & \text{für } x \in \mathbb{N}
                \end{cases}
    $$

    </details>

### Rechenfragen (Python ist benötigt)

!!! question Varianz:
    Berechne die Varianz eines gleichmäßig verteilten 20-seitigen Würfels.
    <input type="text" id="lname" name="lname" placeholder="Antwort" style=" padding: 10px 15px; font-size: 14px; border: 1px solid #ccc; border-radius: 5px; box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); transition: border-color 0.3s, box-shadow 0.3s; outline: none; " onfocus="this.style.borderColor='#007BFF'; this.style.boxShadow='0 0 5px rgba(0, 123, 255, 0.5)';" onblur="this.style.borderColor='#ccc'; this.style.boxShadow='inset 0 1px 3px rgba(0, 0, 0, 0.1)';"><br></br>
    <details>
    <summary>Lösung</summary>
    380
    </details>


!!! question Lottospiel:

    Du möchtest endlich reich werden und beschließt, ab sofort Lotto zu spielen. Dabei nimmst du dir vor, aufzuhören, sobald du gewonnen hast. Auf dem Lottoschein steht, dass die Wahrscheinlichkeit für einen Gewinn bei 1:1000 liegt. Wie oft musst du spielen, um mit mindestens 50 prozentiger Wahrscheinlichkeit einmal gewonnen zu haben?
    <input type="text" id="lname" name="lname" placeholder="Antwort" style=" padding: 10px 15px; font-size: 14px; border: 1px solid #ccc; border-radius: 5px; box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); transition: border-color 0.3s, box-shadow 0.3s; outline: none; " onfocus="this.style.borderColor='#007BFF'; this.style.boxShadow='0 0 5px rgba(0, 123, 255, 0.5)';" onblur="this.style.borderColor='#ccc'; this.style.boxShadow='inset 0 1px 3px rgba(0, 0, 0, 0.1)';"><br></br>
    <details>
    <summary>Lösung</summary>
    693
    </details>

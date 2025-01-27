# Poisson-Verteilung

Die Poisson-Verteilung beschreibt die Wahrscheinlichkeit dafür, dass ein Ereignis \(k\)-mal in einem festen Zeitraum auftritt oder Raum, wenn das Ereignis zufällig und mit konstanter durchschnittlicher Rate ($\lambda$) (Erwartungswert) passiert.

**Anwendungsbereiche:**
   
- Wird verwendet, wenn Ereignisse unabhängig voneinander auftreten und eine durchschnittliche Rate ($\lambda$) bekannt ist.
- Es gibt keine feste Anzahl von Versuchen (wie bei der Binomialverteilung).
- Häufig bei seltenen Ereignissen pro Zeiteinheit oder pro Bereich.
- Wenn 𝑛 → ∞ (sehr viele Versuche) und Θ→0 (die Wahrscheinlichkeit für einen einzelnen Erfolg wird sehr klein) nähert sich die Binomialverteilung der Poisson-Verteilung mit Parameter λ.

!!! formel "Poisson-Verteilung"
   
    $\lambda$: Durchschnittliche Anzahl von Ereignissen pro Zeiteinheit oder pro Bezugsgröße.

    Wahrscheinlichkeitsfunktion:
    
    $$P_p(x|\lambda) = \frac{\lambda^x}{x!} e^{-\lambda}$$
    
    Verteilungsfunktion:
    
    $$F_p(x|\lambda) = e^{-\lambda} \cdot \sum \limits_{k = 0} \limits^{x} \dfrac{\lambda^k}{k!}$$

!!! beispiel "Visualisierung der Verteilung"

    Wahrscheinlichkeitsfunktionen:

    ![Wahrscheinlichkeitsfunktion Poisson](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Poisson-Verteilung_1_5_9.svg/800px-Poisson-Verteilung_1_5_9.svg.png)

    Verteilungsfunktionen:

    ![Verteilungsfunktion Poisson](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Poisson_cumulative_distribution_function.svg/768px-Poisson_cumulative_distribution_function.svg.png)


<iframe src="https://www.geogebra.org/classic/S42P9agy?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

## **Vergleich zwischen Binomialverteilung und Poisson-Verteilung**

| **Kriterium**              | **Binomialverteilung**                                                                     | **Poisson-Verteilung**                                          |
|----------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| **Ereignisse pro Versuch** | Entweder Erfolg oder Misserfolg                                                            | Mehrere Ereignisse in einem Zeitraum/Bezugsraum möglich        |
| **Anzahl der Versuche**    | Fixe Anzahl von $n$ Versuchen                                                              | Variabel oder unendlich groß, Ereignisse treten zufällig auf   |
| **Parameter**              | $n$ und $p$                                                                                | $\lambda$ (Durchschnittsrate der Ereignisse)                  |
| **Typische Anwendung**     | Treffer oder Fehler in $n$ unabhängigen Versuchen                                          | Auftreten von Ereignissen in Zeit oder Raum                   |
| **Nähe zur Poisson**       | Kann bei $n \to \infty$, $p \to 0$, und $np = \lambda$ in die Poisson-Verteilung übergehen | Ist eine Näherung zur Binomialverteilung unter oben genannten Bedingungen |



# Herleitung Poisson-Verteilung

$$f_p(x|\lambda) =\dfrac{\lambda^x}{x!}\cdot e^{-\lambda}$$

$f_b(x|\lambda) = \text{Wahrscheinlichkeit, dass das Ereignis x-mal innerhalb der Bezugsgröße auftritt.}$

$\lambda = \text{Häufigkeit, in der durchschnittlich die Ereignisse zur stetigen Bezugsgröße passieren.}$

$x = \text{Anzahl der Ereignisse innerhalb der Bezugsgröße.}$

$x \in \mathbb{N}_{0}$

$e \approx 2.71828 \cdots$ (Das ist die Euler'sche Zahl!)

!!! beispiel
    
    Eine Fertigungsstraße produziert durchschnittlich 6 fehlerhafte Bauteile pro Stunde.

    $\lambda_{Stunde} = 6$ 

    $\lambda_{Minute} = \dfrac{6}{60}=0.1$


## Herleitung

Die Poisson-Verteilung ist die Erweiterung der Binomial-Verteilung und kann in Fällen angewendet werden, wo man aus einem diskreten Raum in den stetigen Raum wechselt.<br>
In solch einem Fall wird $n$ zu einer beliebig großen Zahl welche, wenn man sich die Funktion für die Binomial-Verteilung anguckt, sehr schnell zum Problem führt.

$$f_b(x|\Theta; n) = \binom{n}{x} \cdot \Theta^x \cdot (1 - \Theta)^{n-x}$$

$$\binom{n}{x} = \dfrac{n!}{x! \cdot (n-x)!}$$

Wenn wir ein $\lim \limits_{n \to \infty}$ haben, so würden wir bei nicht in der Lage sein diese Funktion in deren aktuellen Form auszurechnen.

In der Poisson-Verteilung wird erstmal festgelegt, dass $n \cdot \Theta = \lambda = E_X$

Wird dies nun umgestellt nach $\Theta$ erhalten wir $\Theta = \dfrac{\lambda}{n}$

Setzen wir dies nun in die Funktion der Binomial-Verteilung ein erhalten wir

$$\lim \limits_{n \to \infty} f_b(x|\tfrac{\lambda}{n};n) = \lim \limits_{n \to \infty} \binom{n}{x} \cdot (\tfrac{\lambda}{n})^x \cdot (1 - \tfrac{\lambda}{n})^{n-x}$$

Als nächsten Schritt fokussiert man sich auf den Teil

$$\lim \limits_{n \to \infty} (1 - \tfrac{\lambda}{n})^{n-x}$$

Da $x$ im Vergleich zu $n$ hier vernachlässigbar klein wird, können wir den Exponenten so umschreiben, dass wir folgendes bekommen:

$$\lim \limits_{n \to \infty} (1 - \tfrac{\lambda}{n})^n$$

Warum machen wir das aber?
Der Grund ist der, dass es eine sehr ähnlich aussehende Folge gibt die wie folgt aussieht:

$$\lim \limits_{n \to \infty} (1 + \tfrac{k}{n})^n = e^k$$

Sieht sehr ähnlich aus, nicht wahr?<br>
Tatsächlich können wir unsere vorherige Funktion umformen, um die $e^k$ Folge-Funktion zu erhalten:

$$\lim \limits_{n \to \infty} (1 + \tfrac{-\lambda}{n})^n$$

Da $k = -\lambda$ erhalten wir am Ende

$$\lim \limits_{n \to \infty} (1 + \tfrac{-\lambda}{n})^n = e^{-\lambda}$$

und somit

$$\lim \limits_{n \to \infty} f_b(x|\tfrac{\lambda}{n};n) = \lim \limits_{n \to \infty} \binom{n}{x} \cdot (\tfrac{\lambda}{n})^x \cdot e^{-\lambda}$$

Als nächstes lösen wir alle Klammern und den Binomial-Koeffizienten auf

$$\lim \limits_{n \to \infty} f_b(x|\tfrac{\lambda}{n};n) = \lim \limits_{n \to \infty} \dfrac{n!}{x! \cdot (n-x)!} \cdot \dfrac{\lambda^x}{n^x} \cdot e^{-\lambda}$$

Tauschen wir nun $x!$ mit $n^x$ gemäß Kommutativgesetz bekommt man

$$\lim \limits_{n \to \infty} f_b(x|\tfrac{\lambda}{n};n) = \lim \limits_{n \to \infty} \dfrac{n!}{n^x \cdot (n-x)!} \cdot \dfrac{\lambda^x}{x!} \cdot e^{-\lambda}$$

Fokussieren wir uns nun auf

$$\lim \limits_{n \to \infty} \dfrac{n!}{n^x \cdot (n-x)!}$$

Da $x << n$ (d.h. $x$ is vernachlässigbar klein zu $n$), können wir diesen Bruch vereinfachen als

$$\lim \limits_{n \to \infty} \dfrac{n!}{n!} = 1$$

Setzen wir dies nun auch in unsere vorherige Funktion ein erhalten wir

$$\lim \limits_{n \to \infty} f_b(x|\tfrac{\lambda}{n};n) = 1 \cdot \dfrac{\lambda^x}{x!} \cdot e^{-\lambda}$$

und voila... damit wären wir von der Funktion der diskreten Binomial-Verteilung in die Funktion der stetigen Poisson-Verteilung angekommen.

$$f_p(x|\lambda) =\dfrac{\lambda^x}{x!}\cdot e^{-\lambda}$$


!!! beispiel 
    
    Stell dir vor, täglich kommen **100 Personen** in die Fakultät.
    Im Durchschnitt vergisst davon **eine Person** ihren Laptop.

    **Frage**: Wie hoch ist die Wahrscheinlichkeit, dass genau **3 Personen** an einem Tag ihren Laptop vergessen?

    ---

    **Lösung:**

    Die Situation wird mithilfe der **Poisson-Verteilung** modelliert. Die Formel lautet:
    
    $$P(X = k) = \dfrac{\lambda^k}{k!} \cdot e^{-\lambda}$$
    
    - **$\lambda$** = Erwartungswert = 1 (Durchschnittlich vergisst eine Person pro Tag ihren Laptop).
    - **$k$** = Anzahl der Personen, die ihren Laptop vergessen = 3.
    
    **Berechnung:**

    Einsetzen in die Formel:
    
    $$P(X = 3) = \dfrac{1^3}{3!} \cdot e^{-1}$$
    
    **Zwischenschritte:**

    - $1^3 = 1$
    - $3! = 6$
    - $e^{-1} \approx 0,3679$
    
    $$P(X = 3) = \dfrac{1}{6} \cdot 0,3679 \approx 0,0613$$
    
    **Ergebnis**
    Die Wahrscheinlichkeit, dass genau **3 Personen** an einem Tag ihren Laptop vergessen, beträgt **6,13 %**.


### Jetzt seid Ihr dran!

{{ task(
title="Beispiel 1",
question="""Anzahl von Anrufen, die in einer Stunde bei einem Callcenter eingehen ($\lambda = 10$).

**Gesucht:** Wahrscheinlichkeit, dass genau 12 Anrufe in einer Stunde eingehen.
""",
solution="""**Berechnung:**
    
$$
P(X = 12) = \\frac{10^{12} \\cdot e^{-10}}{12!}
$$

**Ergebnis:**

$$
P(X = 12) \\approx 0.0948
$$""",
) }}

{{ task(
title="Beispiel 2",
question="""Anzahl von Verkehrsunfällen an einer bestimmten Kreuzung an einem Tag ($\lambda = 2$).

**Gesucht:** Wahrscheinlichkeit, dass an diesem Tag genau 3 Unfälle passieren.
""",
solution="""**Berechnung:**

$$
P(X = 3) = \\frac{2^3 \\cdot e^{-2}}{3!} = \\frac{8 e^{-2}}{6}
$$

**Ergebnis:**

$$
P(X = 3) \\approx 0.1804
$$""",
) }}

{{ task(
title="Beispiel 3",
question="""Anzahl von Maschinenfehlern in einer Produktionslinie pro Schicht ($\lambda = 1$).

**Gesucht:** Wahrscheinlichkeit, dass genau 0 Maschinenfehler in einer Schicht auftreten.""",
solution="""**Berechnung:**

$$
P(X = 0) = \\frac{1^0 \\cdot e^{-1}}{0!} = e^{-1}
$$

**Ergebnis:**

$$
P(X = 0) \\approx 0.3679
$$""",
) }}

    
{{ task(
title="Beispiel 4",
question="""Anzahl von E-Mails, die ein Mitarbeiter pro Tag erhält ($\lambda = 15$).

**Gesucht:** Wahrscheinlichkeit, dass ein Mitarbeiter an einem Tag genau 10 E-Mails erhält.
""",
solution="""**Berechnung:**

$$
P(X = 10) = \\frac{15^{10} \\cdot e^{-15}}{10!}
$$

**Ergebnis:**

$$
P(X = 10) \\approx 0.0347
$$""",
) }}


{{ task(
title="Beispiel 5",
question="""Anzahl von Flugverspätungen an einem Flughafen pro Woche ($\lambda = 4$).

**Gesucht:** Wahrscheinlichkeit, dass an einem Tag genau 5 Flugverspätungen auftreten.
""",
tip="Achte auf die Einheiten!",
solution="""**Umrechnung auf pro Tag:** $\lambda_{\\text{Tag}} = \\frac{4}{7} \\approx 0.5714$.

**Berechnung:**
    
$$
P(X = 5) = \\frac{0.5714^5 \\cdot e^{-0.5714}}{5!}
$$

**Ergebnis:**

$$
P(X = 5) \\approx 0.0698
$$""",
) }}

### MC-Fragen zur Poisson Verteilung

{{ task(
title="MC-Frage 1",
question="""Wofür wird die Poisson Verteilung vor allem genutzt?

A) Um Ereignisse kontinuierlich zu modellieren

B) Um die Varianz einer kontinuierlichen Verteilung zu berechnen

C) Um diskrete Ereignisse über eine Zeitspanne zu modellieren

D) Um die Anzahl der Lachanfälle während eines Witzes zu berechnen
""",
solution="C",
) }}


{{ task(
title="MC-Frage 2",
question="""Welches Symbol steht in der Poisson Verteilung für die durchschnittlich erwartete Anzahl an Ereignissen?

A) Lambda

B) Omega

C) Alpha

D) Mu
""",
solution="A", 
) }}

{{ task(
title="MC-Frage 3",
question="""Wie wird der Erwartungswert der Poisson Verteilung beschrieben?

A) Durch Lambda

B) Durch die Anzahl der Kaffeepausen

C) Durch den Binomialkoeffizienten

D) Durch Pi
""",
solution="A", 
) }}

{{ task(
title="MC-Frage 4",
question="""Welche Art von Verteilung ist die Poisson Verteilung?

A) Normale Verteilung

B) Kontinuierliche Verteilung

C) Verrückte Verteilung

D) Diskrete Verteilung
""",
solution="D", 
) }}

{{ task(
title="MC-Frage 5",
question="""Welche Aussage über die Varianz der Poisson Verteilung ist korrekt?

A) Die Varianz ist das Doppelte von Lambda

B) Die Varianz entspricht Lambda

C) Die Varianz hängt von der Tageszeit ab

D) Die Varianz ist immer Null
""",
solution="B", 
) }}




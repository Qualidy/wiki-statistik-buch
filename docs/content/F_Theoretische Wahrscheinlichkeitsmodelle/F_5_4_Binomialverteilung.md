# Binomialverteilung

## Ursprung in Baumdiagrammen

Die Binomialverteilung findet ihren Ursprung in Entscheidungsbäumen. Ein **Baumdiagramm** stellt eine Folge von unabhängigen Versuchen mit jeweils zwei möglichen Ergebnissen (Erfolg/Misserfolg) grafisch dar.

!!! beispiel "Baumdiagramme"
    
    Beispiel für ein Baumdiagramm (zwei Würfe mit einer fairen Münze)

    ```
            Start
            /   \
          K      Z  (1. Wurf)
         / \    / \
        K   Z  K   Z  (2. Wurf)
    ```

    - Jede Kante entspricht einer Wahrscheinlichkeit von 50%.
    - Die möglichen Ergebnisse nach zwei Würfen sind KK, KZ, ZK, ZZ.
    - Die Wahrscheinlichkeit für jedes dieser Ergebnisse beträgt $0.5 \cdot 0.5 = 0.25$.

    Baumdiagramme sind besonders anschaulich, weil sie jeden einzelnen Pfad der Möglichkeiten visualisieren und das Zusammenspiel der Wahrscheinlichkeiten verdeutlichen. Dies legt die Grundlage für die Binomialverteilung.

## Binomialverteilung einfach erklärt

Die **Binomialverteilung** beschreibt die Anzahl der Erfolge in einer festen Anzahl von unabhängigen Versuchen, wobei jeder Versuch nur zwei mögliche Ergebnisse hat: **Erfolg** oder **Misserfolg**. Wie die Silbe "Bi" (lateinisch: Zwei) schon andeutet, dreht sich alles um zwei mögliche Resultate: Erfolg oder Misserfolg, ja oder nein, Treffer oder kein Treffer. Solche "entweder oder"-Experimente mit nur zwei möglichen Ergebnissen nennt man **Bernoulli-Experimente**.

!!! beispiel "Klassisches Beispiel"
    Ein klassisches Beispiel ist der Münzwurf, bei dem es nur zwei mögliche Ergebnisse gibt: Kopf (Erfolg) oder Zahl (Misserfolg). Die Binomialverteilung hilft dabei, die Wahrscheinlichkeit für eine bestimmte Anzahl von Erfolgen in einer Serie solcher Versuche zu berechnen.

## Definition der Binomialverteilung

!!! formel "Binomialverteilung"
    Ein Zufallsexperiment ist binomialverteilt, wenn:

    1. Es gibt $n$ unabhängige Versuche.
    2. Jeder Versuch hat zwei mögliche Ergebnisse: Erfolg (mit Wahrscheinlichkeit $p$) oder Misserfolg (mit Wahrscheinlichkeit $1-p$).
    3. Die Erfolgswahrscheinlichkeit $p$ bleibt bei jedem Versuch gleich.

    Die Binomialverteilung ist eine der wichtigsten diskreten Wahrscheinlichkeitsverteilungen. Sie wird oft verwendet, um Prozesse zu modellieren, bei denen es nur zwei mögliche Ausgänge gibt.

## Binomialverteilung Formel

!!! formel "Binomialverteilung Formel"
    ![Binomialverteilung Formel](https://d1g9li960vagp7.cloudfront.net/wp-content/uploads/2019/02/Binomialverteilung_Formel-neu-1024x576.jpg)

    Die Wahrscheinlichkeit, dass in $n$ Versuchen genau $k$ Erfolge auftreten, wird durch folgende Formel beschrieben:

    $$ P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k} $$

    ### Bestandteile der Formel
    - $n$: Anzahl der Versuche.
    - $k$: Anzahl der Erfolge.
    - $p$: Wahrscheinlichkeit eines Erfolgs pro Versuch.
    - $(1-p)$: Wahrscheinlichkeit eines Misserfolgs pro Versuch.
    - $\binom{n}{k} = \frac{n!}{k!(n-k)!}$: Der **Binomialkoeffizient**, der angibt, auf wie viele Arten $k$ Erfolge in $n$ Versuchen angeordnet werden können.

## Erklärung der Bestandteile der Binomialverteilung

### Der Binomialkoeffizient
Der **Binomialkoeffizient** $\binom{n}{k}$ beschreibt die Anzahl der Möglichkeiten, $k$ Erfolge aus $n$ Versuchen auszuwählen:

$$ \binom{n}{k} = \frac{n!}{k!(n-k)!} $$

Hierbei steht $n!$ für die Fakultät von $n$, also das Produkt aller natürlichen Zahlen von $1$ bis $n$.

### Wahrscheinlichkeit eines Erfolgs
Der Term $p^k$ beschreibt die Wahrscheinlichkeit, dass genau $k$ Erfolge eintreten. Wenn die Erfolgswahrscheinlichkeit eines einzelnen Versuchs $p$ ist, multiplizieren wir sie $k$-mal mit sich selbst.

### Wahrscheinlichkeit eines Misserfolgs
Der Term $(1-p)^{n-k}$ beschreibt die Wahrscheinlichkeit, dass die restlichen $(n-k)$ Versuche fehlschlagen.

### Zusammensetzung der Formel
Die gesamte Wahrscheinlichkeit ergibt sich aus der Kombination der möglichen Anordnungen der Erfolge ($\binom{n}{k}$) und den Wahrscheinlichkeiten für Erfolge ($p^k$) und Misserfolge ($(1-p)^{n-k}$).

## Kumulierte Binomialverteilung

!!! formel "Kumulierte Binomialverteilung"
    Die **kumulierte Binomialverteilung** gibt die Wahrscheinlichkeit an, dass die Zufallsvariable $X$ höchstens einen bestimmten Wert $k$ annimmt. Sie berechnet sich durch die Summation der Wahrscheinlichkeiten bis zu $k$:

    $$ F(X \leq k) = \sum_{i=0}^k \binom{n}{i} p^i (1-p)^{n-i} $$

!!! beispiel

    Ein Basketballspieler mit $p = 0.7$ wirft $n = 10$ Mal. Wie hoch ist die Wahrscheinlichkeit, dass er höchstens $k = 3$ Treffer erzielt?

    $$ F(X \leq 3) = P(X = 0) + P(X = 1) + P(X = 2) + P(X = 3) $$

    Für jeden Wert von $i$ wird die Binomialformel angewandt, und die Ergebnisse werden addiert.

## Deskriptive Maße der Binomialverteilung

!!! formel "Deskriptive Maße"
    ### Erwartungswert $E(X)$
    Der Erwartungswert gibt an, wie viele Erfolge man im Durchschnitt erwarten kann:

    $$ E(X) = n \cdot p $$

    ### Varianz $\text{Var}(X)$
    Die Varianz misst die Streuung der Werte der Zufallsvariablen um den Erwartungswert:

    $$ \text{Var}(X) = n \cdot p \cdot (1-p) $$

    ### Standardabweichung $\sigma(X)$
    Die Standardabweichung ist die Wurzel der Varianz:

    $$ \sigma_X = \sqrt{n \cdot p \cdot (1-p)} $$

## Exkurs: Normalapproximation der Binomialverteilung

Bei sehr großen Werten von $n$ kann die Berechnung der Binomialverteilung zeit- und rechenaufwendig werden, da die Berechnung des Binomialkoeffizienten und die Potenzierungen hohe Zahlen umfassen.

Um dies zu vermeiden, wird oft die **Normalapproximation** genutzt, bei der die Binomialverteilung durch eine Normalverteilung angenähert wird. Diese Methode basiert auf der Tatsache, dass die Binomialverteilung für große $n$ und moderate Werte von $p$ (also $n \cdot p \geq 5$ und $n \cdot (1-p) \geq 5$) nahezu symmetrisch wird und der Normalverteilung ähnelt.

Die Approximation reduziert den Rechenaufwand erheblich, da anstelle komplexer Summen und Fakultäten nur Wahrscheinlichkeiten einer Normalverteilung berechnet werden müssen. Dabei wird die **Stetigkeitskorrektur** eingeführt, um die Diskretheit der Binomialverteilung anzupassen.

Das macht die Normalapproximation besonders bei großen Stichproben nützlich und ist eine weitverbreitete Methode in Statistik und Wahrscheinlichkeitstheorie.

Die Binomialverteilung $X \sim B(n, p)$ wird durch die Normalverteilung $Z \sim N(\mu, \sigma^2)$ approximiert, wobei:

- **Mittelwert (Erwartungswert):** $\mu = n \cdot p$

- **Standardabweichung:** $\sigma = \sqrt{n \cdot p \cdot (1 - p)}$

- **Standardisierung** Um Wahrscheinlichkeiten mit der Standardnormalverteilung $Z \sim N(0, 1)$ zu berechnen, wird $X$ wie folgt standardisiert:

$$
Z = \frac{X - \mu}{\sigma}
$$

- **Korrektur der Stetigkeit**

Da die Binomialverteilung diskret ist und die Normalverteilung stetig, wird häufig die **Korrektur der Stetigkeit** angewendet, indem man bei der Berechnung $ \pm 0.5 $ berücksichtigt:

- Für $P(X \leq k)$: $P(X \leq k) \approx P\left(Z \leq \frac{k + 0.5 - \mu}{\sigma}\right)$

- Für $P(X \geq k)$: $P(X \geq k) \approx P\left(Z \geq \frac{k - 0.5 - \mu}{\sigma}\right)$

- Für $P(X = k)$: $P(X = k) \approx P\left(\frac{k - 0.5 - \mu}{\sigma} \leq Z \leq \frac{k + 0.5 - \mu}{\sigma}\right)$

## Verbindung zum Pascalschen Dreieck


Der **Binomialkoeffizient** $\binom{n}{k}$ kann durch das **Pascalsche Dreieck** visualisiert werden. Das Pascalsche Dreieck ist ein dreieckiges Schema, in dem jede Zahl die Summe der beiden darüberliegenden Zahlen ist.

!!! formel "Aufbau des Pascalschen Dreiecks"

    Jede Zeile des Dreiecks entspricht den Koeffizienten der Binomialverteilung für ein gegebenes $n$:

    - Die 0. Zeile entspricht $n = 0$: $\binom{0}{0} = 1$
    - Die 1. Zeile entspricht $n = 1$: $\binom{1}{0} = 1, \binom{1}{1} = 1$
    - Die 2. Zeile entspricht $n = 2$: $\binom{2}{0} = 1, \binom{2}{1} = 2, \binom{2}{2} = 1$

    Die Position einer Zahl im Pascalschen Dreieck wird durch $n$ und $k$ bestimmt:
    - $n$: Zeilennummer (beginnend bei 0)
    - $k$: Spaltennummer (beginnend bei 0)

    ![Pascalsches Dreieck](https://d1g9li960vagp7.cloudfront.net/wp-content/uploads/2021/02/Pascalsches-Dreieck_Binomialkoeffizient-1024x440.png)

!!! beispiel "Berechnung von $\binom{3}{2}$"

    Um den Wert von $\binom{3}{2}$ zu finden:

    - Gehe zur 3. Zeile (beginnend bei 0).
    - Wähle die 2. Spalte (beginnend bei 0).
    - Der Wert ist 3.

    ![Beispiel Pascalsches Dreieck](https://d1g9li960vagp7.cloudfront.net/wp-content/uploads/2021/02/Beispiel-Binomialkoeffizient-1024x392.png)

!!! beispiel "Beispielrechnung für Basketballspiel"
    Ein Basketballspieler trifft mit Wahrscheinlichkeit $p = 0.7$. Er wirft $n = 10$ Mal. Wie hoch ist die Wahrscheinlichkeit, genau 7 Treffer zu erzielen?

    * Binomialkoeffizient:

    $$\binom{10}{7} = \frac{10!}{7!(10-7)!} = \frac{10!}{7!3!} = 120$$

    * Berechnung der Wahrscheinlichkeit:

    $$P(X = 7) = 120 \cdot 0.7^7 \cdot 0.3^3$$

    $$= 120 \cdot 0.0823543 \cdot 0.027$$

    $$\approx 0.2668$$

    Die Wahrscheinlichkeit, genau 7 Treffer zu erzielen, beträgt **26.68%**.

    ### Pascalsches Dreieck für $n = 10$

    ```
                                 1
                              1     1
                           1     2     1
                        1     3     3     1
                     1     4     6     4     1
                  1     5    10    10     5     1
               1     6    15    20    15     6     1
            1     7    21    35    35    21     7     1
         1     8    28    56    70    56    28     8     1
      1     9    36    84   126   126    84    36     9     1
    1   10    45   120   210   252   210   120    45    10    1
    ```

    Hier kann der Wert $\binom{10}{7} = 120$ direkt in der Zeile $n = 10$, Spalte $k = 7$ abgelesen werden.

# Rechenaufgaben zur Binomialverteilung

!!! question "Fertigungsprozess-Fehleranalyse"
    In einem Fertigungsprozess hat ein Produkt eine Fehlerwahrscheinlichkeit von $p = 0.05$. Eine Stichprobe von $n = 20$ Produkten wird untersucht. Berechne:

    1. Die Wahrscheinlichkeit, dass genau 2 Produkte fehlerhaft sind.
    2. Die Wahrscheinlichkeit, dass höchstens 1 Produkt fehlerhaft ist.

    ??? success "Lösung"

        **Schritt 1: Berechnung für genau 2 fehlerhafte Produkte ($X = 2$):**
    
        Formel der Binomialverteilung anwenden:
    
        $$ P(X = 2) = \binom{20}{2} \cdot (0.05)^2 \cdot (0.95)^{18} $$
    
        1. Binomialkoeffizient berechnen:
           $$ \binom{20}{2} = \frac{20!}{2! \cdot (20-2)!} = \frac{20 \cdot 19}{2} = 190 $$
    
        2. Wahrscheinlichkeit berechnen:
           $$ P(X = 2) = 190 \cdot (0.05)^2 \cdot (0.95)^{18} $$
           $$ = 190 \cdot 0.0025 \cdot 0.4228 $$
           $$ \approx 0.201 $$
    
        Die Wahrscheinlichkeit, dass genau 2 Produkte fehlerhaft sind, beträgt **20.1%**.
    
        **Schritt 2: Wahrscheinlichkeit für höchstens 1 fehlerhaftes Produkt ($P(X \leq 1)$):**
    
        $$ P(X \leq 1) = P(X = 0) + P(X = 1) $$
    
        1. Wahrscheinlichkeit für $X = 0$:
           $$ P(X = 0) = \binom{20}{0} \cdot (0.05)^0 \cdot (0.95)^20 $$
           $$ = 1 \cdot 1 \cdot 0.3585 \approx 0.3585 $$
    
        2. Wahrscheinlichkeit für $X = 1$:
           $$ P(X = 1) = \binom{20}{1} \cdot (0.05)^1 \cdot (0.95)^19 $$
           $$ = 20 \cdot 0.05 \cdot 0.3761 $$
           $$ \approx 0.3761 $$
    
        3. Addieren der Wahrscheinlichkeiten:
           $$ P(X \leq 1) = 0.3585 + 0.3761 = 0.7346 $$
    
        Die Wahrscheinlichkeit, dass höchstens 1 Produkt fehlerhaft ist, beträgt **73.46%**.
    

## Aufgabe 2: Umfrageergebnisse

{{ task(title="""Umfrage zur Produktzufriedenheit""",
question="""In einer Umfrage geben 70% der Teilnehmer an, dass sie mit einem neuen Produkt zufrieden sind. Aus einer Stichprobe von 15 Teilnehmern wird gefragt:

1. Wie hoch ist die Wahrscheinlichkeit, dass genau 10 Personen zufrieden sind?
2. Wie hoch ist die Wahrscheinlichkeit, dass mindestens 12 Personen zufrieden sind?
""",
solution="""**Schritt 1: Wahrscheinlichkeit für genau 10 zufriedene Personen ($X = 10$):**

Formel anwenden:

$$P(X = 10) = \\binom{15}{10} \\cdot (0.7)^{10} \\cdot (0.3)^5$$

* Binomialkoeffizient berechnen:

$$ \\binom{15}{10} = \\frac{15!}{10! \\cdot (15-10)!} = \\frac{15 \\cdot 14 \\cdot 13 \\cdot 12 \\cdot 11}{5 \\cdot 4 \\cdot 3 \\cdot 2 \\cdot 1} = 3003 $$

* Wahrscheinlichkeit berechnen:

$$ P(X = 10) = 3003 \\cdot (0.7)^{10} \\cdot (0.3)^5 $$

$$ \\approx 3003 \\cdot 0.0282 \\cdot 0.00243 $$

$$ \\approx 0.205 $$

Die Wahrscheinlichkeit, dass genau 10 Personen zufrieden sind, beträgt **20.5%**.

**Schritt 2: Wahrscheinlichkeit für mindestens 12 zufriedene Personen ($P(X \geq 12)$):**

$$ P(X \geq 12) = P(X = 12) + P(X = 13) + P(X = 14) + P(X = 15) $$

Für jeden Wert von $X$ wird die Wahrscheinlichkeit einzeln berechnet und anschließend addiert (siehe Formel der Binomialverteilung).
""") }}

## Multiple-Choice-Fragen

{{ task("tasks/F_5_4/MC1.yaml") }}

{{ task("tasks/F_5_4/MC2.yaml") }}

{{ task("tasks/F_5_4/MC3.yaml") }}

## Quiz zum Thema Binomialverteilung

{{ task(
title="Frage 1",
question="Was beschreibt die Binomialverteilung?",
solution="Die Anzahl der Erfolge in einer festen Anzahl von unabhängigen Versuchen mit Erfolgswahrscheinlichkeit $p$.",
)
}}
{{ task(
title="Frage 2",
question="Wie berechnet man den Binomialkoeffizienten $\\binom{n}{k}$?",
solution="$\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$",
)
}}
{{ task(
title="Frage 3",
question="Was ist die kumulierte Binomialverteilung?",
solution="Die Wahrscheinlichkeit, dass $X \\leq k$.",
)
}}
{{ task(
title="Frage 4",
question="Wie berechnet man den Erwartungswert einer Binomialverteilung?",
solution="$E(X) = n \\cdot p$.",
)
}}
{{ task(
title="Frage 5",
question="Was ist der Unterschied zwischen der Wahrscheinlichkeitsfunktion und der Verteilungsfunktion?",
solution="Die Wahrscheinlichkeitsfunktion gibt die Wahrscheinlichkeit für einen bestimmten Wert an, die Verteilungsfunktion summiert bis zu einem bestimmten Wert auf.",
)
}}


## Programmieraufgabe mit Lösung

{{ task("tasks/F_5_4/program.yaml") }}

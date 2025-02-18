# D.2 Korrelationsanalyse

## D.2.1 Metrischer Korrelationskoeffizient nach Bravais-Pearson

{{ task("tasks/D_2_korrelationsanalyse/aufgabe_1_d2.yaml") }}

!!! formel "Metrischer Korrelationskoeffizient r"

    $$
    r = \frac{\sum_{i=1}^{n} (x_i - \bar{x}) \cdot (y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2} \cdot \sqrt{\sum_{i=1}^{n} (y_i - \bar{y})^2}}  = \frac{s_{xy}}{s_x \cdot s_y}
    $$


    $$
    r = \frac{ \left( \sum_{i=1}^{n} x_i \cdot y_i \right) - n \cdot \bar{x} \cdot \bar{y}}{\sqrt{\left( \left( \sum_{i=1}^{n} x_i^2 \right) - n \cdot \bar{x}^2 \right) \cdot \left( \left( \sum_{i=1}^{n} y_i^2 \right) - n \cdot \bar{y}^2 \right)}}
    $$

{{ task("tasks/D_2_korrelationsanalyse/aufgabe_2_d2.yaml") }}

## D.2.2 Rangkorrelationskoeffizient nach Spearman-Pearson

!!! formel "Berechnung vom Rangkorrelationskoeffizienten"

    Formel für den Spearman'schen Rangkorrelationskoeffizienten:

    \[
    r_s = 1 - \frac{6 \sum_{i=1}^{n} ( \text{rg}(x_i) - \text{rg}(y_i) )^2}{n (n^2 - 1)}
    \]

    ---

    Wenn man die Rangdifferenz für jedes Paar \( i \) darstellt als

    \[
    d_i = \text{rg}(x_i) - \text{rg}(y_i)
    \]

    kann man diese kürzere Darstellung verwenden:

    \[
    r_s = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n (n^2 - 1)}
    \]

!!! formel "Interpretation vom Rangkorrelationskoeffizienten"
    + Wenn die Rangordnung der Werte in beiden Variablen exakt übereinstimmt, ist der Wert der Rangkorrelation \(r_s\) gleich 1.
    
    + Wenn die Rangordnung völlig entgegengesetzt ist, ist \(r_s\) gleich -1.
    
    + Ein Wert von 0 bedeutet, dass keine monotone Beziehung besteht.


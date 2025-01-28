# Eigenvektoren und Eigenwerte

Die nächste zentrale Definition ist die von Eigenwerten und Eigenvektoren eines Endomorphismus eines Vektorraums.  

!!! info
    Sei \( f: V \to V \) ein Endomorphismus. Ein \( \lambda \in K \) heißt **Eigenwert** von \( f \), wenn es einen Vektor \( v \neq 0 \) gibt mit \( f(v) = \lambda v \). 

 
Ein solcher Vektor heißt dann ein **Eigenvektor** von \( f \) zum Eigenwert \( \lambda \).


!!! info
    Ein Eigenvektor bzgl. \( f \) ist also ein Vektor, der nicht Null ist und der durch \( f \) um einen Faktor \( \lambda \), den Eigenwert, gestreckt wird.  
    Wir definieren:

    $$
    E(f, \lambda) = \{ v \in V \mid f(v) = \lambda v \}
    $$

    für alle \( \lambda \in K \).

Dies ist ein Untervektorraum von \( V \).  
Per Definition ist \( \lambda \in K \) ein Eigenwert von \( f \), wenn es einen Vektor \( v \neq 0 \) gibt, der zu \( E(f, \lambda) \) gehört.  
\( E(f, \lambda) = \{ v \in V \mid f(v) = \lambda v \} \) ist ein **Untervektorraum** von \( V \).

## Berechnen von Eigenwerten und Eigenvektoren

Nach Definition muss \( f(v) = \lambda v \) sein. Das bedeutet konkret (A ist eine Matrix):

$$
A v = \lambda v.
$$

Dies lässt sich auch umschreiben, mit \( E \) der Einheitsmatrix:

$$
A v = \lambda E v
$$

Das lässt sich dann umformen zu:

$$
(A - \lambda E)v = 0
$$

!!! info
    Um nun den Eigenwert zu berechnen, löst man diese Gleichung.  
    Da \( v \neq 0 \) vorausgesetzt wird, folgt, dass es nur dann lösbar ist, wenn \( (A - \lambda E) \) einen nicht trivialen Kern hat (also keinen Kern \( \neq 0 \)).  
    Das bedeutet wiederum, dass die Determinante 0 sein muss:

    $$
    \det(A - \lambda E) = 0.
    $$

    Diese Determinante nennt man das **charakteristische Polynom**. Die Nullstellen dieses Polynoms sind die Eigenwerte.

!!! info
    Zur Bestimmung der Eigenvektoren setzt man den Eigenvektor in die Gleichung:

    $$
    (A - \lambda E)v = 0
    $$

    ein, anstelle des \( \lambda \), und erhält so ein Gleichungssystem, das man lösen kann.  
    Die Lösung dieses Gleichungssystems ist dann der **Eigenvektor** bzw. die **Eigenvektoren**.

!!! beispiel
    **Beispiel:**  
    Wir bestimmen mal die Eigenwerte der folgenden Matrix:

    $$
    A =
    \begin{pmatrix}
    0 & 2 & -1 \\
    2 & -1 & 1 \\
    2 & -1 & 3
    \end{pmatrix}
    $$

    Setzt man diese in die Gleichung \( (A - \lambda E) = 0 \) ein, dann erhaltet ihr:

    $$
    A - \lambda E =
    \begin{pmatrix}
    0 - \lambda & 2 & -1 \\
    2 & -1 - \lambda & 1 \\
    2 & -1 & 3 - \lambda
    \end{pmatrix}
    =0
    $$

    Dann berechnet ihr die **Determinante** dazu:

    \[
    \begin{aligned}
    \det(A - \lambda E) &=
    (0 - \lambda)(-1 - \lambda)(3 - \lambda) + 4 + 2 - (2\lambda + 2 + \lambda + 12 - 4\lambda) \\
    &= -\lambda^3 + 2\lambda^2 + 4\lambda - 8 \\
    &= -(\lambda - 2)(\lambda - 2)(\lambda + 2) = 0
    \end{aligned}
    \]

    Die Nullstellen des Polynoms sind dann die **Eigenwerte**.  
    Also in diesem Fall \( \lambda_{1,2} = 2 \) und \( \lambda_3 = -2 \).

!!! beispiel
    **Bestimmung der Eigenvektoren:**  
    Jetzt geht es weiter mit den Eigenvektoren. Dazu setzen wir die Eigenwerte für \( \lambda \) ein, zuerst \( \lambda = 2 \):

    $$
    A - 2E =
    \begin{pmatrix}
    0 - 2 & 2 & -1 \\
    2 & -1 - 2 & 1 \\
    2 & -1 & 3 - 2
    \end{pmatrix}
    =
    \begin{pmatrix}
    -2 & 2 & -1 \\
    2 & -3 & 1 \\
    2 & -1 & 1
    \end{pmatrix}
    $$

    Dann muss man das folgende **Gleichungssystem lösen**: 

    $$
    (A - \lambda E) \cdot v = 0
    $$

    $$
    (A - 2 E) \cdot v_{2} = 0
    $$

    $$
    \begin{pmatrix}
    -2 & 2 & -1 \\
    2 & -3 & 1 \\
    2 & -1 & 1
    \end{pmatrix}
    \cdot
    v_{2} =
    \begin{pmatrix}
    0 \\
    0 \\
    0
    \end{pmatrix}
    $$

    Man erhält durch Umformung: (z.B. Gauß-Jordan-Algorithmus)

    $$
    \begin{pmatrix}
    1 & 0 & \frac{1}{2} \\
    0 & 1 & 0 \\
    0 & 0 & 0
    \end{pmatrix}
    \cdot
    v_{2} =
    \begin{pmatrix}
    0 \\
    0 \\
    0
    \end{pmatrix}
    $$

    Dadurch ergibt sich dieses Gleichungssystem:

    $$
    1 \cdot v_{2,1} + \frac{1}{2} \cdot v_{2,3} = 0 
    \Rightarrow
    v_{2,1} = - \frac{1}{2} \cdot v_{2,3}
    $$

    $$
    1 \cdot v_{2,2} = 0
    $$
 

    Als möglicher Vektor lässt sich so ablesen:

    $$
    v_{2} =
    \begin{pmatrix}
    \frac{1}{2} \\
    0 \\
    -1
    \end{pmatrix}
    $$

    Die **Eigenvektoren** sind dann **alle Vielfachen** dieses Vektors!

    **Für den Eigenwert \( -2 \) macht ihr das genauso:**

    $$
    A - (-2)E = A + 2E =
    \begin{pmatrix}
    0 + 2 & 2 & -1 \\
    2 & -1 + 2 & 1 \\
    2 & -1 & 3 + 2
    \end{pmatrix}
        =
    \begin{pmatrix}
    2 & 2 & -1 \\
    2 & 1 & 1 \\
    2 & -1 & 5
    \end{pmatrix}
    $$

    $$
    \begin{pmatrix}
    2 & 2 & -1 \\
    2 & 1 & 1 \\
    2 & -1 & 5
    \end{pmatrix}
    \cdot
    v_{-2} =
    \begin{pmatrix}
    0 \\
    0 \\
    0
    \end{pmatrix}
    $$

    So erhaltet ihr den zweiten Eigenvektor, nämlich **alle Vielfachen** des Vektors:

    $$
    v_{-2} =
    \begin{pmatrix}
    \frac{3}{2} \\
    -2 \\
    -1
    \end{pmatrix}
    $$

{{ task(file="tasks/AufgabeEV.yaml") }}

{{ task(file="tasks/AufgabeEV2.yaml") }}

MORE

![](Check Picture EV TF.png)
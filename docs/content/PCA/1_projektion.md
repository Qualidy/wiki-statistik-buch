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

!!! beispiel "Vektor normieren"

    Um einen Vektor zu normieren, teilen wir ihn durch seine Norm.

    $$
    \Bigl| \frac{v}{|v|} \Bigl| = 1
    $$

    <iframe src="https://www.geogebra.org/calculator/dyup65bz?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

Warum funktioniert diese Rechenregel? Betrachten wir dazu die folgende Herleitung:

!!! tip "Herleitung"
    
    Sei $v\in \mathbb{R}^D\setminus \{0\}$ ein Vektor, auf den $w\in \mathbb{R}^D$ projiziert werden soll.
    
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

??? success "Lösung der Programmieraufgaben"

    ```python
    ### David
    
    import numpy as np
    
    def norm(vec: list[int|float]) -> float:
        return float((np.array(vec) @ np.array(vec).T) ** 0.5)
    
    def normalize(vec: list[int|float]) -> np.ndarray:
        return np.array(vec) / norm(vec)
    
    def is_perpendicular(vec_1: list[int|float], vec_2: list[int|float]) -> bool:
        return np.array(vec_1) @ np.array(vec_2).T == 0
    
    def projection_factor(coord: list[int|float], vec: list[int|float]) -> float:
        return float(np.array(coord).T @ normalize(vec)) / norm(vec) 
      
      
      
      -----johannes-----
      
    import doctest
    doctest.testmod()
    import numpy as np
    def norm(v):
        """    
        >>> norm(np.array([3,4]))
        np.float64(5.0)
        >>> norm(np.array([0,1]))
        np.float64(1.0)
        >>> norm(np.array([1,1]))
        np.float64(1.4142135623730951)
        """
        return np.linalg.norm(v)
    
    def normalize(v):
    
        v_norm = norm(v)
        if v_norm == 0:
            raise ZeroDivisionError("Der Nullvektor kann nicht normiert werden.")
        return v / v_norm
      
      
    def is_perpendicular(v, w, toleranz=0.0000001):
        """
        >>> is_perpendicular(np.array([1, 2]), np.array([-2, 1]))
        np.True_
        >>> is_perpendicular(np.array([3, 4]), np.array([6, 8]))
        np.False_
        >>> is_perpendicular(np.array([0, 1]), np.array([1, 0]))
        np.True_
        >>> is_perpendicular(np.array([1, 1]), np.array([1, -1]))
        np.True_
        """
        return abs(np.dot(v, w)) < toleranz
      
      def projection_faktor(v, w):
        """
        >>> projection_faktor(np.array([1, 0]), np.array([2, 3]))
        np.float64(2.0)
        >>> projection_faktor(np.array([1, 1]), np.array([2, 2]))
        np.float64(2.0)
        >>> projection_faktor(np.array([3, 4]), np.array([6, 8]))
        np.float64(2.0)
        >>> projection_faktor(np.array([1, 2]), np.array([-2, 1]))
        np.float64(0.0)
        >>> projection_faktor(np.array([2, 1]), np.array([-2, 1]))
        np.float64(-0.6)
        """
        dot_product = v @ w
        norm_squared = v@v
    
        if norm_squared == 0:
            raise ZeroDivisionError("Der Vektor v darf nicht der Nullvektor sein.")
    
        return dot_product / norm_squared
      
      
      
      
      ########Daniel#########
      
      import unittest
    from parameterized import parameterized
    
    def norm(v: list):
        return sum(i**2 for i in v)**0.5
    
    def normalize(v: list):
        length = norm(v)
        if length > 0:
            erg = []
            for i in v:
                erg.append(i / length)
            return erg
        else:
            raise ValueError("Die Länge des zu normalisierenden Vektors muss größer als 0 sein!")
    
    def is_perpendicular(v: list, w: list):
        if len(v) == len(w):
            erg = 0
            for i in range(len(v)):
                erg += v[i] * w[i]
            return erg == 0
        else:
            raise ArithmeticError("Dimension der Vektoren müssen übereinstimmen")
    
    def projection_faktor(v, w):
        if len(v) != len(w):
            raise ArithmeticError("Die Dimensionen der Vektoren müssen übereinstimmen")
        
        # Berechnung des Skalarprodukts von v und w
        dot_product_vw = sum(v_i * w_i for v_i, w_i in zip(v, w))
        
        # Berechnung der Norm von v
        length_v = norm(v)
        
        if length_v == 0:
            raise ValueError("Der Vektor v darf nicht der Nullvektor sein")
        
        # Berechnung des Projektionsfaktors
        k = dot_product_vw / (length_v ** 2)
        return k
    
    class TestVectorFunctions(unittest.TestCase):
    
        @parameterized.expand([
            ([3, 4], 5.0),
            ([1, 1, 1], (3**0.5)),
            ([0, 0, 0], 0.0),
            ([2, 2, 2], (12**0.5)),
            ([-3, -4], 5.0)
        ])
        def test_norm(self, v, expected):
            self.assertAlmostEqual(norm(v), expected, places=7)
    
        @parameterized.expand([
            ([3, 4], [0.6, 0.8]),
            ([1, 1, 1], [1/(3**0.5)]*3),
            ([0, 0, 0], ValueError),
            ([2, 2, 2], [1/(3**0.5)]*3),
            ([-3, -4], [-0.6, -0.8])
        ])
        def test_normalize(self, v, expected):
            if expected == ValueError:
                with self.assertRaises(ValueError):
                    normalize(v)
            else:
                result = normalize(v)
                for r, e in zip(result, expected):
                    self.assertAlmostEqual(r, e, places=7)
    
        @parameterized.expand([
            ([1, 0], [0, 1], True),
            ([1, 2, 3], [4, 5, 6], False),
            ([1, 2], [2, -1], True),
            ([0, 0, 0], [0, 0, 0], True),
            ([1, 2, 3], [1, 2], ArithmeticError)
        ])
        def test_is_perpendicular(self, v, w, expected):
            if expected == ArithmeticError:
                with self.assertRaises(ArithmeticError):
                    is_perpendicular(v, w)
            else:
                self.assertEqual(is_perpendicular(v, w), expected)
    
        @parameterized.expand([
            ([1, 2, 3], [4, 5, 6], 2.2857142857142856),
            ([3, 4], [1, 2], 0.44),
            ([1, 0], [0, 1], 0.0),
            ([2, 2, 2], [1, 1, 1], 0.5),
            ([1, 2], [2, -1], 0.0),
            ([0, 0, 0], [1, 2, 3], ValueError),
            ([1, 2, 3], [1, 2], ArithmeticError)
        ])
        def test_projection_faktor(self, v, w, expected):
            if expected == ValueError:
                with self.assertRaises(ValueError):
                    projection_faktor(v, w)
            elif expected == ArithmeticError:
                with self.assertRaises(ArithmeticError):
                    projection_faktor(v, w)
            else:
                self.assertAlmostEqual(projection_faktor(v, w), expected, places=7)
    
    if __name__ == '__main__':
        unittest.main()
        
        
        
    ------Marc------
    import numpy as np
    test = np.array([[1],[2],[2]])
    def norm(v):
        return (v.T @ v)**(1/2)
    
    def normalize(v):
        norm_v = norm(v)
        if norm_v == 0:
            raise ValueError("Der Vektor hat eine Norm von 0, kann nicht normalisiert werden.")
        return v / norm_v  
    
    
    
    def is_perpendicular(v,w):
        return v.T @ w == 0
        
    
    
    def projection_factor(v, w):
        return (w.T @ v).item() / (norm(v) ** 2)  
        
      
      
      
      
    ######### Marina
    
    
    import numpy as np
    
    def projection_vector(w, v):
    
        w = np.array(w)
        v = np.array(v)
        
        #sum(w_i * v_i for w_i, v_i in zip(w, v))
        dot_product = np.dot(w, v)
    
        vector_sqaured = np.dot(v, v)
        return (dot_product/vector_sqaured) * v
    
    
    def normalize_vector(v):
        return (sum(x**2 for x in v))**0.5
    
    
    def are_perpendicular(v1, v2):
    
        v1 = np.array(v1)
        v2 = np.array(v2)
        
        dot_product = np.dot(v1, v2)
        return np.isclose(dot_product, 0)
    
    
    def length_vector(w, v):
        proj_vec = projection_vector(w,v)
        return normalize_vector(proj_vec)
      
      
    ### Fabian 
    
    def norm(v) -> float:
        return np.sqrt(sum([(n**2) for n in v]))
      
      
    def normalize(v) -> list[float]:
        if not any(v):
            raise ValueError('Nullvektor kann nicht normalisiert werden')
        l = norm(v)
        return [s / l for s in v]
      
      
    def is_nullvektor(v):
        return all([s==0 for s in v])
      
      
    def is_perpendicular(v, w) -> bool:
        if is_nullvektor(v) or is_nullvektor(w):
            return False
        return np.array(v).T @ w == 0
      
      
    def projection_factor(v, w) -> float:
        return (np.array(w).T @ v) / norm(v) ** 2
    
    
    ###### Noah
                  
    def norm(v):
        return (sum(num**2 for num in v))**0.5
      
    def normalize(v):
        div = norm(v)
        return [num/div for num in v]
      
    def perpendicular(v, w):
        vt_x_w = sum(v*w for v,w in zip(v,w))
        if vt_x_w == 0:
            return [f"The two vectors {v}, {w} are perpendicular.", vt_x_w]
        else:
            return [f"The two vectors {v}, {w} are NOT perpendicular.", vt_x_w]
          
    def projection_factor(v, w):
        return perpendicular(v, w)[1] / (norm(v)**2)
    
    def projection(v, w):
        factor = projection_factor(v, w)
        return [factor*num for num in v]
      
      
    ########## Tobias
    
    import numpy as np
    from unittest import TestCase, main
    from parameterized import parameterized
    
    
    def norm(v):
        return np.sqrt(sum([elem ** 2 for elem in v]))
    
    
    class NormTest(TestCase):
        @parameterized.expand([
            [[1, 0, 0], 1],
            [[1, 1, 1, 1], 2],
            [[0, 0], 0],
        ])
        def test_norm_0(self, v, result):
            self.assertEqual(norm(v), result)
    
    
    def normalize(v):
        v = np.array(v)
        return v / norm(v)
    
    
    class NormalizeTest(TestCase):
        @parameterized.expand(([
            [[2, 0, 0], [1, 0, 0]],
            [[1, 0], [1, 0]]
        ]))
        def test_normalize_0(self, v, w):
            self.assertListEqual(list(normalize(v)), w)
    
    
    def is_perpendicular(v, w):
        v = np.array(v)
        w = np.array(w)
        return v.T @ w == 0
    
    
    class PerpendicularTest(TestCase):
        @parameterized.expand([
            [[1, 0, 0], [0, 0, 1], True],
            [[1, 2], [2, 4], False],
            [[1, 2, 3], [2, 4, 1], False]
        ])
        def test_perpendicular_0(self, v, w, result):
            self.assertEqual(is_perpendicular(v, w), result)
    
    
    def projection_factor(v, w):
        if is_perpendicular(v, w):
            return 0
    
        w = np.array(w)
    
        return (w.T @ normalize(v)) / norm(v)
    
    
    class ProjectionTest(TestCase):
        @parameterized.expand([
            [[1, 0], [3, 4], 3],
            [[0, 1], [3, 4], 4],
            [[0, 1, 0], [1, 2, 3], 2],
            [[0, 1, 0], [-1, 0, 2], 0],
            [[1, 1, 1], [1, 2, 3], 2]
        ])
        def test_projection(self, v, w, k):
            self.assertAlmostEqual(projection_factor(v, w), k)
    
      
      
    ```


## Projektion auf einen Hyperraum

!!! formel "Hyperebene"
    
    Eine **Hyperebene** ist ein Raum, der eine Dimension kleiner ist, als der Hauptraum.

!!! beispiel

    Wenn der Hauptraum der 3-dimensionale Raum ist, dann ist ein Hyperraum eine Ebene, die unendlich groß ist und 
    durch den Nullpunkt geht. Diese Ebene muss nicht auf einer der Achsen liegen, sondern kann auch "quer"
    im Raum sein. Das wichtige ist, dass man sich auf dieser Ebene nur noch in zwei verschiedene Richtungen bewegen kann,
    während man im 3d-Raum noch drei orthogonale Richtungsvektoren hatte.

    Wenn der Hauptraum ein 2d-Koordinatensystem ist, dann ist jede Gerade, die durch den Nullpunkt geht eine Hyperebene.
    
Jeder Hyperraum hat einen Normalenvektor, der senkrecht auf den Raum steht. Dieser ist nützlich, um alle 
Punkte aus dem großen Raum auf den Hyperraum herunter zu projizieren.

<iframe src="https://www.geogebra.org/calculator/aejercma?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

!!! formel "Normalenvektor"
    
    Sei $n \in \mathbb{R}^D$ ein Vektor. Dann erzeugt $n$ eine Hyperebene 
    $H := \{ x \in \mathbb{R}^D | x \perp n \}$
    
!!! formel "Hessesche Normalform"
    
    Es sei $E$ eine Ebene mit zugehörigen Normalenvektor $n$. Falls die Ebene nicht durch den Nullpunkt geht,
    kann ein *Stützvektor* $a \in E$ genutzt werden, um die gesamte Ebene als die Punkte $x$ zu beschreiben,
    die die Gleichung 
    
    $$
    (x-a)\cdot n = 0 \text{ bzw. } (x-a)^t n = 0
    $$

    erfüllen.

    In unseren Untersuchungen sind ist jedoch immer $a = 0$, da alle betrachteten Räume durch den Nullpunkt gehen.


!!! beispiel 

    Gegeben sei eine Ebene $E$, die durch die Vektoren 
    $v = \begin{pmatrix} 1 \\ -2 \\ 0.5 \end{pmatrix}$ und $u = \begin{pmatrix} 3 \\ -1 \\ 0 \end{pmatrix}$
    aufgespannt wird.

    Dann ist $n = \begin{pmatrix} 0.5 \\ 1.5 \\ 5 \end{pmatrix}$ Normalenvektor von $E$ und $n \perp v, u$. 

    <iframe src="https://www.geogebra.org/calculator/fq84pxup?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>
    

{{ task("tasks/pca/projektion/normalenvektor.yaml") }}

{{ task("tasks/pca/projektion/projektion_auf_ebene.yaml") }}

{{ task("tasks/pca/projektion/final_projection.yaml") }}

{{ task("tasks/pca/projektion/projektion_auf_ebene_programmieren.yaml") }}



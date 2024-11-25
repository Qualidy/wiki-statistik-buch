# C.2.1 Eindimensionale Häufigkeitsverteilung

!!! formel "Absolute empirische Häufigkeitsfunktion"
    
    Es sei $X = (x_1, x_2, \cdots, x_n)$ ein Mermal.
    Um die absolute empirische Häufigkeitsfunktion zu bestimmen,
    kann folgende Formel genutzt werden:
    
    $$
    f_h(x) =
    \begin{cases} 
    n_k & \text{für } x = x_k, \\ 
    0 & \text{sonst.}
    \end{cases}
    $$
    
    $n_k$ steht für die Anzahl des Auftretens von $x_k$ in $X$.

!!! beispiel
    
    Sei $X=(1, 2, 1, 2, 3, 2, 1, 1)$. 
    Dann sind z.B. $x_1 = 1$, $x_2 = 2$, $x_8 = 1$ und $x_9$ gibt es nicht!
    
    $n_1 = 4$, weil der Wert $x_1 = 1$ in $X$ insgesamt $4$ mal auftaucht.
    
    $n_2 = 3$ weil der Wert $x_2 = 2$ in $X$ insgesamt $3$ mal auftaucht.
    
    $n_3 = 4$ weil der Wert $x_3 = 1$ in $X$ insgesamt $4$ mal auftaucht.
    
    $n_4 = 3$ weil der Wert $x_4 = 2$ in  $X$ insgesamt $3$ mal auftaucht.
    
    $n_5 = 1$ weil der Wert $x_5 = 3$ in $X$ insgesamt $1$ mal auftaucht.

    ...

    $n_8 = 4$ weil der Wert $x_8 = 1$ in $X$ insgesamt $4$ mal auftaucht.
    
    
    Nutzen wir nun die **absolute empirische Häufigkeitsfunktion**:
    
    Es ist $f_h(2) = 3$. Denn $x=2$ und damit ist z.B. $x = x_2$. Also wird $n_2 = 3$ zurückgegeben.
    
    Es ist $f_h(7) = 0$. Denn $x=7$ und es gibt kein $k$ mit $x_k=x=7$. Also wird der "sonst"-Fall ausgegeben.
     
**Implementierung in Python:**

In Python lassen sich die absoluten Häufigkeiten $n_k$ mit der Methode `count` ermitteln:

```python
X = (1, 2, 1, 2, 3, 2, 1, 1) 

def f_h(x, data):
    return data.count(x)

print(f_h(1, data=X)) # 4 
```

!!! formel "Relative empirische Häufigkeitsfunktion"

    Es sei $X = (x_1, x_2, \cdots, x_n)$ ein Mermal.
    Um die relative empirische Häufigkeitsfunktion zu bestimmen,
    kann folgende Formel genutzt werden:
    
    $$
    f_h^*(x) =
    \begin{cases} 
    \frac{n_k}{n} = n_k^* & \text{für } x = x_k, \\ 
    0 & \text{sonst.}
    \end{cases}
    $$

    $n_k$ steht für die Anzahl des Auftretens von $x_k$ in $X$.

**Implementierung in Python:**

```python
X = (1, 2, 1, 2, 3, 2, 1, 1) 

def f_h_rel(x, data):
    return data.count(x) / len(data)

print(f_h_rel(1, data=X)) # 0.5 
print(f_h_rel(7, data=X)) # 0.0
```

{{ task("tasks/C_2_1_relative_counts/aufgabe.yaml") }}

{{ task("tasks/C_2_2_4_get_counts/aufgabe.yaml") }}

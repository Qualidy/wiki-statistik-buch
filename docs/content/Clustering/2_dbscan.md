# DBScan

DBScan ist ein Clusteringalgorithmus, der selbstständig eine passende Anzahl von Clustern sucht.
Elemente, die er nicht einem Cluster zuordnen kann, werden als "Ausreißer" markiert.

!!! formel "Algorithmus"

    **Hyperparameter:**

    * 𝑛∈ℕ : die Anzahl der Nachbarn, die ein Punkt braucht, um als Kernpunkt zu gelten.
    * 𝜀∈(0,∞): der Abstand, in dem ein Punkt als Nachbar eines anderen Punktes gilt.
    * Eine Abstandsfunktion 𝑑.

    **Algorithmus:**

    1. Berechnen Sie für jeden Datenpunkt die Anzahl der Nachbarn, die näher als ein bestimmter Grenzwert 𝜀∈(0,∞) liegen.
    2. Markiere alle Punkte mit mindestens 𝑛∈ℕ Neiboren als Kernpunkte.
    3. Wähle einen beliebigen Kernpunkt 𝑝, der nicht Teil eines Clusters ist, und füge ihn zu einem neuen Cluster 𝑐 hinzu.
    4. Füge alle Kernpunkte, die einen maximalen Abstand von 𝜀 zu 𝑝 haben, dem Cluster 𝑐 hinzu.
    5. Wiederholen Sie Schritt 4 für alle neu hinzugefügten Kernpunkte des Clusters.
    6. Wenn es in diesem Cluster keine weiteren Kernpunkte mehr hinzuzufügen gibt, wiederholen Sie Schritt 3. Wenn alle Kernpunkte zu Clustern hinzugefügt wurden, fahren Sie mit Schritt 7 fort.
    7. Für jeden Nicht-Kernpunkt 𝑝^′ wird der nächstgelegene Kernpunkt-Nachbar 𝑝 mit einem maximalen Abstand von 𝜀 gesucht und 𝑝′ zum Cluster von 𝑝 hinzugefügt.
    8. Alle verbleibenden Nicht-Kernpunkte werden dem Ausreißer-Cluster hinzugefügt.

!!! beispiel

    [📙Clustering der Benzin- und Dieselpreise in Indien](https://www.kaggle.com/code/viktorreichert/dbscan-clustering-of-fuel-price-in-india)

    ![img_1.png](img_1.png)

!!! beispiel
    
    ![Folie192.PNG](dbscan_images/Folie192.PNG)
    ![Folie193.PNG](dbscan_images/Folie193.PNG)
    ![Folie194.PNG](dbscan_images/Folie194.PNG)
    ![Folie195.PNG](dbscan_images/Folie195.PNG)
    ![Folie196.PNG](dbscan_images/Folie196.PNG)
    ![Folie197.PNG](dbscan_images/Folie197.PNG)
    ![Folie198.PNG](dbscan_images/Folie198.PNG)
    ![Folie199.PNG](dbscan_images/Folie199.PNG)
    ![Folie200.PNG](dbscan_images/Folie200.PNG)
    ![Folie201.PNG](dbscan_images/Folie201.PNG)
    ![Folie202.PNG](dbscan_images/Folie202.PNG)
    ![Folie203.PNG](dbscan_images/Folie203.PNG)
    ![Folie204.PNG](dbscan_images/Folie204.PNG)
    ![Folie205.PNG](dbscan_images/Folie205.PNG)
    ![Folie206.PNG](dbscan_images/Folie206.PNG)

{{ task("tasks/clustering/dbscan.yaml") }}

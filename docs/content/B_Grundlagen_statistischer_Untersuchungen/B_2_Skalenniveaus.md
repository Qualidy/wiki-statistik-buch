#Skalenniveaus


### Zusammenfassung zu Skalen

Eine Skala ist eine Zusammenstellung aller möglichen Ausprägungen eines Merkmals und dient als Maßstab für die Datenerhebung. Je nach Skalenniveau (Nominal-, Ordinal-, Intervall- oder Verhältnisskala) unterscheiden sich die zulässigen mathematischen Operationen, wobei höhere Skalenniveaus mehr mathematische Möglichkeiten bieten.


Übersicht der Skalenniveaus

Skalenniveau         | Zulässige mathematische Operationen          | Beispiele
---------------------|---------------------------------------------|-------------------------------------------
Nominalskala         | = / ≠                                       | - Geschlecht: {männlich, weiblich}
                     |                                             | - Name: {Anja, Alexander, Astrid, …}
                     |                                             | - Farbe: {blau, rot, grün, …}
Ordinalskala         | = / ≠; < / > (z. B. "besser/schlechter")    | - Zufriedenheit: {sehr unzufrieden, unzufrieden, indifferent, zufrieden, sehr zufrieden}
                     |                                             | - Schulnoten: {sehr gut, gut, …}
                     |                                             | - Dienstgrad: {Jäger, Gefreiter, Obergefreiter, …}
Metrisch (kardinal)  |                                             | 
Intervallskala       | = / ≠; < / >; + / −                         | - Temperatur: {…, -1, 0, 1, …} °C
                     |                                             | - Geburtsjahr: {…, 2001, 2002, …}
Verhältnisskala      | = / ≠; < / >; + / −; × / ÷                  | - Monatseinkommen: [0; ∞) EUR
                     |                                             | - Alter: [0; ∞) Jahre
                     |                                             | - Gewicht: [0; ∞) g
                     |                                             | - Kinderzahl: {0, 1, 2, …}

Tabelle 1: Überblick über die Skalenniveaus

!!! question "Aufgabe Gruppierer:"
    Erstelle eine Funktion `group(values)`, dass eine liste in ein dictionary verwandelt und zählt,
    wie oft jedes Element in der Liste auftaucht. z.b. 
    ```python
    group(['mo', 'di', 'mo']) # {'mo': 2, 'di': 1}
    ```

    ??? Tests
        ```python
        from unittest import TestCase, main
        from parameterized import parameterized

        class TestGroup(TestCase):

            @parameterized.expand([
                (['C', 'H', 'O', 'C', 'Cl', 'N', 'C', 'H'], {'C': 3, 'H': 2, 'O': 1, 'Cl': 1, 'N': 1}),
                (['C', 'H', 'C', 'C', 'H', 'O', 'C', 'H'], {'C': 4, 'H': 3, 'O': 1})
            ])
            def test_group(self, input_list, expected):
                self.assertDictEqual(group(input_list), expected)
        ```


    ??? solution "Lösung mit for-Schleifen"
        ```python
        def groupby(values):
            grouped_dict = {}
            for value in values:
                if value in grouped_dict:
                    grouped_dict[value] += 1
                else:
                    grouped_dict[value] = 1
            return grouped_dict
        ```
    
    ??? solution "Lösung mit Dictionary Comprehension"
        ```python
        def group(values):
            return {value: values.count(value) for value in set(values)}
        ```

    ??? solution "Löung mit Doctests"
        ```python
        def group(values:list)->dict:
            """    
            >>> group(['mo', 'di', 'mo'])
            {'mo': 2, 'di': 1}

            >>> group([1, 2, 2, 3, 1, 1])
            {1: 3, 2: 2, 3: 1}

            >>> group([])
            {}

            >>> group(['a', 'a', 'a', 'b', 'c', 'c'])
            {'a': 3, 'b': 1, 'c': 2}
            """
            return {ele:values.count(ele) for ele in set(values)}
        ```

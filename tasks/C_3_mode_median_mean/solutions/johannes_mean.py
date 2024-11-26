#  das arithmetische Mittel,
import doctest
doctest.testmod()
def arithmetische_mittel(values:list):
    """
    >>> arithmetische_mittel([1,2,3])
    2.0
    >>> arithmetische_mittel([1,2])
    1.5
    >>> arithmetische_mittel([1,2,0,0,0,0])
    0.5
    >>> arithmetische_mittel([1,2,0,0,0,0])
    0.5
    >>> arithmetische_mittel([])
    Traceback (most recent call last):
      File "/opt/homebrew/Cellar/python@3.13/3.13.0_1/Frameworks/Python.framework/Versions/3.13/lib/python3.13/doctest.py", line 1395, in __run
        exec(compile(example.source, filename, "single",
        ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     compileflags, True), test.globs)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "<doctest __main__.arithmetische_mittel[4]>", line 1, in <module>
        arithmetische_mittel([])
        ~~~~~~~~~~~~~~~~~~~~^^^^
      File "/var/folders/4w/4kbvllw55js83tswczqll0kc0000gq/T/ipykernel_5572/265014954.py", line 21, in arithmetische_mittel
        raise ZeroDivisionError("...")
    ZeroDivisionError: ...
    """
    if values:
        return sum(values)/len(values)
    raise ZeroDivisionError("...")

print(f"{arithmetische_mittel(data)}")
import pandas as pd
print(f"{pd.Series(data).mean()}")

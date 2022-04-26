# kspfx
Jelikož používám zastaralou knihovnu [baseconvert](https://pypi.org/project/baseconvert/#description), která byla vyvíjena na Python 3.5, tak musíme udělat
malinké úpravy, aby fungovala s moderni verzí Pythonu, ale nejdříve musíme samotný baseconvert nainstalovat a to jednoduchým příkazem 
```
pip install baseconvert
```
# Jak na to?
Ve složce, kde máme Base convert nainstalovaný (Obvykle venv/lib/site-packages/baseconvert) upravíme soubor baseconvert.py.
Jediné co stačí změnit je tento řádek
```
from fractions import gcd
```
na
```
from math import gcd
```
A vše je hotovo!

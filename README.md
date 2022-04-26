# kspfx
Jelikož používám zastaralou knihovnu [Base convert](https://pypi.org/project/baseconvert/#description), která byla vyvíjena na Python 3.5, tak musíme udělat
malinké úpravy, aby fungovala s moderni verzí Pythonu
# Jak na to?
Ve složce, kde máme Base convert nainstalovaný (Obvykle venv/lib/site-packages/baseconvert) upravíme soubor baseconvert.py.
Jediné co stačí změnit tento řádek
```
from fractions import gcd
```
na
```
from math import gcd
```
A vše je hotovo!

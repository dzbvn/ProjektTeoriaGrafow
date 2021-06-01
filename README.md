# Projekt Teoria Grafów

Algorytm wczytuje grafy z plików tekstowych, w których zawarta jest lista sąsiedztwa. Aby zmienić wczytywany plik, musimy zmienić nazwę pliku w 124 linijce kodu w main.py

Format wprowadzanej listy sąsiedztwa:
>[A => B2 => C4\
> B => D3 => C3\
> C => D-1 => E4\
> D => E2]

Za pomocą takiej listy wczytujemy poniższy graf:
 
![graf1](https://lh3.googleusercontent.com/proxy/9RCesD3R-uPBYZyIfLv74glZkbEcMd0LeDU9gmAuiyVtLvDe5llRfwCW_opGXvFIuWCa4ljgK1ArGB5Xj_BuJVqifxiYyGL6HDxchw7T9oLMxvE-Bw)

Obsługiwany jest również format, w którym w jednym pliku mamy parę list, wtedy musimy oddzielić je przecinkami.
Przykład:
>[[A => B2 => C4\
> B => D3 => C3\
> C => D-1 => E4\
> D => E2],\
> [A => B4 => C2\
> B => C3 => D2 => E3\
> C => B1 => D4 => E5\
> E => D-5]]

Źródła wykorzystane w części analitycznej:\
https://en.wikipedia.org \
https://eduinf.waw.pl

Szkielety grafów zrealizowane zostały za pomocą strony https://graphonline.ru/en

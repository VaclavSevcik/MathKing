# Language
* [Česky](#matematicky-kral)
* [English](#mathking)

# Početní kral

Aplikace pro generování příkladů pro učitele prvního stupně základních škol. 
Generátor dokáže generovat příklady v rozsahu čísel nastavených uživatelem. 
Uživatel si může zvolit operace se kterými budou příklady generovány. 

Tato aplikace může být například využita při hře početní král, nebo při vytváření testů či jako materiál na procvičování pro ty, kterým to tolik nejde, zvídavé, nebo ty zlobivé.

## Pravidla hry
Hra je postavena na zautomatizování základních počtů a celkovému zlepšení v počtech. Lze tuto hru pojat kompetitivně pro větší motivaci žáků. Například první 3-5 žáků dostane malou jedničku.
Také je možné ocenit pokrok jednotlivých dětí. Třeba zapisovat výsledky do tabulky a pochválit, nebo povzbudit, když vidíš výsledky hry. V hodnocení se meze nekladou.

Hra může být vhodná na úvod hodiny jako rychlá rozcvička. Je vhodná pro třídy, kde se počítají počty. Nejspíše od 3.-5. třída. Podle mě je vhodné ji nasadit třeba na pololetí, při velké oblibě i déle.

### Průběh hry
Žáci dostanou otočený papír s příkladami. Poté na pokyn učitele ho otočí a po dobu 1 minuty se snaží vypočítat co nejvíce příkladů. 
Po skončení (možné upozornit na posledních 10 sekund) všichni odloží psací potřeby (jinak diskvalifikace žáka). 
Poté si vymění se spolužákem papíry a učitel přečte výsledky a žáci si navzájem opraví řešení. Poté spočtou počet správných řešení.
 Při shodě bodů se hodnotí kdo má méně špatně vypočítaných příkladů. Po skončení početního krále možnost nechat papíry žákům, aby mohli, třeba za úkol se v počtech zlepšit.
 
### Výhody hry
Žáci dokáží automatizovat některé příklady. Snadnější přechod na těžší počty (sčítání, odčítání, násobení pod sebou, nebo dělení větších čísel). 
Motivace i pro ty kterým počty jdou. Je pro ně soutěž zajímavá a mohou nejlepší mezi sebou soupeřit (může být i motivace jiná než známky, třeba celoroční vyhodnocení).

### Nevýhody hry
Je potřeba motivovat ty, kterým moc počty nejdou, třeba právě nějakým individuálním hodnocení (zlepšení během roku, atd.). Nebo říci jim, že nemusí to brát kompetitivně, ale to je těžší dětem vysvětlovat.

### Postřehy učitelů z praxe

## Možnosti generování

Uživatel si může zvolit z:
- sčítání
- odčítání
- násobení
- celočíselné dělení

Generátor vytváří dva PDF soubory:
- se samotnými příklady pro žáky (v zvoleném počtu kopií)
- s výsledky pro učitele

Uživatel si může nastavit kolik sad se stejnými příklady chce generovat do PDF. Poté stačí PDF vytisknout a rozstříhat na jednotlivé zadání. Příklady z jednoho zadání nikdy nepřesáhnou hranu listu A4.

## Instalace

Před začátkem používání je nutné připravit pro program prostředí počítače. Nastavení lze provést dvěma způsoby:

### Spuštění přes binární soubor (Windows)
 - Instalace Python 3 stáhnout z store: https://www.microsoft.com/cs-cz/p/python-38/9mssztt1n39l? nebo
 (instalace + nastavení proměnné prostředí PATH na složku s interpretem python) stažení na stánce: https://www.python.org/downloads/windows/
 - spuštění programu
### Spuštění přes python (Linux, Mac, Windows)
 -  Instalace python (https://www.python.org/downloads/) a nastavení cesty PATH jak na python tak na složku Scripts u interpretu, kde je program pip.
 -  Instalace pip install -r requirements.txt
 -  Spuštění modulu MathKing.py

# MathKing
The generator of examples (basic math) for elementary school teachers. 

## Generator possibilities

The user can choose from:
- addition
- subtraction
- multiplication
- integer division

The generator creates two PDFs:
- generated examples for pupils (contents contains number of sample according to number of copies)
- the PDF with results for teacher

The user can set how much samples want to generate to PDF. After print the user only cuts the sample and they able to use in class.

## Installation

Before using the generator is necessary to prepare computer environment. The settings is able to sets two ways:

### Through binary file (Windows)
- first step is install Python 3 from windows store: https://www.microsoft.com/cs-cz/p/python-38/9mssztt1n39l? or
(install manually and set the environment variable PATH with path to interpret folder). The python available on page: https://www.python.org/downloads/windows/
- run the binary file with program

### Through python interpret (Linux, Mac, Windows)
 -  Installation of python (https://www.python.org/downloads/) and set PATH like in previous way. Plus set path to folder Script in Python folder (because of program pip).
 -  Installation: pip install -r requirements.txt
 -  Run the modul in python3 MathKing.py without argument
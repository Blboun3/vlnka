# vlnka
Aktualizovanější nezávislá verze programu Vlna 1.5 (autor: RNDr. Petra Olšáka) vytvořená v Pythonu

Program Vlna (i Vlnka) mají za úkol přidat "\~" do .tex souborů před všechny české předpony a tím předejít tzv. "sirotkům", jednoznakovým předložkám/spojkám na koncích řádek. Program toto řeší vložením "\~" což vytvoří nezlomitelnou mezeru.

! Program se neinstaluje, k jeho použití je potřeba Python 3 (nebo novější). !

Použití: 
```
python3 main.py soubor.tex
```
případně
```
python3 main.py *.tex
``` 
( Všechny .tex soubory ve složce )

Program má také integrovanou funkci na vytvoření kopie zpracovávaných souborů ( proměnná "copy", nastavné na False kopie nedělá, základně nastavená na False)

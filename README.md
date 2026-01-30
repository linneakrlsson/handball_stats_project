# Handball Statistics Project

I detta skolprojekt har jag analyserat statistik från herrarnas Bundesliga i handboll för säsongen 2022/2023.  
Syftet med projektet är att genom en Streamlit-applikation möjliggöra tydliga och lättillgängliga visualiseringar av enskilda spelares prestationer under säsongen.

De flesta analysmodeller och index som presenteras i applikationen är egenutvecklade. Dessa bör tolkas som analytiska indikationer snarare än exakta eller absoluta värden. Modellerna är baserade på tillgänglig statistik och syftar till att ge insikt i prestation samt möjliggöra jämförelser mellan spelare, men utgör inte heltäckande mått på individuell kvalitet.

---

Data

Datan är ursprungligen hämtad från **Kaggle** och baseras på filen `handball_stats.csv` från *Handball Bundesliga Stats 2022/2023*.  
På grund av ett stort antal förkortningar och inkonsekventa kolumnnamn har datan rensats och bearbetats. Den städade versionen har sparats som en ny CSV-fil och det är denna som används i projektet.

---

Använda bibliotek

- Streamlit  
- Pandas  
- Seaborn  
- Matplotlib  

---

Projektstruktur

**VIKTIGT:** Följande mapp- och filstruktur måste behållas för att applikationen ska fungera korrekt.

| File | Description |
|------|------------|
| `streamlit_app.py` | Huvudfil för applikationen och användargränssnitt |
| `plots.py` | Samtliga visualiseringar och rankingdiagram |
| `data.py` | Dataladdning och feature engineering |
| `handball_stats_cleaned.csv` | Rensad och bearbetad dataset ||

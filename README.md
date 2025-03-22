# B-Team12: Hotelreservationsystem

## Autoren
Tanja Luescher
Sarina Grabherr
Fabia Holzer
Stirling Mulholland

## Deliverables
Der Abgabetermin 15.06.2025  für die Projektarbeit ist auf Moodle angegeben. Dabei gibt jedes Team
Folgendes an:
- Source Code und Artefakte
o Link zum Deepnote-Projekt mit allen ausführbaren Notebooks, Dateien und der
endgültigen Datenbank,
[Deepnote-Projekt](https://deepnote.com/workspace/FHNW-98157d3c-c139-4c9e-a143-1cabfe774ad5/project/B-Team12-hotelreservation-c198bb5c-da9b-4a42-90aa-865b4b8bde28/notebook/520bcd201f574cfcb10519b35812afcf)
o Link zum GitHub-Repository,
[GitHub-Repository](https://github.com/satafasti/team12_hotelreservation)
o Link zu einer Projekt Board
[Projekt Board](https://www.notion.so/1a62a269cd5a805f8983f8caf82b576a?v=1a62a269cd5a80769d6d000c6d5a6a27 )
- Dokumentation/Bericht (Link zu GitHub Markdown-Datei(en))
- Link zum Präsentationsvideo (das auf Microsoft Stream, SWITCHtube oder YouTube
gehostet wird; eingeschränkter/ungelisteter Zugang möglich und empfohlen). Es wird
empfohlen, dass jedes Teammitglied an der Videopräsentation beiträgt.

#  Einleitung

## Kontext

## User Stories

### Minimale User Stories

1. Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit
ich dasjenige auswählen kann, welches meinen Wünschen
entspricht. Wünsche sind:
1.1. Ich möchte alle Hotels in einer Stadt durchsuchen,
damit ich das Hotel nach meinem bevorzugten Standort
(Stadt) auswählen kann.
1.2. Ich möchte alle Hotels in einer Stadt nach der
Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.
1.3. Ich möchte alle Hotels in einer Stadt durchsuchen,
die Zimmer haben, die meiner Gästezahl entsprechen (nur 1
Zimmer pro Buchung).
1.4. Ich möchte alle Hotels in einer Stadt durchsuchen,
die während meines Aufenthaltes ("von" (check_in_date)
und "bis" (check_out_date)) Zimmer zur Verfügung haben,
damit ich nur relevante Ergebnisse sehe.
1.5. Ich möchte Wünsche kombinieren können, z.B. die
verfügbaren Zimmer zusammen mit meiner Gästezahl und der
mindest Anzahl Sterne.
1.6. Ich möchte die folgenden Informationen pro Hotel
sehen: Name, Adresse, Anzahl der Sterne.
2. Als Gast möchte ich Details zu verschiedenen Zimmertypen
(Single, Double, Suite usw.), die in einem Hotel verfügbar
sind, sehen, einschliesslich der maximalen Anzahl von Gästen
für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine
fundierte Entscheidung zu treffen.
2.1. Ich möchte die folgenden Informationen pro Zimmer
sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung,
Ausstattung, Preis pro Nacht und Gesamtpreis.
2.2. Ich möchte nur die verfügbaren Zimmer sehen, sofern
ich meinen Aufenthalt (von – bis) spezifiziert habe.
3. Als Admin des Buchungssystems möchte ich die Möglichkeit haben,
Hotelinformationen zu pflegen, um aktuelle Informationen im
System zu haben.
3.1. Ich möchte neue Hotels zum System hinzufügen
3.2. Ich möchte Hotels aus dem System entfernen
3.3. Ich möchte die Informationen bestimmter Hotels
aktualisieren, z. B. den Namen, die Sterne usw.
4. Als Gast möchte ich ein Zimmer in einem bestimmten Hotel
buchen, um meinen Urlaub zu planen.
5. Als Gast möchte ich nach meinem Aufenthalt eine Rechnung
erhalten, damit ich einen Zahlungsnachweis habe.
Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.
6. Als Gast möchte ich meine Buchung stornieren, damit ich nicht
belastet werde, wenn ich das Zimmer nicht mehr benötige.
Hint: Sorgt für die entsprechende Invoice.
7. Als Gast möchte ich eine dynamische Preisgestaltung auf der
Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten
Preis buchen kann.
Hint: Wendet in der Hochsaison höhere und in der Nebensaison
niedrigere Tarife an.
8. Als Admin des Buchungssystems möchte ich alle Buchungen aller
Hotels sehen können, um eine Übersicht zu erhalten.
9. Als Admin möchte ich eine Liste der Zimmer mit ihrer
Ausstattung sehen, damit ich sie besser bewerben kann.
10. Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten,
z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu
aktualisieren, damit das Backend-System aktuelle Informationen
hat.
3
Hint: Stammdaten sind alle Daten, die nicht von anderen Daten
abhängen.

### User Stories mit DB-Schemaänderung

mindestens zwei der folgenden User Stories

1. Als Admin möchte ich alle Buchungen bearbeiten können, um
fehlende Informationen zu ergänzen (z.B. Telefonnummer).
2. Als Gast möchte ich auf meine Buchungshistorie zuzugreifen
("lesen"), damit ich meine kommenden Reservierungen verwalten
kann.
2.1. Die Anwendungsfälle für meine Buchungen sind
"neu/erstellen", "ändern/aktualisieren",
"stornieren/löschen".
3. Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für
ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.
4. Als Gast möchte ich vor der Buchung Hotelbewertungen lesen,
damit ich das beste Hotel auswählen kann.
5. Als Gast möchte ich für jeden Aufenthalt Treuepunkte sammeln,
die ich dann für Ermässigungen einlösen kann.
Hint: Nur häufige Gäste sollten Treuepunkte erhalten.
Definieren Sie eine Regel, um häufige Gäste zu identifizieren.
6. Als Gast möchte ich meine Buchung mit der von mir bevorzugten
Zahlungsmethode bezahlen, damit ich meine Reservierung
abschliessen kann.

### User Stories mit Datenvisualisierung

eine der folgenden User Stories 

1. Als Admin möchte ich die Belegungsraten für jeden Zimmertyp in
meinem Hotel sehen, damit ich weiss, welche Zimmer am
beliebtesten sind und ich meine Buchungsstrategien optimieren
kann.
Hint: Wählt ein geeignetes Diagramm, um die Auslastung nach
Zimmertyp darzustellen (z. B. wie oft jeder Zimmertyp gebucht
wird).
4
2. Als Admin möchte ich eine Aufschlüsselung der demografischen
Merkmale meiner Gäste sehen, damit ich gezieltes Marketing
planen kann.
Hint: Wählt ein geeignetes Diagramm, um die Verteilung der
Gäste nach verschiedenen Merkmalen darzustellen (z. B.
Altersspanne, Nationalität, wiederkehrende Gäste).
Möglicherweise müssen Sie der Tabelle „Gäste“ einige Spalten
hinzufügen.

### Optionale User Stories

1. Als Admin möchte ich die Gesamteinnahmen meines Hotels sehen,
damit ich die finanzielle Leistung des Hotels analysieren kann.
1.1. Zeigt die Gesamteinnahmen (Revenue) an, die sich aus
allen Buchungen für einen bestimmten Zeitraum ergeben.
1.2. Eine zeitliche Aufschlüsselung (z. B. Umsatz nach
Monat, Quartal, Jahr) bereitstellen.
Hint: Füge eine Trendlinie ein, um zu veranschaulichen,
wie sich die Einnahmen im Laufe der Zeit verändern.
2. Als Gastnutzer möchte ich die Details meiner Reservierung in
einer lesbaren Form erhalten (z.B. die Reservierung in einer
dauerhaften Datei speichern), damit ich meine Buchung später
überprüfen kann.
Hint: Erzeugt eine «booking.txt»-Datei oder verwendet die
Python-Bibliothek «fpdf» oder eine ähnliche Library, um eine
PDF-Version zu erzeugen.
3. Als Gastnutzer möchte ich eine Karte mit Zoom- und
Filterfunktion sehen können, welche Sehenswürdigkeiten oder
Restaurants in der Nähe meines gebuchten Hotels liegen, um
meine Aufenthaltsplanung zu erleichtern.
Hint: Verwende die Python-Bibliothek «geopandas» oder eine
ähnliche.
4. Als Gastnutzer möchte ich ein Zimmer buchen und eine
Buchungsbestätigung mit allen Details per E-Mail erhalten, um
einen verbindlichen Nachweis meiner Reservierung zu haben.
Hint: Verwende die Python-Bibliothek «smtplib» oder eine
ähnliche.

## Zusammenfassung Unterrichtseinheit 1 Iteration 1
In der ersten Unterrichtseinheit haben wir grundlegende Programmierkonzepte in Python kennengelernt und diese durch praktische Anwendungen vertieft. Ein zentraler Bestandteil war das **Input-Process-Output (IPO)-Modell**, das den Ablauf einer Anwendung in **Datenaufnahme (Input), Verarbeitung (Process) und Ausgabe (Output)** unterteilt. Dieses Modell haben wir direkt in unseren Übungen angewendet.
Wir haben eine **fiktive Musikdatenbank** erstellt, in der Musiktracks mit Variablen gespeichert wurden. Dabei haben wir unterschiedliche **Datentypen** kennengelernt, darunter Strings (*str*) für Namen und Kategorien sowie *float* für Preise. Mit der *type()*-Funktion konnten wir die Datentypen überprüfen.
Um die Daten für den Nutzer verständlich auszugeben, haben wir uns mit der *print()*-Funktion und **formatierten Strings (*f"..."*)** beschäftigt. Zusätzlich haben wir die **Benutzereingabe mit *input()*** integriert, sodass der Nutzer angeben konnte, wie viele Tracks er kaufen möchte. Basierend auf dieser Eingabe wurde der **Gesamtpreis berechnet**. 
Eine weitere wichtige Anwendung war die **Preisberechnung mit Rabatten**. Falls der Nutzer das gesamte Album kaufte, wurde automatisch ein **10 %-Rabatt** gewährt. Zudem haben wir gelernt, wie man **Dezimalzahlen formatiert** (*{:.2f}*), um Preise korrekt darzustellen.
Diese Übungen gaben uns einen ersten Einblick in die Entwicklung datengetriebener Anwendungen. Besonders wichtig war dabei, den Programmablauf durch **Debugging und Testen mit *print()*** besser zu verstehen.

## Zusammenfassung Unterrichtseinheit 1 Iteration 2
In der zweiten Unterrichtseinheit haben wir uns intensiv mit **Bedingungen und Geschäftslogik** in Python beschäftigt. Dabei haben wir gelernt, wie Programme mithilfe von *if*, *elif* und *else* unterschiedliche Entscheidungen treffen können, um dynamisch auf verschiedene Szenarien zu reagieren.
Die wichtigste Erkenntnis ist, dass Programme basierend auf Bedingungen verschiedene Aktionen ausführen können. Eine *if*-Bedingung prüft, ob eine Aussage wahr ist, und führt dann einen bestimmten Codeblock aus. Falls die Bedingung nicht zutrifft, greift *else* und es wird ein alternativer Code ausgeführt. Durch *elif* können mehrere Bedingungen nacheinander geprüft werden, um verschiedene Fälle zu unterscheiden. Diese Strukturen ermöglichen es, dass Programme flexibel auf unterschiedliche Situationen reagieren können, beispielsweise um nur digitale Musiktracks anzuzeigen.
Ein weiterer wichtiger Aspekt war die Kombination von Bedingungen mit Datenverarbeitung. In den Übungen haben wir geprüft, welche Musiktracks digital verfügbar sind, und nur diese angezeigt. Dabei haben wir auch gelernt, wie *or* und *and* genutzt werden, um Mehrfachbedingungen zu definieren. Dies ist besonders wichtig, wenn Programme komplexere Entscheidungen treffen sollen, beispielsweise ob mindestens eine oder mehrere Bedingungen erfüllt sein müssen.
Zusätzlich haben wir die **Interaktion mit Benutzern** durch *input()* kennengelernt. Damit kann ein Programm Eingaben vom Nutzer abfragen und darauf reagieren. Ein Beispiel dafür war die Entscheidung, ob ein Nutzer das gesamte Album kaufen möchte, wodurch ein Rabatt gewährt wurde. Falls der Nutzer nur einzelne Tracks kaufen wollte, wurde die Anzahl abgefragt und der Preis entsprechend berechnet. Dies zeigt, wie Programme mit Nutzern kommunizieren können, anstatt nur statische Daten auszugeben.
Unsere Übungen haben auch gezeigt, dass **Geschäftslogik** eine zentrale Rolle in der Programmierung spielt. Wir haben gelernt, wie man Regeln in Code umsetzt, zum Beispiel Rabatte berechnet, den Lagerbestand überprüft oder zwischen digitalen und physischen Medien unterscheidet. Diese Konzepte sind essenziell für reale Anwendungen, wie Online-Shops oder Buchungssysteme.
Ein weiteres wichtiges Konzept, das wir kennengelernt haben, war die **Verwendung von Tuples**. Tuples sind eine effiziente Möglichkeit, **unveränderliche Daten** zu speichern, da sie nicht nachträglich verändert werden können. Dies ist besonders nützlich für feste Datensätze, wie Album- oder Trackinformationen.

# Zusammenfassung Unterrichtseinheit 1 Iteration 3 

### Liste
- Im Gegensatz zu Tupeln sind Listen veränderbar, d.h. die Elemente in Listen können hinzugefügt, aktualisiert oder entfernt werden
- Liste in Listen
- Index/Element einer Liste beginnt mit 0
- Bei der Iteration in umgekehrter Reihenfolge können wir -1 als letztes Element in der Liste verwenden

### Hinzufügen, Entfernen, Aktualisieren und Löschen von Listenelementen
list.append(elem) -- fügt ein einzelnes Element an das Ende der Liste an. Häufiger Fehler: gibt nicht die neue Liste zurück, sondern ändert nur das Original.
list.insert(index, elem) -- fügt das Element am angegebenen Index ein, wobei Elemente nach rechts verschoben werden.
list.extend(list2) fügt die Elemente in list2 an das Ende der Liste an. Die Verwendung von + oder += auf eine Liste ist ähnlich wie die Verwendung von extend().
list.index(elem) -- sucht das angegebene Element am Anfang der Liste und gibt seinen Index zurück. Wirft einen ValueError, wenn das Element nicht vorkommt (verwenden Sie „in“, um ohne ValueError zu prüfen).
list.remove(elem) -- sucht nach der ersten Instanz des angegebenen Elements und entfernt es (wirft einen ValueError, wenn es nicht vorhanden ist)
list.reverse() -- kehrt die Liste an Ort und Stelle um (gibt sie nicht zurück)
list.pop(index) -- Entfernt das Element am angegebenen Index und gibt es zurück. Gibt das ganz rechte Element zurück, wenn index weggelassen wird (ungefähr das Gegenteil von append()).

### For-Schleife
- um ein Stück Code für eine bestimmte Anzahl von Iterationen zu wiederholen
- für jedes Element in einer Liste 
- eine Schleife mit einer Liste kombinieren eine Platzhaltervariable verwenden 
- einen passenden Variablennamen verwenden
- es wird bis zum letzten Element der Liste iteriert
- Die Platzhaltervariable enthält das Element der Liste
- Verwenden Sie range (), um die Anzahl der Iterationen anzugeben.

die Funktion variable.lower() wird verwendet, um die Zeichenkette in Kleinbuchstaben umzuwandeln
Durchsuchen einer Liste durch Vergleich der Benutzerauswahl mit dem entsprechenden Element in der Liste
Die Variable flag wird verwendet, um zu prüfen, ob das Element gefunden wurde oder nicht.
Verwenden Sie die Funktion len(), um die Anzahl der Titel in track_list anzuzeigen.
Verwenden Sie die „in“-Klausel, um Titel mit einem Teiltitel zu suchen.

### While-Schleife
 Eine while-Schleife wird oft verwendet, um einen Codeblock zu wiederholen, solange eine bestimmte Bedingung erfüllt ist
Bedingte Variable innerhalb der Schleife ändern 

 den booleschen Wert direkt als Variable X = y!= 5 setzen

### K.I.S.S. Principle
Keep It Simple, Stupid or Keep It Super Simple
Choosing unnecessarily complex solutions make it difficult for other people to understand and maintain the code

### Functions

- For modularity in code. They represent "actions" can be reused. 
- abstraction. 
- optional input parameters. 
- processing logic that corresponds to the action or the responsibility they fulfill. 
- functions may optionally return one or more values.
- function definition : def function_name(parameter_1, parameter_2, ...):
- function call.   executes what is defined in a function. function_name(parameter_1, parameter_2, ...)
- pass values from the function call to the function using arguments and parameters. 
- The value(s) generated by the function after processing can be returned to the processing block using the return statement. 
- The return statement without any value can be used to terminate the function and pass control back to the processing block.

readability, understandability and extendability
logical groupings 

### Errors and Exceptions

Python distinguishes between two types of problems in programming:
Errors: These are problems that cannot be interpreted by Python and prevent the program from starting. Errors commonly indicate that something is missing or incomplete in the code and needs to be corrected before running a program. For example:
SyntaxError - missing parentheses, missing colon in if/elif/else statements or for/while loops, missing required keywords like "in" in a for loop etc.
IndentationError - incorrect no. of spaces/tabs due to which Python cannot interpret blocks
NameError - Using variables before defining them, misspelled function names etc.
Exceptions: These are problems that occur when the program is running. When an exception is encountered, Python cannot continue the execution of the code and results in a code crash. Exceptions can be handled gracefully by adding the code that might potentially cause a problem inside the try-except block.
Python has the following syntax for handling exceptions:
try
except

# Zusammenfassung Unterrichtseinheit 2 Iteration 1

In dieser Unterrichtseinheit haben wir uns mit den Grundlagen von Object Oriented Programming (OOP) beschaeftigt. Wir haben gelernt, dass eine **class** ein Bauplan ist, in dem festgelegt wird, welche **attribute** (z. B. name, age, city) und **methoden** (z. B. eat(), sleep(), play()) ein Objekt besitzen soll. Eine **class** selbst fuehrt noch keinen Code aus, sondern dient als Vorlage fuer die Erstellung von **objects**. Ein **object** ist eine konkrete Instanz einer **class** mit eigenen Werten und kann die in der Klasse definierten **methoden** nutzen.

Ein zentrales Element ist der **__init__**-Konstruktor. Er wird automatisch ausgefuehrt, wenn ein Objekt erstellt wird, und dient zur Initialisierung der **attribute**. Der **self**-Parameter verweist dabei auf das aktuelle Objekt und ist notwendig, um innerhalb der Klasse auf die **attribute** und **methoden** zuzugreifen. Ohne **self** koennen innerhalb einer Methode keine objektbezogenen Daten verwendet werden.











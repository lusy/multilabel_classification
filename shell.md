## unique Labels der Dokumente ausgeben
```sh
cat dataset.csv | cut -f2 | tr "," "\n" | sort | uniq
```

## Labels mit Zeilennummer
```sh
cat dataset.csv | cut -f2 | tr "," "\n" | sort | uniq | nl -w1
```

## Header Zeile überspringen und unique Labels ausgeben
```sh
tail -n +2 dataset.csv | cut -f2 | tr "," "\n" | sort | uniq | nl -w1
```

## joinen von zwei Dateien die Labels und Topicverteilung enthalten
```sh
cut -f1,2 dataset_titles_sample.csv > dataset_labels.csv
```
```sh
join -t'    ' -1 1 -2 2 dataset_labels.csv doc_topics_sample.txt > topics_and_labels.csv
```

## Haufigkeit der Labelkombinationen
### | Header überspringen | nur die zweite Spalte mit den labels | sortieren | Häufigkeiten der Labelkombinationen zählen | nach Häufigkeit sortieren
```sh
cat dataset.csv | tail -n +2 | cut -f2 | sort | uniq -c | sort -nr
```

## Häufigkeiten der Labels 
### | Header überspringen | nur die 2te Spalte | Komma durch newline ersetzen | sortieren | zählen | nach Häufigkeit sortieren
```sh
cat dataset.csv | tail -n +2 | cut -f2 | sed 's/,/\n/g' | sort | uniq -c | sort -rn
```

## merge Titel und Abstract zur einer Spalte(Tab wir durch Space ersetzt)
```sh
cat dataset.csv | awk -F"\t" '{print $1"\t"$2"\t"$3"\t"$4" "$5}'
```

## topic model ins svmlight format bringen
### zuerst nur die IDs und Labels cutten | dann join mit Topic Models | Zeilen Zahl von Topic Models wegwerfeen | ins svmlight format bringen
```sh
cut -f1,2 dataset_titles.csv | join -t'    ' -1 1 -2 2 - results/doc-topics.txt | cut --complement -f3 | python ../src/doc_topics2svmlight_format.py
```

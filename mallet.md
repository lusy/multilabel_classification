# Vorverarbeitung des Datensatzes für Mallet
```bash
mallet/bin/mallet import-file --input data/data_titles.csv --output data/titles.mallet --remove-stopwords --keep-sequence
```

# Training von 50 Topics
```bash
mallet/bin/mallet train-topics --input data/titles.mallet --output-doc-topics data/result/doc-topics.txt --num-topics 50 --output-state data/topic-state.gz --num-iterations 100 --xml-topic-report data/report.xml
```

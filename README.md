# HEIG_ADS_Labo3

Pipelines



## Task 3

Command used: 

```bash
grep -o '\[[0-9]*/[A-Z][a-z]*/[0-9]*:[0-9]*:[0-9]*' ads_website.log | cut -d'/' -f1-2 | sort | uniq -c | tr -d  '[' | sed -e 's/^ *//;s/ /,/'> accesses.csv
```

To create the csv, I used python. it can be easily run by doing:

```bash
python3 script.py
```

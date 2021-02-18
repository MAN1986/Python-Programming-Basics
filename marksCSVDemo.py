import csv
# a student will fail if total marks are less than 5
with open('marks.csv','r') as f:
    r=csv.DictReader(f)
    r=list(r)
for rec in r:
    for k,v in rec.items():
        if(v=='A'):
            rec[k]=0
        if(v.replace('.','').isdigit()):
            rec[k]=float(v)
for rec in r:
    s=sum([rec['LA1'],rec['LA2'],rec['LA3'],rec['LA4']])
    rec['Total']=s
    del rec['LA1'],rec['LA2'],rec['LA3'],rec['LA4']
with open('Final.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=r[0].keys())
    w.writeheader()
    for rec in r:
        if(rec['Total']<5):
            w.writerow(rec)


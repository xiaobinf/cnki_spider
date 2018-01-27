import csv
#'http://dbpub.cnki.net/grid2008/dbpub/detail.aspx?dbcode=SCPD&dbname=SCPD2014&filename=CN103866401A'
patentUrl=[]
with open("urls.csv",'r') as f:
    reader=csv.reader(f)
    for row in reader:
        patentUrl.append('http://dbpub.cnki.net/grid2008/dbpub/detail.aspx?dbcode=SCPD&dbname=SCPD2014&filename='+"".join(row))

    print(patentUrl)

with open('patentUrls.csv','a') as w:
    writer=csv.writer(w)
    writer.writerow(patentUrl)
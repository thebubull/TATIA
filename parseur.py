import csv

columnsNames = ["WikiID", "FreebaseID", "Title", "Author", "Date", "Book genres","Summary"]

def parse():
    with open("data/data.csv",'w',encoding="utf-8",newline = '') as data:
        with open("booksummaries/booksummaries.txt",'r', encoding = "utf-8") as f_in:
            writer = csv.writer(data)
            writer.writerow(columnsNames)
            for line in f_in:
                L = []
                line = line.split('\t')
                L.append(line[0])
                L.append(line[1])
                L.append(line[2])
                L.append(line[3])
                L.append(line[4])
                L.append(line[5])
                L.append(line[6])
                writer.writerow(L)
            
parse()

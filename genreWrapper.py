import csv
import json

columnsNames = ["WikiID", "FreebaseID", "Title", "Author", "Date", "Book genres", "Summary"]
groups = {}


def read_groups():
    with open("groups.csv", 'r', encoding="utf-8", newline='') as inFile:
        csv_reader = csv.reader(inFile, delimiter=';')
        next(csv_reader, None)
        for row in csv_reader:
            groups[row[0]] = row[2]


def wrap():
    with open("data.csv", 'r', encoding="utf-8", newline='') as inFile:
        with open("data-test.csv", 'w', encoding="utf-8") as testFile:
            with open("data-grouped.csv", 'w', encoding="utf-8") as outFile:
                csv_reader = csv.reader(inFile, delimiter=',')
                next(csv_reader, None)
                test_writer = csv.writer(testFile, delimiter=',', lineterminator='\n')
                csv_writer = csv.writer(outFile, delimiter=',', lineterminator='\n')

                test_writer.writerow(columnsNames)
                csv_writer.writerow(columnsNames)
                for row in csv_reader:
                    if row[5]:
                        current_groups = []
                        genres = json.loads(row[5])
                        for genre in genres:
                            g = groups[genre]
                            current_groups.append(g) if ((g not in current_groups) and g != '') else current_groups
                        if len(current_groups) == 0:
                            row[5] = ''
                            test_writer.writerow(row)
                        else:
                            row[5] = ';'.join(current_groups)
                            csv_writer.writerow(row)
                    else:
                        test_writer.writerow(row)


read_groups()
wrap()

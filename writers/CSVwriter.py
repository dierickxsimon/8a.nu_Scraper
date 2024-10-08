import csv

class CSVwriter:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, data):
        fieldnames = data[0].keys()
        with open(self.filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator="\n")
            writer.writeheader()
            writer.writerows(data)
            
        print('file written to', self.filename)

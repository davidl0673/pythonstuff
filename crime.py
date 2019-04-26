import csv 
from string import punctuation
from collections import Counter
class SortCrime:
    def __init__(self):
        self.crime_years = {}
        self.crime_count = {}
        self.crimes = []
        self.yearcrimes = []
    def parse_crime(self, filename):    
        with open(filename) as f:
            f.readline()
            reader = csv.reader(f)
            for row in reader:
                crime = {
                    'offensetype': row[3],           
                    'yearcommited': row[1]
                }
                self.crimes.append(crime)

    def count(self):
        for crime in self.crimes:
            crime_type = crime['offensetype']
            if crime_type in self.crime_count:
                self.crime_count[crime_type] += 1 
            else:
                self.crime_count[crime_type] = 1 
    
    def count_by_year(self):
        for crime in self.crimes:
            year = crime['yearcommited'].split('/')[-1]
            if year in self.crime_years:
                self.crime_years[year] += 1 
            else:
                self.crime_years[year] = 1 
            

crime = SortCrime()
crime.parse_crime('crime.txt')
crime.parse_crime('crime2012.txt')
crime.parse_crime('crime2013.txt')
crime.parse_crime('crime2014.txt')


crime.count()

crime.count_by_year()
print(crime.crime_years)

counter = Counter(crime.crime_count)
least_common = counter.most_common()[:-1-1:-1] 
print('the most common crime was', counter.most_common(1))
print('the least common crime was',least_common) 

#use classes to encasulate the data

# rain data is gonna be very simular as well as count words 

#python.org had tons of answers the whole timeeeeeeee 
    


#simular to the count words lab
from datetime import datetime


with open('rain_data.txt') as f:
    rows = f.readlines()
    offset = 0
    for row in rows:
        offset += 1 
        row = row.strip()
        if set(row) == set('-'):
            break
    #get row list at index one and index two
   
    datapoints = []
    
    for row in rows[offset:]:
        row_list = row.split()

        #if row_list[1] == '-': other way you could go through that shit 
            #continue
        try:
            date = datetime.strptime(row_list[0], '%d-%b-%Y')
            data_point = {'date': date,  'total_rain': int(row_list[1])}
            datapoints.append(data_point)
        except ValueError:
            continue

    max_rain = max(datapoints, key= lambda day: day['total_rain'])
    print(max_rain)

yearly_rainfall = {}

for datapoint in datapoints:
    year = datapoint['date'].year
    if year in yearly_rainfall:
        yearly_rainfall[year] = yearly_rainfall[year] + datapoint['total_rain']
    else: 
        yearly_rainfall[year] = datapoint['total_rain']

print(yearly_rainfall.items())
    


print(yearly_rainfall) 
max_year_rain = max(yearly_rainfall.items(), key= lambda year:year[1])
print(max_year_rain)
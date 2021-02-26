import csv

cwb_filename = 'sample_input.csv'
data = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    for row in mycsv:
        data.append(row)
   
    stationid = ['C0A880','C0F9A0','C0G640','C0R190','C0X260']
    
    for j in range(5):
        target_data = list(filter(lambda item: item['station_id'] == stationid[j], data))
        num = len(target_data)
        MAX = -1

        for i in range(num):
            if float(target_data[i]['TEMP']) > float(MAX):
                MAX = target_data[i]['TEMP']
        if MAX == -1:
            result = [stationid[j],'NONE']
        else:
            result = [stationid[j], float(MAX)]
        
        stationid[j] = result
    
    print(stationid)
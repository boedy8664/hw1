# hw1
Add an csv file as input, in this code we have 107061231.csv as input.
In this code, it first create an empty list to save the data that we read in the csv file, called data.
And create another list that include the station id that we want to analyze.
Read the particular data that we want to analyze. For example, TEMP.
Then save it into a list called target_data
Set the determined condition(filter the data of '-99.000' and '-999.000') to get the maximum TEMP of the particular station id.
Save the result into the list that save the station id and print the result out.
To sum up, we choose the input csv file, and it will output the maximum TEMP of the particular station id.
result: [['C0A880', 26.6], ['C0F9A0', 30.3], ['C0G640', 29.1], ['C0R190', 29.4], ['C0X260', 30.3]]


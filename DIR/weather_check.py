import csv
with open("weather_data.csv",'r') as file:
    read_file=list(csv.reader(file))
user_input=input("Enter the city : ")
city_found = False
for row in read_file:
    if row[0]==user_input:
        print(f"The weather of the city {row[0]} is {row[1]}")
        city_found = True
if not city_found:
    print("City not found in the data")
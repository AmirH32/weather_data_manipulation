MONTHS = [
    ["January", 6, 3],
    ["February", 7, 3],
    ["March", 10, 4],
    ["April", 13,6],
    ["May", 17, 9],
    ["June", 20, 12],
    ["July", 22, 14],
    ["August", 21, 14],
    ["September", 19, 12],
    ["October", 14, 9],
    ["November", 10, 6],
    ["December", 7, 3]
    ]

# For expandability, I could read a plain text file and create a list of all items stored within it and then loop through this list to create a 2D list (given that the file is given in the desired format [month \n minimum temperature \n maximum temperature]) from which I can perform the rest of my program on



### Six months with the highest maximum temperatures ###

print("\n==========  The six hottest months are:  ==========\n")

hotMonths = sorted(MONTHS, key=lambda item : item[1])
# Sorts the MONTHS list using item[1] (the max temp) as the value to sort with

for i in range(-1, -7, -1):
    print(f"Month: {hotMonths[i][0]:11} Maximum temp: {str(hotMonths[i][1]):6} Minimum temp: {str(hotMonths[i][2])} ")



### Months with a minimum temperature below 9 ###

print("\n==========  Months with a minimum temperature below 9:  ==========\n")

low_minTemp = [i for i in MONTHS if i[2] < 9]
# Loops through month as i and stores i if the value of i[2] (min temp) is less than 9

sorted_low_minTemp = sorted(low_minTemp, key=lambda item : item[2], reverse = True)
# Sorts the low_minTemp list by the min temp item and then reverses the order

for month_stats in sorted_low_minTemp:
    print(f"Month: {month_stats[0]:11} Maximum temp: {str(month_stats[1]):6} Minimum temp: {str(month_stats[2])}") 



### Months with a maximum temperature above 20 ###

print("\n========== Months with a maximum temperature above 20: ==========\n")

high_maxTemp = [i for i in MONTHS if i[1] > 20]
# Loops through month as i and stores i if the value of i[1] (max temp) is greater than 20

sorted_high_maxTemp = sorted(high_maxTemp, key=lambda item : item[1], reverse = True)
# Sorts the high_maxTemp list by the max temp item and then reverses the order

for month_stats in sorted_high_maxTemp:
    print(f"Month: {month_stats[0]:11} Maximum temp: {str(month_stats[1]):6} Minimum temp: {str(month_stats[2])}") 
# I could turn this loop into a function to avoid repeating code    

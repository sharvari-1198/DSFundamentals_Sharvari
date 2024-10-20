# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:34:30 2024

@author: Sharvari
"""

# Function to parse the CSV file and return a list of dictionaries
def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Extract the header and data
    header = lines[0].strip().split(',')            #Splits the first line (header) by commas to get column names.
    data = [line.strip().split(',') for line in lines[1:]]      #Splits each subsequent line by commas to get data rows.
    
    data_dc = [{header[i]: row[i] for i in range(len(header))} for row in data] #converts each row into a dictionary with keys from the header
    #print(data_dc)
    return data_dc

#convert date string to a comparable tuple (year, month, day)
def convert_date(date_str):
    day, month, year = map(int, date_str.split('-'))        #Splits the date string by hyphens and converts the parts to integers.
    return (year, month, day)

# Function to calculate the average calories per day between the given dates
def calculate_average_calories(data, start_date, end_date):
    # Convert date strings to tuples
    start_date = convert_date(start_date)
    end_date = convert_date(end_date)
    
    # Filter data within the specified date range and calculate total calories
    total_calories = 0
    count = 0
    for entry in data:
        entry_date = convert_date(entry['Date'].strip())
        if start_date <= entry_date <= end_date:
            total_calories += int(entry['Calories'].strip())
            count += 1
    
    # Calculate average calories per day
    if count > 0:
        average_calories = total_calories / count
        return average_calories
    else:
        return None
    
def calc_standard_deviation(data, start_date, end_date):
    start_date = convert_date(start_date)
    end_date = convert_date(end_date)
    
    calories_list = []
    for entry in data:
        entry_date = convert_date(entry['Date'].strip())
        if start_date <= entry_date <= end_date:
            calories_list.append(int(entry['Calories'].strip()))
    
    if len(calories_list) > 1:
        mean = sum(calories_list) / len(calories_list)
        variance = sum((x - mean) ** 2 for x in calories_list) / (len(calories_list) - 1)
        standard_deviation = variance ** 0.5
        return standard_deviation
    else:
        return None
    
# Function to find the highest calories per day for each day within the specified date range
def highest_calories_per_day(data, start_date, end_date):
    start_date = convert_date(start_date)
    end_date = convert_date(end_date)
    
    daily_totals = {}
    for entry in data:
        entry_date = convert_date(entry['Date'].strip())
        if start_date <= entry_date <= end_date:
            if entry_date in daily_totals:
                daily_totals[entry_date] += int(entry['Calories'].strip())
            else:
                daily_totals[entry_date] = int(entry['Calories'].strip())
    
    if daily_totals:
        max_calories = max(daily_totals.values())
        return max_calories
    else:
        return None

# Function to find the highest calorie meal per day
def highest_calorie_meal(data, start_date, end_date):
    start_date = convert_date(start_date)
    end_date = convert_date(end_date)
    
    max_meal = 0
    for entry in data:
        entry_date = convert_date(entry['Date'].strip())
        if start_date <= entry_date <= end_date:
            meal_calories = int(entry['Calories'].strip())
            if meal_calories > max_meal:
                max_meal = meal_calories
    
    return max_meal if max_meal > 0 else None

    

def main():    
    file_path = "calories.csv"
    
    start_date = input("Enter start date (dd-mm-yyyy): ")
    end_date = input("Enter end date (dd-mm-yyyy): ")
    
    data = read_csv("calories.csv")
    
    average_calories = calculate_average_calories(data, start_date, end_date)
    standard_deviation = calc_standard_deviation(data, start_date, end_date)
    highest_calories = highest_calories_per_day(data, start_date, end_date)
    highest_meal = highest_calorie_meal(data, start_date, end_date)
    
    '''if average_calories:
        print(f'Average calories per day from {start_date} to {end_date}:')
        for date, avg_calories in average_calories.items():
            print(f'  Date: {date[2]:02d}-{date[1]:02d}-{date[0]}, Average Calories: {avg_calories:.2f}')
    else:
        print(f'No data available for the given date range.')'''
        
    if average_calories is not None:
        print(f'Average calories per day from {start_date} to {end_date}: {average_calories}')
    else:
        print(f'No data available for the given date range.')
    
    if standard_deviation is not None:
        print(f'Standard deviation of calories from {start_date} to {end_date}: {standard_deviation}')
    else:
        print(f'No data available for calculating standard deviation.')
    
    if highest_calories is not None:
        print(f'Highest calories per day from {start_date} to {end_date}: {highest_calories}')
    else:
        print(f'No data available for highest calories per day.')
        
    if highest_meal is not None:
        print(f'Highest calorie meal from {start_date} to {end_date}: {highest_meal}')
    else:
        print(f'No data available for highest calorie meal.')
    
    
if __name__ == "__main__":
    main()
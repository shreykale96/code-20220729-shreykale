"""BMI CALCULATOR PROGRAM LIBRARY
Order of Operations : 
load_dataset()
perform_cleanup()
calculate_bmi_parameters()
get_overweight_users()
export_results()

"""

import pandas as pd #loading Pandas library
import json #Loading Json library
import time

def load_dataset(file_name):
    """Loads the user specified JSON and returns the Pandas Data Frame of the loaded dataset. Pass the name of the file if in same
    directory or the location"""
    text = open(file_name,"r") #reading the test file 
    read_text = text.read()
    """ Try and Except block to read and load the JSON file without errors and asking to load correct file if errors found"""
    try:
        print('Attempting to read data')
        json_load = json.loads(read_text)
        print('Data Read Successfully')
        user_data = pd.DataFrame(json_load) #Loading the file into a DataFrame using Pandas
        return user_data
    except:
        print("Errors found while loading. Please check the dataset once and try again ")
    
    
    


def perform_cleanup(data_frame):
    """Function which cleans up Null Values and other semantic checks for the columns and returns the cleaned dataframe"""
    data_frame.replace("",float('NaN'),inplace=True) # replace empty values (" ") with NaN
    data_frame.replace(0,float('NaN'),inplace=True)
    data_frame.dropna(inplace=True) #Droping all Null values
    """ Proceeding to clean both all columns for any non-numeric values such as text 
        or special symbols etc in Weight and Height columns and for numeric values in Gender column"""
    print('\nStarting Data Cleanup\n')
    
    data_frame = data_frame[~data_frame['Gender'].str.isnumeric().replace(float('NaN'),True)] #Cleaing Gender column
    
    if data_frame['WeightKg'].dtype == 'O': #Cleaning Coulmn WeightKg for any non numeric values
        data_frame = data_frame[data_frame['WeightKg'].str.isnumeric().replace(float('NaN'),True)] #Cleaing WeightKg column

    if data_frame['HeightCm'].dtype == 'O': #Cleaning Coulmn HeightCm for any non numeric values
        data_frame = data_frame[data_frame['HeightCm'].str.isnumeric().replace(float('NaN'),True)] #Cleaing HightCm column
    
    data_frame[['HeightCm','WeightKg']] = data_frame[['HeightCm','WeightKg']].astype(float) #Type Casting Height and Weight to Float Values

    time.sleep(1)
    print('\nData Cleanup Complete\n')
    
    return data_frame #Returning the cleaned dataframe for BMI calculations

    


def health_risk(bmi_category):
    """Function which is being used to determine the Health Risks associated with the user specific BMI Category.
    Based on the BMI Category calculated(which are being passed to the function) the function will return the respected 
    Health Risk associated values : Malnutrition Risk, Low Risk, Enhanced Risk, Medium Risk, High Risk and Very High Risk"""
    
    if bmi_category == "Underweight":
        return "Malnutrition Risk"
    elif bmi_category == "Normal Weight":
        return "Low Risk"
    elif bmi_category == "Overweight":
        return "Enhanced Risk"
    elif bmi_category == "Moderately Obese":
        return "Medium Risk"
    elif bmi_category == "Severely Obese":
        return "High Risk"
    else:
         return "Very High Risk"
    

def bmi_category(bmi):
    """Function which is being used to determine the BMI Cateogry of the user based on the BMI values calculated. This will
        retun the BMI Cateogry based on the BMI Value which are : Underweight, Normal Weight, Overweight, Moderately Obese,
        Severely Obese and Very Severely Obese"""
    
    if bmi <= 18.4:
        return "Underweight"
    elif bmi >= 18.5 and bmi <=24.9:
        return "Normal Weight"
    elif bmi >= 25 and bmi <=29.9:
        return "Overweight"
    elif bmi >= 30 and bmi <= 34.9:
        return "Moderately Obese"
    elif bmi >= 35 and bmi <= 39.9:
        return "Severely Obese"
    else:
         return "Very Severely Obese"

def calculate_bmi_parameters(data_frame):
    """Function which is being used to calculate the BMI Values from the formula : BMI(kg/m^2) = mass(kg) / height(m)^2
    Along with BMI Values, BMI Category and Health Risk values are also being populated with the use of BMI Values.
    Pass the dataframe to calculate the bmi parameters"""
    print('\nCalculating BMI Parameters such as BMI, BMI Category and Health Risk\n')
    time.sleep(2)
    print('\nCalculating BMI Values\n')
    data_frame['BMI'] = round((data_frame['WeightKg'] / ((data_frame["HeightCm"]/100)**2)),1) #Rouding off to nearest 1 decimal place
    time.sleep(2)
    print('\nDone!\n')
    time.sleep(1)
    print('\nCalculating BMI Categories\n')
    data_frame['BMI Category'] = data_frame["BMI"].apply(bmi_category) #Calculating BMI Category
    time.sleep(2)
    print('\nDone!\n')
    print('\nCalculating Health Risk\n')
    data_frame['Health Risk'] = data_frame['BMI Category'].apply(health_risk) #Calculating Health Risk
    time.sleep(1)
    print('\nDone!\n')
    time.sleep(1)
    print('\nAll Calculations Complete\n')

def get_overweight_users(data_frame): #Function to get the value count of overweight users
    """Pass the dataframe and it prints the Number of Overweight Users in the dataset"""
    print('\n Calculating Overweight Users')
    time.sleep(1)
    over_weight_users = data_frame['BMI Category'].str.count('Overweight').sum() #Calculates the overweight users
    time.sleep(2)
    print("\n\nOverweight Users from the dataset : {}\n\n".format(over_weight_users))

def export_results(data_frame):
    """Exports the results of the data in a excel sheet for further viewing and analysis"""
    print('\nExporting Dataset\n')	
    data_frame.to_excel('BMI Calculations.xlsx',index=False)
    time.sleep(2)
    print('\nExport Complete')

if __name__ == '__main__':
    user_data = load_dataset('test data.json')
    time.sleep(2)
    print('\nPerforming Cleanup of Data')
    user_data = perform_cleanup(user_data)
    time.sleep(1)
    print('\nClean up Done')
    time.sleep(1)
    print('\nCalculating BMI Parameters')
    calculate_bmi_parameters(user_data)
    time.sleep(2)
    print('\nBMI Parameters Generated')
    time.sleep(2)
    print('\nGetting Overweight User Data')
    get_overweight_users(user_data)
    print('\nExporting Results')
    export_results(user_data)
    time.sleep(2)
    print('\nExport Successful')

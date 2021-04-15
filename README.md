# TelGer
An application made with Python that manages all the complex sales that encounter telecom distributors. 
Multiple frameworks are used such as Kivy for GUI, OpenPyXl for xlsx files, json to store and load the data..etc.
It shows you how many of each product you have and it stores the price and the existing amount of each product and solved the problem of not knowing what have been selled by forcing the user to enter all prices to be stored then the user (distributor) can add each sale to be calculated and added to .xlsx file in a proper way that can be accessed any time later. the directory that contains the xlsx files is in the following format: storage/(current_year)/(current_month)/(current_day).xlsx
if the application runs multiple times in a single day then it will only load the file and won't create new file unless it's the first time opened in the day.

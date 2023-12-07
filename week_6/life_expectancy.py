with open('week_6/life_expectancy.csv') as life_exectancy_data:
    choices = ["Record High" , "Record Low", "Record in Specific Year", "Record for Specific Country"]
    def pick_choice():
        for i, choice in enumerate(choices):
            print(f"{i + 1} - {choice}")
        return int(input("Which action would you like to use? "))

        
    
    
    
    for data in life_exectancy_data:
        data = data.strip()
        data = data.split(",")
        country = data[0]
        country_code = data[1]
        year = data[2]
        life_expectancy = data [3]

    
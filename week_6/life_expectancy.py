#made a loop to keep requesting more information until quit. Have the min/max/average for a country, and the min/max/average for a year. I also included the largest increase/decrease worldwide, and also for a specific country.
with open('week_6/life_expectancy.csv') as life_exectancy_file:
    life_expectancy_data = life_exectancy_file.readlines()

    choices = ["Record High", "Record Low", "Record High in Specific Year", "Record Low in Specific Year","Record High for Specific Country", "Record Low for Specific Country", "Country Stats", "Year Stats", "Biggest Drop Worldwide", "Biggest Gain Worldwide", "Biggest Drop Specific Country", "Biggest Gain Specific Country", "Quit"]
    country_code_list = [('AFG', 'Afghanistan'), ('', 'Africa'), ('ALB', 'Albania'), ('DZA', 'Algeria'), ('ASM', 'American Samoa'), ('AND', 'Andorra'), ('AGO', 'Angola'), ('AIA', 'Anguilla'), ('ATG', 'Antigua and Barbuda'), ('ARG', 'Argentina'), ('ARM', 'Armenia'), ('ABW', 'Aruba'), ('AUS', 'Australia'), ('AUT', 'Austria'), ('AZE', 'Azerbaijan'), ('BHS', 'Bahamas'), ('BHR', 'Bahrain'), ('BGD', 'Bangladesh'), ('BRB', 'Barbados'), ('BLR', 'Belarus'), ('BEL', 'Belgium'), ('BLZ', 'Belize'), ('BEN', 'Benin'), ('BMU', 'Bermuda'), ('BTN', 'Bhutan'), ('BOL', 'Bolivia'), ('BES', 'Bonaire Sint Eustatius and Saba'), ('BIH', 'Bosnia and Herzegovina'), ('BWA', 'Botswana'), ('BRA', 'Brazil'), ('VGB', 'British Virgin Islands'), ('BRN', 'Brunei'), ('BGR', 'Bulgaria'), ('BFA', 'Burkina Faso'), ('BDI', 'Burundi'), ('KHM', 'Cambodia'), ('CMR', 'Cameroon'), ('CAN', 'Canada'), ('CPV', 'Cape Verde'), ('CYM', 'Cayman Islands'), ('CAF', 'Central African Republic'), ('TCD', 'Chad'), ('OWID_CIS', 'Channel Islands'), ('CHL', 'Chile'), ('CHN', 'China'), ('COL', 'Colombia'), ('COM', 'Comoros'), ('COG', 'Congo'), ('COK', 'Cook Islands'), ('CRI', 'Costa Rica'), ('CIV', "Cote d'Ivoire"), ('HRV', 'Croatia'), ('CUB', 'Cuba'), ('CUW', 'Curacao'), ('CYP', 'Cyprus'), ('CZE', 'Czech Republic'), ('COD', 'Democratic Republic of Congo'), ('DNK', 'Denmark'), ('DJI', 'Djibouti'), ('DMA', 'Dominica'), ('DOM', 'Dominican Republic'), ('ECU', 'Ecuador'), ('EGY', 'Egypt'), ('SLV', 'El Salvador'), ('GNQ', 'Equatorial Guinea'), ('ERI', 'Eritrea'), ('EST', 'Estonia'), ('ETH', 'Ethiopia'), ('FRO', 'Faeroe Islands'), ('FLK', 'Falkland Islands'), ('FJI', 'Fiji'), ('FIN', 'Finland'), ('FRA', 'France'), ('GUF', 'French Guiana'), ('PYF', 'French Polynesia'), ('GAB', 'Gabon'), ('GMB', 'Gambia'), ('GEO', 'Georgia'), ('DEU', 'Germany'), ('GHA', 'Ghana'), ('GIB', 'Gibraltar'), ('GRC', 'Greece'), ('GRL', 'Greenland'), ('GRD', 'Grenada'), ('GLP', 'Guadeloupe'), ('GUM', 'Guam'), ('GTM', 'Guatemala'), ('GIN', 'Guinea'), ('GNB', 'Guinea-Bissau'), ('GUY', 'Guyana'), ('HTI', 'Haiti'), ('HND', 'Honduras'), ('HKG', 'Hong Kong'), ('HUN', 'Hungary'), ('ISL', 'Iceland'), ('IND', 'India'), ('IDN', 'Indonesia'), ('IRN', 'Iran'), ('IRQ', 'Iraq'), ('IRL', 'Ireland'), ('IMN', 'Isle of Man'), ('ISR', 'Israel'), ('ITA', 'Italy'), ('JAM', 'Jamaica'), ('JPN', 'Japan'), ('JOR', 'Jordan'), ('KAZ', 'Kazakhstan'), ('KEN', 'Kenya'), ('KIR', 'Kiribati'), ('KWT', 'Kuwait'), ('KGZ', 'Kyrgyzstan'), ('LAO', 'Laos'), ('LVA', 'Latvia'), ('LBN', 'Lebanon'), ('LSO', 'Lesotho'), ('LBR', 'Liberia'), ('LBY', 'Libya'), ('LIE', 'Liechtenstein'), ('LTU', 'Lithuania'), ('LUX', 'Luxembourg'), ('MAC', 'Macao'), ('MKD', 'Macedonia'), ('MDG', 'Madagascar'), ('MWI', 'Malawi'), ('MYS', 'Malaysia'), ('MDV', 'Maldives'), ('MLI', 'Mali'), ('MLT', 'Malta'), ('MHL', 'Marshall Islands'), ('MTQ', 'Martinique'), ('MRT', 'Mauritania'), ('MUS', 'Mauritius'), ('MYT', 'Mayotte'), ('MEX', 'Mexico'), ('FSM', 'Micronesia (country)'), ('MDA', 'Moldova'), ('MCO', 'Monaco'), ('MNG', 'Mongolia'), ('MNE', 'Montenegro'), ('MSR', 'Montserrat'), ('MAR', 'Morocco'), ('MOZ', 'Mozambique'), ('MMR', 'Myanmar'), ('NAM', 'Namibia'), ('NRU', 'Nauru'), ('NPL', 'Nepal'), ('NLD', 'Netherlands'), ('NCL', 'New Caledonia'), ('NZL', 'New Zealand'), ('NIC', 'Nicaragua'), ('NER', 'Niger'), ('NGA', 'Nigeria'), ('NIU', 'Niue'), ('PRK', 'North Korea'), ('MNP', 'Northern Mariana Islands'), ('NOR', 'Norway'), ('OMN', 'Oman'), ('PAK', 'Pakistan'), ('PLW', 'Palau'), ('PSE', 'Palestine'), ('PAN', 'Panama'), ('PNG', 'Papua New Guinea'), ('PRY', 'Paraguay'), ('PER', 'Peru'), ('PHL', 'Philippines'), ('POL', 'Poland'), ('PRT', 'Portugal'), ('PRI', 'Puerto Rico'), ('QAT', 'Qatar'), ('REU', 'Reunion'), ('ROU', 'Romania'), ('RUS', 'Russia'), ('RWA', 'Rwanda'), ('SHN', 'Saint Helena'), ('KNA', 'Saint Kitts and Nevis'), ('LCA', 'Saint Lucia'), ('MAF', 'Saint Martin (French part)'), ('SPM', 'Saint Pierre and Miquelon'), ('VCT', 'Saint Vincent and the Grenadines'), ('WSM', 'Samoa'), ('SMR', 'San Marino'), ('STP', 'Sao Tome and Principe'), ('SAU', 'Saudi Arabia'), ('SEN', 'Senegal'), ('SRB', 'Serbia'), ('SYC', 'Seychelles'), ('SLE', 'Sierra Leone'), ('SGP', 'Singapore'), ('SXM', 'Sint Maarten (Dutch part)'), ('SVK', 'Slovakia'), ('SVN', 'Slovenia'), ('SLB', 'Solomon Islands'), ('SOM', 'Somalia'), ('ZAF', 'South Africa'), ('KOR', 'South Korea'), ('SSD', 'South Sudan'), ('ESP', 'Spain'), ('LKA', 'Sri Lanka'), ('SDN', 'Sudan'), ('SUR', 'Suriname'), ('SWZ', 'Swaziland'), ('SWE', 'Sweden'), ('CHE', 'Switzerland'), ('SYR', 'Syria'), ('TWN', 'Taiwan'), ('TJK', 'Tajikistan'), ('TZA', 'Tanzania'), ('THA', 'Thailand'), ('TLS', 'Timor'), ('TGO', 'Togo'), ('TKL', 'Tokelau'), ('TON', 'Tonga'), ('TTO', 'Trinidad and Tobago'), ('TUN', 'Tunisia'), ('TUR', 'Turkey'), ('TKM', 'Turkmenistan'), ('TCA', 'Turks and Caicos Islands'), ('TUV', 'Tuvalu'), ('UGA', 'Uganda'), ('UKR', 'Ukraine'), ('ARE', 'United Arab Emirates'), ('GBR', 'United Kingdom'), ('USA', 'United States'), ('VIR', 'United States Virgin Islands'), ('URY', 'Uruguay'), ('UZB', 'Uzbekistan'), ('VUT', 'Vanuatu'), ('VAT', 'Vatican'), ('VEN', 'Venezuela'), ('VNM', 'Vietnam'), ('WLF', 'Wallis and Futuna'), ('ESH', 'Western Sahara'), ('OWID_WRL', 'World'), ('YEM', 'Yemen'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')]
    record_low = 150
    record_high = 0
    country_data = []
    year_data = []
    record_low_country = ""
    record_high_country = ""
    record_high_year = ""
    record_low_year = ""
    record_high_country_code = ""
    record_low_country_code = ""
    country_code = ''
    user_choice_year = " "
    user_choice_country = " "
    largest_drop = None
    largest_gain = None
    country_with_largest_drop = None
    country_with_largest_gain = None
    
    def pick_choice():
        while True:
            for i, choice in enumerate(choices):
                print(f"{i + 1} - {choice}")
            user_input = input("Which action would you like to use? ")
            if user_input.isdigit() and 1 <= int(user_input) <= len(choices):
                return int(user_input)
            else:
                print("Invalid input. Please enter a valid choice.")

                

    user_action = pick_choice()   

    while user_action != len(choices) +1 :    
        choices = ["Record High" , "Record Low", "Record High in Specific Year", "Record Low in Specific Year", "Record High for Specific Country", "Record Low for Specific Country", "Quit"]
        
        #record high
        if user_action == 1:
            for data in life_expectancy_data:
                data = data.strip()
                data = data.split(",")
                country = data[0]
                country_code = data[1]
                year = data[2]
                life_expectancy = float(data[3])
                if life_expectancy > record_high:
                    record_high = life_expectancy
                    record_high_country = country
                    record_high_year = year
                    record_high_country_code = country_code
            print(f"The record high was {record_high_country} ({record_high_country_code}) in {record_high_year}, with a life expectancy of {record_high:.2f} years.)")

        #record low
        if user_action == 2:
            for data in life_expectancy_data:
                data = data.strip()
                data = data.split(",")
                country = data[0]
                country_code = data[1]
                year = data[2]
                life_expectancy = float(data[3])
                if life_expectancy < record_low:
                    record_low = life_expectancy
                    record_low_country = country
                    record_low_year = year
                    record_low_country_code = country_code
            print(f"The record low was {record_low_country} ({record_low_country_code}) in {record_low_year}, with a life expectancy of {record_low:.2f} years.)")
        
        #record high for year
        if user_action == 3:
            user_choice_year = int(input("Enter a year, and I'll retrieve the country with the highest life expectancy. Please only use 4 digit year format. "))
            for data in life_expectancy_data:
                data = data.strip()
                data = data.split(",")
                country = data[0]
                country_code = data[1]
                year = int(data[2])
                life_expectancy = float(data[3])
                if year == user_choice_year and life_expectancy > record_high:
                    record_high = life_expectancy
                    record_high_country = country
            if record_high != 0:
            
                print(f"In {user_choice_year}, {record_high_country} had the highest life expectancy at {record_high:.2f} years.")
            else:
                print("No data found for that year.")

        #record low for year
        if user_action == 4:
            user_choice_year = int(input("Enter a year, and I'll retrieve the country with the lowest life expectancy. Please only use 4 digit year format. "))
            for data in life_expectancy_data:
                data = data.strip()
                data = data.split(",")
                country = data[0]
                country_code = data[1]
                year = int(data[2])
                life_expectancy = float(data[3])
                if year == user_choice_year and life_expectancy < record_low:
                    record_low = life_expectancy
                    record_low_country = country
            if record_low != 150:
                print(f"In {user_choice_year}, {record_low_country} had the lowest life expectancy at {record_low:.2f} years.")
            else:
                print("No data found for that year.")

        

        #record high for country
        if user_action == 5:
            need_abbreviation_list = input("Do you need to see the country abbreviation list? It is very long, but you'll need it to look up country. Type Y or N: ").upper()
            if need_abbreviation_list == "Y":
                print(country_code_list)
            else:
                print("Great!")
            user_choice_country_abbreviation = input("Please type in the three letter code for the country to see the year it had it's highest life expectancy. ").upper()
            if any(user_choice_country_abbreviation == code for code, _ in country_code_list):
                for data in life_expectancy_data:
                    data = data.strip()
                    data = data.split(",")
                    country = data[0]
                    country_code = data[1]
                    year = int(data[2])
                    life_expectancy = float(data[3])
                    if country_code == user_choice_country_abbreviation and life_expectancy > record_high:
                        record_high_year = year
                        record_high = life_expectancy
                        user_choice_country = country
                print(f"{user_choice_country} had their highest life expectancy in {record_high_year}, at {record_high:.2f} years.")
            else:
                print("Your choice doesn't match any countries on file.")
        


        #record low for country
        if user_action == 6:
            need_abbreviation_list = input("Do you need to see the country abbreviation list? It is very long, but you'll need it to look up country. Type Y or N: ").upper()
            if need_abbreviation_list == "Y":
                print(country_code_list)
            else:
                print("Great!") 
            user_choice_country_abbreviation = input("Please type in the three letter code for the country to see the year it had it's highest life expectancy. ").upper()
            if any(user_choice_country_abbreviation == code for code, _ in country_code_list): 
        
                for data in life_expectancy_data:
                    data = data.strip()
                    data = data.split(",")
                    country = data[0]
                    country_code = data[1]
                    year = int(data[2])
                    life_expectancy = float(data[3])
                    if country_code == user_choice_country_abbreviation and life_expectancy < record_low:
                        record_low = life_expectancy
                        user_choice_country = country
                        record_low_year = year
                print(f"{user_choice_country} had its lowest life expectancy in {record_low_year}, at {record_low:.2f} years.")
            else:
                print("No country with that code is on file.") 

        #country stats
        if user_action == 7:
            need_abbreviation_list = input("Do you need to see the country abbreviation list? It is very long, but you'll need it to look up country. Type Y or N: ").upper()
            if need_abbreviation_list == "Y":
                print(country_code_list)
            else:
                print("Great!") 
            user_choice_country_abbreviation = input("Please type in the three letter code for the country to see the year it had it's highest life expectancy. ").upper()
            if any(user_choice_country_abbreviation == code for code, _ in country_code_list): 
        
                for data in life_expectancy_data:
                    data = data.strip()
                    data = data.split(",")
                    country = data[0]
                    country_code = data[1]
                    year = int(data[2])
                    life_expectancy = float(data[3])
                    if country_code == user_choice_country_abbreviation:
                        user_choice_country = country
                        country_data.append(life_expectancy)
                        total = sum(country_data)
                        country_average = total / len(country_data)
                        if life_expectancy > record_high:
                            record_high = life_expectancy
                            record_high_year = year
                        if life_expectancy < record_low:
                            record_low = life_expectancy
                            record_low_year = year
                print(f"{user_choice_country}:")
                print(f"Average life span: {country_average}. Worst on record: {record_low:.2f} years in {record_low_year} years. Best on record: {record_high:.2f} in {record_high_year}.")
                        

        #year stats    
        if user_action == 8:
            user_choice_year = int(input("Please enter a year to see the lowest, highest, and average life span of that year. Please use only four digit year format. "))
            for data in life_expectancy_data:
                data = data.strip()
                data = data.split(",")
                country = data[0]
                country_code = data[1]
                year = int(data[2])
                life_expectancy = float(data[3])
                if year == user_choice_year:
                    year_data.append(life_expectancy)
                    total = sum(year_data)
                    year_average = total / len(year_data)
                    if life_expectancy > record_high:
                        record_high = life_expectancy
                        record_high_country = country
                        record_high_country_code = country_code
                    if life_expectancy < record_low:
                        record_low = life_expectancy
                        record_low_country = country
                        record_high_country_code = country_code
            print(f"In {user_choice_year}")
            print(f"{record_high_country} ({record_high_country_code}) had the highest life expectancy at {record_high:.2f} years. {record_low_country} had the losest, at {record_low:.2f} years. The worldwide average for that year was {year_average:.2f} years.")

        #drop worldwide
        if user_action == 9:
            for data in life_expectancy_data:
                data = data.strip()
                data = data.split(",")
                country = data[0]
                country_code = data[1]
                year = int(data[2])
                life_expectancy = float(data[3])
                stored_country = country
                stored_year = year
                stored_life_expectancy = life_expectancy
                largest_drop = 0
                if country == stored_country:
                    difference = stored_life_expectancy - life_expectancy
                    if difference > largest_drop:
                        largest_drop = difference
                        country_with_largest_drop = country
                        year_with_largest_drop = year
                        life_expectancy_before_drop = life_expectancy
                else:
                    stored_country = country        
                    difference = stored_life_expectancy - life_expectancy
                    if difference > largest_drop:
                        largest_drop = difference
                        country_with_largest_drop = country
                        year_with_largest_drop = year
                        life_expectancy_before_drop = life_expectancy
            
            print(f"The country that had the most dramatic drop in life expectancy was {country_with_largest_drop}, from {year_with_largest_drop} to {year_with_largest_drop + 1}, with a drop of {largest_drop} years.")
        #gain worldwide
        if user_action == 10:
            for data in life_expectancy_data:
                data = data.strip()
                data = data.split(",")
                country = data[0]
                country_code = data[1]
                year = int(data[2])
                life_expectancy = float(data[3])
                stored_country = country
                stored_year = year
                stored_life_expectancy = life_expectancy
                largest_gain = 150
                if country == stored_country:
                    difference = stored_life_expectancy - life_expectancy
                    if difference < largest_gain:
                        largest_gain = difference
                        country_with_largest_gain = country
                        year_with_largest_gain = year
                        life_expectancy_before_gain = life_expectancy
                else:
                    stored_country = country        
                    difference = stored_life_expectancy - life_expectancy
                    if difference < largest_gain:
                        largest_gain = difference
                        country_with_largest_gain = country
                        year_with_largest_gain = year
                        life_expectancy_before_gain = life_expectancy
                largest_gain_absolute = abs(largest_gain)
                print(f"The country with the largest gain in life expectancy was {country_with_largest_gain}. Between year {year_with_largest_gain} and {year_with_largest_gain + 1}, there was an increase in life expectancy of {largest_gain_absolute} years.")

        #drop country
        if user_action == 11:
            need_abbreviation_list = input("Do you need to see the country abbreviation list? It is very long, but you'll need it to look up country. Type Y or N: ").upper()
            if need_abbreviation_list == "Y":
                print(country_code_list)
            else:
                print("Great!") 
            user_choice_country_abbreviation = input("Please type in the three letter code for the country to see the year it had it's highest life expectancy. ").upper()
            if any(user_choice_country_abbreviation == code for code, _ in country_code_list):
                largest_drop = 0
                for data in life_expectancy_data:
                    data = data.strip()
                    data = data.split(",")
                    country = data[0]
                    country_code = data[1]
                    year = int(data[2])
                    life_expectancy = float(data[3])
                    stored_year = year
                    user_choice_country = country
                    stored_life_expectancy = life_expectancy
                    difference = stored_life_expectancy - life_expectancy
                    if difference > largest_drop:
                        largest_drop = difference
                        year_with_largest_drop = year

            print(f"In {user_choice_country}, the largest drop in life expectancy occured between {year_with_largest_drop} and {year_with_largest_drop + 1}, and fell {largest_drop} years.")
            

        #gain country
        if user_action == 12:
            need_abbreviation_list = input("Do you need to see the country abbreviation list? It is very long, but you'll need it to look up country. Type Y or N: ").upper()
            if need_abbreviation_list == "Y":
                print(country_code_list)
            else:
                print("Great!") 
            user_choice_country_abbreviation = input("Please type in the three letter code for the country to see the year it had it's highest life expectancy. ").upper()
            if any(user_choice_country_abbreviation == code for code, _ in country_code_list):
                for data in life_expectancy_data:
                    data = data.strip()
                    data = data.split(",")
                    country = data[0]
                    country_code = data[1]
                    year = int(data[2])
                    life_expectancy = float(data[3])
                    stored_year = year
                    largest_gain = 150
                    stored_life_expectancy = life_expectancy
                    difference = stored_life_expectancy - life_expectancy
                    if difference < largest_gain:
                        largest_gain = difference
                        year_with_largest_gain = year
                    absolute_gain = abs(largest_gain)

            print(f"In {user_choice_country}, the largest gain in life expectancy occured between {year_with_largest_gain} and {year_with_largest_gain + 1}, and increased {absolute_gain} years.")



        record_low = 150
        record_high = 0
        record_low_country = ""
        record_high_country = ""
        record_high_year = ""
        record_low_year = ""
        record_high_country_code = ""
        record_low_country_code = ""
        country_code = ''
        user_choice_year = " "
        user_choice_country = " "   
        
        user_action = pick_choice()
    print("Goodbye!")
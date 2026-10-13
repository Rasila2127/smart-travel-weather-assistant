from utils import country_info
from difflib import SequenceMatcher
from test_api import get_country,get_all_countries,get_weather
from storage import saved_destinations,updated_json


countries=get_all_countries()
# city=get_weather("New Delhi")
# weather_info(city)

while True:
    print("==================================")
    print("* SMART-TRAVEL-WEATHER-ASSISTANT *")
    print("*----------Main Menu-------------*")
    print("*      1. Search Country         *")
    print("*      2. Saved Destinations     *")
    print("*      3. Exit                   *")
    print("==================================")
    
    choice=int(input("enter your choice (1/2/3):"))
    if choice==1:
        c_name=input("Enter Country name:")

        suggestions=[]
        
        found=False
        for country in countries:
            country_name=country["name"]
            if c_name.lower()==country_name.lower():
                found=True
                country_info(country)


        
        if not found:
            print("Country not found")
            print("Did you mean:")
            for country in countries:
                similarity = SequenceMatcher(None, c_name.lower(), country["name"].lower()).ratio()
                suggestions.append((country["name"], similarity))
            sorted_suggestions=sorted(suggestions,reverse=True,key=lambda x:x[1])
            top_suggestions=sorted_suggestions[:3]
                           
            for i,suggestion in enumerate(top_suggestions):
                print(f"{i+1}. {suggestion[0]}")
            print("0. Back")
            while True:
                try:
                    select=int(input("enter choice(0-3):"))
                    if select==0:
                        break
                    
                    elif 1<=select <=len(top_suggestions):
                        selected=top_suggestions[select-1]
                        selected_country=selected[0]
                        for country in countries:
                            if country["name"]==selected_country:
                                country_info(country)
                                break
                        break
                
                    
                    else:
                        print(" Please enter an integer between 1 to ",len(top_suggestions))        
                except ValueError:
                    print("Invalid input! Please enter integer value.")
                    
        
    elif choice==2:
        saved=saved_destinations() 
        back_to_main=False
        while True:
            
            if not saved:
                print("no destination saved yet!!")
                while True:
                    try:
                        back=int(input("Enter 0 to back: "))
                        if back==0:
                            break
                        else:
                            print("Please enter 0")
                    except ValueError:
                        print("Please enter 0")
                if back==0:
                    break
                
                

            else:
                if back_to_main:
                    break
                for i,dictionary in enumerate(saved):
                    print("==============================")
                    print(f"    Destination no:",i+1)
                    print("------------------------------")
                    print("country:",dictionary["country"])
                    print("capital:",dictionary["capital"])
                    print("currency:",dictionary["currency"])
                    print("flag:",dictionary["flag"])
                    print("==============================")

                print("1. Back")
                print("2. Delete")

                
            
                while True:
                    try:
                        
                        d_or_b=int(input("wants to delete or back?"))
                        if d_or_b==1:
                            back_to_main=True
                            break 
                        elif d_or_b== 2:

                            while True:
                                try:
                                    dest_number=int(input("Enter destination number to delete:"))
                                    if 1<= dest_number<=len(saved):
                                        dest_delete=saved[dest_number-1]
                                        saved.remove(dest_delete)
                                        updated_json(saved)
                                        print("Destination deleted successfully!!")
                                        break
                                    else:
                                        print("Please enter valid number")
                                except ValueError:
                                    print("Please enter a valid integer!!")
                            break
                        else:
                            print("Please enter number 1 or 2 !!")
                    except ValueError:    
                        print("Please enter valid input!!")
                
    elif choice==3:
        print("You exit successfully!!")
        break


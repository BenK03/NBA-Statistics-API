# Imports
import requests
from Linked_List import List

base_url = 'http://rest.nbaapi.com/api/PlayerDataAdvanced/name/'

players_stats = List()
print("| Compare Current NBA Players |")

def get_name(): 
    firstname = input("What is the players first name?: ")
    lastname = input("What is the players last name?: ")
    firstname = firstname.capitalize()
    lastname = lastname.capitalize()
    
    fullname = f"{firstname}%20{lastname}"
    return fullname       

def get_nba_player(name):
    url = f"{base_url}{name}"
    response = requests.get(url)

    # if response code is good insert player statistics into linked list
    if response.status_code == 200:
        stats = response.json()
        players_stats.insert(100, stats)
        ans = input("Would you like to compare another player?(Y/N): ")
        
        # recall functions if they answer "Y"
        if ans == "Y":
            fullname = get_name()
            get_nba_player(fullname)
        
        else:
            print("\nHere are your statistics:")
            for value in players_stats:
                true_shooting = ((value[0]['tsPercent'])*100)
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(f"{value[0]['playerName']}: Season: {value[0]['season']} | Team: {value[0]['team']} | Age: {value[0]['age']} | Position: {value[0]['position']} | GP: {value[0]['games']} | PER(player efficiency rating): {value[0]['per']} | True Shooting Percentage: {true_shooting:.1f}% | Assist Percent: {value[0]['assistPercent']}% | Steal Percent: {value[0]['stealPercent']}% | Total Rebound Percent: {value[0]['totalRBPercent']}% | Turnover Percent: {value[0]['turnoverPercent']}% | Win Shares: {value[0]['winShares']}")
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                
    # if response code fails ask if they want to try again or show results
    else:
        print(f"Invalid Player.\n{response.status_code}")
        ans = input("Would you like to try again?(Y/N): ")
        
        # recall functions if they answer "Y"
        if ans == 'Y':
            fullname = get_name()
            get_nba_player(fullname)
        
        else:
            print("\nHere are your statistics:")
            for value in players_stats:
                true_shooting = ((value[0]['tsPercent'])*100)
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(f"{value[0]['playerName']}: Season: {value[0]['season']} | Team: {value[0]['team']} | Age: {value[0]['age']} | Position: {value[0]['position']} | GP: {value[0]['games']} | PER(player efficiency rating): {value[0]['per']} | True Shooting Percentage: {true_shooting:.1f}% | Assist Percent: {value[0]['assistPercent']}% | Steal Percent: {value[0]['stealPercent']}% | Total Rebound Percent: {value[0]['totalRBPercent']}% | Turnover Percent: {value[0]['turnoverPercent']}% | Win Shares: {value[0]['winShares']}")
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                
fullname = get_name()
stats = get_nba_player(fullname)











    




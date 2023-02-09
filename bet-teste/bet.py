import requests 
import json 

#Your Betzap credentials 
username = "your_username" 
password = "your_password" 
bet_url = "https://www.bet.com/api/" 
#Log in to Bet
payload = {'username': username, 'password': password} 
r = requests.post(bet_url + "login", data=payload) 
if r.status_code != 200: 
    print("Error logging into Bet") 
    exit()  
else: 
    #Get the bearer token from the response content and add it to the header of subsequent requests 
    bearer_token = json.loads(r.content)['token'] 
    headers = {"Authorization": "Bearer "+ bearer_token}

# Get list of bets for current user  
r = requests.get(bet_url + "bets", headers=headers)  
if r.status_code != 200:  
    print("Error getting bets from Bet")  
    exit()  
else:  
    #Get the bets from the response content and loop through each one to check for updates  
    bets = json.loads(r.content)['bets']  

    for bet in bet:  

        #Get details of each bet and check if it's been updated or not  

        r = requests.get(bet_url + "bets/" + str(bet['id']), headers=headers)  

        if r.status_code != 200:  

            print("Error getting bet details from Bet")  

            exit()  

        else:    

            bet_details = json.loads(r.content)['details']    

            if bet_details["updated"]:    

                #Do something with the updated bet, e.g. send an alert or update a database    

                print("Bet has been updated")
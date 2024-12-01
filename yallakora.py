import requests
from bs4 import BeautifulSoup
from csv import DictWriter

date = input("Enter the date in the following format MM/DD/YYYY : ")
page = requests.get(f"https://www.yallakora.com/match-center?date={date}")


source = page.content
# encoding = page.encoding
# print(f"Detected encoding: {encoding}")
soup =BeautifulSoup(source, "lxml")

detailes = []

champions = soup.find_all("div", {"class" : "matchCard"}) # contnts of champions 

for i in range(len(champions)):

    champions_name = champions[i].contents[1].find("h2").text.strip()  # name of champions 

    match_det = champions[i].contents[3].find_all("div", {"class" : "liItem" }) # content of matches

    detailes.append({"type of champion" : champions_name})

    for i in range(len(match_det)):
        team_A = match_det[i].find("div", {"class" : "teamA"}).text.strip() # teams name 
        team_B = match_det[i].find("div", {"class" : "teamB"}).text.strip() # vs teams name 
 
        score = match_det[i].find_all("span", {"class" : "score"}) # teams score
        result = f"{score[0].text}-{score[1].text}"

        time = match_det[i].find("span", {"class" : "time"}).text # match time 
        detailes.append({"teamA" : team_A, "team_B" : team_B, "score" : result, "time" : time  })

with open(r"D:\Applications\Yallakora.csv", "w", newline='', encoding='utf-8') as file:
    # Define the column names for the CSV
    keys = ["type of champion", "teamA", "team_B", "score", "time"]

    # Create a DictWriter object
    dict_writer = DictWriter(file, fieldnames=keys)
    
    # Write the header (column names)
    dict_writer.writeheader()

    # Write all rows from detailes list
    dict_writer.writerows(detailes)

print("CSV file created successfully.")

# print(keys)


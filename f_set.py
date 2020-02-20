import csv
import pandas
# shows list of teams in dictionery
def show_team():
    teamlist = ['Sunrisers Hyderabad','Royal Challengers Bangalore','Kolkata Knight Riders','Gujarat Lions','Rising Pune Supergiants'
            ,'Delhi Daredevils' , 'Mumbai Indians','Kings XI Punjab' ,'Rajasthan Royals']
    dict_teams = dict(enumerate(teamlist ,1 ))
    for key , val in dict_teams.items():
        print(key , val)
    inp = int(input('Choose your team :'))
    if inp in dict_teams.keys():
        return dict_teams[inp]
def Toss_win(team):
    count = 0
    won = 0
    l = []
    with  open(r'matches.csv') as csvfile :
        alldata = csv.DictReader(csvfile)
        for data in alldata :
            if team in [data['TEAM1'], data['TEAM2']]:
                count += 1
                if team in data['TOSS_WINNER']:
                    won += 1
        l.append(count)
        l.append(won)
    return(l)
def yearwise(team):
    with  open(r'matches.csv') as csv_obj:
        csv_read = csv.DictReader(csv_obj)
        a = set()
        [a.add(data['SEASON'])for data in csv_read]
        a = sorted(a)
        d ={}
        for year in a:
            count = 0
            won = 0
            d[year] = {}
            with  open(r'matches.csv') as csv_obj:
                csv_read = csv.DictReader(csv_obj)
                for data  in csv_read:
                    if team in [data['TEAM1'], data['TEAM2']] and data['SEASON'] == year:
                        count+=1
                        if team in data['WINNER']:
                            won+= 1
            d[year]['Matches played']= count
            d[year]['Win'] = won
        return(d)


def citywise(team):
    with  open(r'matches.csv') as csv_obj:
        csv_read = csv.DictReader(csv_obj)
        city = set()
        [city.add(data['CITY']) for data in  csv_read]
        city = sorted(city)
        d = {}
        for each in city[1:]:
            count = 0
            won = 0
            d[each]= {}
            with  open(r'matches.csv') as csv_obj:
                csv_read = csv.DictReader(csv_obj)
                for alldata in csv_read:
                    if team in [alldata['TEAM1'],alldata['TEAM2']] and alldata['CITY']== each:
                        count +=1
                        if team in alldata['WINNER']:
                            won+=1
            d[each]['Match played'] = count
            d[each]['Win'] = won
    return d

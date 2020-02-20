import csv
import f_set
csv_obj = open(r'matches.csv')
csv_read = csv.DictReader(csv_obj)
while True :
    print('******MATCH ANALYSIS******')
    print('='*40)
    print('Choose your  option :\n')
    print('\t1  TOSS WIN ANALYSIS')
    print('\t2 YEARWISE MATCH PLAYED/WON ')
    print('\t3 CITYWISE MATCH PLAYED/WON')
    print('\t4. EXIT')
    print('-'*40)
    choice =  int(input("Enter your choice :"))
    if choice == 1:
        team = f_set.show_team()
        toss  = f_set.Toss_win(team)
        print('-'*60)
        print(team)
        print('-' * 60)
        print("\tMATCHES PLAYED :",toss[0])
        print('\tTOSS WON : ', toss[1], 'times' )
        print('\t% of WIN :' ,(toss[1]/ toss[0])*100 , '%')
        print('-' * 60)

    if choice == 2:
        team = f_set.show_team()
        dict_yearwise = f_set.yearwise(team)
        print(team)
        print('-' * 40)
        print('YEAR\t\tMatches played\t\t\tWin')
        print('-'*40)
        for key in dict_yearwise:
            print(key, '\t\t\t', dict_yearwise[key]['Matches played'], '\t\t\t\t', dict_yearwise[key]['Win'])
        print('-' * 40)

    if choice==3:
        team = f_set.show_team()
        citiwise = f_set.citywise(team)
        print('-' * 50)
        print(team)
        print('-' * 50)
        print('CITY\t\t\t\tMatches played\t\t\t\tWin')
        print('-' * 50)
        for key in citiwise.keys():
            print("{:>16}  {:>12}  {:>17} ".format(key, citiwise[key]['Match played'], citiwise[key]['Win']))

        print('-' * 50)
    if choice ==4:
        print('Thank you...!')
        break
    if choice > 4:
        print('*****Invalid Choice*****\n')


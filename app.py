from constants import PLAYERS, TEAMS
import copy
import sys

players = copy.deepcopy(PLAYERS)
teams = copy.deepcopy(TEAMS)


# creating a copy of original data to modify and iterate over without altering underlying data


def clean_data(player_list):
    """
    Takes a collection as argument
    Updates 'experience key' value to bool
    Split height attribute and convert to integer, then update 'height' key values
"""
    for player in player_list:
        value, unit = player['height'].split(' ')
        int_value = int(value)
        player['height'] = int_value
        # convert height str to integer

        if player['experience'] == 'YES':
            player['experience'] = True
        elif player['experience'] == 'NO':
            player['experience'] = False
        else:
            print("Unknown Value")
        # convert experience value to boolean
    return player_list


def balance_teams(list_players, list_teams):
    """

    :param list_players: list of players
    :param list_teams: list of teams
    :return: dictionary where keys = team names, values = lists of dictionary with player attributes
    and players split evenly across teams
    """
    team_size = int(len(list_players) / len(list_teams))
    teams_dict = {}
    for i in range(len(list_teams)):
        split_team = list_players[0: team_size]
        teams_dict[list_teams[i]] = split_team
        del list_players[0: team_size]
        # remove new player list from originally passed player list to avoid player overlap for next loop iteration
    return teams_dict


def display_team_names(team_list):
    """

    :param team_list: takes list of team names
    :return: prints out numbered lit of teams
    """
    print()
    print('Available Teams: ')
    for i in range(len(team_list)):
        print('{}) {}'.format(i + 1, team_list[i]))


def display_team_stats(team_dict):
    """
    :param team_dict:  takes a dictionary as argument, assumes dictionary has team name as keys
    and lists with player attributes aa values
    Prompts user to input the team name,
    iterates over the specified item in the dictionary and prints the team stats
    :return: does  not return any values, prints values for team stats to console
     """
    print()
    team = input("Type in a team name to display the stats > ")
    team = str(team.capitalize())
    if team in team_dict.keys():
        print()
        print('Team', team, 'Sats')
        print('--' * 10)
        print('Total Players: {}'.format(len(team_dict[team])))
        print()
        player_names = [player['name'] for player in team_dict[team]]
        player_heights = [player['height'] for player in team_dict[team]]
        experience_dict = {
            'experienced': [player for player in team_dict[team] if player['experience'] is True],
            'inexperienced': [player for player in team_dict[team] if player['experience'] is False]
        }
        print('Players on Team: ')
        print(', '.join(player_names))
        print()
        print('Number of experienced players: {}'.format(len(experience_dict['experienced'])))
        print('Number of inexperienced players: {}'.format(len(experience_dict['inexperienced'])))
        avg_height = round(sum(player_heights) / len(team_dict[team]), 1)
        print()
        print('Average player height: {}'.format(avg_height))
        print()
    else:
        print('Invalid Input! Please type in a correct team name to see the stats!')
        display_team_stats(team_dict)
        # catch invalid input and use recursion to re-prompt user input


def display_main_menu():
    """
    displays main menu options
    :return: user's choice of option
    """
    print()
    print('-' * 5, 'Main Menu', '-' * 5)
    print('Here are your options: ')
    print('1) Display Team Stats')
    print('2) Quit Program')
    print()
    user_choice = input('Enter an option by number > ')
    return user_choice


if __name__ == "__main__":
    clean_data(players)

    final_teams_dict = balance_teams(players, teams)

    team_name_list = list(final_teams_dict)
    while True:
        user_input = display_main_menu()
        if user_input == '1':
            display_team_names(team_name_list)
            display_team_stats(final_teams_dict)
            while True:
                continue_option = input('Would you like to see stats for more teams? (y/n) > ')
                if continue_option == 'y':
                    display_team_names(team_name_list)
                    display_team_stats(final_teams_dict)
                elif continue_option == 'n':
                    break
                else:
                    print('Invalid Input! Please enter y or n ')
                    continue
        elif user_input == '2':
            sys.exit('Good Bye!')
        else:
            print('Cannot recognize your input! Please, try again and enter a valid option number!')

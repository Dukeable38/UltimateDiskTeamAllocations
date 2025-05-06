import csv


# General lists
attending_players = []
team_list = []
white_team = []
black_team = []
bench_team = []

# General variables
blackTeamTotalScore = 0
whiteTeamTotalScore = 0

# Skill seperations
cracked_players7 = []
expert_players6 = []
expirenced_players5 = []
good_players4 = []
average_players3 = []
novice_players2 = []
new_players1 = []

# Configurables
acceptableAverageScoreDiff = 2

# PHASE 0 ===== Gather data from players, only those who are present
def load_team_data(file_path):  
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Skip the header row
            for row in reader:
                # Assuming 'attendance' is the 5th column (index 4)
                try:
                    attendance = int(row[4])
                    if attendance == 1:
                        attending_players.append(row)
                except IndexError:
                    print(f"Warning: Row {row} has fewer than 5 columns. Skipping.")
                except ValueError:
                    print(f"Warning: Attendance value '{row[4]}' in row {row} is not an integer. Skipping.")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    return attending_players
# ==========================================



# Adds a player to a particular team and increase the team stats accordingly
def add_player_to_team(player, team_they_join,):
    global blackTeamTotalScore
    global whiteTeamTotalScore
    
    if team_they_join == 'black':
        black_team.append(player)
        blackTeamTotalScore += int(player[1])
    elif team_they_join == 'white':
        white_team.append(player)
        whiteTeamTotalScore += int(player[1])
    else:
        bench_team.append(player)

# Prints out the first window revealing the starting allocations
def print_statistics(print_screen_number):

    # variables and stats
    sizeOfBlack = len(black_team)
    sizeOfWhite = len(white_team)
    startingCountDiff = abs(sizeOfBlack - sizeOfWhite)
    startingScoreDiff = abs(blackTeamTotalScore-whiteTeamTotalScore)
    startingScoreAvgDiff = (blackTeamTotalScore/sizeOfBlack) - (whiteTeamTotalScore/sizeOfWhite)

    if print_screen_number == 1:
        

        # prints summery DEBUG
        print("[1. Pre-Allocations (manditory allocations)]")
        print("===================") 
        print(f"The BLACK team has {len(black_team)} players:")
        for player in black_team:
            print(f"-> {player[0]} : Skill Level {player[1]}")
        print(" -- -- -- -- -- -- --")
        print(f"Total Score: {blackTeamTotalScore} | Average Score: {round(blackTeamTotalScore / len(black_team),2)}")
        print()
        print("===================")
        print(f"The WHITE team has {len(white_team)} players:")
        for player in white_team:
            print(f"-> {player[0]} : Skill Level {player[1]}")
        print(" -- -- -- -- -- -- --")
        print(f"Total Score: {whiteTeamTotalScore} | Average Score: {round(whiteTeamTotalScore / len(white_team),2)}")
        print("")
        print("")
        

        print(" = = = = = = = = = = = = = = = = = = = ")
        print(f"Team count difference: {startingCountDiff} | Score Difference: {startingScoreDiff} | Average Score Difference: {round(startingScoreAvgDiff,2)}")
        print(" = = = = = = = = = = = = = = = = = = = ")
    
    elif print_screen_number == 2:
        print("----")
        print(f"Black Team: {sizeOfBlack} ({blackTeamTotalScore})")
        print(f"White Team: {sizeOfWhite} ({whiteTeamTotalScore})")
        
        

    elif print_screen_number == 3:
        print()
        print()
        print("~~ ! = = = GRAND SUMMERY = = = ! ~~")
        print()
        print(f"== BLACK TEAM ({sizeOfBlack} players) ==")
        for player in black_team:
            if player[3] != 'both': # Print manditory first
                if player[2] == 'f':
                    print(f"* {player[0]} :: {player[1]} (F)")
                else:
                    print(f"* {player[0]} :: {player[1]}")
        for player in black_team:
            if player[3] == 'both': # Print allocated second
                if player[2] == 'f':
                    print(f"-> {player[0]} :: {player[1]} (F)")
                else:
                    print(f"-> {player[0]} :: {player[1]}")
        print(" - - - - Black Team Stats - - - - ")
        print(f"Total Score: {blackTeamTotalScore} | Avg Score: {round(blackTeamTotalScore/sizeOfBlack,2)}")
        print()
        print(f"== WHITE TEAM ({sizeOfWhite} players) ==")
        for player in white_team:
            if player[3] != 'both': # Print manditory first
                if player[2] == 'f':
                    print(f"* {player[0]} :: {player[1]} (F)")
                else:
                    print(f"* {player[0]} :: {player[1]}")
        for player in white_team:
            if player[3] == 'both': # Print allocated second
                if player[2] == 'f':
                    print(f"-> {player[0]} :: {player[1]} (F)")
                else:
                    print(f"-> {player[0]} :: {player[1]}")
        print(" - - - - White Team Stats - - - - ")
        print(f"Total Score: {whiteTeamTotalScore} | Avg Score: {round(whiteTeamTotalScore/sizeOfWhite,2)}")
        print()
        print()
        print(" = = = = = = = = = = = = = = = = = = = ")
        print(f"Team count difference: {abs(sizeOfBlack - sizeOfWhite)} | Score Difference: {abs(blackTeamTotalScore-whiteTeamTotalScore)} | Average Score Difference: {round((blackTeamTotalScore/sizeOfBlack) - (whiteTeamTotalScore/sizeOfWhite),2)}")
        print(" = = = = = = = = = = = = = = = = = = = ")

def print_team_summery():
    print("")

# PHASE 2 ===== 

# Gets the size and score difference from both teams
def get_difference():
    
    # Nicknames for ease
    blackSize = len(black_team)
    whiteSize = len(white_team) 

    # General differnce calculations
    sizeDifference = abs(blackSize - whiteSize) # Size difference between both teams (ABS = positive number only)
    actualScoreDiff = abs(blackTeamTotalScore - whiteTeamTotalScore) # Same deal as above
    avgScoreDiff = abs((blackTeamTotalScore/blackSize) - (whiteTeamTotalScore/whiteSize)) # Also same deal

    #Who has a bigger team?
    if blackSize > whiteSize: # BLACK bigger than WHITE
        smallerTeam = 'white'
        largerTeam = 'black'
    elif whiteSize > blackSize: # WHITE bigger than BLACK
        smallerTeam = 'black'
        largerTeam = 'white'
    else: # Even
        smallerTeam = 'even'
        largerTeam = 'even'
    # Who has a bigger score?
    if blackTeamTotalScore > whiteTeamTotalScore: #BLACK more score than WHITE
        lessScore = 'white'
    elif whiteTeamTotalScore > blackTeamTotalScore: #WHITE more score than BLACK
        lessScore = 'black'
    else:
        lessScore = 'even'
        
    return sizeDifference, actualScoreDiff, avgScoreDiff, smallerTeam, largerTeam, lessScore

# Picks a random player from a selected list
# def pickRandomPlayer(list_to_choose_from):
#     choice = random.choice(list_to_choose_from)
#     return choice
     
def sort_remaining_players():
    for player in team_list:
        print()
        if player[3] == 'both': # All remaining BOTH shirt players
            sizeD, scoreD, avgSD, smallerT, largerT, lessS = get_difference()

            # Size difference between teams

            if sizeD == 0: # There IS NO difference in team player count
                if lessS == 'even':
                    add_player_to_team(player, 'black') # All even, just go black mate

                # No Size difference between teams
                else:
                    add_player_to_team(player, lessS) # Since we are equal, go to the *weaker team*

            else: # There IS A difference in team player count

                # Case A: Larger team has a greater score
                if smallerT == lessS : # If the little team has the smaller score

                    add_player_to_team(player, smallerT) # Since the larger team has more score, go to *smaller team*


                # Case B: Smaller team has a greater score
                if smallerT != lessS:
                    # Case B1: The smaller team is to powerful
                    if avgSD >= acceptableAverageScoreDiff:
                        add_player_to_team(player, largerT) # Since there is a large difference, go to the *larger team* 

                    # Case B2:The bigger teams score difference is reasonable, still *smaller team* 
                    else:
                        add_player_to_team(player,smallerT)
        
            print_statistics(2)
            print(f"{player[0]} joined a team")

        else:
            pass
            # print(f"some incorrect happend, {player[0]} skipped out...")
    
    print(" Allocations FINISHED!")
    print_statistics(3)

def initalise_first_sorting():
    global team_list

    # Load data using function
    file_path = 'team_data.csv'
    team_list = load_team_data(file_path)

    # Sorts BLACKS and WHITES into their sides (force)
    print("=======") 
    for player in team_list: # Sorts every player who only wears one colour shirt
        if player[3] == 'black':
            add_player_to_team(player, 'black')
        elif player[3] == 'white':
            add_player_to_team(player, 'white')
        else:
            pass # These people are reserved for later
    print_statistics(1)
    sort_remaining_players()


initalise_first_sorting()
        

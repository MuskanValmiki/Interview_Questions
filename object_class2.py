class Team:
    def __init__(self,team_name,total_player_count,team_color):
        self.total_player_count = total_player_count
        self.team_color = team_color
        self.team_name = team_name

class Score:
    def score(self,month,year,points,result):
        self.month = month
        self.year = year
        self.points = points
        self.result = result

class TeamScore(Team,Score):
    def __init__(self, team_name, total_player_count, team_color):
        super().__init__(team_name, total_player_count, team_color)
    def display_status(self):
        print("Team Name :",self.team_name)
        print("Total Player :",self.total_player_count)
        print("Team Color :",self.team_color)
        print("Month :",self.month)
        print("Year :",self.year)
        print("Points :",self.points)
        print("Result Win or Lose :",self.result)

teamName = input("Enter Team Name :")
countPlayer = int(input("Enter Player No :"))
color_team = input("Enter Team color :")

months = int(input("Enter month no :"))
year = int(input("Enter Year :"))
points = int(input("Enter Points No :"))
Result = input("Enter Win or Lose :")

result = TeamScore(teamName,countPlayer,color_team)
result.score(months,year,points,Result)
result.display_status()
# here we display Team and score
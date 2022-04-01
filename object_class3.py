class Team:
    def __init__(self,Team):
        self.Team = Team   
    def team(self):
        print("Team :",self.Team)

class FrontEnd(Team):
    def __init__(self, Team):
        super().__init__(Team)       
    def frontend(self,team_size,programming_language):
        self.team_size = team_size 
        self.programming_laguage = programming_language

class Backend(Team):
    def __init__(self, Team):
        super().__init__(Team)
    def backend(self,programming_language,server_size,team_size):
        self.programming_language = programming_language
        self.server_size = server_size
        self.team_size = team_size

class Sprint(FrontEnd,Backend):
    def show(self):
        print("FrontEnd Team :")
        print("Team Size :",self.team_size)
        print("Progarmming Language :",self.programming_language)
        print("Backend team")
        print("Server Size :",self.server_size)
        print("Programming Language :",self.programming_language)
        print("team Size :",self.team_size)

name_team = input("Enter Team Name :")
size_team = input("Enter Team Size :")
lang = input("Enter Language :")
size_server = input("enter Server Size E.G 1PB :")
result = Sprint(name_team)
result.team()
result.frontend(size_team,lang)
result.backend(lang,size_server,size_team)
result.show()
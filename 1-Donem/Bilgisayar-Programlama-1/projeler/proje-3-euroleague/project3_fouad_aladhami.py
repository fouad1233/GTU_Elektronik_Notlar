#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 13:34:07 2021

@author: fuad
"""
my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"
#Keyifli okumalar diliyorum :-)
import random 
class Person:
    def __init__(self , name, lastname):
        self.name = name
        self.lastname = lastname
        
    def get_name(self):
        return self.name + ' ' + self.lastname
    def __str__(self):
        return self.name + ' ' + self.lastname
    def __lt__(self, other ):
        if self.lastname == other.lastname:
            if self.name < other.name :
                return True
            else:
                return False
        if self.lastname < other.lastname :
            return True 
        else:
            return False

class Player(Person):
    id_counter = 0
    #players_and_points = {}
    #detailed_points = []
    def __init__(self,name, lastname):
        Person.__init__(self, name, lastname)
        self.power= random.randint(4,8)
        #self.playerid =0
        self.points = 0
        Player.id_counter += 1
        self.player_id = Player.id_counter
        self.detailed_points =[]
        self.lofplayer = []
        self.player_and_id ={}
    def get_id(self):
        # if self.name + self.lastname not in self.lofid:
        #     self.player_id += 1
        #     self.lofplayer.append(self.name + self.lastname)
        #     self.player_and_id[self.name + self.lastname] = self.player_id
        #     return self.player_id
        # else:
            
        #     return self.player_and_id[self.name + self.lastname]
        return self.player_id
    def set_team(self,t):
        self.player_team = t
    def get_team(self):
        return self.player_team
        
    
    def reset(self):
        self.points = 0
        self.detailed_points =[]
        Player.id_counter = 0
        #Player.players_and_points = {}
    def get_power(self):
        return self.power
    def add_to_points(self,x):
        self.detailed_points.append(x)
        self.points += x
        # try :
        #     Player.players_and_points[self.name + self.lastname] +=  x
        # except:
        #     Player.players_and_points[self.name + self.lastname] =  x

        
    
    def get_points(self):
        # try:
        #     self.points = Player.players_and_points[self.name + self.lastname]

        #     return self.points
        # except :
        return self.points
    # def get_points1(self):
    #     try:
    #         self.point = Player.players_and_points[self.name + self.lastname]

    #         return self.point
    #     except :
            #return self.points
    def get_points_detailed(self):
        return self.detailed_points
    
    def __lt__(self,other):
        if self.get_points() == other.get_points() and self.lastname == other.lastname :  
            return self.name < other.name
        if self.get_points() == other.get_points():
            return self.lastname < other.lastname
        return self.get_points() < other.get_points()
class Manager(Person):
    m_id_counter = 0
    # managers_and_points = {}
    def __init__(self, name, lastname):
        Person.__init__(self, name, lastname)
        
        self.influenced = []
        Manager.m_id_counter += 1
        self.id = Manager.m_id_counter
        self.lofmanager = []
        self.influence = 0
        self.managers_and_id ={}
    def get_id(self):
        # if self.name + self.lastname not in self.lofid:
        #     self.manager_id += 1
        #     self.lofplayer.append(self.name + self.lastname)
        #     self.player_and_id[self.name + self.lastname] = self.manager_id
        #     return self.manager_id
        # else:
            
        #     return self.player_and_id[self.name + self.lastname]
        return self.id
    def reset(self):
        self.influence = 0
        self.influenced = []
        Manager.m_id_counter = 0
        #Manager.managers_and_points = {}
    
    
    def set_team(self ,t):
        self.team = t
    def get_team(self):
        return self.team
    def get_influence_detailed(self):
        return self.influenced
    def add_influence(self,x):
        self.influenced.append(x)
        self.influence += x
        
        # try :
        #     Manager.managers_and_points[self.name + self.lastname]+=  x
        # except:
        #     Manager.managers_and_points[self.name + self.lastname] =  x
    def get_influence(self):
        return self.influence
        
    # def get_influence1(self):
    #     try:
    #         self.influence = Manager.managers_and_points[self.name + self.lastname]

    #         return self.influence
    #     except :
    #         return self.influence
        #return sum(self.influenced )
    
    def __lt__(self,other):
        if self.get_influence() == other.get_influence() and self.lastname == other.lastname :  
            return self.name < other.name
        if self.get_influence() == other.get_influence():
            return self.lastname < other.lastname
        return self.get_influence() < other.get_influence()
    
class Team(Person):
    count = 0 
    def __init__(self,teamname, manager, players):
        
        def namecreator(fullname):
            
            fullname.split()
            # if len(fullname.split()) == 2:
            first=fullname.split()[0]
            last=fullname.split()[-1]
            return(first , last)
        self.teamname = teamname
        self.manager = manager 
        self.players = players
        Team.count += 1
        self.team_id  = Team.count
        self.scored = 0
        self.conceded = 0
        self.wins = 0 
        self.losses = 0
        self.fixturelist = []
        self.lofteam = []
        
        self.team_and_id ={}
    def reset(self):
        self.fixturelist = []
        self.manager.reset() 
        self.scored = 0
        self.conceded = 0
        self.wins = 0 
        self.losses = 0
        Team.count = 0
        for i in self.players:
             i.reset()
        #self.players.fixture(0) 
    
    def get_id(self):
        # if self.name + self.lastname not in self.lofid:
        #     self.team_id += 1
        #     self.lofteam.append(self.name + self.lastname)
        #     self.team_and_id[self.name + self.lastname] = self.team_id
        #     return self.team_id
        # else:
            
        #     return self.team_and_id[self.name + self.lastname]
        return self.team_id
    def get_name(self):
        return self.teamname
    def get_roster(self):
        return self.players
    def get_manager(self):
        return self.manager
    def add_to_fixture(self,m):
        self.fixturelist.append(m)
    def get_fixture(self):
        return self.fixturelist
    
    def add_result(self,s):
        self.scored += s[0]
        self.conceded += s[1]
        if s[0] > s[1]:
            self.wins += 1
        elif s[0] < s[1]:
            self.losses +=1
    def get_scored(self):
        return self.scored
    
    def get_conceded(self):
        return self.conceded
    
    def get_wins(self):
        
        return self.wins
    def add_wins(self,x):
        self.wins += x

    def get_losses(self):
        return self.losses
    def add_losses(self,x):
        self.losses += x
    
    def __str__(self):
        return self.teamname
    def __lt__(self,other):
        if self.wins == other.wins:
            self.net = self.scored - self.conceded
            other.net = other.scored - self.conceded
            return self.net < other.net
        else :
            return self.wins < other.wins
class Match:
    def __init__(self, home_team, away_team, week_no) :
        self.home_team = home_team
        self.away_team = away_team
        self.week_no = week_no
        self.played = False
        self.home_team_matchscore = 0
        self.away_team_matchscore = 0
        self.winner = None
        self.scored = 0
        self.conceded  = 0
    def get_week_number(self):
        return self.week_no
    def is_played(self):
        return self.played
    def play(self):
        def namecreator(fullname):
            
            fullname.split()
            # if len(fullname.split()) == 2:
            first=fullname.split()[0]
            last=fullname.split()[-1]
            return(first , last)
        self.played= True
        home_score = 0
        away_score = 0
        self.home_manager_point = random.randint(-10, 10)
        self.away_manager_point = random.randint(-10, 10)
        #Addding the managers point to influence item in Manager class
        self.home_team.get_manager().add_influence(self.home_manager_point)
        self.away_team.get_manager().add_influence(self.away_manager_point)
        home_score += self.home_manager_point
        away_score += self.away_manager_point
        home_period_scores =[]
        away_period_scores =[]
        counter = 0
        self.periods = 4
        
        while counter < self.periods :
            counter += 1
            home_period = 0
            away_period = 0
            hplayerpoints  = [0,0,0,0,0]
            aplayerpoints  = [0,0,0,0,0]
           
            for i in range(len(self.home_team.get_roster())):
                
                a = self.home_team.get_roster()[i].get_power()+ int(random.randint(-5,5))
                b = self.away_team.get_roster()[i].get_power()+ random.randint(-5,5)
                if i == 0:
                    hplayerpoints[0] += a
                    aplayerpoints[0] += b
                elif i == 1:
                    hplayerpoints[1] += a
                    aplayerpoints[1] += b
                elif i == 2:
                    hplayerpoints[2] += a
                    aplayerpoints[2] += b
                elif i == 3:
                    hplayerpoints[3] += a
                    aplayerpoints[3]+= b
                elif i == 4:
                    hplayerpoints[4] += a
                    aplayerpoints[4] += b
                
                home_period += a 
                away_period += b 
            
            
            home_period_scores.append(home_period )
            home_period = 0
            away_period_scores.append(away_period )
            away_period = 0
            home_score += sum(home_period_scores)
            away_score += sum(away_period_scores)
            home_period_scores =[]
            away_period_scores =[]
            if home_score == away_score and counter >= 4:
                self.periods += 1
        for i in range(5):
            self.home_team.get_roster()[i].add_to_points(hplayerpoints[i])
            #print(hplayerpoints[i],'home')
            # if i == 0:
                
            #     print(aplayerpoints)
            self.away_team.get_roster()[i].add_to_points(aplayerpoints[i])
            #print(aplayerpoints[i],'away')
        home_score += sum(home_period_scores)
        away_score += sum(away_period_scores)
        self.home_team_matchscore,self.away_team_matchscore =home_score,away_score
        self.home_team.scored += self.home_team_matchscore
        self.home_team.conceded += self.away_team_matchscore
        self.away_team.scored += self.away_team_matchscore
        self.away_team.conceded += self.home_team_matchscore
        if home_score > away_score:
            self.home_team.get_wins() 
            self.home_team.wins +=1
            self.away_team.losses +=1
            # self.scored+= home_score
            # self.conceded += away_score
            
            self.winner = self.home_team.get_name()
        else:
            self.winner = self.away_team.get_name()
            self.away_team.wins+= 1
            self.home_team.losses += 1
            # self.scored  += away_score 
            # self.conceded += home_score
        
    def get_periods_number(self):
        return self.periods
        
    def get_match_score(self):
        return (self.home_team_matchscore,self.away_team_matchscore )
    def get_teams(self):
        return (self.home_team,self.away_team )
    def get_home_team(self):
        return self.home_team
    def get_away_team(self):
        return self.away_team
    def get_winner(self):
        if self.played == True :
            return self.winner
        else :
            return None
        
    def __str__(self):
        if self.is_played()== False:
            return str(self.home_team) + ' vs. ' +str(self.away_team)
        else:
            return str(self.home_team)+' ' + '(' + str(self.home_team_matchscore) +')'+ ' vs. '+'(' + str(self.away_team_matchscore) +') ' +str(self.away_team) 

class Season:
    
    mydict = {}
    
    player = []
    manager = []
    team = []
    def __init__(self,teams, managers, players):
        self.fixtureisbuilded = False
        
        Season.player = []
        Season.manager = []
        Season.team = []
        def namecreator(fullname):
            fullname.split()
            first=fullname.split()[0]
            last=fullname.split()[-1]
            return(first , last)
        self.weeknumber = 0
        self.playerslist = []
        self.managerslist = []
        self.teamslist = []
        fteams = open(teams , "r")
        a = fteams.read()
        self.teams = a.strip().split('\n')
        fteams.close()
        fmanagers = open(managers , "r")
        a = fmanagers.read()
        self.managers = a.strip().split('\n')
        
        for i in range(len(self.managers)):
            self.managerslist.append(Manager( namecreator(self.managers[i] )[0] ,namecreator(self.managers[i] )[1] ))
        fmanagers.close()
        
        fplayers = open(players , "r")
        a = fplayers.read()
        self.players = a.strip().split('\n')
        
        
        for i in range(len(self.players)):
            self.playerslist.append(Player( namecreator(self.players[i] )[0] ,namecreator(self.players[i] )[1] ))
        
        fplayers.close()
        
        
        for i in range(len(self.teams)):
            self.teamslist.append(Team(self.teams[i] , self.managerslist[i] , [ self.playerslist[5*i] ,self.playerslist[5*i+1],self.playerslist[5*i+2],self.playerslist[5*i+3],self.playerslist[5*i+4]]))
        random.shuffle(self.teamslist)
        self.endfixture = []
        self.matchfixture  = []
        self.build_fixture()
    def reset(self):
        Season.player = []
        Season.manager = []
        Season.team = []
        self.weeknumber = 0
        self.build_fixture()
        
    def build_fixture(self):
        self.weeknumber = 0
        
        for i in self.playerslist:
            i.reset()
        for i in self.managerslist:
            i.reset()
        for i in self.teamslist:
            i.reset()
        random.shuffle(self.teamslist)
    
        self.fixtureisbuilded = True
        def copylist(board):
            c = 0
            yeniliste = []
            for i in range(len(board)):
                yeniliste.append([])
                
                a = len(board[0])
                for i in range(a):
                    yeniliste[c].append(board[c][i])
                c +=1
            return yeniliste
        teams = len(self.teamslist)
        fixture = []
        high = []
        low = [] 
        a = 0
        b = teams
        count = 0
        for i in range(teams//2):
            high.append(self.teamslist[a])
            a += 1
            b -= 1
            low.append(self.teamslist[b])
        while count < teams -1 :
            count += 1
            week = []
            mylist = []
            for i in range(2,teams+1):
                mylist.append(i)
            for i in range (teams//2):  
                week.append([high[i] , low[i]])
            fixture.append(week)
            high.insert(1,low[0])
            low.remove(low[0])
            low.append(high[-1])
            high.remove(high[-1])
        fixture = fixture[: :-1]
        fixture2 = []
        for i in range(len(fixture)):
            fixture2.append(copylist(fixture[i]))
        for i in range (len (fixture)):
            for j in range (len (fixture[0])):
                a, b = fixture[i][j][0] , fixture[i][j][1] 
                fixture[i][j][0] , fixture[i][j][1] = b,a
        self.endfixture = fixture2 + fixture
        #return self.endfixture[0][0][0].get_manager()
        for i in range(len(self.endfixture)):
            for j in range(len(self.endfixture[0])):
                self.endfixture[i][j][0].add_to_fixture(Match(self.endfixture[i][j][0], self.endfixture[i][j][1], i+1))
                self.endfixture[i][j][1].add_to_fixture(Match(self.endfixture[i][j][0], self.endfixture[i][j][1], i+1))
        #for i in range()
        self.matchfixture = []
        self.perweek = []
        for i in range(len(self.endfixture)):
            for j in range(len(self.endfixture[0])):
                self.perweek.append(Match(self.endfixture[i][j][0], self.endfixture[i][j][1], i+1))
            self.matchfixture.append(self.perweek)
            self.perweek = []
    def get_all_fixtures(self):
        
           
        return self.matchfixture
    def get_week_fixture(self,week_no):
        if week_no < 1 or week_no > len(self.endfixture):
            return None 
        else:
            return self.matchfixture[week_no - 1]
        
    def play_week(self):
        
        if self.fixtureisbuilded == True:

            self.weeknumber+= 1
            if self.weeknumber <= len(self.matchfixture):
                # Player.reset(self)
                # Manager.reset(self)
                for i in range(len(self.matchfixture[self.weeknumber - 1]) ):
                    
                    self.matchfixture[self.weeknumber - 1][i].play()
            else:
                
                self.weeknumber-= 1
                #print('yeter artık ' + str(len(self.matchfixture)) +'haftası oynandı ve bitti basma bir daha ' )
                pass
            self.bestplayerlist = []
            totalpoints=[]
            # for i in self.playerslist:
            #     print(i.get_points())
            if len(Season.player)==0:
                for i in self.playerslist:
                    Season.player.append(0)
            firstpoints = Season.player.copy()
            Season.player=[]
            for player in self.playerslist:
                Season.player.append(player.get_points())
            for points in range(len(firstpoints)):
                totalpoints.append(int(Season.player[points])-int(firstpoints[points]))
            #playerdict = {}
            pcopy = totalpoints.copy()
            pcopy.sort()
            def namecreator(fullname):
                fullname.split()
                first=fullname.split()[0]
                last=fullname.split()[-1]
                return(first , last)
            for i in range(len(totalpoints)):
                if totalpoints[i]==pcopy[-1]:
                    self.bestplayerlist.append(self.playerslist[i] )
            self.bestplayer = max(self.bestplayerlist)
            
            ################################################
            self.bestmanagerlist = []
            mtotal = []
            if len(Season.manager) == 0:
                for i in range(len(self.managerslist)):
                    Season.manager.append(0)
            mfirst = Season.manager.copy()
            Season.manager = []
            for manager in self.managerslist:
                Season.manager.append(manager.get_influence())
            for points in range(len(mfirst)):
                mtotal.append(int(Season.manager[points])-int(mfirst[points]))
            mcopy = mtotal.copy()
            mcopy.sort()
            #for i in range(len(mcopy)):
                #print(mtotal,mcopy)
            for i in range(len(mtotal)):
                if mtotal[i]== mcopy[-1]:
                    self.bestmanagerlist.append(self.managerslist[i])
            self.bestmanager = max(self.bestmanagerlist)
            ##################################################
            self.bestteamlist = []
            ttotal = []
            if len(Season.team) == 0:
                for i in range(len(self.teamslist)):
                    Season.team.append(0)
            tfirst = Season.team.copy()
            Season.team = []
            # for i in self.teamslist:
            #     print(i.get_scored())
            for team in self.teamslist :
                Season.team.append(team.get_scored())
            for points in range(len(tfirst)):
                ttotal.append(int(Season.team[points])-int(tfirst[points]))
            tcopy = ttotal.copy()
            tcopy.sort()
            #for i in range(len(tcopy)):
                #print(ttotal,tcopy)
            for i in range(len(ttotal)):
                if ttotal[i]== tcopy[-1]:
                    self.bestteamlist.append(self.teamslist[i])
            self.bestteam = max(self.bestteamlist)
                    
                    
        else:
            
            return None
            
    def get_week_no(self):
        return self.weeknumber + 1
    def get_best_player(self):
        #copy_player_list = self.playerslist.copy()
        #print(copy_player_list)
        #copy_player_list.sort()
        
        #print(copy_player_list)
        #for i in range(len(copy_player_list)):
            #print(copy_player_list[i] , copy_player_list[i].get_points1() )
        try :   
            return self.bestplayer
        except:
            return None
    def get_best_manager(self):
        # copy_manager_list = self.managerslist.copy()
        # copy_manager_list.sort()
        # for i in range(len(copy_manager_list)):
        #     print(copy_manager_list[i] , copy_manager_list[i].get_influence() )
        try :
            return self.bestmanager
        except :
            return None
    
    def get_most_scoring_team(self):
        # copy_team_list = self.teamslist.copy()
        # copy_team_list.sort()
        # for i in range(len(copy_team_list)):
        #      print(copy_team_list[i] , copy_team_list[i].get_wins() )
        try:
            return self.bestteam
        except:
            return None
        
            
    def getteamlist(self):
        return  self.teamslist
        
    def getmanagers(self):
        return  self.managerslist
    def getplayers(self):
        return  self.playerslist
    def get_champion(self):
        try :
            if self.weeknumber >= len(self.matchfixture):
                #print('the champion is')
                copyteamlist = Season.teamlist.copy()
                copyteamlist.sort()
                return copyteamlist[-1]
            else:
                return None
        except:
            return None
if __name__ == "__main__":
    #inst  = Player('Dimitris', 'Diamantidis')
    #inst2 = Player('Juan Carlos', 'Navarro')
    # pp = Player('Oz','Blayzer')
    # fb_players = [Player('Jan', 'Vesely'), Player('Achille', 'Polonara'), Player('Marko', 'Guduric'), Player('Marial', 'Shayok'), Player('Nando de', 'Colo')]
    # fb_manager = Manager('Sasa', 'Dordevic') 
    # ta_manager = Manager('Ioannis', 'Sfairopoulos')
    # ta_players = [pp,Player('Angelo',' Caloiaro'),Player('Jake','Cohen'),Player('Keenan','Evans'),Player('Mathias',' Lessort')]
    # team1 = Team('Fenerbahce Beko Istanbul',fb_manager, fb_players)
    # team2 = Team('Maccabi Playtika Tel Aviv', ta_manager, ta_players)
    # ta_manager = Manager('Ioannis Sfairopoulos', 'Dordevic')
    # inst = Match(team1, team2, 15)
    # inst.get_match_score()
    inst = Season('teams.txt','managers.txt', 'players.txt')
    # inst.build_fixture()
    # inst.play_week()
    # print(inst.get_best_player())
    # Dejan Davidovac
    # inst.get_best_player().get_points()
    # 13
    # inst.get_best_player().get_points_detailed()
    # team2 = Team('Maccabi Playtika Tel Aviv', ta_manager, ta_players)
    # inst = Match(team1, team2, 15)
    
    
    
    
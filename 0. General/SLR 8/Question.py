player_name = ["Sam","Steven","Craig","Matt","Jake","Gavin"]
player_score = [[0,15],[1,17],[1,9],[1,21],[0,18],[0,19]]

#Blue team is zero
#Red team is 1

red_team_total = 0
blue_team_total = 0
red_high_score = ["Name", 0]
blue_high_score = ["Name", 0]

for i in range(len(player_name)):
        if player_score[i][0] == 0:
                blue_team_total += player_score[i][1]
                if blue_high_score[1] < player_score[i][1]:
                        blue_high_score = [player_name[i], player_score[i][1]]
        else:
                red_team_total += player_score[i][1]
                if red_high_score[1] < player_score[i][1]:
                        red_high_score = [player_name[i], player_score[i][1]]
        
        

        
print ("RedTeam",red_team_total)
print ("BlueTeam", blue_team_total)
print ("BlueTeam HighScore", red_high_score[0])
print ("RedTeam HighScore", blue_high_score[0])




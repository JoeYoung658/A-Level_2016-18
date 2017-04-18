player_name = ["Sam","Steven","Craig","Matt","Jake","Gavin"]
player_score = [[0,15],[1,17],[1,9],[1,21],[0,18],[0,19]]

#Blue team is zero
#Red team is 1

r_total = 0
b_total = 0
r_high_score = ["Name", 0]
b_high_score = ["Name", 0]

for i in range(len(player_name)):
	if player_score[i][0] == 0:
		b_total += player_score[i][1]
		if b_high_score[1] < player_score[i][1]:
			b_high_score = [player_name[i], player_score[i][1]]
	else:
		r_total += player_score[i][1]
		if r_high_score[1] < player_score[i][1]:
			r_high_score = [player_name[i], player_score[i][1]]
	
	

	
print ("RedTeam",r_total)
print ("BlueTeam", b_total)
print ("BlueTeam HighScore", r_high_score[0])
print ("RedTeam HighScore", b_high_score[0])

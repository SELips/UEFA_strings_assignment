# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
first_player_scored = 'Ruud Gullit'
second_player_scored = 'Marco van Basten' 

goal_0 = 32
goal_1 = 54

scorers = first_player_scored + " " + str(goal_0) +", " + second_player_scored +" " + str(goal_1)

report = f'{first_player_scored} scored in the {goal_0}nd minute\n{second_player_scored} scored in the {goal_1}th minute'

"""David heeft dit al een keer nagekeken en zei dat het goedgekeurd was, maar er blijft een rood kruis bij de opdracht staan. 
Dus hier nog een keer met de verbeteringen."""
# Part 2
player = 'Erwin Koeman'
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find(' ')+1:])
name_short = f'{first_name[0]}.{player[-1-last_name_len:]}'
chant = f'{first_name}! ' * (len(first_name)-1) + f'{first_name}!'
good_chant = chant[-1]!=" "

# ITCS 1140 S1601 2022FA
# Author Joshua Mcbratnie
# date 08/29/2022
# Create a program that prompts the user for 3 bowling scores. The program should then display the 3 scores and the average

#uncomment (cntrl + / one time) lines 6-17 to run standard program (non-modular).  
#ask user for scores
print("lets average your 3 bowling scores")
#user input and declared variables
first_score= int(input("What is your first score: "))
second_score= int(input("what is your second score: "))
third_score= int(input("What is your third score: "))
average_score = 0 
#Math functions / processing 
average_score = (first_score + second_score + third_score) / 3
# Outputting the average
print("The average of the three scores is: ", "{:.2f}".format(average_score))

# program 2
# # uncomment(cntrl + / one time) lines 20-39 to run modular program
# #lines 22-25 declare global variables.
# count = 0 
# user_scores = []
# max_scores = 0
# total_score = 0 
# max_scores = int(input("how many scores do you have: "))
# #use while to iterate through total amount of rounds.
# while count < max_scores:
#     user_ask = int(input("please enter your score: "))
#     user_scores.append(user_ask)
#     count = count + 1
# #use for to iterate through list of scores.
# for num in user_scores:
#     total_score = total_score + num
# #use avg score to calculate the average
# if count == max_scores:
#     average_score = total_score / max_scores
# #display the average score
# print("The average score for all games played was : ", "{:.2f}".format (average_score))
    
    
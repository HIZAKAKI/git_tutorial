# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()

count_t_name1 = lower_name1.count("t")
count_r_name1 = lower_name1.count("r")
count_u_name1 = lower_name1.count("u")
count_e_name1 = lower_name1.count("e")
count_l_name1 = lower_name1.count("l")
count_o_name1 = lower_name1.count("o")
count_v_name1 = lower_name1.count("v")
count_t_name2 = lower_name2.count("t")
count_r_name2 = lower_name2.count("r")
count_u_name2 = lower_name2.count("u")
count_e_name2 = lower_name2.count("e")
count_l_name2 = lower_name2.count("l")
count_o_name2 = lower_name2.count("o")
count_v_name2 = lower_name2.count("v")

true_total = (count_t_name1 + count_r_name1 + count_u_name1 + count_e_name1
              + count_t_name2 + count_r_name2 + count_u_name2 + count_e_name2)
love_total = (count_l_name1 + count_o_name1 + count_v_name1 + count_e_name1
              + count_l_name2 + count_o_name2 + count_v_name2 + count_e_name2)

love_score = true_total * 10 + love_total

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
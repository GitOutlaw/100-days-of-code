print("Welcome to the love Calculator")

name1 = input("What is your name?:\n")
name2 = input("What is their name?:\n")

combined_name = name1 + name2
name_lower = combined_name.lower()

count_name_t = name_lower.count("t")
count_name_r = name_lower.count("r")
count_name_u = name_lower.count("u")
count_name_e = name_lower.count("e")

count_name_l = name_lower.count("l")
count_name_o = name_lower.count("o")
count_name_v = name_lower.count("v")
count_name_e = name_lower.count("e")

true_total = str(count_name_t + count_name_r + count_name_u + count_name_e)
love_total = str(count_name_l + count_name_o + count_name_v + count_name_e)

final = str(true_total + love_total)
final_int = int(final)

if final_int < 10 or final_int > 90:
    print(f"Your score is {final_int}, you go together like coke and mentos.")

elif final_int >= 40 and final_int <= 50:
    print(f"Your score is {final_int}, you are alright together.")
else:
    print(f"Your score is {final_int}")
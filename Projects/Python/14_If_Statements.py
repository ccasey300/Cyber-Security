# program using if statements
# 23/01/23
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall man.")
elif is_male and not is_tall:
    print("You are a short male.")
elif not is_male and is_tall:
    print("You are a tall female.")
else:
    print("You are a short female.")


print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

first_branch = input("left or right?").lower()

if first_branch == "right":
    print("Game Over.")
elif first_branch == "left":
    second_branch = input("swim or wait?").lower()
    if second_branch == "swim":
        print("Game Over.")
    elif second_branch == "wait":
        third_branch = input("which door? Red or Blue or Yellow?").lower()
        if third_branch == "blue" or third_branch == "red":
            print("Game Over.")
        elif third_branch == "yellow":
            print("You Win!")

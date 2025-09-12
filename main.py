import stones

print("[Rules] Don't pick the last stone!\n")

pile = stones.initialize()
is_user_turn = True

while pile > 0:
    print(stones.show(pile))

    if is_user_turn:
        removed = stones.pick_for_user()

    else:
        removed = stones.pick_for_computer(pile)
        print("The computer removed " + str(removed))
    
    pile -= removed
    is_user_turn = not is_user_turn

# We already swapped the turn, so the previous player lost.
if is_user_turn:
    print("The computer picked the last stone and you won!")
else:
    print("The player picked the last stone and lost!")

input("Press Enter to exit...")

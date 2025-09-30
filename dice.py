#DICE:
import random
roll=0
while True:
     dice1=random.randint(1,6)
     dice2=random.randint(1,6)
     roll=roll+1
     print(f"{roll=} {dice1=} {dice2=}")
     if dice1!=dice2:
          continue
     else:
          print(f"it took {roll} rolls to get a double")
          Break

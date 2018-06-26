import sys, os, random, time
import box


if len(sys.argv) != 3:
    print("We need exactly three three arguments. Please restart.")
    os._exist()

numbers_left = list(range(1,10))

start_time = time.time()
username = sys.argv[1]
time_length = float(sys.argv[2])
end_time = start_time + time_length

def get_roll(numbers_left):
    if sum(numbers_left)<= 6:
        #roll only one dice if remaining sum \leq 6
        return ramdom.randint(1, 6)
    else:
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        return roll1 + roll2


#Initialize the flags
no_choice = False
zero_left = False

while (time.time()<end_time):
    #while we have time remaining
    print("Numbers left: ", numbers_left)
    roll = get_roll(numbers_left)
    print("Roll: ", roll)


    #check if there exists choices to eliminate
    if box.isvalid(roll, numbers_left) == False:
        #the user loses
        no_choice = True
        break

    print("Seconds left: ", round(end_time - time.time(), 2))

    list_of_int = box.parse_input(input("Numbers to eliminate: "), numbers_left)
    #remove user's selection from the number list
    for i in list_of_int:
        numbers_left.remove(i)
    #if every element has been removed:
    if len(numbers_left)==0:
        zero_left = True
        break

if no_choice:
    print("Game over!", "\n")
    print("Score for player ", username, ": ", sum(numbers_left), " points")
    print("Time played: ", round(time.time()-start_time,2), " seconds")
    print('Better luck next time >:)')
elif zero_left:
    print("Score for player ", username, ": ",  "0 points")
    print("Time played: ", round(time.time()-start_time,2), " seconds")
    print("Congratulations!! You shut the box!")
else:
    #the case that running out of time
    print("Game over!", "\n")
    print("Score for player ", username, ": ", sum(numbers_left), " points")
    print("Time played: ", round(time.time()-start_time,2), " seconds")
    print('Better luck next time >:)')

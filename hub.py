import AASCII

# Robot selection
def main():
    global user_name
    user_name = input("What is your name? ")
    print("Chose your robot!")
    print("Robot A:")
    print(AASCII.robot_one())
    print("Robot B:")
    print(AASCII.robot_two())
    print("Robot C:")
    print(AASCII.robot_three())

    while True:
        global user_robot
        user_robot = input("Robot chosen:")
        if user_robot != "A" or user_robot != "B" or user_robot != "C":
           print("Please enter A or B or C")
        if user_robot == "A" or user_robot == "B" or user_robot == "C":
            break

    print("You have chosen: " + user_name + " Robot " + user_robot)
    return user_robot, user_name

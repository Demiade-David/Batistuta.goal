# import random

# max_turns = 6
# turn = 0
# secret = random.randint(1, 10) 

# while True:
#     p_choice = int(input("Enter a number between 1 and 10: "))
#     turn += 1
#     if p_choice == secret:
#         print(f"You win! The secret number was {secret}.")
#         break
#     elif turn >= max_turns:
#             print("You didn'pen guess any of the numbers. Your turns are over.")
#             break
#     else:
#             print(f"Wrong guess. Computer picked {secret}. Try again.")
#             print(f"You have {max_turns - turn} turns left.")
#             secret = random.randint(1, 10)
# try:
#    age= int(input("Enter your age: "))
#    if age >= 18:
#        print("You are eligible to drive.")
#    else:
#        print("You are not eligible to drive.")
# except:
#    print("Invalid input. Please enter a valid integer.")
# finally:
#     print("Execution completed.")
# def write_to_file():
#     try:
#         with open("text.txt", "a") as file:
#                 content= input("Enter some text to write to the file: ")
#                 file.write(f"\n{content}\n")
#     except:
#         print("An error occurred while writing to the file.")


# while True:
#     choice = input("Hello, welcome to the file writer program.\n Would you like to write to the file?\n 1. Yes\n 2. No\n")
#     if choice == '1':
#         write_to_file()

#     else:
#         print("Thank you! See you next time.")
#         break

# import turtle




# import turtle

# pen= turtle.Turtle()

# screen= turtle.Screen()

# pen.speed(0.5)
# pen.color("blue")
# screen.bgcolor("black") 
# screen.title("Simple Turtle Spiral Art")

# def draw_square():
#     for i in range(36):
#         pen.forward(100)
#         pen.right(90)


#     for i in range(36):
#         pen.circle(50)
#         pen.right(10)


# draw_art()



# # 1. Setup the screen
# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")  # Set background to black for contrast
# screen.title("Simple Turtle Spiral Art")

# # 2. Setup the turtle
# t = turtle.Turtle()
# t.speed(0)  # Set speed to fastest (0)

# # List of colors to use for the spiral
# # colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# # 3. Drawing the spiral
# for i in range(100):
#     # Change color every iteration
#     t.pencolor("white") 
    

#     t.forward(i * 3)
    
#     t.left(118)



# import turtle
# def draw_star(t, size, color):
#     t.pencolor(color)
#     t.begin_fill()
#     for _ in range(5):
#         t.forward(size)
#         t.right(144)
#     t.end_fill()

# # Now you can easily draw many stars:
# t = turtle.Turtle()
# t.penup()
# t.goto(-100, 0)
# t.pendown()
# draw_star(t, 50, "gold")

# t.penup()
# t.goto(50, 50)
# t.pendown()
# draw_star(t, 30, "red")

# import turtle

# pen= turtle.Turtle()

# pen.speed(0.5)
# pen.color("white")
# screen= turtle.Screen()
# screen.bgcolor("black")
# pen.hideturtle


# for i in range(i*4):
#     pen.forward(200)
#     pen.left(118)

# screen.mainloop
# screen.update



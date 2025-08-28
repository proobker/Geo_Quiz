import turtle
import os
import data
import write

screen = turtle.Screen()
dat = data.Data()
pen = write.Pen()
screen.title("Guess game")
image = ""
while True:
    choice = screen.textinput("Choose a state for game","""Enter\n 1. USA\n2. Nepal\n3. Europe
                            """)
    if choice == "usa":
        image = "img/blank_states_img.gif"
        dat.df = "data/50_states.csv"
        screen.setup(width=740, height=500)
        placement = "a state"
        break
    elif choice == "nepal":
        image = "img/nepal_map.gif"
        dat.df = "data/Nepal_Districts.csv"
        screen.setup(width=1024, height=700)
        placement = "a district"
        break
    elif choice == "europe":
        image = "img/europe.gif"
        dat.df = "data/europe_countries.csv"
        screen.setup(width=690, height=690)
        placement = "a country"
        break

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, image)
screen.bgpic(image_path)
dat.load()

game = True
total_states = dat.total
written_states = 0
i = 0

while game == True:
    # #auto fill mod
    # user = dat.state[i]
    # x = dat.getx(user)
    # y = dat.gety(user)
    # pen.enter(input=user, x_coor=x, y_coor=y, size=10)
    # dat.rmv(user)
    # written_states += 1
    # if written_states >= total_states:
    #     pen.enter(input="Map complete", x_coor=0, y_coor=600, size=20)
    #     game = False
    #     turtle.exitonclick()
    # i+=1
    user = screen.textinput(f"{written_states}/{total_states}", f"Enter name of {placement}").lower()
    if dat.check(user):
        x = dat.getx(user)
        y = dat.gety(user)
        pen.enter(input=user, x_coor=x, y_coor=y, size=10)
        dat.rmv(user)
        written_states += 1
        if written_states >= total_states:
            pen.goto(0,225)
            pen.write("Map is Complete", True, align="center", font=("Arial", 30, "bold"))
            game = False
            turtle.exitonclick()

turtle.mainloop()

# #collecting x and y coordinates of the districts of map
# import pandas
# import turtle
# import os
# import data
# import write

# screen = turtle.Screen()
# dat = data.Data()
# pen = write.Pen()
# screen.title("Guess game")
# screen.setup(width=690, height=690)
# image = "img/europe.gif"

# script_dir = os.path.dirname(os.path.abspath(__file__))
# image_path = os.path.join(script_dir, image)
# screen.bgpic(image_path)

# data = {
#     "state" : [],
#     "x" : [],
#     "y" : [],
# }

# collection = True

# def get_mouse_click_coor(x, y):
#     user = screen.textinput(f"hello", "Enter a name of a state").lower()
#     data["state"].append(user)
#     data["x"].append(int(x))
#     data["y"].append(int(y))
    
# while collection:
#     turtle.onscreenclick(get_mouse_click_coor)
#     c = input("c ")
#     if c == "Y":
#         collection = False
#         f = pandas.DataFrame(data)
#         f.to_csv("day 25 project\Guess the Place Game\data_collection.csv")
#         turtle.exitonclick()
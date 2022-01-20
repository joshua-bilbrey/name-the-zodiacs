import turtle
import pandas
from guessing_brain import find_nearest_zodiac, guess_zodiac
from time import sleep

FONT = ("Lucida Calligraphy", 12, "bold")
ALIGN = "center"
# ZODIACS = {
#     "Pisces": (-328.0, 5.0),
#     "Aquarius": (-283.0, 164.0),
#     "Capricorn": (-149.0, 271.0),
#     "Sagittarius": (-8.0, 305.0),
#     "Scorpio": (172.0, 249.0),
#     "Libra": (268.0, 164.0),
#     "Virgo": (312.0, 23.0),
#     "Leo": (253.0, -181.0),
#     "Cancer": (171.0, -267.0),
#     "Gemini": (1.0, -315.0),
#     "Taurus": (-165.0, -275.0),
#     "Aries": (-279.0, -149.0),
# }

screen = turtle.Screen()
screen.setup(width=832, height=832)
screen.tracer(0)
images = ["images/zodiacs.gif", "images/zodiacs_blank.gif", "images/zodiacs_aries.gif", "images/zodiacs_aquarius.gif",
          "images/zodiacs_cancer.gif",
          "images/zodiacs_capricorn.gif", "images/zodiacs_gemini.gif", "images/zodiacs_leo.gif",
          "images/zodiacs_libra.gif", "images/zodiacs_pisces.gif",
          "images/zodiacs_sagittarius.gif", "images/zodiacs_scorpio.gif", "images/zodiacs_taurus.gif",
          "images/zodiacs_virgo.gif"]
for image in images:
    screen.addshape(image)
turtle.shape("images/zodiacs_blank.gif")

zodiacs = pandas.read_csv("zodiac_data.csv")
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color("white")

game_on = True
guessed_zodiacs = []
missed_zodiacs = []
click_x_coor = 0
click_y_coor = 0


def get_coor(x, y):
    global click_x_coor, click_y_coor
    click_x_coor = x
    click_y_coor = y


turtle.onscreenclick(get_coor)
pen.goto(0, 380)
pen.write("Click on a constellation.", align=ALIGN, font=FONT)

while game_on:
    try:
        turtle.shape("images/zodiacs_blank.gif")
        click_x_coor = 0
        click_y_coor = 0
        screen.update()
        sleep(0.1)

        # if click coordinates are not zero find the nearest zodiac and update the screen
        if click_x_coor != 0 and click_y_coor != 0:
            nearest_zodiac = find_nearest_zodiac(click_x_coor, click_y_coor, zodiacs)
            turtle.shape(f"images/zodiacs_{nearest_zodiac.lower()}.gif")
            screen.update()

            # if user guesses the zodiac correctly add to list and write zodiac name near constellation
            if nearest_zodiac not in guessed_zodiacs:
                if guess_zodiac(nearest_zodiac, guessed_zodiacs, screen):
                    new_x = zodiacs[zodiacs.names == nearest_zodiac].x.item()
                    new_y = zodiacs[zodiacs.names == nearest_zodiac].y.item()
                    pen.goto(new_x, new_y)
                    pen.write(nearest_zodiac, align=ALIGN, font=FONT)
                    guessed_zodiacs.append(nearest_zodiac)

        # check if user has guessed all zodiacs
        if len(guessed_zodiacs) == 12:
            game_on = False
            pen.goto(0, 50)
            pen.write("Congratulations!", align=ALIGN, font=FONT)
    except turtle.Terminator:
        game_on = False

for name in zodiacs.names.to_list():
    if name not in guessed_zodiacs:
        missed_zodiacs.append(name)

zodiac_study = pandas.DataFrame(missed_zodiacs)
zodiac_study.to_csv("zodiac_study.csv")

# zodiacs = {
#     "names": ["Pisces", "Aquarius", "Capricorn", "Sagittarius", "Scorpio", "Libra", "Virgo", "Leo", "Cancer",
#               "Gemini", "Taurus", "Aries"],
#     "x": [],
#     "y": [],
# }
#
#
# def get_coor(x, y):
#     print(x, y)
#     zodiacs["x"].append(float(x))
#     zodiacs["y"].append(float(y))
#
#
# turtle.onscreenclick(get_coor)
#
#
#
#
# zodiac_data = pandas.DataFrame(zodiacs)
# zodiac_data.to_csv("zodiac_data.csv")

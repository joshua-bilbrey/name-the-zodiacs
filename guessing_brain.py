from math import sqrt


def find_nearest_zodiac(x_coor, y_coor, data_frame):
    if (x_coor, y_coor) != (0, 0):
        smallest_distance = 832
        for name in data_frame.names.to_list():
            x_distance = x_coor - data_frame[data_frame.names == name].x.item()
            y_distance = y_coor - data_frame[data_frame.names == name].y.item()
            total_distance = sqrt((x_distance * x_distance) + (y_distance * y_distance))
            if total_distance < smallest_distance:
                closest_zodiac = name
                smallest_distance = total_distance
        return closest_zodiac


def guess_zodiac(correct_answer, correct_guesses, turtle_screen):
    try:
        answer = turtle_screen.textinput(title=f"{len(correct_guesses)}/12 Zodiacs Correct",
                                         prompt="Which Zodiac is this?").title()
        return answer == correct_answer
    except AttributeError:
        return False

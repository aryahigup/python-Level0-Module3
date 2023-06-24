from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
window = Tk()
window.withdraw()
ans = simpledialog.askinteger(title='Story', prompt='You have the choice to enter one of the the following places. '
                                                    'Type the number you want to choose. 1) Cave 2) Cottage 3) Camper')
if ans == 1:
    ans = simpledialog.askinteger(title='Story', prompt='You walk into a cave, and come up to a fork in the tunnels. '
                                                        'Which do you choose? 1) left path with the sound of water 2) '
                                                        'right path with a soft glow emanating')
    if ans == 1:
        messagebox.showinfo(title='Story', message="You walk down the left path to find a magic boat in a small river. "
                                                   "You take the boat and go home.")
    elif ans == 2:
        messagebox.showinfo(title='Story', message="You take the right path and find glow worms on the walls of the "
                                                   "cave.")
elif ans == 2:
    messagebox.showinfo(title='Story', message="You enter the cabin and find a nice bed by a roaring fireplace. "
                                               "You take a nice nap in the warmth.")
elif ans == 3:
    messagebox.showinfo(title='Story', message="You enter the camper and set off on a road trip across the country, "
                                               "stopping at monuments along the way.")
pass
from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    ans1 = simpledialog.askstring(title='Are you happy', prompt='Are you happy? y or n')
    if ans1 == 'y':
        messagebox.showinfo(title='Are you happy', message="Keep doing what you're doing")
    elif ans1 == 'n':
        ans2 = simpledialog.askstring(title='Are you happy', prompt='Do you want to be happy? y or n?')
        if ans2 == 'y':
            messagebox.showinfo(title='Are you happy', message="Change something")
        elif ans2 == 'n':
            messagebox.showinfo(title='Are you happy', message="Keep doing what you're doing")
    pass

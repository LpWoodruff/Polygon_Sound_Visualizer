import tkinter as tk


class Ball_app:
    def __init__(self, master):
        color_primary = "grey"
        color_secondary = "White"

        # APP SPECIFIC INFO
        self.master = master
        master.title("Ball Sound Simulation")
        master.configure(bg=color_primary)
        master.geometry("1000x700")

        #The Top of the page
        self.top_frame = tk.Frame(master, bg=color_secondary) 

        self.SL_ball_num = tk.Scale(master, from_=0, to=100, orient='horizontal')
        self.SL_ball_num.pack()


        #Body
        self.body_frame = tk.Frame(master, bg=color_secondary)
        self.body_canvas = tk.Canvas(self.body_frame, bg=color_secondary,  width=700, height=900)


        self.body_frame.pack()
        self.body_canvas.pack()
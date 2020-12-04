import tkinter as tk

def timer(label_timer, time_remaining, end_page):
	if time_remaining > 0:
		label_timer.config(text = str(time_remaining))
		time_remaining -= 1
		label_timer.after(1000, lambda: timer(label_timer, time_remaining, end_page))
		return 0
	else:
		end_page()
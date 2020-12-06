import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
from tkinter.messagebox import showinfo
import datetime
import time
import os
os.system('cls')

# Creating the MAIN_APPLICATION:
main_application = tk.Tk()
main_application.geometry("750x500")
main_application.title("Notepad")

# CREATING, DESIGNING and ADDING FUNCTIONS to the MENU_BAR.

# Creating MENU_BAR:
main_menu = tk.Menu()

# Adding ICONS for MENU_BAR OPTIONS:

# 1) FILE_ICONS:
new_icon = tk.PhotoImage(file="resized/new.png")
open_icon = tk.PhotoImage(file="resized/open.png")
save_icon = tk.PhotoImage(file="resized/save.png")
save_as_icon = tk.PhotoImage(file="resized/save_as.png")
exit_icon = tk.PhotoImage(file="resized/exit.png")

# 2) EDIT_ICONS:
cut_icon = tk.PhotoImage(file="resized/cut.png")
copy_icon = tk.PhotoImage(file="resized/copy.png")
paste_icon = tk.PhotoImage(file="resized/paste.png")
clear_all_icon = tk.PhotoImage(file="resized/clear_all.png")
find_icon = tk.PhotoImage(file="resized/find.png")
find_and_replace_icon = tk.PhotoImage(file="resized/find_replace.png")

# 3) VIEW_ICONS:
tool_bar_icon = tk.PhotoImage(file="resized/tool_bar.png")
status_bar_icon = tk.PhotoImage(file="resized/status_bar.png")

# 4) COLOR_THEME_ICONS:
#light_theme_icon = tk.PhotoImage(file="resized/light_theme.png")
#darkula_theme_icon = tk.PhotoImage(file="resized/darkula_theme.png")

# 5) STATS:
created_time_icon = tk.PhotoImage(file="resized/created_time.png")
modified_time_icon = tk.PhotoImage(file="resized/modified_time.png")

# CREATING and ADDING the OPTIONS of the MENU_BAR:
# Creating:
file = tk.Menu(main_menu, tearoff=False)  # FILE
edit = tk.Menu(main_menu, tearoff=False)  # EDIT
view = tk.Menu(main_menu, tearoff=False)  # VIEW
# color_theme = tk.Menu(main_menu, tearoff=False)  # COLOR_THEME
stats = tk.Menu(main_menu, tearoff=False)  # STATS

# Adding:
main_menu.add_cascade(label="File", menu=file)  # FILE
main_menu.add_cascade(label="Edit", menu=edit)  # EDIT
main_menu.add_cascade(label="View", menu=view)  # VIEW
# main_menu.add_cascade(label="Color Theme", menu=color_theme)  # COLOR_THEME
main_menu.add_cascade(label="Stats", menu=stats)

# CREATING and ADDING FUNCTIONS to the OPTIONS of the MENU_BAR:
text_url = " "

# 1) FILE_FUNCTION:
# Creating:
# 1.1) NEW_FILE:


def new_file(event=None):
    global text_url
    text_url = " "
    text_editor.delete(1.0, tk.END)
# 1.2) OPEN_FILE:


def open_file(event=None):
    global text_url
    text_url = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title="select file", filetypes=(("Text file", "*.txt"), ("All files", "*.txt")))
    try:
        with open(text_url, "r") as for_read:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(text_url))
# 1.3) SAVE_FILE:


def save_file(event=None):
    global text_url
    try:
        if text_url:
            content = str(text_editor.get(1.0, tk.END))
            with open(text_url, "w", encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(
                ("Text file", "*.txt"), ("All files", "*.txt")))
            content2 = text_editor.get(1.0, tk.END)
            text_url.write(content2)
            text_url.close()
    except:
        return
# 1.4) SAVE_AS_FILE:


def save_as_file(event=None):
    global text_url
    try:
        content = text_editor.get(1.0, tk.END)
        text_url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(
            ("Text file", "*.txt"), ("All files", "*.txt")))
        text_url.write(content)
        text_url.close()
    except:
        return
# 1.5) EXIT_FILE:


def exit_fun(event=None):
    global text_url, text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel(
                "warning", "Do you want to save this file")
            if mbox is True:
                if text_url:
                    content = text_editor.get(1.0, tk.END)
                    with open(text_url, "w", encoding="utf-8") as for_read:
                        for_read.write(content)
                        main_application.destroy()
                else:
                    content2 = text_editor.get(1.0, tk.END)
                    text_url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(
                        ("Text file", "*.txt"), ("All files", "*.txt")))
                    text_url.write(content2)
                    text_url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return


# Adding:
file.add_command(label="New", image=new_icon, compound=tk.LEFT,
                 accelerator="Ctrl+N", command=new_file)
file.add_command(label="Open", image=open_icon, compound=tk.LEFT,
                 accelerator="Ctrl+O", command=open_file)
file.add_command(label="Save", image=save_icon, compound=tk.LEFT,
                 accelerator="Ctrl+S", command=save_file)
file.add_command(label="Save As", image=save_as_icon,
                 compound=tk.LEFT, accelerator="Ctrl+Alt+S", command=save_as_file)
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT,
                 accelerator="Ctrl+", command=exit_fun)

# 2) EDIT_FUNCTION:
# Creating:
# 2.5) FIND_FUNCTION:


def find_fun(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(
                    word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config(
                    'match', foreground="red", background="blue")

    find_popup = tk.Toplevel()
    find_popup.geometry("400x200")
    find_popup.title("Find Word")
    find_popup.resizable(0, 0)

    # Frame for Find
    find_frame = ttk.LabelFrame(find_popup, text="Find Word")
    find_frame.pack(pady=20)

    text_find = ttk.Label(find_frame, text="Find")  # LABEL
    find_input = ttk.Entry(find_frame, width=30)  # ENTRY BOX
    find_button = ttk.Button(find_frame, text="Find", command=find)  # BUTTON
    text_find.grid(row=0, column=0, padx=4, pady=4)  # TEXT LABEL GRID
    find_input.grid(row=0, column=1, padx=4, pady=4)  # ENTRY GRID
    find_button.grid(row=2, column=0, padx=8, pady=4)  # BUTTON GRID


# 2.6) FIND and REPLACE FUNCTION:
def find_and_replace_fun(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(
                    word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config(
                    "match", foreground="red", background="blue")

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_popup = tk.Toplevel()
    find_popup.geometry("400x200")
    find_popup.title("Find Word")
    find_popup.resizable(0, 0)

    # Frame for Find
    find_frame = ttk.LabelFrame(find_popup, text="Find and Replace word")
    find_frame.pack(pady=20)

    # LABEL
    text_find = ttk.Label(find_frame, text="Find")
    text_replace = ttk.Label(find_frame, text="Replace")

    # ENTRY BOX
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    # BUTTON
    find_button = ttk.Button(find_frame, text="Find", command=find)
    replace_button = ttk.Button(
        find_frame, text="Replace", command=replace)

    # TEXT LABEL GRID
    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)

    # ENTRY GRID
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    # BUTTON GRID
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)


# Adding:
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT,
                 accelerator="Ctrl+X", command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT,
                 accelerator="Ctrl+C", command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT,
                 accelerator="Ctrl+V", command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT,
                 accelerator="Ctrl+Alt+X", command=lambda: text_editor.delete(1.0, tk.END))
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT,
                 accelerator="Ctrl+F", command=find_fun)
edit.add_command(label="Find and Replace", image=find_and_replace_icon, compound=tk.LEFT,
                 command=find_and_replace_fun)

# 3) VIEW_FUNCTION:
# Creating:
show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_tool_bar = tk.BooleanVar()
show_tool_bar.set(True)
# 3.1) TOOL_BAR:


def hide_tool_bar():
    global show_tool_bar
    if show_tool_bar:
        tool_bar_label.pack_forget()
        show_tool_bar = False
    else:
        text_editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bars.pack(side=tk.BOTTOM)
        show_tool_bar = True
# 3.2) STATUS_BAR:


def hide_status_bar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False
    else:
        status_bars.pack(side=tk.BOTTOM)
        show_status_bar = True


# Adding:
view.add_checkbutton(label="Tool Bar", onvalue=True,
                     offvalue=0, variable=show_tool_bar, image=tool_bar_icon, compound=tk.LEFT, command=hide_tool_bar)
view.add_checkbutton(label="Status Bar", onvalue=True,
                     offvalue=0, variable=show_status_bar, image=status_bar_icon, compound=tk.LEFT, command=hide_status_bar)

# 4) COLOR_THEME:
# Creating:
#theme_choose = tk.StringVar()
#color_icons = (light_theme_icon, darkula_theme_icon)
# color_dict = {
#    'Light': ("#000000", "#ffffff"),
#    'Darkula': ("#6ad9d9", "#2b2e2e")
# }
# def change_theme():
#    get_theme = theme_choose.get()
#    color_tuple = color_dict.get(get_theme)
#    fg_color, bg_color = color_tuple[0], color_tuple[1]
#    text_editor.config(background=bg_color, foreground=fg_color)
# Adding:
#color_count = 0
# for color_name in color_dict:
#    color_theme.add_radiobutton(
#        label=color_name, image=color_icons[color_count], compound=tk.LEFT, command=change_theme)
#    color_count += 1

# 5) STATS:
# Creating:
# 5.1) CREATED_TIME:


def created_time():
    global text_url
    ctime = time.ctime(os.path.getctime(text_url))
    showinfo("Created time of the file is ", ctime)

    return os.stat(text_url).st_ctime

# 5.2) MODIFIED_TIME:


def modified_time():
    global text_url
    mtime = time.ctime(os.path.getmtime(text_url))
    showinfo("Modified time of the file is ", mtime)

    return os.stat(text_url).st_mtime


# Adding:
stats.add_command(label="Created time", image=created_time_icon,
                  compound=tk.LEFT, command=created_time)
stats.add_command(label="Modified time", image=modified_time_icon,
                  compound=tk.LEFT, command=modified_time)


# TOOL_BAR:

# Creating a TOOL_BAR:
tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP, fill=tk.X)

# CREATING & ADDING FUNCTIONS to the TOOL_BAR.

# 1) FONT FUNCTION:
# Adding:
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label, width=30,
                        textvariable=font_family, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5, pady=5)
# Creating:
font_now = "Arial"
font_size_now = 16


def change_font(main_application):
    global font_now
    font_now = font_family.get()
    text_editor.configure(font=(font_now, font_size_now))


font_box.bind("<<ComboboxSelected>>", change_font)

# 2) SIZE FUNCTION:
# Adding:
size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label, width=20,
                         textvariable=size_variable, state="readonly")
font_size["values"] = tuple(range(8, 100, 2))
font_size.current(6)
font_size.grid(row=0, column=1, padx=5)
# Creating:


def change_size(main_application):
    global font_size_now
    font_size_now = size_variable.get()
    text_editor.configure(font=(font_now, font_size_now))


font_size.bind("<<ComboboxSelected>>", change_size)

# 3) BOLD FUNCTION:
# Adding:
bold_icon = tk.PhotoImage(file="resized/bold.png")
bold_button = ttk.Button(tool_bar_label, image=bold_icon)
bold_button.grid(row=0, column=2, padx=5)
# Creating:
# print(tk.font.font(font=text_editor["font"]).actual())


def bold_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"] == "normal":
        text_editor.configure(font=(font_now, font_size_now, "bold"))
    if text_get.actual()["weight"] == "bold":
        text_editor.configure(font=(font_now, font_size_now, "normal"))


bold_button.configure(command=bold_fun)

# 4) ITALIC FUNCTION:
# Adding:
italic_icon = tk.PhotoImage(file="resized/italic.png")
italic_button = ttk.Button(tool_bar_label, image=italic_icon)
italic_button.grid(row=0, column=3, padx=5)
# Creating:


def italic_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"] == "roman":
        text_editor.configure(font=(font_now, font_size_now, "italic"))
    if text_get.actual()["slant"] == "italic":
        text_editor.configure(font=(font_now, font_size_now, "roman"))


italic_button.configure(command=italic_fun)

# 5) UNDERLINE FUNCTION:
# Adding:
underline_icon = tk.PhotoImage(file="resized/underline.png")
underline_button = ttk.Button(tool_bar_label, image=underline_icon)
underline_button.grid(row=0, column=4, padx=5)
# Creating:


def underline_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"] == 0:
        text_editor.configure(font=(font_now, font_size_now, "underline"))
    if text_get.actual()["underline"] == 1:
        text_editor.configure(font=(font_now, font_size_now, "normal"))


underline_button.configure(command=underline_fun)

# 6) ALIGN LEFT FUNCTION:
# Adding:
align_left_icon = tk.PhotoImage(file="resized/left_align.png")
align_left_button = ttk.Button(tool_bar_label, image=align_left_icon)
align_left_button.grid(row=0, column=5, padx=5)
# Creating:


def align_left():
    text_get_all = text_editor.get(1.0, "end")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "left")


align_left_button.configure(command=align_left)

# 7) ALIGN CENTER FUNCTION:
# Adding:
align_center_icon = tk.PhotoImage(file="resized/center_align.png")
align_center_button = ttk.Button(tool_bar_label, image=align_center_icon)
align_center_button.grid(row=0, column=6, padx=5)
# Creating:


def align_center():
    text_get_all = text_editor.get(1.0, "end")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "center")


align_center_button.configure(command=align_center)

# 8) ALIGN RIGHT FUNCTION:
# Adding:
align_right_icon = tk.PhotoImage(file="resized/right_align.png")
align_right_button = ttk.Button(tool_bar_label, image=align_right_icon)
align_right_button.grid(row=0, column=7, padx=5)
# Creating:


def align_right():
    text_get_all = text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_get_all, "right")


align_right_button.configure(command=align_right)

# 9) FONT_COLOR_BUTTON:
# Adding:
font_color_icon = tk.PhotoImage(file="resized/font_color.png")
font_color_button = ttk.Button(tool_bar_label, image=font_color_icon)
font_color_button.grid(row=0, column=8, padx=5)
# Creating:


def Color_choose():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_button.configure(command=Color_choose)

# TEXT_EDITOR:

# Creating TEXT_EDITOR:
text_editor = tk.Text(main_application)
text_editor.config(wrap="word", relief=tk.FLAT)

# Creating SCROLL_BAR:
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Creating STATUS BAR with WORD and CHARACTER COUNT:
# Adding:
status_bars = ttk.Label(main_application, text="Status Bar")
status_bars.pack(side=tk.BOTTOM)
# Creating:
text_change = False


def change_word(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        word = len(text_editor.get(1.0, "end-1c").split())
        character = len(text_editor.get(1.0, "end-1c").replace(" ", ""))
        status_bars.config(text=f"charater :{character} word :{word}")
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", change_word)


# The below line adds the entire "Menu" function to our main_application.
main_application.config(menu=main_menu)

main_application.mainloop()

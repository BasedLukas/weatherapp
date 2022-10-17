import tkinter as tk
import configs
import functions as f
from PIL import ImageTk, Image


def mainwindow():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry = "750x750"
    root.iconbitmap("app_icon.ico")

    # create welcome text
    welcome = tk.Label(root, text="Welcome to the weather app", font=20,pady=20, padx= 20)

    # Create menu using city list from configs
    selection = tk.StringVar()
    selection.set(" \n  Choose A City  \n ")
    menu = tk.OptionMenu(root, selection , *configs.city_names)

    # Create ok button command
    def popup():
        # Disable OK button until a city is selected
        city = selection.get()
        if "Choose A City" in city:
            return

        # Call API using selected city
        data = f.gui_api_call(city)
        report = f.format_data_to_string(data)
        f.download_icon(data)

        # Create toplevel box
        popup_box= tk.Toplevel()
        popup_box.iconbitmap("app_icon.ico")
        popup_box.title(f"{city} weather")

        # open image
        # global is used due to a bug in tkinter. The garbage collector deletes img if it is not referenced somewhere else
        im = Image.open("icon.png")
        global img
        img = ImageTk.PhotoImage(im)
        image_label = tk.Label(popup_box, image=img)
        image_label.configure(background="#add8e6")
        image_label.pack(side=tk.TOP)

        tk.Label(popup_box, text= report, font=('Mistral 14')).pack(side=tk.TOP)
        tk.Button(popup_box, text="OK", command=popup_box.destroy).pack(side=tk.BOTTOM,pady=30,ipady=30, ipadx=20)

    # create ok button
    ok = tk.Button(root, text="OK",command=popup, padx=5, pady=5)

    # create quit button
    quitbutton = tk.Button(root, text="QUIT", command=root.destroy,padx=5, pady=5)

    # Pack all the widgets in
    welcome.pack(side=tk.TOP) #Label
    menu.pack(side=tk.TOP, pady=50, ipady=5, ipadx=10 ) #OptionMenu
    ok.pack(side=tk.LEFT, padx=75, pady=50, ipady=10, ipadx=10)   #Button
    quitbutton.pack(side=tk.RIGHT, padx=75, pady=50, ipady=10, ipadx=10) #Button

    root.mainloop()









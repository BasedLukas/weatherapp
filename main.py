def launch_gui():
    import gui
    gui.mainwindow()
    quit()
def launch_cli():
    import functions as f
    list_of_cities = f.city_list()
    # If user imputs incorrect values we return to main menu
    try:
        city, country = f.search_cities(list_of_cities)
    except:
        return
    data = f.api_call(city, country)
    weather = f.format_data_to_string(data)
    print(weather)



while True:
    print("select an option")
    print("1 Launch CLI")
    print("2 Launch GUI")
    print("0 Quit")
    selection = input("")
    if selection == "0":
        print("Goodbye")
        break
    elif selection == "1":
        print("Loading...")
        launch_cli()
    elif selection == "2":
        launch_gui()
    print()


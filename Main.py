from tkinter import messagebox
import sqlite3
from tkinter import *
from tkinter import filedialog
import webbrowser
from pynput.keyboard import Key, KeyCode, Listener
import threading
import time
from tkinter.font import Font
from functools import partial
from tkinter import ttk

conn = sqlite3.connect('Report_Counter.db', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Stats(ID INT, Name TEXT, Detail RAEL)''')
c.execute('''CREATE TABLE IF NOT EXISTS Commands(ID INT, Name TEXT, Detail RAEL)''')


c.execute("SELECT COUNT(ID) FROM Stats")
if (c.fetchall()[0][0]) == 0:
    c.execute('''INSERT INTO Stats(ID, Name, Detail) VALUES(?, ? ,?)''',(1, 'Report Count', 0))
    c.execute('''INSERT INTO Stats(ID, Name, Detail) VALUES(?, ? ,?)''',(2, '+1 KeyBind', 105))
    c.execute('''INSERT INTO Stats(ID, Name, Detail) VALUES(?, ? ,?)''',(3, '-1 KeyBind', 102))
    conn.commit()
else:
    print("No setup had to be done")

global Count

c.execute("SELECT Detail FROM Stats WHERE ID=1")
Count = (c.fetchall()[0][0])



STOP = 0


def Run():
    def Main():
        Page1 = Tk()
        Page1.title("Elite Sit Counter")
        Page1.configure(background="#BEBEBE")
        Page1.geometry("+200+200")
        # Page1.attributes("-fullscreen", True)
        # Page1.attributes("-topmost", True)

        myFont = Font(family="Times New Roman", size=20)

        def Edit_KeyBind():
            Page2 = Toplevel()
            Page2.title("Elite Sit Counter")
            Page2.configure(background="#BEBEBE")
            Page2.geometry("+250+250")
            Page2.transient([Page1])

            Keys = {"a": "65", "b": "66", "c": "67", "d": "68", "e": "69", "f": "70", "g": "71", "h": "72", "i": "73", "j": "74", "k": "75", "l": "76", "m": "77", "n": "78", "o": "79", "p": "80", "q": "81", "r": "82", "s": "83", "t": "84", "u": "85", "v": "86", "w": "87", "x": "88", "y": "89", "z": "90", "f1": "112", "f2": "113", "f3": "114", "f4": "115", "f5": "116", "f6": "117", "f7": "118", "f8": "119", "f9": "120", "f10": "121", "f11": "122", "f12": "123", "-": "189", "=": "187", "1": "49", "2": "50", "3": "51", "4": "52", "5": "53", "6": "44", "7": "45", "8": "46", "9": "47", "0": "48", "kp_end": "97", "kp_downarrow": "98", "kp_pgdn": "99", "kp_leftarrow": "100", "kp_5": "101", "kp_rightarrow": "102", "kp_home": "103", "kp_uparrow": "104", "kp_pgup": "105"}

            key_list = list(Keys.keys())
            val_list = list(Keys.values())

            Label(Page2, text="KeyBind +1", bd=2).grid(row=0,column=0,pady=2,sticky='e')
            combo1 = ttk.Combobox(Page2, values=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', '-', '=', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'kp_end', 'kp_downarrow', 'kp_pgdn', 'kp_leftarrow', 'kp_5', 'kp_rightarrow', 'kp_home', 'kp_uparrow', 'kp_pgup'])
            combo1.grid(column=1, row=0)

            Label(Page2, text="KeyBind -1", bd=2).grid(row=1,column=0,pady=2,sticky='e')
            combo2 = ttk.Combobox(Page2, values=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', '-', '=', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'kp_end', 'kp_downarrow', 'kp_pgdn', 'kp_leftarrow', 'kp_5', 'kp_rightarrow', 'kp_home', 'kp_uparrow', 'kp_pgup'])
            combo2.grid(column=1, row=1)

            c.execute("SELECT Detail FROM Stats WHERE ID=2")
            Val1 = (str(c.fetchall()[0][0]))
            Val11 = (list(Keys).index(str(key_list[val_list.index(Val1)])))

            c.execute("SELECT Detail FROM Stats WHERE ID=3")
            Val2 = (str(c.fetchall()[0][0]))
            Val21 = (list(Keys).index(str(key_list[val_list.index(Val2)])))

            combo1.current(Val11)
            combo2.current(Val21)

            def Update():
                Num1 = Keys[(combo1.get())]
                c.execute("UPDATE Stats SET Detail=? WHERE ID=2",(Num1,))
                Num2 = Keys[(combo2.get())]
                c.execute("UPDATE Stats SET Detail=? WHERE ID=3",(Num2,))
                conn.commit()
                Page2.destroy()
                Page1.destroy()
                Run()

            B01 = Button(Page2, text="Done", font=myFont, fg="Black", bg="Green", command=Update, bd=2)
            B01.grid(row=2,column=1)

        menubar = Menu(Page1)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Edit KeyBinds", command=Edit_KeyBind)
        menubar.add_cascade(label="File", menu=filemenu)

        filemenu.add_separator()

        Page1.config(menu=menubar)



        def Close():
            STOP = 1
            Page1.destroy()
            conn.close()
            # thread.exit()
            # listener.exit()

        Message_var = StringVar()
        label0 = Label(Page1, textvariable=Message_var, width=29)
        label0.grid(row=1,column=0)
        label0.configure(font=myFont)

        try:
            response = requests.get('https://raw.githubusercontent.com/connorhess/Report-Counter/master/Message.txt')
            Message = response.text
            Message_var.set(Message)
        except:
            Message_var.set("Offline/No Message")


        B0 = Button(Page1, text="Exit (Use This One to Close Program)", font=myFont, width=29, height=1, fg="Black", bg="Red", command=Close, bd=2)
        B0.grid(row=0,column=0)


        frame_width = 445
        frame_height1 = 100
        frame_height2 = 260

        F1 = Frame(Page1, height=frame_height1, width=frame_width, bg="#E9E9E9", relief="raise")
        F1.grid(row=2,column=0)
        F1.grid_propagate(0)


        label1 = Label(F1, text='Total Sits: ', anchor='e', pady=4)
        label1.grid(row=0,column=0,sticky='e', pady=(0, 5))
        label1.configure(font=myFont)

        Stats = StringVar()
        label2 = Label(F1, textvariable=Stats, anchor='w', pady=4)
        label2.grid(row=0,column=1,sticky='w', pady=(0, 5))
        label2.configure(font=myFont)

        label3 = Label(F1, text='Sits Needed: ', anchor='e', pady=4)
        label3.grid(row=1,column=0,sticky='e', pady=5)
        label3.configure(font=myFont)

        Sits_from_80 = StringVar()
        label4 = Label(F1, textvariable=Sits_from_80, anchor='w', pady=4)
        label4.grid(row=1,column=1,sticky='w', pady=5)
        label4.configure(font=myFont)

        c.execute("SELECT Detail FROM Stats")
        count = (c.fetchall()[0][0])
        Stats.set(count)
        Sits_from_80.set((80-int(count)))

        def update():
            # c.execute("SELECT Detail FROM Stats")
            # count = (c.fetchall()[0][0])
            print(Count)
            Stats.set(Count)

        def Web_browser_forums():
            new = 2
            webbrowser.open("https://elitelupus.com/forums/",new=new)

        def WB_open(Url):
            new = 2
            webbrowser.open(Url,new=new)

        B1 = Button(F1, text="Search Ban", font=myFont, width=12, height=1, fg="white", bg="green", command=partial(WB_open,"https://elitelupus.com/bans/search/"), bd=2)
        B1.grid(row=0,column=3)

        B2 = Button(F1, text="Forums", font=myFont, width=12, height=1, fg="white", bg="green", command=Web_browser_forums, bd=2)
        B2.grid(row=1,column=3)



        F2 = Frame(Page1, height=frame_height2, width=frame_width, bg="#E9E9E9", relief="raise")
        F2.grid(row=3,column=0)
        F2.grid_propagate(0)

        myFont2 = Font(family="Times New Roman", size=14)
        width2 = 14
        BG = "light green"
        FG = "black"
        FG2 = "Black"
        BG2 = "White"
        FG3 = "Red"
        BG3 = "Grey"

        B3 = Button(F2, text="Ban Appeal", font=myFont2, width=width2, height=1, fg=FG, bg=BG, command=partial(WB_open,"https://elitelupus.com/forums/forumdisplay.php?fid=15"), bd=2)
        B3.grid(row=0,column=0)

        B4 = Button(F2, text="Warn Appeal", font=myFont2, width=width2, height=1, fg=FG, bg=BG, command=partial(WB_open,"https://elitelupus.com/forums/forumdisplay.php?fid=25"), bd=2)
        B4.grid(row=0,column=1)

        B5 = Button(F2, text="Staff Applications", font=myFont2, width=width2, height=1, fg=FG, bg=BG, command=partial(WB_open,"https://elitelupus.com/forums/forumdisplay.php?fid=14"), bd=2)
        B5.grid(row=0,column=2)


        B6 = Button(F2, text="Player Reports", font=myFont2, width=width2, height=1, fg=FG, bg=BG, command=partial(WB_open,"https://elitelupus.com/forums/forumdisplay.php?fid=16"), bd=2)
        B6.grid(row=1,column=0)

        B7 = Button(F2, text="Rules", font=myFont2, width=width2, height=1, fg=FG, bg=BG, command=partial(WB_open,"https://elitelupus.com/forums/showthread.php?tid=6355"), bd=2)
        B7.grid(row=1,column=1)

        B8 = Button(F2, text="Job Rules", font=myFont2, width=width2, height=1, fg=FG, bg=BG, command=partial(WB_open,"https://elitelupus.com/forums/showthread.php?tid=8627"), bd=2)
        B8.grid(row=1,column=2)


        B9 = Button(F2, text="Staff Reports", font=myFont2, width=width2, height=1, fg=FG, bg=BG, command=partial(WB_open,"https://elitelupus.com/forums/forumdisplay.php?fid=17"), bd=2)
        B9.grid(row=2,column=0)



        B10 = Button(F2, text="Report Issue", font=myFont2, width=width2, height=1, fg=FG2, bg=BG2, command=partial(WB_open,"https://github.com/connorhess/Report-Counter/issues/new?labels=bug"), bd=2)
        B10.grid(row=3,column=0)

        B11 = Button(F2, text="New Suggestion", font=myFont2, width=width2, height=1, fg=FG2, bg=BG2, command=partial(WB_open,"https://github.com/connorhess/Report-Counter/issues/new?labels=enhancement"), bd=2)
        B11.grid(row=3,column=1)

        B12 = Button(F2, text="Info", font=myFont2, width=width2, height=1, fg=FG2, bg=BG2, command=partial(WB_open,"https://www.node-s.co.za/products/report-counter"), bd=2)
        B12.grid(row=3,column=2)


        # B13 = Button(F2, text="Donate", font=myFont2, width=width2, height=1, fg=FG2, bg=BG2, command=partial(WB_open,"https://pay.yoco.com/node-s?reference=Donate"), bd=2)
        # B13.grid(row=4,column=0)


        B14 = Button(F2, text="Join Server 1", font=myFont2, width=width2, height=1, fg=FG3, bg=BG3, command=partial(WB_open,"steam://connect/54.37.246.36:27015"), bd=2)
        B14.grid(row=5,column=0)

        B15 = Button(F2, text="Join Server 2", font=myFont2, width=width2, height=1, fg=FG3, bg=BG3, command=partial(WB_open,"steam://connect/54.37.246.36:27016"), bd=2)
        B15.grid(row=5,column=1)

        B16 = Button(F2, text="Join Server 3", font=myFont2, width=width2, height=1, fg=FG3, bg=BG3, command=partial(WB_open,"steam://connect/54.37.246.36:27017"), bd=2)
        B16.grid(row=5,column=2)


        B17 = Button(F2, text="Join Server 4", font=myFont2, width=width2, height=1, fg=FG3, bg=BG3, command=partial(WB_open,"steam://connect/gmod-drp1-usa.elitelupus.com:27015"), bd=2)
        B17.grid(row=6,column=0)

        B18 = Button(F2, text="Join Server 5", font=myFont2, width=width2, height=1, fg=FG3, bg=BG3, command=partial(WB_open,"steam://connect/gmod-drp2-usa.elitelupus.com:27015"), bd=2)
        B18.grid(row=6,column=1)

        B19 = Button(F2, text="Join Server 6", font=myFont2, width=width2, height=1, fg=FG3, bg=BG3, command=partial(WB_open,"steam://connect/gmod-drp3-usa.elitelupus.com:27015"), bd=2)
        B19.grid(row=6,column=2)


        B20 = Button(F2, text="Join Server 7", font=myFont2, width=width2, height=1, fg=FG3, bg=BG3, command=partial(WB_open,"steam://connect/139.99.233.75:27015"), bd=2)
        B20.grid(row=7,column=0)





        def Animate():
            while True:
                if STOP == 1:
                    thread.exit()
                time.sleep(0.2)
                # c.execute("SELECT Detail FROM Stats")
                # count = (c.fetchall()[0][0])
                Sits_from_80.set((80-int(Count)))
                Stats.set(Count)

        thread = threading.Thread(target=Animate)
        thread.setDaemon(True)
        thread.start()

        Page1.mainloop()


    thread = threading.Thread(target=Main)
    thread.setDaemon(True)
    thread.start()

    def Add_count():
        c.execute("SELECT Detail FROM Stats WHERE ID=1")
        Current = (c.fetchall()[0][0])

        global Count
        Count = Current

        if Current >= 0:
            New = Current + 1
        else:
            New = 1

        Count += 1

        c.execute("UPDATE Stats SET Detail=? WHERE ID=1",(New,))
        conn.commit()

    def Remove_count():
        c.execute("SELECT Detail FROM Stats WHERE ID=1")
        Current = (c.fetchall()[0][0])

        global Count
        Count = Current

        if Current >= 0:
            New = Current - 1
        else:
            New = 0

        Count -= 1

        c.execute("UPDATE Stats SET Detail=? WHERE ID=1",(New,))
        conn.commit()




    # Create a mapping of keys to function (use frozenset as sets/lists are not hashable - so they can't be used as keys)
    # Note the missing `()` after function_1 and function_2 as want to pass the function, not the return value of the function
    c.execute("SELECT Detail FROM Stats WHERE ID=2")
    Keybind1 = (c.fetchall()[0][0])
    c.execute("SELECT Detail FROM Stats WHERE ID=3")
    Keybind2 = (c.fetchall()[0][0])
    combination_to_function = {
        frozenset([KeyCode(vk=Keybind1)]): Add_count,  # Add 1
        frozenset([KeyCode(vk=Keybind2)]): Remove_count,  # Remove 1
    }


    # The currently pressed keys (initially empty)
    pressed_vks = set()


    def get_vk(key):
        """
        Get the virtual key code from a key.
        These are used so case/shift modifications are ignored.
        """
        return key.vk if hasattr(key, 'vk') else key.value.vk


    def is_combination_pressed(combination):
        """ Check if a combination is satisfied using the keys pressed in pressed_vks """
        return all([get_vk(key) in pressed_vks for key in combination])


    def on_press(key):
        """ When a key is pressed """
        vk = get_vk(key)  # Get the key's vk
        pressed_vks.add(vk)  # Add it to the set of currently pressed keys

        for combination in combination_to_function:  # Loop through each combination
            if is_combination_pressed(combination):  # Check if all keys in the combination are pressed
                combination_to_function[combination]()  # If so, execute the function


    def on_release(key):
        """ When a key is released """
        vk = get_vk(key)  # Get the key's vk
        pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys


    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

Run()

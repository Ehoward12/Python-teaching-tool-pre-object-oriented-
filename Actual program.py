#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ehoward
#
# Created:     13/11/2014
# Copyright:   (c) ehoward 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
#import all relevant tkinter information
#import Tkinter as tk, tkColorChooser, tkFileDialog, time
#import tk for the use of text boxes within a canvas, import colour choose for RGB select, import file dialog for loading and saving
#from tkFileDialog import askopenfilename
#import this specifically for use of opening and getting values

#_______________________________________________________________________________

#define the size of the screen, not canvas
master = Tk()
#main window for everything
master.geometry("800x600+300+150")
#Question mark button import
image1 = PhotoImage(file="q.gif")
#creates the alphabet for further use
alphabet = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
#stores default label coordiantes
CheckList = [[[50, 17], [150, 17], [250, 17], [350, 17]], [[50, 150], [150, 250], [250, 350], [350, 450]]]
#stores information on certain widgets used within the code
Widgetlist = [[[["#0000E6", "Width", "white", "3", "sunken", "100", "100", "150", "25"], ["#0000E6", "Height", "white", "3", "sunken", "100", "225", "150", "25"], ["#0000E6", "Colour depth", "white", "3", "sunken", "100", "350", "150", "25"]] ,
[["#0000E6", "white", "300", "100", "400", "25"], ["#0000E6", "white", "300", "225", "400", "25"]], [[]]]]
#stores all possible hexadecimal values to use when converting hex to binary
Hexlist = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
#stores all possible 4 bit binary values for use when converting binary to hex
Binlist = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
#place of storage for all widgets created through the use of widgetlist
WidgetStore = [[[], [], []], [[], []]]
#is used to show which window the program is currently in, defaults to 0
check = 0
#Used to show which window it is going to after clicking one of the navigational buttons found in the defaultbuttons function
t = 0
#makevars is used to check if it has created the variables needed for a bitmap yet, such as width and height
MakeVars = 0
#used as a variable to check if entry boxes have been filled in
Userinput = 0
#defines a list to store all of the colour variables for each pixel in hexadecimal
PixelCollist = []
#Each coordinate list stores the coordinate of a corner of a pixel for each pixel, is used later when switching windows
PixelXcoord1list = []
PixelYcoord1list = []
PixelXcoord2list = []
PixelYcoord2list = []
GoldenRectangleinfo = []
#global all of the variables defined so that they are recognised by other functions
global check, t, MakeVars, Userinput, PixelCollist, Hexlist, Binlist, Either, GoldenRectangleinfo
#_______________________________________________________________________________

#A function used to create all labels with data stored within the widgetlist
def CreateLabel(LabelLocation, LocationSet):
    for i in range(0, len(Widgetlist[t][0])):
        if LocationSet[i] == Place:
            WidgetStore[0][i] = Label(LabelLocation[i], bg=Widgetlist[t][0][i][0], text=Widgetlist[t][0][i][1], fg=Widgetlist[t][0][i][2], borderwidth=int(Widgetlist[t][0][i][3]), relief=Widgetlist[t][0][i][4])
            WidgetStore[0][i].place(x=int(Widgetlist[t][0][i][5]), y=int(Widgetlist[t][0][i][6]), width=int(Widgetlist[t][0][i][7]), height=int(Widgetlist[t][0][i][8]))
#_______________________________________________________________________________

#A function used to create all entry boxes with data stored within the widgetlist
def CreateEntry(vcmd):
    for i in range(0, len(Widgetlist[t][1])):
        WidgetStore[1][i] = Entry(master, bg=Widgetlist[t][1][i][0], borderwidth=0, fg=Widgetlist[t][1][i][1], validate="key", validatecommand=vcmd)
        WidgetStore[1][i].place(x=Widgetlist[t][1][i][2], y=Widgetlist[t][1][i][3], width=Widgetlist[t][1][i][4], height=Widgetlist[t][1][i][5])
#_______________________________________________________________________________

#class used for creating the start window and validating its entry boxes
class Initiation():
    #default window
    def CreateBitmapWindow(self):
        #used to delete all objects on screen if it is trying to get to this window
        if t == 1:
            WidgetReplace()
        #makes check equal to 0 so that it recognises that it is within this window
        check = 0
        #hexcheck is equal to 0 so that it recognises that it did not come from the hex window
        HexCheck = 0
        #hexcheck is equal to 0 so that it recognises that it did not come from the binary window
        BinCheck = 0
        #imports the image for the generate bitmap button background
        image2 = PhotoImage(file="green.gif")
        #imports the image for the background of the create bitmap window
        background = PhotoImage(file="Tkinterbackground.gif")
        #variable for the colour depth option menu, contains what is currently being displayed on the menu title
        var2 = StringVar(master)
        var2.set("Please select a colour depth")
        #converts master for self for class purposes
        self.master = master
        #creates a variable for validating text boxes, each value represents something from a text box
        vcmd = (self.master.register(self.OnValidate),
        '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        #creates the background using previously imported image
        BackgroundLabel = Label(master, image=background)
        BackgroundLabel.pack()
        #goes to the create label command to create labels using the window as locals
        CreateLabel([master, master, master], [Place, Place, Place])
        #creates entry passing through the validation values for use when creating them
        CreateEntry(vcmd)
        #defined as these so that they can be used to get the value of them when user has input values
        self.WidthInputBox = WidgetStore[1][0]
        self.HeightInputBox = WidgetStore[1][1]
        #creates optionmenu along with possible options
        ColourDepthOption = OptionMenu(master, var2, "1 bit (Monotone)", "2 Bit                                                                                                               ", "3 Bit", "4 Bit", "6 Bit", "8 Bit", "15 Bit", "24 Bit (RGB)")
        #configurates the colour of the text and the background
        ColourDepthOption.config(bg="#0000E6", fg="white")
        #configures the actual drop down bar
        ColourDepthOption["menu"].config(bg="#0000E6", fg="white")
        #places the menu in this position
        ColourDepthOption.place(x = 300, y = 350, width=400, height=25)
        #creates the helpbutton which upon click will transport the user to the help window
        HelpButton = Button(master, image=image1, relief="raised", command=lambda: Help())
        HelpButton.place(x = 100, y = 508, height=45)
        #creates the generate bitmap button which upon click will trasport the user to the bitmap tab and changes the value of t for further use
        CreateBitmapButton = Button(master, text="Generate bitmap", image=image2, relief="raised", command=lambda t=1: BitmapValidation(self.WidthInputBox, self.HeightInputBox, var2))
        CreateBitmapButton.place(x = 300, y = 508, width=400, height=45)
        #adds these variables to the widgetlist, contains values of what will be destroyed when moving to a new window
        WidgetList = [BackgroundLabel, WidgetStore[1][0], WidgetStore[1][1], WidgetStore[0][0], WidgetStore[0][1], WidgetStore[0][2], ColourDepthOption, HelpButton, CreateBitmapButton]
        #makes this variable equal to 0 which means that this will be the first time it will be creating the pixels
        l=0
        #globals all of the variables used in this function to be used at later occasions
        global WidgetList, check, l, HexCheck, BinCheck
        #send it to define the default buttons
        DefaultButtons(master)
        master.mainloop()
#_______________________________________________________________________________

    #this function checks all text entered in the text boxes for anything that shouldn't be allowed, all values from vcmd are brought in through the parameters
    def OnValidate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        #checks to see if text entered is characters and not numbers or symbols
        if text in '0123456789':
            #checks that the length of the value if allowed is not over 100, not equal to zero and can be converted into a float, if not it will not allow the values to be entered
            if len(value_if_allowed) > 0:
                if int(value_if_allowed) > 95:
                    return False
                if value_if_allowed[0] == "0":
                    return False
            if len(value_if_allowed) == 0:
                return True
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
#_______________________________________________________________________________

#checks for empty user inputs from the create bitmap tab
def BitmapValidation(WidthInputBox, HeightInputBox, var2):
    Hexget = []
    Binget = []
    #binget and hexget are defined as empty lists, used later to store the data of each text box containing binary and hex values
    ColourDepth = var2.get()
    Width=WidthInputBox.get()
    Height=HeightInputBox.get()
    #values from each user input on the create bitmap tab is put into variables
    if Width == "":
        Width = 0
    elif Height == "":
        Height = 0
    #checks to see if the values are empty or have not been filled in
    if ColourDepth == "Please select a colour depth" or Width == "" or Height == "":
        error()
    #if the colour depth has not been input, the program brings up an error
    else:
        #goes through a loop to append an empty, editable location for each pixel with binary and hex
        for i in range(0, int(Width)*int(Height)):
            Hexget.append(None)
            Binget.append(None)
            #globals all above variables to be used in a later function
            global ColourDepth, Width, Height, Hexget, Binget
        #destroys all of the widgets on screen
        WidgetReplace()
        #make vars is equal to 1 as it has now created the information needed for each pixel
        MakeVars = 1
        #transports it to the bitmap window
        BitmapWindow(Width, Height, ColourDepth, MakeVars)
#_______________________________________________________________________________

#second window/tab, displays the actual bitmap once created, all values from create bitmap screen are taken through the parameters so that the value of them can be used
def BitmapWindow(Width, Height, ColourDepth, MakeVars):
    #another background is imported and placed
    background1 = PhotoImage(file="Tkinterbackground2.gif")
    Background1 = Label(master, image=background1)
    Background1.background1 = background1
    Background1.place(x=0, y=0)
    #a bitmap has not been loaded and therefore loadcheck is set to 0
    LoadCheck = 0
    #RGB button is placed, set automatically to diabled which is overwritten if the user selected 24 bits
    RGB = Button(master, text="RGB", bg="white", state=DISABLED, borderwidth=2, command=lambda: RGBselect())

    #checks which colour depth has been chosen and chooses the contents of the optionmenu accordingly, these are colours which the user can create on the binary tab by chnaging values
    if ColourDepth == "1 bit (Monotone)":
        DepthCheck = 1
        ColourList = ["White                                                                                                            ","Black"]
    elif ColourDepth == "3 Bit":
        DepthCheck = 3
        ColourList = ["White                                                                                                            ","Black", "Brown", "Lime Green", "Light Pink", "Sky Blue"]
    elif ColourDepth == "6 Bit":
        DepthCheck = 6
        ColourList = ["White                                                                                                            ","Black", "Brown", "Lime Green", "Light Pink", "Sky Blue", "Moss Green", "Dark Purple", "Dark Red"]
    elif ColourDepth == "15 Bit":
        DepthCheck = 15
        ColourList = ["White                                                                                                            ","Black", "Brown", "Lime Green", "Light Pink", "Sky Blue", "Moss Green", "Dark Purple", "Dark Red"]
    elif ColourDepth == "8 Bit":
        DepthCheck = 8
        ColourList = ["White                                                                                                            ","Black", "Grey", "Light Grey", "Dark Grey"]
    elif ColourDepth == "2 Bit                                                                                                               ":
        DepthCheck = 2
        ColourList = ["White                                                                                                            ","Black", "Grey"]
    elif ColourDepth == "4 Bit":
        DepthCheck = 4
        ColourList = ["White                                                                                                            ","Black", "Grey", "Light Grey", "Dark Grey"]
    elif ColourDepth == "24 Bit (RGB)":
        DepthCheck = 24
        ColourList = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Black", "White                                                                                                            "]
        #makes it so that the RGB button is not diabled
        RGB = Button(master, text="RGB", bg="white", state=NORMAL, borderwidth=2, command=lambda: RGBselect())

    #makes a button that defaults to the brush tool but passes to a function which chnages the text to fill when clicked
    FillButton = Button(master, text="Brush", bg="white", borderwidth=2, command=FillSwitch)
    FillButton.place(x=150, y=50, width=50)
    #used as a grey background for the golden spiral button
    Blueback = Label(master, bg="#0000E6", borderwidth=0)
    Blueback.place(x=706, y=0, height=21, width=100)
    #creates a button which upon click, will send to the create golden spiral grid function, is disabled if width or height is less than 10
    if int(Width) < 10 or int(Height) < 10 or Width != Height:
        GoldenSpiralButton = Button(master, text="Golden Spiral", bg="gold", fg="black", borderwidth=0, state=DISABLED, command=lambda: CreateSpiralStructure(0, 0, int(Width), int(Height), 0, 1, 0))
    else:
        GoldenSpiralButton = Button(master, text="Golden Spiral", bg="gold", fg="black", borderwidth=0, state=NORMAL, command=lambda: CreateSpiralStructure(0, 0, int(Width), int(Height), 0, 1, 0))
    GoldenSpiralButton.place(x=710, y=0, width=90, height=18)
    RGB.place(x=600, y=50, width=50)
    #makes check equal to 1 so that it can be identified that it is currently on the bitmap tab
    check = 1
    #creates a value for the colour select optionmenu and defaults it to "please select a colour"
    var = StringVar(master)
    var.set("Please select a colour")

    #creates canvas , colours it grey, makes it so that hovering over the canvas makes the cursor a pencil
    canvas = Canvas(master, bg="grey", height=500, width=500, cursor="pencil")
    canvas.place(x=150, y=75)

    #making the optionmenu, contents and placed within the screen, var needs to be a parameter
    ColourOption = OptionMenu(master, var, *ColourList)
    ColourOption.config(bg="#0000E6", fg="white")
    ColourOption["menu"].config(bg="#0000E6")
    ColourOption.place(x = 200, y = 50, width=400, height=25)

    #[top x-cord][top y-cord][bottom x-cord][bottom y-cord] - this is the way rectangles are created
    #user input to input the height and width
    #used to find the height and width of each individual pixel
    if MakeVars == 1:
        PixelWidth = float(500)/float(int(Width))
        PixelHeight = float(500)/float(int(Height))
        #globals this for future use
        global canvas, var, check, PixelWidth, PixelHeight
    #default sets the brush/fill button to be brush
    CursorSelect = "Brush"


    #adds widgets to list that will be destroyed in widgetreplace
    WidgetList = [Background1, canvas, ColourOption, RGB, Blueback, GoldenSpiralButton]
    #userinput now is equal to 1 as users have input text
    Userinput = 1
    #creates a variable which can be used to call methods within the class PixelManipulation()
    PixelManip = PixelManipulation()
    #used later in the program
    o = 0
    global WidgetList, Userinput, PixelManip, DepthCheck, o, LoadCheck, PixelWidth, PixelHeight, FillButton, CursorSelect
    DefaultButtons(master)
    #checks if this is the first time creating the pixels, if it is then it will create them from scratch
    if l == 0:
        #variables are reset or defined
        #count is used to set the item id of each pixel within dictlist
        count = 0
        #dictlist contains all of the dictionaries for every pixel, each pixel has a dictionary containing its data
        Dictlist = []
        #stores the colour variables for each colour
        PixelCollist = []
        #stores the colour of variables for each colour in hexadecimal
        HexadecimalPixellist = []
        #stores the colour of each pixel in binary
        BinaryPixellist = []
        #stores each coordinate of each pixel in lists
        PixelXcoord1list = []
        PixelYcoord1list = []
        PixelXcoord2list = []
        PixelYcoord2list = []

        #all variables are globalled for future use
        global PixelCollist, PixelXcoord1list, PixelYcoord1list, PixelXcoord2list, PixelYcoord2list, HexadecimalPixellist, BinaryPixellist, o, Dictlist, count
        for s in range(0, int(Width)):
            #creates rectangles in the x axis using variables defined previously
            PixelManip.CreatePixel("#FFFFFF",s * PixelWidth ,0 ,PixelWidth+(s*PixelWidth) ,PixelHeight)
            for i in range(0, int(Height) - 1):
                #creates rectangles in the y axis using variables defined previosuly
                PixelManip.CreatePixel("#FFFFFF",s * PixelWidth ,PixelHeight*i + PixelHeight ,PixelWidth+(s*PixelWidth) ,PixelHeight + PixelHeight + (PixelHeight*i))
    elif l == 1:
        #recreates pixels using lists that have already been defined if this is the seconf or more time creating the bitmap
        global HexCheck, BinCheck
        PixelManip.RecreatePixel()

    else:
        #used to load pixels
        #b is used to count how many times it has gone through the loops
        b = 0
        i = 0
        #count is reset for new bitmap creation
        count = 0
        #dictlist is reset for new bitmap creation
        Dictlist = []
        global count, Dictlist

        #craetes pixels in the x and y by going through loadpixel instead of createpixel, follows different rules
        for s in range(0, int(Width)):
            #creates rectangles in the x axis
            PixelManip.LoadPixel(PixelCollist[b],s * PixelWidth ,0 ,PixelWidth+(s*PixelWidth) ,PixelHeight)
            b += 1

            for i in range(0, int(Height) - 1):
                #creates rectangles in the y axis
                PixelManip.LoadPixel(PixelCollist[b],s * PixelWidth ,PixelHeight*i + PixelHeight ,PixelWidth+(s*PixelWidth) ,PixelHeight + PixelHeight + (PixelHeight*i))
                b +=1
#_______________________________________________________________________________

#the third tab/window used to display the hexadecimal values behind each pixel
class HexadecimalWindow(tk.Frame):

    #this function is used when scrolling to scroll through both the hexadecimal value canvas and the x axis identifier canvas
    def ScrollX(self, *args):
        self.canvas.xview(*args)
        self.canvas2.xview(*args)
#_______________________________________________________________________________

    #this function is used when scrolling to scroll through both the hexadecimal value canvas and the y axis identifier canvas
    def ScrollY(self, *args):
        self.canvas.yview(*args)
        self.canvas3.yview(*args)
#_______________________________________________________________________________

    #allows the mouse wheel to be used for scrolling through the y axis
    def OnMouseWheel(self, event):
        self.canvas.yview_scroll(-1*(event.delta/120), "units")
        self.canvas3.yview_scroll(-1*(event.delta/120), "units")
        # this prevents default bindings from firing, which
        # would end up scrolling the widget twice
        return "break"
#_______________________________________________________________________________

    #contains all teh main data for creating the frames, canvases and scrollbars
    def main(self):
        #makes check to equal 2 to show that it is currently on widow 3
        check = 2
        #imports background image and sets it as background
        background1 = PhotoImage(file="Tkinterbackground2.gif")
        Background1 = Label(master, image=background1)
        Background1.background1 = background1
        Background1.place(x=0, y=0)
        #creates the three main frames to contain all other widgets
        framee = tk.Frame(master, borderwidth=1)
        framee2 = tk.Frame(master, borderwidth=1, bg="black")
        framee3 = tk.Frame(master, borderwidth=1, bg="black")
        #puts each canvas inside each corrosponding frame
        self.canvas = tk.Canvas(framee, borderwidth=0, background="white")
        self.canvas2 = tk.Canvas(framee2, borderwidth=0)
        self.canvas3 = tk.Canvas(framee3, borderwidth=0)
        #puts each frame inside each corrosponding canvas
        self.frame = tk.Frame(self.canvas, bg="white", borderwidth=0)
        self.frame2 = tk.Frame(self.canvas2, bg="white", borderwidth=0)
        self.frame3 = tk.Frame(self.canvas3, bg="white", borderwidth=0)
        #attatches a x and y axis scroll bar to the main canvas so that the user can scroll through the hexadecimal values, each, when activated, is taken to the functions above to move the canvases
        self.vsb = tk.Scrollbar(self.canvas, orient="vertical", command=self.ScrollY)
        self.hsb = tk.Scrollbar(self.canvas, orient="horizontal", command = self.ScrollX)
        #binds the canvases to the mousewheel function
        self.canvas.bind_all("<MouseWheel>", self.OnMouseWheel)
        self.canvas2.bind_all("<MouseWheel>", self.OnMouseWheel)
        self.canvas3.bind_all("<MouseWheel>", self.OnMouseWheel)
        #configures the canvases to the scrollbar function
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.configure(xscrollcommand=self.hsb.set)
        self.canvas2.configure(xscrollcommand=self.hsb.set)
        self.canvas3.configure(yscrollcommand=self.vsb.set)
        #places the scrollbars on screen
        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        #places the canvases on screen
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas2.pack(side="left", fill="both", expand=True)
        self.canvas3.pack(side="left", fill="both", expand=True)
        #creates small windows to add the text boxes which will hold the hexadecimal values
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")
        self.canvas2.create_window((4,4), window=self.frame2, anchor="nw",
                                  tags="self.frame2")
        self.canvas3.create_window((4,4), window=self.frame3, anchor="nw",
                                  tags="self.frame3")
        #binds functions which takes it to the where the scroll regions are defined
        self.frame.bind("<Configure>", self.OnFrameConfigure)
        self.frame2.bind("<Configure>", self.OnFrame2Configure)
        self.frame3.bind("<Configure>", self.OnFrame3Configure)

        #places the major frames on the screen and configures their sizes
        framee.place(x=150, y=75, width=500, height=500)
        framee2.place(x=150, y=45, width=500, height=30)
        framee3.place(x=110, y=75, width=40, height=500)

        #adds all major widgets to list so that they can be destroyed in widgetreplace
        WidgetList = [framee, Background1, framee, framee2, framee3]
        #globals necessary variables to be used in later fucntions
        global check, WidgetList
        #goes to populate the canvases
        self.populate()
        #attatches default buttons
        DefaultButtons(master)
#_______________________________________________________________________________

    def Function(self):
        self.canvas.xview
        self.canvas2.xview
#_______________________________________________________________________________

    #populates the canvases with all necessary information
    def populate(self):
        #default sets to 0, will be used to show where the hexadecimal input boxes are stored
        g = 0
        #creates another vcmd to use for validation
        vcmd = (self.master.register(self.OnValidate),
        '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        #loop which creates entry boxes in the x and y axis
        for s in range(0, int(Width)):
            #used to set teh contents of each entry box, changes throughout with variable g
            vars1 = StringVar()
            vars1.set(HexadecimalPixellist[g])
            g+=1
            #creates a label which sets the row number in the x axis
            tk.Label(self.frame2, text=s + 1, width=9, borderwidth=3, bg="white").grid(column=s*1, row=0)

            #disables the editation of the hexadecimal entry boxes if the colour depth is not 24 bit
            if ColourDepth == "24 Bit (RGB)":
                Hexget[g - 1] = tk.Entry(self.frame, text=vars1, borderwidth=2, width=11, bg ="grey", validate="key", validatecommand=vcmd, state=NORMAL)
            else:
                Hexget[g - 1] = tk.Entry(self.frame, text=vars1, borderwidth=2, width=11, bg ="grey", validate="key", validatecommand=vcmd, state=DISABLED)
            #adds the entry box to the grid
            Hexget[g - 1].grid(row=0, column=1*s)

            #loop creates pixels in the y axis
            for i in range(0, int(Height) - 1):
                #sets the variable for contents of each enrty box
                vars2 = StringVar()
                vars2.set(HexadecimalPixellist[g])
                g+=1
                #again checks whether to enable or diable the editation of each hexadecimal entry box
                if ColourDepth == "24 Bit (RGB)":
                    Hexget[g - 1] = tk.Entry(self.frame, text=vars2, borderwidth=2, bg="grey", width=11, validate="key", validatecommand=vcmd, state=NORMAL)
                else:
                    Hexget[g - 1] = tk.Entry(self.frame, text=vars2, borderwidth=2, bg="grey", width=11, validate="key", validatecommand=vcmd, state=DISABLED)
                Hexget[g - 1].grid(row=1*i + 1, column=1*s)

        #loop creates the row and column identifiers
        for i in range(1, int(Height) + 1):
            tk.Label(self.frame3, text=i, width=3, justify="left", height=1, borderwidth=2, bg="white").grid(column=0, row=i*1 + 1)
        #label created in the cornder to fill empty space
        tk.Label(master, bg="black").place(x=110, y=45, height=30, width=40)
        #enable hexcheck as it has passed through the hexadecimal function
        HexCheck = 1
        BinCheck = 0
        #global all future necessary values
        global Hexget, HexCheck, BinCheck
        #adds clear labels at the end to force all other labels to be placed higher
        tk.Entry(self.frame, borderwidth=0, bg="white", width=11 * int(Width) + 1).grid(row=int(Height) + 5, column=0, columnspan=int(Width))
        tk.Entry(self.frame, borderwidth=0, bg="white", width=2).grid(row=0, column=int(Width) + 1, rowspan=int(Height))
#_______________________________________________________________________________

    #sets scroll region on canvas
    def OnFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#_______________________________________________________________________________

    def OnFrame2Configure(self, event):
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all"))
#_______________________________________________________________________________

    def OnFrame3Configure(self, event):
        self.canvas3.configure(scrollregion=self.canvas3.bbox("all"))
#_______________________________________________________________________________

    #validates the text boxes to only allow hexadecimal relevant values
    def OnValidate(self, action, index, value_if_allowed,
    prior_value, text, validation_type, trigger_type, widget_name):

        if text.upper() in '0123456789ABCDEF':
            if len(value_if_allowed) < 1:
                return False
            if len(value_if_allowed) > 7:
                return False
            if text == text.upper():
                return True
            else:
                return False
        else:
            return False
#_______________________________________________________________________________

#final fourth window/tab used to display binary values for each pixel - mostly the same as the hexadecimal tab
class BinaryWindow(tk.Frame):

    def ScrollX(self, *args):
        self.canvas.xview(*args)
        self.canvas2.xview(*args)
#_______________________________________________________________________________

    def ScrollY(self, *args):
        self.canvas.yview(*args)
        self.canvas3.yview(*args)
#_______________________________________________________________________________

    def OnMouseWheel(self, event):
        self.canvas.yview_scroll(-1*(event.delta/120), "units")
        self.canvas3.yview_scroll(-1*(event.delta/120), "units")
        # this prevents default bindings from firing, which
        # would end up scrolling the widget twice
        return "break"
#_______________________________________________________________________________

    def main(self):
        check = 3
        background1 = PhotoImage(file="Tkinterbackground2.gif")
        Background1 = Label(master, image=background1)
        Background1.background1 = background1
        Background1.place(x=0, y=0)
        framee = tk.Frame(master)
        framee2 = tk.Frame(master, borderwidth=1, bg="black")
        framee3 = tk.Frame(master, borderwidth=1, bg="black")

        self.canvas = tk.Canvas(framee, borderwidth=0, background="white")
        self.canvas2 = tk.Canvas(framee2, borderwidth=0)
        self.canvas3 = tk.Canvas(framee3, borderwidth=0)
        self.frame = tk.Frame(self.canvas, bg="white")
        self.frame2 = tk.Frame(self.canvas2, bg="white")
        self.frame3 = tk.Frame(self.canvas3, bg="white")
        self.vsb = tk.Scrollbar(self.canvas, orient="vertical", command=self.ScrollY)
        self.hsb = tk.Scrollbar(self.canvas, orient="horizontal", command=self.ScrollX)
        self.canvas.bind_all("<MouseWheel>", self.OnMouseWheel)
        self.canvas2.bind_all("<MouseWheel>", self.OnMouseWheel)
        self.canvas3.bind_all("<MouseWheel>", self.OnMouseWheel)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.configure(xscrollcommand=self.hsb.set)
        self.canvas2.configure(xscrollcommand=self.hsb.set)
        self.canvas3.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas2.pack(side="left", fill="both", expand=True)
        self.canvas3.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")
        self.canvas2.create_window((4,4), window=self.frame2, anchor="nw",
                                  tags="self.frame2")
        self.canvas3.create_window((4,4), window=self.frame3, anchor="nw",
                                  tags="self.frame3")
        self.frame.bind("<Configure>", self.OnFrameConfigure)
        self.frame2.bind("<Configure>", self.OnFrame2Configure)
        self.frame3.bind("<Configure>", self.OnFrame3Configure)

        framee.place(x=150, y=119, width=500, height=450)
        framee2.place(x=150, y=45, width=500, height=30)
        framee3.place(x=110, y=75, width=40, height=500)

        WidgetList = [framee, Background1, framee, framee2, framee3]
        global check, WidgetList
        self.populate()
        DefaultButtons(master)
#_______________________________________________________________________________

    def populate(self):

        g = 0
        vcmd = (self.master.register(self.OnValidate),
        '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        #creates the default PBM file data at the top of the canvas
        tk.Label(master, text="P1", bg ="white", borderwidth=0).place(x=150, y=75)
        tk.Label(master, text="# feep.pbm", bg ="white", borderwidth=0).place(x=150, y=87)
        tk.Label(master, text=Width + " " + Height, bg ="white", borderwidth=0).place(x=150, y=100)
        tk.Label(self.frame3, text="-1", width=3, justify="left", height=1, borderwidth=2, bg="white").grid(column=0, row=0)
        tk.Label(self.frame3, text="0", width=3, justify="center", height=1, borderwidth=2, bg="white").grid(column=0, row=1)

        for s in range(0, int(Width)):
            vars1 = StringVar()
            vars1.set(BinaryPixellist[g])
            tk.Label(self.frame2, text=s + 1, width=22, borderwidth=3, bg="white").grid(column=s*1, row=0)
            g+=1
            Binget[g - 1] = tk.Entry(self.frame, text=vars1, borderwidth=2, bg ="grey", width=25, validate="key", validatecommand=vcmd)
            Binget[g - 1].grid(row=3, column=1*s)

            for i in range(0, int(Height) - 1):
                vars2 = StringVar()
                vars2.set(BinaryPixellist[g])
                g+=1
                Binget[g - 1] = tk.Entry(self.frame, text=vars2, borderwidth=2, bg="grey", width=25, validate="key", validatecommand=vcmd)
                Binget[g - 1].grid(row=1*i + 4, column=1*s)

        for i in range(1, int(Height) + 1):
            tk.Label(self.frame3, text=i, width=3, justify="left", height=1, borderwidth=2, bg="white").grid(column=0, row=i + 2)

        tk.Label(master, bg="black").place(x=110, y=45, height=30, width=40)

        BinCheck = 1
        HexCheck = 0
        global Binget, BinCheck, HexCheck

        tk.Entry(self.frame, borderwidth=0, bg="white", width=25 * int(Width) + 1).grid(row=int(Height) + 3, column=0, columnspan=int(Width))
        tk.Entry(self.frame, borderwidth=0, bg="white", width=2).grid(row=0, column=int(Width) + 1, rowspan=int(Height))
#_______________________________________________________________________________

    def OnFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#_______________________________________________________________________________

    def OnFrame2Configure(self, event):
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all"))
#_______________________________________________________________________________

    def OnFrame3Configure(self, event):
        self.canvas3.configure(scrollregion=self.canvas3.bbox("all"))
#_______________________________________________________________________________

    def OnValidate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):

        if text in '01':
            if len(value_if_allowed) > DepthCheck:
                return False
            return True
        else:
            return False
#_______________________________________________________________________________

#function used to create the widgets used on every window
def DefaultButtons(master):
    #adds a title to the program
    master.title("BCS (Bitmap Customisation System)")
    #imports all images which are used to show which tab is selected
    line = PhotoImage(file="line1.gif")
    line2 = PhotoImage(file="line2.gif")
    line3 = PhotoImage(file="line3.gif")
    line4 = PhotoImage(file="selectedline.gif")
    line5 = PhotoImage(file="selectedline2.gif")
    #imports the icon for the corner of the screen
    master.iconbitmap(default='BCSicon.ico')
    #sets the default value for the option file menu
    var1 = StringVar(master)
    var1.set("File")

    #creates the file menu, attatches the command which sends it to a function to direct it to different fucntions depending on its value
    FileMenu = OptionMenu(master, var1, "Save", "Load", "Exit", command=FileMenuChoice)
    FileMenu.place(x=0, y=0, width=50, height=18)
    FileMenu.config(borderwidth=2, bg="white")
    #creates each button tab at the top of the screen, each sends the program to the widget replacecheck and changes the value of t
    CreateNewBitmapButton = Button(master, bg="white", text="Create new", command=lambda t=1: WidgetReplaceCheck(t))
    CreateNewBitmapButton.place(x=50, y=0, width=100, height=18)
    BitmapButton = Button(master, bg="white", text="Bitmap", command=lambda t=2: WidgetReplaceCheck(t))
    BitmapButton.place(x=150, y=0, width=100, height=18)
    HexadecimalButton = Button(master, bg="white", text="Hexadecimal", command=lambda t=3: WidgetReplaceCheck(t))
    HexadecimalButton.place(x=250, y=0, width=100, height=18)
    BinaryButton = Button(master, bg="white", text="Binary", command=lambda t=4: WidgetReplaceCheck(t))
    BinaryButton.place(x=350, y=0, width=100, height=18)

    #holds all of the values for each label created within the function
    Labellist = [["Labell", "0", "17"], ["Label1", "150", "17"], ["Label2", "250", "17"], ["Label3", "350", "17"],
    ["Label4", "50", "17"], ["Label5", "50", "0"], ["Label6", "150", "0"], ["Label7", "250", "0"], ["Label8", "350", "0"], ["Label9", "450", "0"]]
    #stores the line values to be used when it creates the labels
    Linelist = [line, line2, line2, line2, line2, line3, line3, line3, line3, line3]

    #creates each label surrounding the tab buttons at the top of the screen, each label consists of a image line either red or blue
    for i in range(0, len(Labellist)):
        Labellist[i][0] = Label(master, image=Linelist[i], borderwidth=0)
        Labellist[i][0].Line = Linelist[i]
        Labellist[i][0].place(x=Labellist[i][1], y=Labellist[i][2])

    #adds in further labels
    Label10 = Label(master, image=line4, borderwidth=0)
    Label10.line4 = line4
    Label10.place(x=CheckList[0][check][0], y=CheckList[0][check][1])
    Label11 = Label(master, image=line5, borderwidth=0)
    Label11.line5 = line5
    Label11.place(x=CheckList[1][check][0], y=0)
    Label12 = Label(master, image=line5, borderwidth=0)
    Label12.line5 = line5
    Label12.place(x=CheckList[1][check][1], y=0)
#_______________________________________________________________________________

#function to check the value of the fill/brush button and chnage the text of it accordingly
def FillSwitch():

        if FillButton["text"] == "Fill":
            # switch to Brush
            FillButton["text"] = "Brush"
            canvas["cursor"] = "pencil"
            CursorSelect = "Brush"
        else:
            # reset to Fill
            FillButton["text"] = "Fill"
            canvas["cursor"] = "spraycan"
            CursorSelect = "Fill"

        global CursorSelect
#_______________________________________________________________________________

#function to check what has been chosen on the filemenu and directs the user to different functions accordingly
def FileMenuChoice(val):

        if val == "Exit":
            #destroys current master and closes the program
            master.destroy()
            master.quit()

        if val == "Load":
            #opens a tk dialog box which allows the user to choose a file, only PBM files are allowed
            Tk().withdraw()
            filename = askopenfilename()
            if filename[len(filename) - 3:len(filename)] == "pbm":
                PBMLoad(filename)
            else:
                error()

        #sends the user to the save function
        if val == "Save":
            PBMSave()
#_______________________________________________________________________________

#function for loading bitmaps
def PBMLoad(filename):

    #loadcheck is set to 1 as it has loaded a bitmap
    LoadCheck = 1
    #opens file name that user has selected
    file = open(filename)
    #reads all lines in the file
    readline = file.readlines()
    #sets the width and height from lines read
    Width = readline[2].split(" ")[0]
    Height = readline[2].split(" ")[1]
    #sets the colour depth depending on the length of each binary value from the data read
    ColourDepth = str(len(readline[3].split(" ")[0]))
    #sets the depthcheck to the colour depth for later use
    DepthCheck = int(ColourDepth)

    #adds text extensions depedning on colour depth
    if ColourDepth == "1":
        ColourDepth = "1 bit (Monotone)"
    elif ColourDepth == "24":
        ColourDepth = "24 Bit (RGB)"
    elif ColourDepth == "2":
        ColourDepth = "2 Bit                                                                                                               "
    else:
        ColourDepth = ColourDepth + " Bit"

    #resets or sets all used variables
    Hexget = []
    Binget = []
    HexadecimalPixellist = []
    PixelCollist = []
    PixelXcoord1list = []
    PixelYcoord1list = []
    PixelXcoord2list = []
    PixelYcoord2list = []
    BinCheck = 0
    HexCheck = 0

    #appends empty places to lists for later use
    for i in range(0, int(Width)*int(Height)):
        Hexget.append(None)
        Binget.append(None)
        HexadecimalPixellist.append(None)
        PixelCollist.append(None)

    #sets more variables for later use
    BinaryPixellist = []
    Userinput = 1
    l = 2

    #finds the binary values from the open PBM file and appends it to a list, finds all hexadecimal values from binary to hex function
    for i in range(0, int(Width)):
        for s in range(0, int(Height)):
            getattr(globals()['PixelManipulation'](), 'BinaryLengthener')(readline[s + 3].split(" ")[i])
            BinaryPixellist.append(number3)
    getattr(globals()['PixelManipulation'](), 'BinaryToHex')()

    #shortens all binary to colour depth used
    for i in range(0, len(PixelCollist)):
        getattr(globals()['PixelManipulation'](), 'BinaryShortner')(BinaryPixellist[i])
        BinaryPixellist[i] = number3

    Userinput = 1
    l = 2

    #globals all variables for future use
    global Width, Height, ColourDepth, BinaryPixellist, Userinput, Hexget, Binget, l,LoadCheck, DepthCheck, HexadecimalPixellist, PixelCollist, BinCheck, HexCheck, PixelXcoord1list, PixelYcoord1list, PixelXcoord2list, PixelYcoord2list
    #deletes all of the current on screen widgets
    WidgetReplace()
    #sends the user to the bitmap window and passes through the width height and colour depth
    BitmapWindow(Width, Height, ColourDepth, 1)
#_______________________________________________________________________________

#function used to save current binary pixel values to a pbm file
def PBMSave():

    #test to see if width and height has been defined, if not it brings up an error
    try:
        Width
        d = 0
        Tk().withdraw()
        #allows the user to select a place to store a pbm file
        filename = tkFileDialog.asksaveasfile(mode='w', defaultextension=".pbm")
        #adds default values to the pbm file
        Contents = ("""P1
# feep.pbm
""" + Width + " " + Height)
        #loop to add all of the hexadecimal values into the variable contents
        for s in range(0, int(Width)):
            Contents = Contents + """
"""
            d += 1
            for i in range(0, len(PixelCollist) + 1, int(Height)):
                if i + d - 1 > len(PixelCollist) - 1 and i + d - 1:
                    break
                Contents = Contents + BinaryPixellist[i + d - 1] + " "
        #write the variable contents to the file
        filename.write(Contents)
        filename.close()
    except NameError:
        error()
        return False
#_______________________________________________________________________________

#used to direct the program to specific places depending on the value of t
def WidgetReplaceCheck(t):

    #checks if user has issued any inputs, if not it dispalys an error
    if Userinput == 1:

        #if the variable t is equal to 1 then it deletes all of the current widgets and goes to the create bitmap window
        if t == 1:
            WidgetReplace()
            Init.CreateBitmapWindow()

        #checks if there are bianry values to get from the binary text boxes, if so it appends it to the list before continuing
        if BinCheck == 1:
            for i in range(0, len(PixelCollist)):
                BinaryPixellist[i] = Binget[i].get()
                #lengthens binary so that it can be used in conversions
                PixelManip.BinaryLengthener(BinaryPixellist[i])
                BinaryPixellist[i] = number3
            #creates hexadecimal values
            PixelManip.BinaryToHex()
            for i in range(0, len(PixelCollist)):
                #shortern binary values back to original size
                PixelManip.BinaryShortner(BinaryPixellist[i])
                #sets new binary values
                BinaryPixellist[i] = number3

        #sends to hexadecimal window if t is equal to 3
        if t == 3:
            #lengthens binary values, converts to hexadecimal and then shorterns again
            for i in range(0, len(PixelCollist)):
                PixelManip.BinaryLengthener(BinaryPixellist[i])
                BinaryPixellist[i] = number3
            PixelManip.BinaryToHex()
            for i in range(0, len(PixelCollist)):
                PixelManip.BinaryShortner(BinaryPixellist[i])
                BinaryPixellist[i] = number3
            #deletes all current widgets
            WidgetReplace()
            #sends to hexadecimal window
            Hex = HexadecimalWindow(master)
            Hex.main()

        if t == 4:
            #checks if the program has come from the hexadecimal window
            if HexCheck == 1:
                #if so it updates the hexadecimal and binary values
                for i in range(0, len(PixelCollist)):
                    HexadecimalPixellist[i] = Hexget[i].get()
                PixelManip.BinarylistFactory(2)
            #deletes all of the widgets on screen
            WidgetReplace()
            #transports to binary window
            Bin = BinaryWindow()
            Bin.main()

        #checks to see if it needs to be transported to the bitmap window
        if t == 2:
            #checks if hexadecimal values have been updated and if so, changes the hexadecimal pixel list to new values
            if HexCheck == 1:
                for i in range(0, len(Hexget)):
                    HexadecimalPixellist[i] = Hexget[i].get()
                PixelManip.BinarylistFactory(2)
            #makes l equal to 1 to show that it has created a bitmap window
            l = 1
            global l
            #deletes all current widgets
            WidgetReplace()
            #sends to bitmap window
            BitmapWindow(Width, Height, ColourDepth,0)

    else:
        error()
#_______________________________________________________________________________

def WidgetReplace():
    for i in range(0, len(WidgetList)):
        WidgetList[i].destroy()
#_______________________________________________________________________________

def CreateSpiralStructure(WidthNo1, HeightNo1, WidthNo2, HeightNo2, Which, Either, Count):

        if Which == 0:
            if Either == 1:
                GoldenRectangleinfo.append([WidthNo1 * PixelWidth, HeightNo2 * PixelHeight])
                WidthNo1 = int((WidthNo2 - WidthNo1) / 1.618) + WidthNo1
                GoldenRectangleinfo[Count].extend([WidthNo1 * PixelWidth, HeightNo1 * PixelHeight])
                for i in range(0, (HeightNo2 - HeightNo1)):
                    master.after(50, LabelCreate(int(PixelXcoord1list[(WidthNo1 * int(Height)) + HeightNo1 + i]) + 150, int(75 + (PixelHeight * HeightNo1) + (PixelHeight * i)), 2, PixelHeight))
            else:
                GoldenRectangleinfo.append([WidthNo2 * PixelWidth, HeightNo1 * PixelHeight])
                WidthNo2 = int((WidthNo2 - WidthNo1) / 1.618) + WidthNo1
                GoldenRectangleinfo[Count].extend([WidthNo2 * PixelWidth, HeightNo2 * PixelHeight])
                for i in range(0, (HeightNo2 - HeightNo1)):
                    master.after(50, LabelCreate(int(PixelXcoord1list[(WidthNo2 * int(Height)) + HeightNo1 + i]) + 150, int(75 + (PixelHeight * HeightNo1) + (PixelHeight * i)), 2, PixelHeight))

            if (WidthNo2 - WidthNo1) * (HeightNo2 - HeightNo1) < 2:
                Which = 3
            else:
                Count += 1
                CreateSpiralStructure(WidthNo1, HeightNo1, WidthNo2, HeightNo2, 1, Either, Count)

        elif Which == 1:
            if Either == 1:
                GoldenRectangleinfo.append([WidthNo1 * PixelWidth, HeightNo1 * PixelHeight])
                HeightNo1 = int((HeightNo2 - HeightNo1) / 1.618) + HeightNo1
                GoldenRectangleinfo[Count].extend([WidthNo2 * PixelWidth, HeightNo1 * PixelHeight])
                for i in range(0, (WidthNo2 - WidthNo1)):
                    master.after(50, LabelCreate((WidthNo1 * PixelWidth) + 150 + (PixelWidth * i), PixelYcoord1list[HeightNo1 + (int(Height) * WidthNo1)] + 75, PixelWidth, 2))
            else:
                GoldenRectangleinfo.append([WidthNo2 * PixelWidth, HeightNo2 * PixelHeight])
                HeightNo2 = int((HeightNo2 - HeightNo1) / 1.618) + HeightNo1
                GoldenRectangleinfo[Count].extend([WidthNo1 * PixelWidth, HeightNo2 * PixelHeight])
                for i in range(0, (WidthNo2 - WidthNo1)):
                    master.after(50, LabelCreate((WidthNo1 * PixelWidth) + 150 + (PixelWidth * i), PixelYcoord1list[HeightNo2 + (int(Height) * WidthNo2)] + 75, PixelWidth, 2))

            if Either == 1:
                Either = 2
            else:
                Either = 1

            if (WidthNo2 - WidthNo1) * (HeightNo2 - HeightNo1) < 2:
                Which = 3
                CreateSpiral(GoldenRectangleinfo)
            else:
                Count += 1
                CreateSpiralStructure(WidthNo1, HeightNo1, WidthNo2, HeightNo2, 0, Either, Count)

#_______________________________________________________________________________

def LabelCreate(XVal, YVal, W, H):
    Goldenlabel = Label(master, bg="red")
    Goldenlabel.place(x = XVal, y = YVal, width = W, height = H)
    master.update()

#_______________________________________________________________________________

def CreateSpiral(GoldenRectangleinfo):



    for i in range(0, len(GoldenRectangleinfo)):
        NextPixelLocX = 0
        NextPixelLocY = 0
        k = 0
        while k == 0:
            for s in range(1, 50):
                if NextPixelLocX < GoldenRectangleinfo[0][2] - PixelWidth:

                    NextPixelLocX = GoldenRectangleinfo[0][0] + (PixelWidth * s)
                if NextPixelLocX > GoldenRectangleinfo[0][3]:

                    NextPixelLocY = GoldenRectangleinfo[0][1] - (PixelHeight * s)
                master.after(50, canvas.itemconfig(canvas.find_closest(NextPixelLocX, NextPixelLocY), fill = "yellow"))
                master.update()
                if NextPixelLocX >= GoldenRectangleinfo[0][2] - PixelWidth and NextPixelLocY == GoldenRectangleinfo[0][3]:
                    k = 1
                    break


#_______________________________________________________________________________
#opens a new window which explains what the user has to do to use the program
def Help():
    #creates a new window on top of the original, sets title, icon and geometry
    master1 = Toplevel()
    master1.geometry("600x250+385+350")
    master1.title("BCS Help")
    #focuses the window
    master1.grab_set()
    #creates background labels and editable labels
    HelpLabel4 = Label(master1, bg="#954c4c")
    HelpLabel4.place(x=0, y=0, width=600, height=250)
    HelpLabel3 = Label(master1, bg="#c7b1b1")
    HelpLabel3.place(x=10, y=10, width= 235, height=225)
    HelpLabel4 = Label(master1, bg="#c7b1b1")
    HelpLabel4.place(x=275, y=25, width= 315, height=210)
    HelpLabel1 = Label(master1, text="Please select what you need help with:", bg="#c7b1b1").place(x=20, y=20)
    HelpLabel2 = Label(master1, text="""       Welcome to the Bitmap help menu, If you
         wish to know more about an
          aspect of this program, please click it.
           When finished select OK""", bg="#c7b1b1")
    HelpLabel2.place(x=290, y=30)
    #creates buttons that can edit the contents of the help label when clicked, sends to the helpdirect function and sets h according to which button has been selected
    HelpButton1 = Button(master1, text="Bitmap basics", bg="#FFAAAA", command=lambda h=1: HelpDirect(h)).place(x=25, y=50, width=200)
    HelpButton2 = Button(master1, text="How to edit a bitmap", bg="#FFAAAA", command=lambda h=2: HelpDirect(h)).place(x=25, y=100, width=200)
    HelpButton3 = Button(master1, text="Using binary and hex", bg="#FFAAAA", command=lambda h=3: HelpDirect(h)).place(x=25, y=150, width=200)
    HelpButton4 = Button(master1, text="Keyword summary", bg="#FFAAAA", command=lambda h=4: HelpDirect(h)).place(x=25, y=200, width=200)
    HelpButton5 = Button(master1, text="OK", command=lambda: master1.destroy(), bg="#FFAAAA").place(x=380, y=200, width=100)
    #global label value to be used in helpdirect
    global HelpLabel2
#_______________________________________________________________________________

#function used to set the text of helplabel depending on which button has been selected
def HelpDirect(h):
    #checks what the value of h is and sets the text of the label accordingly
    if h == 1:
        HelpLabel2["text"] = """ Type the width and Height into the blue entry
 boxes to begin, each will determine the number
 of pixels per row and per column.
 The colour depth will determine the size
 of the binary number representing each pixel.
 As such it will determine the amount of colours
 you will be able to use, 24 bit being the
 largest with a massive amount of possible colours.
 When done, click the "generate bitmap" button"""
    elif h == 2:
        HelpLabel2["text"] = """Once a bitmap has been created, it is easily edited.
The top drop down menu allows for colour selection,
once a colour has been chosen, click a pixel to edit
it. The default mouse type is the brush. This allows
you to change the colours of the pixels one by one.
Clicking the brush button will change it to a fill tool,
the fill tool changes all pixels of the same colour.
Lastly, when using 24 bits, you can select the RGB
button for a wider range of colours to use"""
    elif h == 3:
        HelpLabel2["text"] = """To further edit a bitmap, changing the code
behind each pixel is also possible. The hexadecimal
code tab is always open for viewing but can only
be edited when using a 24 bit colour depth. Each
text box contains the hexadecimal code behind
each corrosponding pixel. The binary tab is the
same although it can be edited using any colour
depth. In the process of changing the code in
either the binary or hexadecimal tabs, returning
to the bitmap tab should show a difference in
colour according to the select pixel"""
    elif h == 4:
        HelpLabel2["text"] = """Important Keywords relating to bitmaps include:
Pixel - The smallest alloctable location on a screen
Colour depth - Amount of bits used to store each pixel
RGB - Stands for Red Green Blue, this is used to
    customise the consistency of these three colours
    in an indivdual object.
Bitmap - This is a representation of pixels in which
each pixel corrosponds to one or more bits of
information"""

#_______________________________________________________________________________

#function used to bring up an error on screen
def error():
    #creates a new window with a title, icon and geometry
    master1 = Toplevel()
    master1.geometry("300x150+550+375")
    master1.title("ERROR")
    #prioritises focus on window
    master1.grab_set()

    #creates a label to display error
    ErrorLabel = Label(master1, text="""The program has encountered an error,
     please check that all required fields
      are filled correctly.""", foreground="#78780e").place(x=0, y=0, width=300, height=50)
      #button used to exit window
    ErrorButton = Button(master1, text="OK", command=lambda: master1.destroy()).place(x=125, y=100, width=50, height=25)
#_______________________________________________________________________________

#function used to bring up a tkinter colour selection pallette
def RGBselect():
    #chosen colour is selected as a variable and used later to choose the colour of each pixel selected
    mycolour = tkColorChooser.askcolor()
    var.set(mycolour[1])
#_______________________________________________________________________________

class PixelManipulation:

    def __init__(self,xcoord1=0, ycoord1=0, xcoord2=50, ycoord2=50):
        if LoadCheck == 0:
            #create everything with a self to define the current button
            self.canvas = canvas
            #item is needed for each rectangle created so that the colour can be chnaged later
            #this is used to show what event will trigger it to go to colourchange(), this is just a click or a drag
            self.canvas.tag_bind("Pixel", "<B1-Motion>", self.Colourchange)
            self.canvas.tag_bind("Pixel", "<Button-1>", self.Colourchange)
#_______________________________________________________________________________

    def CreatePixel(self, colour, xcoord1, ycoord1, xcoord2, ycoord2):

        #sets all coordinates to self for that specific rectangle
        count += 1
        #craetes the base for a black pixel including its itemID which is scaled using count, the pixel colour and the outline colour
        self.colour_data = {"colour": "#FFFFFF", "item": count, "outline": "black"}
        #creates a self of every variable so that it can be used throughout otehr functions
        self.Item = self.colour_data
        self.colour = colour
        PixelCollist.append(self.colour)
        self.xcoord1 = xcoord1
        PixelXcoord1list.append(self.xcoord1)
        self.ycoord1 = ycoord1
        PixelYcoord1list.append(self.ycoord1)
        self.xcoord2 = xcoord2
        PixelXcoord2list.append(self.xcoord2)
        self.ycoord2 = ycoord2
        PixelYcoord2list.append(self.ycoord2)
        Dictlist.append(self.colour_data)
        global PixelCollist, PixelXcoord1list, PixelYcoord1list, PixelXcoord2list, PixelYcoord2list, count

        #creates rectangle with x and y coordinates, colour data comes from init as it is defult set red, it is tagged pixel so that all pixels can chage colour when clicked
        canvas.create_rectangle(self.xcoord1,self.ycoord1,self.xcoord2,self.ycoord2,fill=self.colour_data["colour"], outline=self.colour_data["outline"], tag="Pixel", activestipple="gray12")
        #sends the program to create the hexadecimal values of every pixel
        PixelManip.HexadecimallistFactory(1)
#_______________________________________________________________________________

    #this function is used to find the pixels next to the pixel selected
    def FindNearPixels(self, Item):

        #creates a blacklist for temporary use when filtering out unwanted pixels
        Changelist = []

        #loop loops for how many pixels there are surrounding the pixel selected
        for i in range(0, len(list(canvas.find_overlapping(canvas.coords(Item)[0], canvas.coords(Item)[1], canvas.coords(Item)[2], canvas.coords(Item)[3])))):
            #filters out the pixels which are laready in the main list
            if list(canvas.find_overlapping(canvas.coords(Item)[0], canvas.coords(Item)[1], canvas.coords(Item)[2], canvas.coords(Item)[3]))[i] not in OverlapTuple:
                #appends all the wanted pixels to the chnagelist
                Changelist.append(list(canvas.find_overlapping(canvas.coords(Item)[0], canvas.coords(Item)[1], canvas.coords(Item)[2], canvas.coords(Item)[3]))[i])

        #filters out pixels diagonal to the pixel selected and only adds ones that are directly nex to it (up, down, left, right)
        i = 0
        while i < len(Changelist):
            if Changelist[i] != Item + 1 and Changelist[i] != Item - 1 and Changelist[i] != Item - int(Height) and Changelist[i] != Item + int(Height):
                Changelist.pop(i)
            else:
                i += 1

        #adds the contents of changelist to the list used and globals it to be used in other functions
        OverlapTuple = OverlapTuple + Changelist
        global OverlapTuple
#_______________________________________________________________________________

    #function is called when the user clicks on a pixel, passes through the event (i.e.click)
    def Colourchange(self, event):
        #resets or defines the list to store all pixels being changed
        OverlapTuple = []
        #this list is used for pixels that are definately going to be filled in during the use of the fill function
        OriginalID = []
        #finds the item closest to the cursor and defines it in the current colour_data
        Dictlist[self.canvas.find_closest(event.x, event.y)[0] - 1]["item"] = self.canvas.find_closest(event.x, event.y)[0]
        #gets the dictionary of the pixel clicked from the dictionary list
        self.Item = Dictlist[self.canvas.find_closest(event.x, event.y)[0] - 1]
        #appends the first pixel id to the list
        OverlapTuple.append(self.Item["item"])
        #appends the first list id to the list so that this will always be in it
        OriginalID.append(self.Item["item"])
        #globals the values
        global OverlapTuple, OriginalID

        #checks what cursor is currently being used by the user
        if CursorSelect == "Fill":
            #sets i to 0, used for while loops to make sure that the program will always stay inside until every pixel id has been checked
            i = 0
            #defines the original colour of the pixel, program will only check for this specific colour
            FillColour = self.Item["colour"]
            #sends to find pixels next to the pixel clicked
            PixelManip.FindNearPixels(self.Item["item"])
            #loop only breaks after every pixel has been checked
            while i < len(OverlapTuple) - 1:
                #sets the item as the dictionary of the current pixel being checked
                self.Item = Dictlist[OverlapTuple[i] - 1]
                #checks to see if that pixel has the original colour, if it does it can be chnaged
                if Dictlist[OverlapTuple[i] - 1]["colour"] == FillColour:
                    #sets this pixel as a definate id in the list so it can never be popped
                    OriginalID.append(self.Item["item"])
                    #globals the defined variables
                    global OriginalID, FillColour
                    #sends to find near pixels of the pixel currently being checked
                    PixelManip.FindNearPixels(self.Item["item"])
                #checks if it is not a definate pixel, if not and it is not a valid colour it will pop it from the list
                elif OverlapTuple[i] not in OriginalID:
                    OverlapTuple.pop(i)
                    i -= 1
                i += 1
            #resets i for more use
            i = 0
            #loop which performs a final check on all of the pixels in the list, if are of a wrong colour type it pops it
            while i < len(OverlapTuple):
                self.Item = Dictlist[OverlapTuple[i] - 1]
                if self.Item["colour"] != FillColour:
                    OverlapTuple.pop(i)
                else:
                    i +=1
            #list to chnage the colour of all pixels in list
            for i in range(0, len(OverlapTuple)):
                #sets the item to be the item dictionary from the dictionary list
                self.Item = Dictlist[OverlapTuple[i] - 1]
                #chnages the colour of it in the dictionary
                self.Item["colour"] = var.get()
                #checks if the colour is not selected, if so it will default it to become white
                if var.get() == "Please select a colour":
                    self.Item["colour"] = "#FFFFFF"
                else:
                    #converts the word of the colour into caps so it can be used properly in the hexadecimal factory
                    self.Item["colour"] = self.Item["colour"].upper()
                    #goes to the hexadecimal factory to convert colour into hex
                    PixelManip.HexadecimallistFactory(0)
                    #goes to binary factory to convert colour into binary
                    PixelManip.BinarylistFactory(0)
                    #changes the outline colour of the pixel if the colour is black so that outline is visable
                    if self.Item["colour"] == "#000000":
                        self.Item["outline"] = "#FFFFFF"
                    else:
                        self.Item["outline"] = "#000000"
                #configures the pixel colour and possibly outline to chnage to what has been set
                canvas.itemconfig(self.Item["item"], fill = self.Item["colour"], outline = self.Item["outline"])
        else:
            #if the optionmenu has not yet been used, defultly sets to white so that pixels dont chnage colour when clicked
            if var.get() == "Please select a colour":
                self.Item["colour"] = "#FFFFFF"
            else:
                #sets colour to colour chosen on optionmenu
                self.Item["colour"] = var.get()
                self.Item["colour"] = self.Item["colour"].upper()
                #gets its hex and binary values
                PixelManip.HexadecimallistFactory(0)
                PixelManip.BinarylistFactory(0)
                #changes its outline colour
                if self.Item["colour"] == "#000000":
                    self.Item["outline"] = "#FFFFFF"
                else:
                    self.Item["outline"] = "#000000"
                #chnages the dictionary pixel colour
                Dictlist[self.Item["item"] - 1]["colour"] = self.Item["colour"]
                global Dictlist
            #configures the colour of the button depending on what the user chose in optionmenu
            canvas.itemconfig(self.Item["item"], fill = self.Item["colour"], outline = self.Item["outline"])
            #chnages the value of pixelcollist
            PixelCollist[self.Item["item"] - 1] = self.Item["colour"]
#_______________________________________________________________________________

    #gets the coordinates from the loadPNG file
    def LoadPixel(self, colour, xcoord1, ycoord1, xcoord2, ycoord2):
        #count increases by 1 every time and is used for the item id
        count+=1
        #creates a default dictionary, does the same as on create pixel for the rest
        self.colour_data = {"colour": "#FFFFFF", "item": count, "outline": "black"}
        self.Item = self.colour_data
        self.Item["colour"] = colour
        self.xcoord1 = xcoord1
        PixelXcoord1list.append(self.xcoord1)
        self.ycoord1 = ycoord1
        PixelYcoord1list.append(self.ycoord1)
        self.xcoord2 = xcoord2
        PixelXcoord2list.append(self.xcoord2)
        self.ycoord2 = ycoord2
        PixelYcoord2list.append(self.ycoord2)
        Dictlist.append(self.Item)
        global PixelCollist, PixelXcoord1list, PixelYcoord1list, PixelXcoord2list, PixelYcoord2list, count, Dictlist
        #creates rectangle with x and y coordinates, colour data comes from init as it is defult set red, it is tagged pixel so that all pixels can chage colour when clicked
        canvas.create_rectangle(self.xcoord1,self.ycoord1,self.xcoord2,self.ycoord2,fill=self.Item["colour"], tags="Pixel", activestipple="gray12")
#_______________________________________________________________________________

    #used so that when user switches windows, pixels can be created from pre-existing variables
    def RecreatePixel(self):
        #checks if it has comne from the hexadecimal window
        if HexCheck == 1:
            #if so it gets the value from the hexadecimallist and replaces the value in pixelcollist with it as this is what is used for creating pixels
            for i in range(0, len(HexadecimalPixellist)):
                PixelCollist[i] = HexadecimalPixellist[i]
        for i in range(0, len(PixelCollist)):
            #creates rectangle using pre-existing variables defined when pixel is first created
            canvas.create_rectangle(PixelXcoord1list[i], PixelYcoord1list[i], PixelXcoord2list[i], PixelYcoord2list[i], fill = PixelCollist[i], tags="Pixel", tag="Pixel", activestipple="gray12")
        #resets vars as it is no longer in either window
        HexCheck = 0
        BinCheck = 0
        global HexCheck, BinCheck
#_______________________________________________________________________________

    #function used to convert binary to hexadecimal for purposes of getting the users inputs on the binary window
    def BinaryToHex(self):
        for s in range(0, len(BinaryPixellist)):
                #creates a new hex value from binary and adds it to hexlist and pixelcollist
                Hextemp = "#"
                for i in range(0, 6):
                    for g in range(0, 16):
                        if BinaryPixellist[s][i*4:4 + i*4] == Binlist[g]:
                            Hextemp = Hextemp + Hexlist[g]
                            HexadecimalPixellist[s] = Hextemp
                            PixelCollist[s] = Hextemp
        #globals newly editted variables
        global PixelCollist, HexadecimalPixellist
#_______________________________________________________________________________

    #lengthens binary code smaller than 24 bit to allow it to have a hexadecimnal value
    def BinaryLengthener(self, BinaryPass):
        #max value for 24 bit
        MaximumValue = 16777215
        #makes the binary number denary
        DenaryTemp = int(BinaryPass, 2)
        #finds the highest possible binary value using the colour depth selected
        max = int((DepthCheck * "1"), 2)
        #finds the percentage of the actual denary value takes up out of the maximum binary value
        per = float(DenaryTemp)/float(max)
        #gets the final variable
        number = MaximumValue * per
        #converts to an integer
        number2 = int(round(number, 0))
        #converts to bianry
        number3 = bin(number2)
        #takes out useless variables that come with converting it to binary
        number3 = number3[2:len(number3)]
        #adds 0's in the empty spaces to make it 24 bit
        if len(number3) != 24:
            for i in range(0, 24 - len(number3)):
                number3 = "0" + number3
        #carries it back
        global number3
#_______________________________________________________________________________

    #entire function is a reverse of binary lengthener
    def BinaryShortner(self, BinaryPass):
        MaximumValue = 16777215
        DenaryTemp = int(BinaryPass, 2)
        per = float(DenaryTemp)/float(MaximumValue)
        max = int((DepthCheck * "1"), 2)
        number = max * per
        number2 = int(round(number, 0))
        number3 = bin(number2)
        number3 = number3[2:len(number3)]
        if len(number3) != DepthCheck:
            for i in range(0, DepthCheck - len(number3)):
                number3 = "0" + number3
        global number3
#_______________________________________________________________________________

    #function is used to find the hexadecimal values of each colour selected
    def HexadecimallistFactory(self, g):
        #list of possible colours
        ColourList = ["RED", "BLUE", "GREEN", "YELLOW", "ORANGE", "PURPLE", "BLACK", "WHITE                                                                                                            ", "BROWN", "LIME GREEN", "LIGHT PINK", "SKY BLUE", "MOSS GREEN", "DARK PURPLE", "DARK RED", "GREY", "LIGHT GREY", "DARK GREY"]
        #list of possible colours hexadecimal values
        HexColourList = ["#FF0000", "#0000FF", "#00FF00", "#FFFF00", "#FF9900", "#CC66FF", "#000000", "#FFFFFF", "#924924", "#B6DB6D", "#DB6DB6", "#6DB6DB", "#249249", "#861861", "#820820", "#AAAAAA", "#DDDDDD", "#666666"]
        #checks if colour selected is in the list, if not it can skip this part
        if self.Item["colour"] in ColourList:
            #changes the colour value to hexadecimal version of colour value
            self.Item["colour"] = HexColourList[ColourList.index(self.Item["colour"])]
            HexadecimalPixellist[self.Item["item"] - 1] = self.Item["colour"]
            #appends it to list
            self.HexadecimalPixellist = HexadecimalPixellist[self.Item["item"] - 1]
        elif g == 1:
            #this is called when it is first creating each pixel, each pixel is default set to white
            HexadecimalPixellist.append("#FFFFFF")
            self.HexadecimalPixellist = "#FFFFFF"
            #creates binary versions of each pixel
            PixelManip.BinarylistFactory(1)
        else:
            #happens when user has selected an RGB colour, gets the colour and puts it into the hex list as it is already in hex form
            HexadecimalPixellist[self.Item["item"] - 1] = self.Item["colour"]
            self.HexadecimalPixellist = HexadecimalPixellist[self.Item["item"] - 1]
        #globals to be used later
        global HexadecimalPixellist
#_______________________________________________________________________________

    def BinarylistFactory(self, j):
        #sets some conditional variables
        w = 0
        d = 0
        global BinaryPixellist

        #only does this if it going to the bitmap window
        if j == 2:
            if d == 0:
                #adds empty variables to the list so that they can be edited via the use of splitting later
                for i in range(0, len(PixelCollist)):
                    BinaryPixellist[i] = ""
                d = 1

            #converts hexadecimal to binary
            for i in range(0, len(PixelCollist)):
                for s in range(0, 7):
                    for f in range(0, 16):
                        if Hexlist[f] == HexadecimalPixellist[i][s]:
                            BinaryPixellist[i] = BinaryPixellist[i] + Binlist[f]
                #checks if it has a colour depth below 24
                if DepthCheck == 1 or DepthCheck == 2 or DepthCheck == 3 or DepthCheck == 4 or DepthCheck == 6 or DepthCheck == 8 or DepthCheck == 15:
                    #sends through binary values to get shortened and appended to the binary list
                    BinaryPass = BinaryPixellist[i]
                    PixelManip.BinaryShortner(BinaryPass)
                    BinaryPixellist[i] = number3

        #used if going to any other window
        else:
            #converts hex into binary and appends it to binary list
            for s in range(0, 7):
                for i in range(0, 16):
                    if Hexlist[i] == self.HexadecimalPixellist[s]:
                        if j == 1:
                            if w == 0:
                                BinaryPixellist.append(Binlist[i])
                                w = 1
                            else:
                                BinaryPixellist[len(PixelCollist) - 1] = BinaryPixellist[len(PixelCollist) - 1] + Binlist[i]
                        elif j == 0:
                            if d == 0:
                                BinaryPixellist[self.Item["item"] - 1] = ""
                                d = 1
                            BinaryPixellist[self.Item["item"] - 1] = BinaryPixellist[self.Item["item"] - 1] + Binlist[i]
                            o = self.Item["item"] - 1

            #shortens binary values if not 24 bits
            if DepthCheck == 1 or DepthCheck == 2 or DepthCheck == 3 or DepthCheck == 4 or DepthCheck == 6 or DepthCheck == 8 or DepthCheck == 15:
                BinaryPass = BinaryPixellist[o]
                PixelManip.BinaryShortner(BinaryPass)
                BinaryPixellist[o] = number3
                o = o + 1
                global o
#_______________________________________________________________________________

#calls the initiation class, travels to create bitmap window
Init = Initiation()
Init.CreateBitmapWindow()

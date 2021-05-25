from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Log-in")
root.geometry("400x200")
root.iconbitmap("C:\\Users\\Bina Umat\\Documents\\Tutorial\\Python\\Logo's Project.PNG")

username = "1"
password = "1"

username1 = Label(root, text="MASUKKAN USERNAME")
username1.pack()
username2 = Entry(root, width=30, font=('Arial Black', 10))
username2.pack()
password1 = Label(root, text="MASUKKAN PASSWORD")
password1.pack()
password2 = Entry(root, width=30, font=('Arial Black', 10))
password2.pack()

# =====================================CALCULATOR=====================================================

def calculator():
    rootCalcu = Tk()
    rootCalcu.title("Calculator")

    global eCalcu

    eCalcu = Entry(rootCalcu, width=43, font=('Arial', 10))
    eCalcu.grid(row=0, column=0, columnspan=5)

    calcuBtn1 = Button(rootCalcu, text="1", pady=20, padx=30, command=lambda: buttonClickCalcu(1))
    calcuBtn1.grid(row=3, column=0)
    calcuBtn2 = Button(rootCalcu, text="2", pady=20, padx=30, command=lambda: buttonClickCalcu(2))
    calcuBtn2.grid(row=3, column=1)
    calcuBtn3 = Button(rootCalcu, text="3", pady=20, padx=30, command=lambda: buttonClickCalcu(3))
    calcuBtn3.grid(row=3, column=2)

    calcuBtn4 = Button(rootCalcu, text="4", pady=20, padx=30, command=lambda: buttonClickCalcu(4))
    calcuBtn4.grid(row=2, column=0)
    calcuBtn5 = Button(rootCalcu, text="5", pady=20, padx=30, command=lambda: buttonClickCalcu(5))
    calcuBtn5.grid(row=2, column=1)
    calcuBtn6 = Button(rootCalcu, text="6", pady=20, padx=30, command=lambda: buttonClickCalcu(6))
    calcuBtn6.grid(row=2, column=2)

    calcuBtn7 = Button(rootCalcu, text="7", pady=20, padx=30, command=lambda: buttonClickCalcu(7))
    calcuBtn7.grid(row=1, column=0)
    calcuBtn8 = Button(rootCalcu, text="8", pady=20, padx=30, command=lambda: buttonClickCalcu(8))
    calcuBtn8.grid(row=1, column=1)
    calcuBtn9 = Button(rootCalcu, text="9", pady=20, padx=30, command=lambda: buttonClickCalcu(9))
    calcuBtn9.grid(row=1, column=2)

    calcuBtnPlus = Button(rootCalcu, text="+", pady=20, padx=29, command=operator.addition)
    calcuBtnPlus.grid(row=1, column=3)
    calcuBtnMin = Button(rootCalcu, text="-", pady=20, padx=31, command=operator.subtraction)
    calcuBtnMin.grid(row=2, column=3)
    calcuBtnMulti = Button(rootCalcu, text="x", pady=20, padx=31, command=operator.multiplication)
    calcuBtnMulti.grid(row=3, column=3)
    calcuBtnDivi = Button(rootCalcu, text=":", pady=20, padx=32, command=operator.division)
    calcuBtnDivi.grid(row=4, column=3)

    calcuBtn0 = Button(rootCalcu, text="0", pady=20, padx=30, command=lambda: buttonClickCalcu(0))
    calcuBtn0.grid(row=4, column=0)
    calcuBtnC = Button(rootCalcu, text="Clear", pady=20, padx=20, command=clear)
    calcuBtnC.grid(row=4, column=1)
    calcuBtnEqual = Button(rootCalcu, text="=", pady=20, padx=29, command=equal)
    calcuBtnEqual.grid(row=4, column=2)

    rootCalcu.mainloop()

class operator():
    def addition():
        global math
        global eCalcu
        global fNumb

        firstNumber = eCalcu.get()
        fNumb = int(firstNumber)
        math = "Addition"
        eCalcu.delete(0, END)

    def subtraction():
        global math
        global eCalcu
        global fNumb

        firstNumber = eCalcu.get()
        fNumb = int(firstNumber)
        math = "Subtraction"
        eCalcu.delete(0, END)

    def multiplication():
        global math
        global eCalcu
        global fNumb

        firstNumber = eCalcu.get()
        fNumb = int(firstNumber)
        math = "Multiplication"
        eCalcu.delete(0, END)

    def division():
        global math
        global eCalcu
        global fNumb

        firstNumber = eCalcu.get()
        fNumb = int(firstNumber)
        math = "Division"
        eCalcu.delete(0, END)

def equal():
    global fNumb

    secondNumber = eCalcu.get()
    sNumb = int(secondNumber)
    eCalcu.delete(0, END)

    if math == "Addition":
        eCalcu.insert(0, fNumb + sNumb)
    elif math == "Subtraction":
        eCalcu.insert(0, fNumb - sNumb)
    elif math == "Multiplication":
        eCalcu.insert(0, fNumb * sNumb)
    elif math == "Division":
        eCalcu.insert(0, fNumb / sNumb)

def clear():
    eCalcu.delete(0, END)

def buttonClickCalcu(number):
    global eCalcu

    current = eCalcu.get()
    eCalcu.delete(0, END)
    eCalcu.insert(0, str(current) + str(number))

# =====================================CALCULATOR=======================================================


# =====================================VIEWER IMAGES====================================================

def forwardBtn(number):
    global status
    global rootViewerImages
    global buttonForward
    global buttonBack
    global buttonExit
    global imagesList
    global label

    label.grid_forget()
    buttonBack.grid_forget()
    buttonForward.grid_forget()
    buttonExit.grid_forget()
    label = Label(rootViewerImages, image=imagesList[number-1])
    buttonForward = Button(rootViewerImages, text=">>", command=lambda: forwardBtn(number+1), padx=20)
    buttonExit = Button(rootViewerImages, text="=======================", state=DISABLED, padx=20)
    buttonBack = Button(rootViewerImages, text="<<", command=lambda: backBtn(number-1), padx=20)
    status = Label(rootViewerImages, text="Images "+str(number)+" of "+str(len(imagesList)), bd=1, relief=SUNKEN, anchor=E)

    label.grid(row=0, column=0, columnspan=3)
    buttonForward.grid(row=1, column=2)
    buttonExit.grid(row=1, column=1)
    buttonBack.grid(row=1, column=0)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    if number == 4:
        buttonForward = Button(rootViewerImages, text=">>", state=DISABLED, padx=20)
        buttonForward.grid(row=1, column=2)

def backBtn(number):
    global status
    global rootViewerImages
    global buttonForward
    global buttonBack
    global buttonExit
    global imagesList
    global label

    label.grid_forget()
    buttonBack.grid_forget()
    buttonForward.grid_forget()
    buttonExit.grid_forget()
    label = Label(rootViewerImages, image=imagesList[number-1])
    buttonForward = Button(rootViewerImages, text=">>", command=lambda: forwardBtn(number+1), padx=20)
    buttonExit = Button(rootViewerImages, text="=======================", state=DISABLED, padx=20)
    buttonBack = Button(rootViewerImages, text="<<", command=lambda: backBtn(number-1), padx=20)
    status = Label(rootViewerImages, text="Images "+str(number)+" of "+str(len(imagesList)), bd=1, relief=SUNKEN, anchor=E)

    label.grid(row=0, column=0, columnspan=3)
    buttonForward.grid(row=1, column=2)
    buttonExit.grid(row=1, column=1)
    buttonBack.grid(row=1, column=0)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    if number == 1:
        buttonBack = Button(rootViewerImages, text="<<", state=DISABLED, padx=20)
        buttonBack.grid(row=1, column=0)

def viewerImages():
    global status
    global rootViewerImages
    global buttonForward
    global buttonBack
    global buttonExit
    global imagesList
    global label

    rootViewerImages = Tk()
    rootViewerImages.title("Viewer Images")

    images1 = ImageTk.PhotoImage(Image.open("C:\\Users\\Bina Umat\\Documents\\Tutorial\\Python\\TheOdd!sOut1.PNG"))
    images2 = ImageTk.PhotoImage(Image.open("C:\\Users\\Bina Umat\\Documents\\Tutorial\\Python\\TheOdd!sOut2.PNG"))
    images3 = ImageTk.PhotoImage(Image.open("C:\\Users\\Bina Umat\\Documents\\Tutorial\\Python\\TheOdd!sOut3.PNG"))
    images4 = ImageTk.PhotoImage(Image.open("C:\\Users\\Bina Umat\\Documents\\Tutorial\\Python\\Logo's Project.PNG"))

    imagesList = [images1, images2, images3, images4]

    label = Label(rootViewerImages, image=images1)
    label.grid(row=0, column=0, columnspan=3)

    buttonForward = Button(rootViewerImages, text=">>", padx=20, command=lambda: forwardBtn(2))
    buttonExit = Button(rootViewerImages, text="=======================", state=DISABLED, padx=20)
    buttonBack = Button(rootViewerImages, text="<<", state=DISABLED, padx=20)
    status = Label(rootViewerImages, text="Images 1 of "+ str(len(imagesList)), bd=1, relief=SUNKEN, anchor=E)

    buttonForward.grid(row=1, column=2)
    buttonExit.grid(row=1, column=1)
    buttonBack.grid(row=1, column=0)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    rootViewerImages.mainloop()

# =====================================VIEWER IMAGES====================================================

# =====================================RUN & OPEN APPS==================================================
def runOpenApps():
    rootRunOpenApps = Tk()
    rootRunOpenApps.title("Run & Open App")
    apps = []

    def openFiles():
        fileName = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Images","*.img"),
                                      ("All Files","*.*")))

        apps.append(fileName)
        for app in apps:
            label = Label(frame, text=app)
            label.pack()

    def runApps():
        for app in apps:
            os.startfile(app)

    canvas = Canvas(rootRunOpenApps, height=400, width=600, bg="green")
    frame = Frame(rootRunOpenApps, bg="white")
    frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)
    canvas.pack()

    openButton = Button(rootRunOpenApps, text="Open Files", padx=10, pady=5, fg="black", bg="white", command=openFiles)
    runButton = Button(rootRunOpenApps, text="Run Files", padx=15, pady=5, fg="black", bg="white", command=runApps)

    openButton.pack()
    runButton.pack()


    rootRunOpenApps.mainloop()

# =====================================RUN & OPEN APPS==================================================

def login():
    global username
    global password

    user = username2.get()
    passw = password2.get()

    if user == username and passw == password:
        messagebox.showinfo("Success", "Welcome " + user)

        rootLogin = Tk()
        rootLogin.title("Main Menu")
        rootLogin.geometry("400x400")

        root.destroy()

        calcuBtn = Button(rootLogin, text="Calculator", width=20, command=calculator)
        calcuBtn.pack(pady=30, ipady=10)
        Button(rootLogin, text="Viewer Images", width=20, command=viewerImages).pack(pady=30, ipady=10)
        Button(rootLogin, text="Run & Open Apps", width=20, command=runOpenApps).pack(pady=30, ipady=10)

        rootLogin.mainloop()
    else:
        messagebox.showerror("Error", "WRONG USERNAME OR PASSWORD")

button1 =Button(root, text="LOG-IN", command=login)
button1.pack(pady=10, ipady=3)

root.mainloop()
from tkinter import *
from random import randint

window = Tk()

dict = {1:"سنگ",
        2:"کاغذ",
        3:"قیچی"}

def stone():
    comp = randint(1,3)
    lbl["text"]=" انتخاب حریف : "+dict[comp]

    scoreComputer= int(lblResultComputer["text"])
    scorePlayer=int(lblResultPlayer["text"])

    if comp == 2:
        lblResultComputer["text"] = str(scoreComputer + 1)
    elif comp == 3:
        lblResultPlayer["text"] = str(scorePlayer + 1)

def paper():
    comp = randint(1,3)
    lbl["text"]=" انتخاب حریف : "+dict[comp]

    scoreComputer= int(lblResultComputer["text"])
    scorePlayer=int(lblResultPlayer["text"])

    if comp == 3:
        lblResultComputer["text"] = str(scoreComputer + 1)
    elif comp == 1:
        lblResultPlayer["text"] = str(scorePlayer + 1)

def scissors():
    comp = randint(1,3)
    lbl["text"]=" انتخاب حریف : "+dict[comp]

    scoreComputer= int(lblResultComputer["text"])
    scorePlayer=int(lblResultPlayer["text"])

    if comp == 1:
        lblResultComputer["text"] = str(scoreComputer + 1)
    elif comp == 2:
        lblResultPlayer["text"] = str(scorePlayer + 1)
    
# rest
def reset():
    lblResultComputer["text"] = 0
    lblResultPlayer["text"] = 0
    lbl["text"] = "انتخاب کنید"



window.title("Stone paper Scissors")
window.minsize(300,400)

window.rowconfigure([0,1,2,3] , weight=1)
window.columnconfigure(0,weight=1)

# set place holder to Entry
mystr = StringVar()
mystr.set('انتخاب کنید')

# use input as label
# input = Entry(textvariable=mystr,
#                 state=DISABLED , font=("None 20"),justify="center").grid(row=0
#                      , column=0 , sticky="nwe" , ipady=20)

lbl = Label(master=window, text="انتخاب کنید",height=2,width=15,font=("None",18,"bold"))
lbl.grid(
    row=0 , column=0, sticky="nwse"
)


# frame for buttons
frmBtn = Frame(master=window,height=100,bg="red")

frmBtn.rowconfigure(0,weight=1)
frmBtn.columnconfigure([0,1,2],weight=1)

btnStone = Button(master=frmBtn, text="سنگ",height=3 ,
    font=("None",16,"bold"),command=stone).grid(row=0,column=0,sticky="wnse",padx="3",pady=4)
btnPaper = Button(master=frmBtn, text="کاغذ",
    font=("None",16,"bold"),command=paper).grid(row=0,column=1,sticky="nsew",padx="3",pady=4)
btnScissors = Button(master=frmBtn, text="قیچی",
    font=("None",16,"bold"),command=scissors).grid(row=0,column=2,sticky="nswe",padx="3",pady=4)

frmBtn.grid(row=1,column=0,sticky="nwe")

# Frame result
frmResult = Frame(master=window,height=200)

# config result
frmResult.columnconfigure([0,1],weight=1)
frmResult.rowconfigure([0,1],weight=1)

#label player
lblPlayer = Label(master=frmResult,text="امتیاز شما")
lblPlayer.grid(row=0,column=0,sticky="nse")

#label player
lblPlayer = Label(master=frmResult,text="امتیاز شما",borderwidth=4,relief="ridge")
lblPlayer.grid(row=0,column=0,sticky="nswe")
#label Computer
lblComputer = Label(master=frmResult,text="امتیاز حریف",borderwidth=4,relief="ridge")
lblComputer.grid(row=0,column=1,sticky="nsew")

# player result
lblResultPlayer = Label(master=frmResult,text="0",font=("None",40),fg="#fff",bg="blue")
lblResultPlayer.grid(row=1,column=0,sticky="nsew")

# Computer result
lblResultComputer = Label(master=frmResult,bg="red",text="0",font=("None",40),fg="#fff",height=3)
lblResultComputer.grid(row=1,column=1,sticky="nsew")

frmResult.grid(row=2,column=0,sticky="nswe")



# btn reset
btnReset = Button(master=window,text="برو از اول",font=("None",16,"bold"),relief="ridge",
        borderwidth=4,command=reset).grid(row=3 , column=0,sticky="nswe")

window.mainloop()
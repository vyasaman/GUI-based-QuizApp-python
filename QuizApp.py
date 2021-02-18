from pymysql import *
from tkinter import *
from tkinter.ttk import *
from time import sleep
root = Tk()
root.geometry('500x400')
db = connect(host='localhost', port=3306, user='root',
             passwd='Aman@123', database='Exam')
cur = db.cursor()

adid = StringVar()
adpas = StringVar()
stid = StringVar()
stpas = StringVar()
msg = StringVar()
tech = StringVar()
var = StringVar()
count = 0
chooseOption = None
tName = StringVar()
m = StringVar()
mName = StringVar()
mPass = StringVar()
mRole = StringVar()
textbox = None
opa = StringVar()
opb = StringVar()
opc = StringVar()
opd = StringVar()


def addMember():
    top = Toplevel()
    top.geometry('500x400')
    role = ('Select Role for the Member', 'student', 'admin')
    lab1 = Label(top, text='Enter Name Of Member').place(
        height=20, width=150, x=50, y=100)
    name = Entry(top, textvariable=mName).place(
        height=20, width=100, x=230, y=100)
    lab2 = Label(top, text='Create Password for Member').place(
        height=20, width=200, x=50, y=130)
    pasword = Entry(top, textvariable=mPass).place(
        height=20, width=100, x=230, y=130)
    lab2 = Combobox(top, textvariable=mRole, value=role)
    sub = Button(top, text='ADD', command=membAdd).place(
        height=30, width=100, x=50, y=200)
    lab2.current(0)
    lab2.place(
        height=20, width=290, x=50, y=160)


def membAdd():
    cur.execute("insert into userdata(uname,pass,role) values('{}','{}','{}')".format(
        mName.get(), mPass.get(), mRole.get()))
    db.commit()


def addQuestion():
    top = Toplevel()
    top.geometry('500x400')
    lab1 = Label(top, text='Enter Question').place(
        height=30, width=200, x=50, y=50)
    textbox = Text(top).place(height=50, width=200, x=50, y=60)

    lab2 = Label(top, text='Enter option 1').place(
        height=30, width=100, x=50, y=70)
    op1 = Entry(top, textvariable=opa).place(height=30, width=100, x=100, y=70)

    lab3 = Label(top, text='Enter option 2').place(
        height=30, width=100, x=50, y=80)
    op2 = Entry(top, textvariable=opb).place(height=30, width=100, x=100, y=80)

    lab4 = Label(top, text='Enter option 3').place(
        height=30, width=100, x=50, y=90)
    op3 = Entry(top, textvariable=opc).place(height=30, width=100, x=100, y=90)

    lab5 = Label(top, text='Enter option 4').place(
        height=30, width=100, x=50, y=100)
    op4 = Entry(top, textvariable=opd).place(
        height=30, width=100, x=100, y=100)

    but = Button(top, text='ADD Question').place(
        height=30, width=100, x=50, y=150)


def addTechnology():
    cur.execute("select * from technology")
    res = cur.fetchall()
    top = Toplevel()
    top.geometry('500x400')
    lab = Label(top, text='List of Technology Present in the Database.').place(
        height=30, width=300, x=50, y=100)
    lb = Listbox(top)
    for i in res:
        lb.insert(i[0], i[1])
    lab1 = Label(top, text='Enter Technology').place(
        height=20, width=100, x=50, y=150)
    t = Entry(top, textvariable=tName).place(
        height=20, width=100, x=50, y=170)
    sub = Button(top, text='Submit', command=techAdding).place(
        height=20, width=100, x=50, y=200)
    msg = Message(top, textvariable=m).place(
        height=50, width=100, x=100, y=250)
    lb.place(height=100, width=100, x=300, y=130)


def techAdding():
    m.set(' ')
    sleep(2)
    cur.execute(
        "insert into technology(t_name) values('{}')".format(tName.get()))
    db.commit()
    m.set("Technology added Succsessfully")


def showResults():
    pass


def get():
    chooseOption = var.get()


def startTest():
    global count
    top = Toplevel()
    top.geometry('500x400')
    tch = tech.get()
    cur.execute("select tid from technology where t_name='{}'".format(tch))
    tid = cur.fetchone()
    cur.execute("select * from question where techID={}".format(tid[0]))
    res = cur.fetchall()

    ques = Label(top, text='Q1. ' + res[0][1]
                 ).place(height=50, width=400, x=100, y=70)

    op1 = Radiobutton(top, text=res[0][2], variable=var, value="a").place(
        height=30, width=100, x=50, y=200)
    op2 = Radiobutton(top, text=res[0][3], variable=var, value="b").place(
        height=30, width=100, x=150, y=200)
    op3 = Radiobutton(top, text=res[0][4], variable=var, value="c").place(
        height=30, width=100, x=50, y=250)
    op4 = Radiobutton(top, text=res[0][5], variable=var, value="d").place(
        height=30, width=100, x=150, y=250)
    nxt = Button(top, text='next', command=get()).place(
        height=30, width=100, x=150, y=300)
    submit = Button(top, text='Submit', command=get()).place(
        height=30, width=100, x=150, y=300)


def result():
    pass


def studentValidation():
    uid = stid.get()
    pswd = stpas.get()
    cur.execute("select * from userdata")
    res = cur.fetchall()

    for i in res:
        if i[0] == int(uid) and i[2] == pswd and i[3].lower() == 'student':

            studentDashboard(i)
            break
        else:
            msg.set('Invalid ID or Password')


def studentDashboard(res):

    msg.set('')
    top2 = Toplevel()
    top2.geometry('500x400')
    head = Label(top2, text='Welcome '+res[1]).place(
        height=30, width=100, x=200, y=70)

    head2 = Label(top2, text='Test Details').place(
        height=30, width=100, x=200, y=120)
    cur.execute("select * from technology")
    res1 = cur.fetchall()
    li = []
    for i in res1:
        li.append(i[1])
    li = tuple(li)
    st = Label(top2, text='Select Quiz Technology').place(
        height=30, width=150, x=50, y=200)
    cb = Combobox(top2, textvariable=tech, values=li).place(
        height=30, width=100, x=200, y=200)
    but = Button(top2, text="startTest", command=startTest).place(
        height=30, width=100, x=150, y=250)


def student():

    top = Toplevel()
    top.geometry('500x400')

    lid = Label(top, text='Enter UID ').place(
        height=20, width=100, x=10, y=70)
    eid = Entry(top, textvariable=stid).place(
        height=20, width=100, x=105, y=70)
    lpas = Label(top, text='Enter Password ').place(
        height=20, width=100, x=10, y=100)
    epas = Entry(top, textvariable=stpas, show='*').place(
        height=20, width=100, x=105, y=100)
    sbut = Button(top, text='submit', command=studentValidation).place(
        height=20, width=50, x=50, y=150)
    errorLabel = Message(top, textvariable=msg, foreground='red').place(
        height=30, width=100, x=50, y=170)


def adminValidation():
    uid = adid.get()
    pswd = adpas.get()
    cur.execute("select * from userdata")
    res = cur.fetchall()

    for i in res:
        if i[0] == int(uid) and i[2] == pswd and i[3].lower() == 'admin':

            adminDashboard(i)
            break
        else:
            msg.set('Invalid ID or Password')


def adminDashboard(res):
    msg.set('')
    t2 = Toplevel()
    t2.geometry('500x400')
    head = Label(t2, text='Welcome '+res[1]).place(
        height=30, width=150, x=200, y=70)

    head2 = Label(t2, text='Dashboard').place(
        height=30, width=100, x=205, y=120)
    addTech = Button(t2, text='Add Technology', command=addTechnology).place(
        height=30, width=100, x=150, y=150)
    addMem = Button(t2, text='Add Member', command=addMember).place(
        height=30, width=100, x=250, y=150)
    addQues = Button(t2, text='Add Question', command=addQuestion).place(
        height=30, width=100, x=150, y=200)
    showRes = Button(t2, text='Show Results', command=showResults).place(
        height=30, width=100, x=250, y=200)


def admin():
    t = Toplevel()
    t.geometry('500x400')

    lab1 = Label(t, text='Enter UID : ').place(
        height=30, width=100, x=10, y=70)
    aid = Entry(t, textvariable=adid).place(height=30, width=100, x=105, y=70)
    lab2 = Label(t, text='Enter Password : ').place(
        height=30, width=100, x=10, y=100)
    apas = Entry(t, textvariable=adpas).place(
        height=30, width=100, x=105, y=100)
    abut = Button(t, text='submit', command=adminValidation).place(
        height=20, width=50, x=50, y=150)
    errorLabel = Message(t, textvariable=msg, foreground='red').place(
        height=30, width=100, x=50, y=170)


wFrame = Frame(root).pack()
wel = Label(wFrame, text="Welcome").place(
    height=30, width=100, x=220, y=50)
wel2 = Label(wFrame, text='Select Login Type').place(
    height=30, width=100, x=200, y=100)
st = Button(wFrame, text='Student', command=student).place(
    height=30, width=100, x=150, y=150)
admin = Button(wFrame, text='Admin', command=admin).place(
    height=30, width=100, x=250, y=150)


root.mainloop()

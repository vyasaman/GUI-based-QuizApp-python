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
corOpt = StringVar()
tid = StringVar()
Ques = StringVar()
qlab = StringVar()


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
        height=27, width=150, x=50, y=40)
    textbox = Entry(top, textvariable=Ques).place(
        height=50, width=300, x=50, y=70)

    lab2 = Label(top, text='Enter option 1').place(
        height=27, width=150, x=50, y=130)
    op1 = Entry(top, textvariable=opa).place(
        height=27, width=150, x=200, y=130)

    lab3 = Label(top, text='Enter option 2').place(
        height=27, width=150, x=50, y=160)
    op2 = Entry(top, textvariable=opb).place(
        height=27, width=150, x=200, y=160)

    lab4 = Label(top, text='Enter option 3').place(
        height=27, width=150, x=50, y=190)
    op3 = Entry(top, textvariable=opc).place(
        height=27, width=150, x=200, y=190)

    lab5 = Label(top, text='Enter option 4').place(
        height=27, width=150, x=50, y=220)
    op4 = Entry(top, textvariable=opd).place(
        height=27, width=150, x=200, y=220)
    lab6 = Label(top, text="Select Correct Option").place(
        height=27, width=150, x=50, y=250)
    correct = Combobox(top, textvariable=corOpt)
    correct['values'] = ('a', 'b', 'c', 'd')
    correct.place(height=27, width=150, x=200, y=250)
    lab7 = Label(top, text='Select Technology').place(
        height=27, width=150, x=50, y=280)
    techid = Combobox(top, textvariable=tid)
    li = []
    cur.execute("select * from technology")
    res = cur.fetchall()
    for i in res:
        li.append(i[1])

    techid['values'] = tuple(li)
    techid.place(height=27, width=150, x=200, y=280)
    but = Button(top, text='ADD Question', command=quesADD).place(
        height=30, width=150, x=50, y=320)
    clr = Button(top, text='Clear', command=clear).place(
        height=30, width=150, x=200, y=320)


def clear():
    ques = Ques.set("")
    opta = opa.set("")
    optb = opb.set("")
    optc = opc.set("")
    optd = opd.set("")
    cor = corOpt.set("")
    techId = tid.set("")


def quesADD():
    ques = Ques.get()
    opta = opa.get()
    optb = opb.get()
    optc = opc.get()
    optd = opd.get()
    cor = corOpt.get()
    techId = tid.get()
    cur.execute("select * from technology where t_name='{}'".format(techId))
    res = cur.fetchone()

    cur.execute(
        "insert into question(question,op1,op2,op3,op4,correct,techID) values('{}','{}','{}','{}','{}','{}','{}')".format(ques, opta, optb, optc, optd, cor, res[0]))
    db.commit()


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
    top = Toplevel()
    top.geometry('500x400')
    lab1 = Label(top, text='Result').place(height=30, width=100, x=200, y=30)
    cur.execute("select * from results")
    res = cur.fetchall()
    lab2 = Label(top, text="").place(height=30, width=100, x=10, y=60)
    lab3 = Label(top, text="UID").place(height=30, width=100, x=0, y=80)
    lab4 = Label(top, text="TechID").place(
        height=30, width=100, x=100, y=80)
    lab5 = Label(top, text="Marks").place(height=30, width=100, x=200, y=80)
    lab6 = Label(top, text="Status").place(height=30, width=100, x=300, y=80)
    lab7 = Label(top, text='Time').place(height=30, width=100, x=400, y=80)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            e = Entry(top)
            e.insert(END, res[i][j])
            e.config(state='disabled')
            e.place(height=30, width=100, x=((j-1)*100), y=((i*30)+100))


def subm(t, status, uid, tecid):
    global count
    t.destroy()
    count = count*10
    if count > 20:
        status = "Pass"
    cur.execute("insert into results(uid,techID,marks,resDate,status) values ({},{},{},Now(),'{}')".format(
        uid, tecid, count, status))
    top = Toplevel()
    top.geometry('500x400')
    lab = Label(top, text='Test Completed').pack()
    count = 0
    but = Button(top, text='Go to Dashboard',
                 command=lambda: top.destroy()).pack()


a = 0


def questionAndOptions(top, nxt, submit):
    try:
        tch = tech.get()
        cur.execute("select tid from technology where t_name='{}'".format(tch))
        tid = cur.fetchone()
        cur.execute("select * from question where techID={}".format(tid[0]))
        res = cur.fetchall()
        global a
        global count
        if a < len(res):
            a += 1

        quescount.set(str(a)+'/'+str(len(res)))
        qlab.set('Q'+str(a)+'. '+res[a-1][1])
        op1 = Radiobutton(top, text=res[a-1][2], variable=var, value="a").place(
            height=30, width=100, x=50, y=200)
        op2 = Radiobutton(top, text=res[a-1][3], variable=var, value="b").place(
            height=30, width=100, x=150, y=200)
        op3 = Radiobutton(top, text=res[a-1][4], variable=var, value="c").place(
            height=30, width=100, x=50, y=250)
        op4 = Radiobutton(top, text=res[a-1][5], variable=var, value="d").place(
            height=30, width=100, x=150, y=250)
        chooseOption = var.get()
        if chooseOption == res[a-1][6]:
            count += 1
        yield res
    except Exception:
        print('question khatam')


quescount = StringVar()


def startTest(uid):
    tch = tech.get()
    cur.execute("select tid from technology where t_name='{}'".format(tch))
    tid = cur.fetchone()
    cur.execute("select * from question where techID={}".format(tid[0]))
    res = cur.fetchall()
    global a
    top = Toplevel()
    top.geometry('700x400')
    queslab = Label(top, text='', textvariable=qlab)
    cnt = Label(top, text='_/_', textvariable=quescount).place(
        height=30, width=50, x=450, y=20)
    nxt = Button(top, text='Next', command=lambda: next(questionAndOptions(top, nxt, submit))).place(
        height=30, width=100, x=100, y=300)
    status = ''
    submit = Button(top, text='Submit', command=lambda: subm(
        top, uid, tid)).place(height=30, width=100, x=200, y=300)

    queslab.place(height=60, width=700, x=0, y=50)


def result(res, res1):
    top = Toplevel()
    top.geometry('500x400')
    lab = Label(top, text='Result for ' +
                res[1]).place(height=30, width=200, x=150, y=50)
    lab1 = Label(top, text='UID').place(height=30, width=150, x=50, y=100)
    lab2 = Label(top, text='TechID').place(height=30, width=150, x=50, y=130)
    lab3 = Label(top, text='Marks Obtained').place(
        height=30, width=150, x=50, y=160)
    lab4 = Label(top, text='Result Time').place(
        height=30, width=150, x=50, y=190)
    lab5 = Label(top, text='Status').place(height=30, width=150, x=50, y=220)

    for i in range(1, len(res1)):
        e = Entry(top)
        e.insert(END, res1[i])
        e.config(state='disabled')
        e.place(height=30, width=150, x=250, y=(((i-1)*30)+100))


def studentValidation(t):
    uid = stid.get()
    pswd = stpas.get()
    cur.execute("select * from userdata")
    res = cur.fetchall()

    for i in res:
        if i[0] == int(uid) and i[2] == pswd and i[3].lower() == 'student':

            studentDashboard(i)
            t.destroy()
            break
        else:
            msg.set('Invalid ID or Password')


def resValid(stname):
    cur.execute("select * from userdata where uname='{}'".format(stname))
    res = cur.fetchone()
    cur.execute("select * from results where uid = {}".format(res[0]))
    res1 = cur.fetchone()
    if res1 != None:
        result(res, res1)


def studentDashboard(res):

    msg.set('')
    stid.set("")
    stpas.set("")
    top2 = Toplevel()
    top2.geometry('500x400')
    lout = Button(top2, text='Logout', command=lambda: top2.destroy()).place(
        height=30, width=100, x=400, y=20)
    head = Label(top2, text='Welcome '+res[1]).place(
        height=30, width=100, x=200, y=70)
    stname = res[1]
    head2 = Label(top2, text='Test Details').place(
        height=30, width=100, x=210, y=120)
    cur.execute("select * from technology")
    res1 = cur.fetchall()
    li = []
    for i in res1:
        li.append(i[1])
    li = tuple(li)
    st = Label(top2, text='Select Quiz Technology').place(
        height=30, width=150, x=50, y=160)
    cb = Combobox(top2, textvariable=tech, values=li).place(
        height=30, width=100, x=200, y=160)
    but = Button(top2, text="startTest", command=lambda: startTest(res[1])).place(
        height=30, width=100, x=150, y=250)
    but1 = Button(top2, text='Result', command=lambda: resValid(stname)).place(
        height=30, width=100, x=300, y=250)


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
    sbut = Button(top, text='submit', command=lambda: studentValidation(top)).place(
        height=20, width=50, x=50, y=150)
    errorLabel = Message(top, textvariable=msg, foreground='red').place(
        height=50, width=150, x=50, y=170)


def adminValidation(t):

    uid = adid.get()
    pswd = adpas.get()
    cur.execute("select * from userdata")
    res = cur.fetchall()

    for i in res:
        if i[0] == int(uid) and i[2] == pswd and i[3].lower() == 'admin':

            adminDashboard(i)
            t.destroy()
            break
        else:
            msg.set('Invalid ID or Password')


def adminDashboard(res):
    msg.set('')
    adid.set("")
    adpas.set("")
    t2 = Toplevel()
    t2.geometry('500x400')
    lout = Button(t2, text='Logout', command=lambda: t2.destroy()
                  ).place(height=30, width=100, x=400, y=20)
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
    abut = Button(t, text='submit', command=lambda: adminValidation(t)).place(
        height=30, width=50, x=50, y=150)
    errorLabel = Message(t, textvariable=msg, foreground='red').place(
        height=60, width=150, x=50, y=190)


def login():
    wFrame = Frame(root).pack()
    wel = Label(wFrame, text="Welcome").place(
        height=30, width=100, x=220, y=50)
    wel2 = Label(wFrame, text='Select Login Type').place(
        height=30, width=100, x=200, y=100)
    st = Button(wFrame, text='Student', command=student).place(
        height=30, width=100, x=150, y=150)
    admn = Button(wFrame, text='Admin', command=admin).place(
        height=30, width=100, x=250, y=150)


login()
root.mainloop()

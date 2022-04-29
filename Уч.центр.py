from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import font
from tkinter.constants import S
from tkinter import *


class SampleAPP(tk.Tk):
    def __init__(self, *arg, **kwargs ):
        tk.Tk.__init__(self, *arg, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
   


        self.frames = {}
        for F in(StartPage, Registration, MenuPage, uroki, online, Matematika, Fizika, Mnemonika, Mental_arifmetika, Ingliz_tili, Arab_tili, Grafik_Dizayn, SMM_Pro, Hisoblash, Hisoblash_2):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame



            frame. grid(row = 0, column = 0, sticky="nsew")

            self.show_frame("StartPage")


    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("O'quv markaz")
        self.controller.geometry('1250x650')   #almashtirish kerak ekanni razmeri
        self.controller.resizable(0, 0)
        self.controller.iconbitmap('lo.ico')  #almashtirish kerak iconka

        self.backGroundImage = PhotoImage(file=r'11.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)
        

        # Названия title
        heading_lable = tk.Label(self, text="O'quv markaz", bg=('#223345'), font = ('Monotype Corsiva', 50, 'bold'), fg="white")
        heading_lable.pack(pady=50)

        # Авторизация
        # логин
        login_lable = tk.Label(self, text="loginni kiriting", font = ('Monotype Corsiva', 20, 'bold'), fg="black")
        login_lable.pack()
       
        my_login = tk.StringVar()

        login_entry = tk.Entry(self, textvariable = my_login, font = ('Monotype Corsiva', 20, 'bold'), fg="black")
        login_entry.pack(pady=20)
       
       
         # Авторизация
         # пароль
        password_lable = tk.Label(self, text="parolni kiriting", font = ('Monotype Corsiva', 20, 'bold'), fg="black")
        password_lable.pack()


        my_password = tk.StringVar()

        password_entry = tk.Entry(self, textvariable = my_password, font = ('Monotype Corsiva', 20, 'bold'), fg="black")
        password_entry.pack(pady=20)

        def check_password():
            if my_password.get() == "1" and my_login.get() == "1":
                controller.show_frame('MenuPage')
                
                
                #right_label = tk.Label(self, text="Добро пожаловать")
                #right_label.pack()

            else:
                wrong_lable['text'] = "Login yoki parol xato"

        password_button = tk.Button(self, text=" Kirish ", command=check_password,  width = 15)
        password_button.pack()

        wrong_lable = tk.Label(self, bg=('#223345'), font = ('Monotype Corsiva', 20, 'bold'), fg="white")
        wrong_lable.pack(pady=30)


        def reg():
            controller.show_frame('Registration')
        pa_button = tk.Button(self, text=" Ro'yhatdan o'tish ", command=reg,  width = 15)
        pa_button.pack()

# Пункт регистраци

class Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#58BAE1")
        self.controller = controller

        heading_lable = tk.Label(self, text="Yangi ro'yhat", font = ('Monotype Corsiva', 50, 'bold'), fg="red", bg="#58BAE1")
        heading_lable.pack(pady=10)

        name_1_lable = tk.Label(self, text="Familiya", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#58BAE1")
        name_1_lable.pack(pady=10)

        name_1_entry = tk.Entry(self,  font = ('Monotype Corsiva', 15, 'bold'), fg="black")
        name_1_entry.pack(pady=0)

        name_2_lable = tk.Label(self, text="Ism", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#58BAE1")
        name_2_lable.pack(pady=10)

        name_2_entry = tk.Entry(self,  font = ('Monotype Corsiva', 15, 'bold'), fg="black")
        name_2_entry.pack(pady=0)

        name_3_lable = tk.Label(self, text="Login", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#58BAE1")
        name_3_lable.pack(pady=10)

        name_3_entry = tk.Entry(self,  font = ('Monotype Corsiva', 15, 'bold'), fg="black")
        name_3_entry.pack(pady=0)

        name_4_lable = tk.Label(self, text="Parol", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#58BAE1")
        name_4_lable.pack(pady=10)

        name_4_entry = tk.Entry(self, font = ('Monotype Corsiva', 15, 'bold'), fg="black")
        name_4_entry.pack(pady=0)

        name_5_lable = tk.Label(self, text="Parolni qaytatdan kiriting", font = ('Monotype Corsiva', 15, 'bold'), fg="red", bg="#58BAE1")
        name_5_lable.pack(pady=10)

        name_5_entry = tk.Entry(self, font = ('Monotype Corsiva', 15, 'bold'), fg="black")
        name_5_entry.pack(pady=0)

        save_button = tk.Button(self, text=" Yangi ro'yhat ", command=0, bg="#AEA0A0",  width = 25, font = ('Monotype Corsiva', 15, 'bold'), fg="black")
        save_button.pack()
        save_button.place(x = 485, y = 510)

        def exit():
            controller.show_frame('StartPage')

        uroki_button = tk.Button(self, text=" orqaga ", command=exit, bg="#AEA0A0",  width = 25, font = ('Monotype Corsiva', 15, 'bold'), fg="black")
        uroki_button.pack()
        uroki_button.place(x = 485, y = 560)


# Пункт главного меню

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#4AF8A6")
        self.controller = controller
     
              
        heading_lable = tk.Label(self, text="Xush kelibsiz! \n Rejimni tanlang", font = ('Monotype Corsiva', 40, 'bold'), fg="#003EFF", bg="#4AF8A6")
        heading_lable.pack(pady=10)

        def Nuroki():
            controller.show_frame('uroki')

        uroki_button = tk.Button(self, text=" Offlayn darslar ", command = Nuroki, bg="#4AF8A6",  width = 15, font = ('Monotype Corsiva', 25, 'bold'), fg="#003EFF")
        uroki_button.place(x = 450, y = 200)
        #uroki_button.pack()
        


        def online():
            controller.show_frame('online')

        online_button = tk.Button(self, text=" Zamonaviy kasblar ",  command=online, bg="#4AF8A6", width = 15, font = ('Monotype Corsiva', 25, 'bold'), fg="#003EFF")
        online_button.place(x = 450, y = 300)
        #online_button.pack()

        def exit():
            controller.show_frame('StartPage')

        uroki_button = tk.Button(self, text=" Tizimdan chiqish ", command=exit, bg="#4AF8A6",  width = 25, font = ('Monotype Corsiva', 25, 'bold'), fg="#003EFF")
        uroki_button.place(x = 400, y = 500)
        #uroki_button.pack()
         



      

class uroki(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        def get_send():
            controller.show_frame('Matematika')

        contact_button = tk.Button(self, text="Matematika", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 100, y = 200)


        def get_send():
            controller.show_frame('Fizika')

        contact_button = tk.Button(self, text="Fizika", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 100, y = 300)

        def get_send():
            controller.show_frame('Mnemonika')

        contact_button = tk.Button(self, text="Mnemonika", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 100, y = 400)

        def get_send():
            controller.show_frame('Mental_arifmetika')

        contact_button = tk.Button(self, text="Mental arifmetika", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 100, y = 500)

        def get_send():
            controller.show_frame('Ingliz_tili')

        contact_button = tk.Button(self, text="Ingliz tili", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 600, y = 200)

        def get_send():
            controller.show_frame('Arab_tili')

        contact_button = tk.Button(self, text="Arab tili", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 600, y = 300)



        def Hisoblash():
            controller.show_frame('Hisoblash')

        contact_button = tk.Button(self, text="Hisoblash", command=(Hisoblash), font=('Monotype Corsiva', 20, 'bold'), fg='blue', bg='yellow')
        contact_button.place(x = 600, y = 450)

           




        def back_menu():
            controller.show_frame('MenuPage')

        uroki_button = tk.Button(self, text=" orqaga ", command=back_menu, bg="yellow",  width = 10, font = ('Monotype Corsiva', 25, 'bold'), fg="red")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)





        heading_lable = tk.Label(self, text="Kerakli darslarni tanlang", font = ('Monotype Corsiva', 40, 'bold'), fg="red", bg="yellow")
        heading_lable.pack(pady=50)

 
class Hisoblash(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="blue")
        self.controller = controller



        def back_menu():
            controller.show_frame('MenuPage')

        uroki_button = tk.Button(self, text=" orqaga ", command=back_menu, bg="yellow",  width = 7, font = ('Monotype Corsiva', 15, 'bold'), fg="red")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)
        


        button_1 = tk.Label(self, text= "O'quv muddatini tanlang \n 1-oy  480 000 so'm (masalan 1)", font = ('Monotype Corsiva', 15, 'bold'), fg="white", bg="blue")
        button_1.place(x = 500, y = 90)
        result_1 = tk.Label(self, text='Оплата ')
        result_1.place(x=570,y=250, width=120, height=40)
        c = 480000
        entry_1 = tk.Entry(self)
        entry_1.place(x = 570, y = 160)

        def hisoblash():
            narx = c
            result_1.config(text=int(narx) * int(entry_1.get() ))

        tugma = tk.Button(self, text='рассчитать', command=hisoblash)
        tugma.place(x = 590, y = 200)








        
class online(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        def get_send():
            controller.show_frame('Grafik_Dizayn')

        contact_button = tk.Button(self, text="Grafik Dizayn", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 100, y = 200) 


        def get_send():
            controller.show_frame('SMM_Pro')

        contact_button = tk.Button(self, text="SMM pro", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 100, y = 300)

        def get_send():
            controller.show_frame('Shaxsiy Brend')

        contact_button = tk.Button(self, text="Shaxsiy Brend", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 100, y = 400)


        def get_send():
            controller.show_frame('Full stack dasturlash')

        contact_button = tk.Button(self, text="Full stack dasturlash", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 100, y = 500)


        def get_send():
            controller.show_frame('Python dasturlash')

        contact_button = tk.Button(self, text="Python dasturlash", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 600, y = 200)


        def get_send():
            controller.show_frame('C++')

        contact_button = tk.Button(self, text="C++", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 600, y = 300)

        def get_send():
            controller.show_frame('C#')

        contact_button = tk.Button(self, text="C#", command=(get_send), font=('Monotype Corsiva', 20, 'bold'), fg='red', bg='yellow')
        contact_button.place(x = 600, y = 400)


        def Hisoblash_2():
            controller.show_frame('Hisoblash_2')

        contact_button = tk.Button(self, text="Hisoblash", command=(Hisoblash_2), font=('Monotype Corsiva', 20, 'bold'), fg='blue', bg='yellow')
        contact_button.place(x = 600, y = 500)


  
        
        def back_menu():
            controller.show_frame('MenuPage')
            
        uroki_button = tk.Button(self, text=" orqaga ", command=back_menu, bg="yellow",  width = 10, font = ('Monotype Corsiva', 25, 'bold'), fg="red")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)


        heading_lable = tk.Label(self, text="Kerakli darslarni tanlang", font = ('Monotype Corsiva', 40, 'bold'), fg="red", bg="yellow")
        heading_lable.pack(pady=50)


class Hisoblash_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="blue")
        self.controller = controller


        button_1 = tk.Label(self, text= "Online o'quv muddatini tanlang \n 1-oy  280 000 so'm (masalan 1)", font = ('Monotype Corsiva', 15, 'bold'), fg="white", bg="blue")
        button_1.place(x = 500, y = 90)
        result_1 = tk.Label(self, text='Оплата ')
        result_1.place(x=570,y=250, width=120, height=40)
        c = 280000
        entry_1 = tk.Entry(self)
        entry_1.place(x = 570, y = 160)

        def hisoblash():
            narx = c
            result_1.config(text=int(narx) * int(entry_1.get() ))

        tugma = tk.Button(self, text='рассчитать', command=hisoblash)
        tugma.place(x = 590, y = 200)



        def back_menu():
            controller.show_frame('MenuPage')
            
        uroki_button = tk.Button(self, text=" orqaga ", command=back_menu, bg="yellow",  width = 10, font = ('Monotype Corsiva', 20, 'bold'), fg="red")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)









       
       
class Matematika(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        self.backGroundImage = PhotoImage(file=r'PicsArt_09-06-02.04.06.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        big_lable = tk.Label(self, text='Davronov Keldiyor', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 100, y=100)
        text = tk.Label(self, text='Tel:        +998936568855', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=200)
        text = tk.Label(self, text='Narx:        10$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=300)



        big_lable = tk.Label(self, text='Xolmatov Xumoyun', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 700, y=100)
        text = tk.Label(self, text='Tel:        +998933566699', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=200)
        text = tk.Label(self, text='Narx:        15$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=300)

        def back_menu():
            controller.show_frame('uroki')
            
        uroki_button = tk.Button(self, text=" orqaga ", command=back_menu, bg="#223345",  width = 10, font = ('Monotype Corsiva', 15, 'bold'), fg="white")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)




class Fizika(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        self.backGroundImage = PhotoImage(file=r'11.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        big_lable = tk.Label(self, text='Imomaliyev Mirkomil', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 100, y=100)
        text = tk.Label(self, text='Tel:        +998976956633', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=200)
        text = tk.Label(self, text='Narx:        10$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=300)


        big_lable = tk.Label(self, text='Berikbayev Jamshid', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 700, y=100)
        text = tk.Label(self, text='Tel:        +998333666655', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=200)
        text = tk.Label(self, text='Narx:        12$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=300)

        def back_menu():
            controller.show_frame('uroki')
            
        uroki_button = tk.Button(self, text=" orqaga ", command=back_menu, bg="#223345",  width = 10, font = ('Monotype Corsiva', 15, 'bold'), fg="white")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)


class Mnemonika(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        self.backGroundImage = PhotoImage(file=r'11.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        big_lable = tk.Label(self, text='Mamatkulov Davron', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 100, y=100)
        text = tk.Label(self, text='Tel:        +998976952226', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=200)
        text = tk.Label(self, text='Narx:        10$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=300)


        big_lable = tk.Label(self, text='Berikbayev Jamshid', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 700, y=100)
        text = tk.Label(self, text='Tel:        +998333666655', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=200)
        text = tk.Label(self, text='Narx:        12$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=300)

        def back_menu():
            controller.show_frame('uroki')
            
        uroki_button = tk.Button(self, text=" orqaga ", command=back_menu, bg="#223345",  width = 10, font = ('Monotype Corsiva', 15, 'bold'), fg="white")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)


class Mental_arifmetika(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        self.backGroundImage = PhotoImage(file=r'11.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        big_lable = tk.Label(self, text='Jumaniyozov Akmal', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 100, y=100)
        text = tk.Label(self, text='Tel:        +998976958217', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=200)
        text = tk.Label(self, text='Narx:        10$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=300)


        big_lable = tk.Label(self, text='Mamatqulov Xurshid', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 700, y=100)
        text = tk.Label(self, text='Tel:        +998333665496', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=200)
        text = tk.Label(self, text='Narx:        12$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=300)

        def back():
            controller.show_frame('uroki')
            
        uroki_button = tk.Button(self, text=" orqaga ", command=back, bg="#223345",  width = 10, font = ('Monotype Corsiva', 15, 'bold'), fg="white")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)


class Ingliz_tili(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        self.backGroundImage = PhotoImage(file=r'11.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        big_lable = tk.Label(self, text='Egamberdiya Sayyora', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 100, y=100)
        text = tk.Label(self, text='Tel:        +998999955685', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=200)
        text = tk.Label(self, text='Narx:        15$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=300)


        big_lable = tk.Label(self, text='Haydarova Munisa', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 700, y=100)
        text = tk.Label(self, text='Tel:        +998996335562', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=200)
        text = tk.Label(self, text='Narx:        12$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=300)

        def back():
            controller.show_frame('uroki')
            
        uroki_button = tk.Button(self, text=" orqaga ", command=back, bg="#223345",  width = 10, font = ('Monotype Corsiva', 15, 'bold'), fg="white")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)


class Arab_tili(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        self.backGroundImage = PhotoImage(file=r'11.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        big_lable = tk.Label(self, text='Jumaqulov Doston', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 100, y=100)
        text = tk.Label(self, text='Tel:        +998999959313', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=200)
        text = tk.Label(self, text='Narx:        15$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=300)


        big_lable = tk.Label(self, text='Egamqulov Holmurod', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 700, y=100)
        text = tk.Label(self, text='Tel:        +998996335562', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=200)
        text = tk.Label(self, text='Narx:        10$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=300)

        def back():
            controller.show_frame('uroki')
            
        uroki_button = tk.Button(self, text=" orqaga ", command=back, bg="#223345",  width = 10, font = ('Monotype Corsiva', 15, 'bold'), fg="white")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)


class Grafik_Dizayn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        self.backGroundImage = PhotoImage(file=r'11.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        big_lable = tk.Label(self, text='Toshmatov Farxod', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 100, y=100)
        text = tk.Label(self, text='Tel:        +998999959966', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=200)
        text = tk.Label(self, text='Narx:        15$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=300)


        big_lable = tk.Label(self, text='Eshmurodov Dilmurod', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 700, y=100)
        text = tk.Label(self, text='Tel:        +998996335562', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=200)
        text = tk.Label(self, text='Narx:        10$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=300)

        def back():
            controller.show_frame('online')
            
        uroki_button = tk.Button(self, text=" orqaga ", command=back, bg="#223345",  width = 10, font = ('Monotype Corsiva', 15, 'bold'), fg="white")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)


class SMM_Pro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller


        self.backGroundImage = PhotoImage(file=r'11.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        big_lable = tk.Label(self, text='Xudoyqulov Abror', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 100, y=100)
        text = tk.Label(self, text='Tel:        +998999959966', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=200)
        text = tk.Label(self, text='Narx:        15$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 100, y=300)


        big_lable = tk.Label(self, text='Eshmurodov Mirziyod', font=('Candara', 30, 'bold'), fg='white', bg='green')
        big_lable.pack(pady=30)
        big_lable.place(x = 700, y=100)
        text = tk.Label(self, text='Tel:        +998996335562', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=200)
        text = tk.Label(self, text='Narx:        10$    soatiga', font=('Candara', 20, 'bold'), fg='white', bg='green')
        text.pack(pady=30)
        text.place(x = 700, y=300)

        def back():
            controller.show_frame('online')
            
        uroki_button = tk.Button(self, text=" orqaga ", command=back, bg="#223345",  width = 10, font = ('Monotype Corsiva', 15, 'bold'), fg="white")
        uroki_button.pack()
        uroki_button.place(x = 30, y = 30)







if __name__=="__main__":
    app = SampleAPP()
    app.mainloop()





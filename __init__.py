from tkinter import *
import tkinter.messagebox as mb
class loginak(frame):
    def _init_(self,master):
        super()._init_(master)
        self.label_username=label(self,text="username",font=("times new roman",15))
        self.label_password=label(self,text="password",font=("times new roman",15))
        self.enter_username=entry(self)
        self.entry_password=entry(self)
        self.label_username.grid(row=0,sticky=e)
        self.label_password.grid(row=1,sticky=e)
        self.entry_username.grid(row=0,column=1)
        self.entry_password.grid(row=1,column=1)
        self.button=button(self,text='login',command=self.login)
        self.button.grid(columnspan=2)
        self.pack()
        def login(self):
            username=self.entry_username.get()
            password=self.entry_password.get()

            if(username =='ak' and password =='admin'):                                  
                mb.showinfo("login",'login successfully')
            else:
                mb.showinfo('login','login failed')


ak=tk()
login=loginak(ak)
ak.mainloop()
        

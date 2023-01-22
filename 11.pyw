import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random as ran
import os
def root():
    r=tk.Tk()
    r.title("GETWUW")
    r.attributes('-fullscreen', True)
    color=["cyan","blue","green","orange","yellow","pink","violet","gray","#7ed1e1","#e6f4f7","#abdbe3","#DBCE5A","#5AA1D9","#EADAAB","#EBAB4C","#CCC586"]
    clr=ran.choice(color)
    r.config(bg=clr)
    mname=tk.Label(r,text="MODULE",bg=clr,font='sans 18 bold')
    mname.place(x=335,y=300)
    def get():
        gmd=(getmodule.get()).lower()
        getmodule.set("")
        if gmd and len(gmd)>1:
                    fname=gmd+".txt"
                    try:
                            f=open(fname,'r')
                    except:
                            mb.showerror('FALSE','NO SUCH MODULE FOUND')
                    else:
                        data=f.read()
                        if(len(data)>0):
                            r.destroy()
                            g=tk.Tk()
                            g.title(gmd)
                            g.geometry('1200x1200')
                            g.config(bg="black")
                            g.attributes('-fullscreen', True)
                            v=tk.Scrollbar(g,orient='vertical')
                            v.pack(side="right", fill='y')
                            t=tk.Text(g,yscrollcommand=v.set,height=38,width=157,font="sans 11 bold",fg='black')
                            t.config(bg="white")
                            
                    
                            mLbl="Let us learn about "+gmd.upper()+" Module in Python"
                            l=tk.Label(g,text=mLbl,bg="black",fg='white',font="Courier 14 bold")

                            
                            v.config(command=t.yview)
                            l.pack()                       
                            t.insert(tk.END,data) 
                            f.close()
                            t.config(state="disable")
                            t.place(x=52,y=40)
                            def saveit():
                                    t.config(state="disable")
                                    Q=t.get(1.0, "end-1c")
                                    #mb.showinfo('df',Q)
                                    #print(Q)
                                    f=open(fname,'w')
                                    f.write(Q)
                                    f.close()
                                    
                            save=tk.Button(g,text="SAVE",fg="white",bg='black',activebackground='black',borderwidth=0,command=saveit,font="sans 9 bold")
                            save.place(x=650,y=737)
                            def editit():
                                t.config(state="normal")
                                
                            edit=tk.Button(g,text="EDIT",fg="white",bg='black',activebackground='black',borderwidth=0,command=editit,font="sans 9 bold")
                            edit.place(x=250,y=737)
                            def printnow():
                                f=open(fname,'r')
                                x=f.read()
                                f.close()
                                if(len(x)>0):
                                    os.startfile(fname,'print')                                
                            prntnow=tk.Button(g,text='DOWNLOAD',bd=1,font="sans 10 bold",borderwidth=0,activebackground='black',fg='white',bg='black',command=printnow)
                            prntnow.place(x=1105,y=737)
                            def des():
                                g.destroy()
                                root()
                            desb=tk.Button(g,text=" X ",fg="white",bg='black',activebackground='black',borderwidth=0,command=des,font="sans 15 bold")
                            desb.place(x=1300,y=2)
                            
                        else:
                            ask=mb.askyesno('FALSE','NO DATA_FOUND \n Do you want to provide information!!')
                            if ask:
                                r.destroy()
                                g=tk.Tk()
                                g.title(gmd)
                                g.geometry('1200x1200')
                                g.config(bg="black")
                                g.attributes('-fullscreen', True)
                                v=tk.Scrollbar(g,orient='vertical')
                                v.pack(side="right", fill='y')
                                t=tk.Text(g,yscrollcommand=v.set,height=38,width=157,font="sans 11 bold",fg='black')
                                t.config(bg="white")
                                
                        
                                mLbl="Enter information about "+gmd.upper()+" Module"
                                l=tk.Label(g,text=mLbl,bg="black",fg='white',font="Courier 14 bold")
                                #l.config(font=("Courier",14))
                                v.config(command=t.yview)
                                l.pack()                       
                                t.insert(tk.END,"") 
                                f.close()
                                #t.config(state="disable")
                                t.place(x=52,y=40)
                                def saveit():
                                    t.config(state="disable")
                                    Q=t.get(1.0, "end-1c")
                                    #mb.showinfo('df',Q)
                                    #print(Q)
                                    f=open(fname,'w')
                                    f.write(Q)
                                    f.close()
                                    
                                save=tk.Button(g,text="SAVE",fg="white",bg='black',activebackground='black',borderwidth=0,command=saveit,font="sans 9 bold")
                                save.place(x=650,y=737)
                                def editit():
                                    t.config(state="normal")
                                    
                                edit=tk.Button(g,text="EDIT",fg="white",bg='black',activebackground='black',borderwidth=0,command=editit,font="sans 9 bold")
                                edit.place(x=250,y=737)
                                def printnow():
                                    f=open(fname,'r')
                                    x=f.read()
                                    f.close()
                                    if(len(x)>0):
                                        os.startfile(fname,'print')

                                    
                                prntnow=tk.Button(g,text='DOWNLOAD',bd=1,font="sans 10 bold",borderwidth=0,activebackground='black',fg='white',bg='black',command=printnow)
                                prntnow.place(x=1105,y=737)
                                def des():
                                    g.destroy()
                                desb=tk.Button(g,text=" X ",fg="white",bg='black',activebackground='black',borderwidth=0,command=des,font="sans 15 bold")
                                desb.place(x=1300,y=2)
                                g.mainloop()
                                root()
                            else:
                                mb.showinfo('SORRY','TRY again later!!')
        elif len(gmd)>0 and len(gmd)<2:
            mb.showerror('FALSE','Enter Proper Module Name')
        else:
            mb.showerror("FALSE","ENTER MODULE NAME")

        
    getmodule=tk.StringVar()
    mname_e=tk.Entry(r,bd=1,width=30,font='sans 18 bold',textvariable=getmodule)
    mname_e.place(x=450,y=300)
    mbtn=tk.Button(r,text="G E T",bd=1,font='sans 14 bold',command=get,cursor="arrow")
    mbtn.place(x=850,y=299)

    smname=tk.Label(r,text="REQUEST",bg=clr,font='sans 18 bold')
    smname.place(x=325,y=375)
    def set():
        smd=setmodule.get()
        if smd and len(smd)>1:
                fname=smd.capitalize()
                f=open('MODULELIST','r')
                lis2=f.read()
                tozo=list(lis2.split('-'))
                smd=smd.lower()
                if smd not in tozo:            
                    f=open('MODULELIST','a')
                    apnd='-'+smd.lower()
                    f.write(apnd)
                    f.close()
                    crtfile=smd+".txt"
                    crtfile=crtfile.lower()
                    #print(crtfile)
                    f=open(crtfile,'w')
                    f.close()
                    mb.showinfo(smd,"Succesfully Updated")
                else:
                    mb.showerror('FALSE','File already exist!!')
        elif len(smd)>0 and len(smd)<2:
            mb.showerror('FALSE','Enter Proper Module Name')
        else:
            mb.showerror("FALSE","Enter Module Name")
        setmodule.set("")
    setmodule=tk.StringVar()
    sname_e=tk.Entry(r,bd=1,width=30,font='sans 18 bold',textvariable=setmodule)
    sname_e.place(x=450,y=375)
    sbtn=tk.Button(r,text="S E T",bd=1,font='sans 14 bold',command=set)
    sbtn.place(x=850,y=372)

    ###SHOW ALLL###
    def showall():
        r.destroy()
        f=open('MODULELIST','r')
        lis2=f.read()
        tozo=list(lis2.split('-'))

        f.close()
        showll=tk.Tk()
        showll.geometry('500x330')
        showll.title("MODULES")
        showll.config(bg="black")
        showll.attributes('-fullscreen', True)
        #showll.minsize(500,330)
        #showll.maxsize(500,330)
        t=tk.Text(showll,width=97,height=25,bg=clr,font="sans 17 bold")
        l=tk.Label(showll,text="A L L   A V A I L A B L E   M O D U L E S",font="sans 15 bold",bg="black",fg="white")
        l.place(x=530,y=10)
        t.place(x=50,y=50)
        count=0
        print(tozo)
        for i in (sorted(tozo)):
            count+=1
            c=count
            Q=str(c)+')'+i.capitalize()+'\n'  
            t.insert(tk.END,Q)
        t.config(state="disable")
        def des():
            showll.destroy()
        desb=tk.Button(showll,text=" X ",fg="white",bg="black",activebackground="black",activeforeground="black",borderwidth=0,command=des,font="sans 15 bold")
        desb.place(x=1310,y=5)
        reser=tk.Label(showll,text="A l l  r i g h t s  r e s e r v e d  © v n r v j i e t . h y d",bg='black',fg='white',font="sans 9 bold")
        reser.pack(side='bottom')
        showll.mainloop()
        return root()
    sall=tk.Button(r,text="S H O W A L L",bd=1,command=showall,font="sans 14 bold")
    sall.place(x=520,y=450)


    def des():
        r.destroy()
    desb=tk.Button(r,text=" X ",fg="black",bg=clr,activebackground=clr,activeforeground=clr,borderwidth=0,command=des,font="sans 15 bold")
    desb.place(x=1305,y=10)
    def about():
        r.destroy()
        abt=tk.Tk()
        abt.attributes('-fullscreen',True)
        Devl=tk.Label(abt,text="A B O U T  U S",fg="black",font="sans 15 bold")
        Devl.pack(pady=15,side='top')
        sl=tk.Label(abt,text="VIJAY",fg="black",font="sans 15 bold")
        vl=tk.Label(abt,text="RAHUL",fg="black",font="sans 15 bold")
        rl=tk.Label(abt,text="CHANDRA",fg="black",font="sans 15 bold")
        pl=tk.Label(abt,text="SAIPAVAN",fg="black",font="sans 15 bold")
        bl=tk.Label(abt,text="SHANTHAN",fg="black",font="sans 15 bold")
        shl=tk.Label(abt,text="BHANU",fg="black",font="sans 15 bold")
        cl=tk.Label(abt,text="SATHISH",fg="black",font="sans 15 bold")

        sl.place(x=150,y=150)
        vl.place(x=450,y=150)
        rl.place(x=750,y=150)
        pl.place(x=1050,y=150)

        bl.place(x=300,y=250)
        shl.place(x=600,y=250)
        cl.place(x=900,y=250)

        descrpt=tk.Label(abt,text="COMPUTER SCIENCE AND ENGINEERING 2021-25",font="sans 25 bold",fg="BLACK")
        descrpt.place(x=285,y=500)
        clg=tk.Label(abt,text="V N R  V J I E T",font="sans 18 bold",fg="BLACK")
        clg.place(x=550,y=555)
        
        def des():
            abt.destroy()
        desb=tk.Button(abt,text=" X ",fg="black",borderwidth=0,command=des,font="sans 15 bold")
        desb.place(x=1305,y=10)
        reser=tk.Label(abt,text="A l l  r i g h t s  r e s e r v e d  © v n r v j i e t . h y d",font="sans 9 bold")
        reser.pack(side='bottom')
        def fmain():
            def feedback():
                fd.place_forget()
                t=tk.Text(abt,width=20,height=7,bg='white',fg='black',font='sans 11 bold')
                t.place(x=1150,y=590)
                
                def cancel():
                    t.destroy()
                    can.place_forget()
                    submit.place_forget()
                    fmain()
                can=tk.Button(abt,text='CANCLE',command=cancel,fg="white",activeforeground='white',activebackground='black',bg='black',borderwidth=1,font="sans 7 bold")
                can.place(x=1250,y=725)
                def sub(): 
                    Q=t.get(1.0, "end-1c")
                    if(len(Q)>0):
                        f=open('feedback.txt','a')
                        f2=open('feedback.txt','r')
                        data=f2.read()
                        f2.close()
                        if(len(data)>0):
                            Q='\n'+Q
                        else:
                            Q=Q
                        f.write(Q)
                        f.close()
                        t.destroy()
                        submit.place_forget()
                        can.place_forget()
                        mb.showinfo('FEEDBACK','Thank you for the feedback')
                    else:
                        mb.showerror('FALSE','TYPE YOUR FEEDBACK')
                submit=tk.Button(abt,text='SUBMIT',command=sub,fg="white",activeforeground='white',activebackground='black',bg='black',borderwidth=1,font="sans 7 bold")
                submit.place(x=1165,y=725)
            fd=tk.Button(abt,text='FEEDBACK',command=feedback,fg="white",activeforeground='white',activebackground='black',bg='black',borderwidth=1,font="sans 7 bold")
            fd.place(x=1185,y=725)
        fmain()
        def REVIEWS():
            def reviews():
                f2=open('feedback.txt','r')
                data=f2.read()
                f2.close()
                if(len(data)>0):
                    rev.place_forget()
                    f=open('feedback.txt','r')
                    data=f.read()
                    f.close()
                    t=tk.Text(abt,width=25,height=8,font='sans 11 bold')
                    t.place(x=1150,y=610)
                    t.insert(tk.END,data)
                    t.config(state='disable')
                    def close():
                        t.destroy()
                        clo.place_forget()
                        REVIEWS()
                    
                    clo=tk.Button(abt,text='X',command=close,fg="white",activeforeground='white',activebackground='black',bg='black',borderwidth=1,font="sans 7 bold")
                    clo.place(x=1325,y=590)
                else:
                    mb.showinfo('FALSE','NO RESPONSES YET')
            rev=tk.Button(abt,text='REVIEWS',command=reviews,fg="white",activeforeground='white',activebackground='black',bg='black',borderwidth=1,font="sans 7 bold")
            rev.place(x=1249,y=725)
        REVIEWS()
        abt.mainloop()
        return root()
    abt=tk.Button(r,text="A B O U T",bd=1,command=about,font="sans 15 bold")
    abt.place(x=680,y=450)
    reser=tk.Label(r,text="A l l  r i g h t s  r e s e r v e d  © v n r v j i e t . h y d",bg=clr,font="sans 9 bold")
    reser.pack(side='bottom')
    reser=tk.Label(r,text="G E T W U W",bg=clr,font="sans 20 bold")
    reser.pack(pady=20,side='top')
    r.mainloop()
root()

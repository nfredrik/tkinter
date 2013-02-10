import Tkinter 
from Tkinter import *

#entry = None
entry  = Entry(root, width=50).pack(side=TOP,padx=10,pady=10)


def on_button():
    print 'got it', entry.get()

root =Tk()
root.title('entry widget')
Label (text='enter URL to the jenkins job').pack(side=TOP,padx=10,pady=10)
#entry  = Entry(root, width=50).pack(side=TOP,padx=10,pady=10)
Button(root, text='open',command=on_button).pack(side= LEFT)
Button(root, text='edit').pack(side= LEFT)
Button(root, text='exit').pack(side= RIGHT)
Button(root, text='close').pack(side= RIGHT)
root.mainloop()



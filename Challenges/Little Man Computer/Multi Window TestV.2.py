import tkinter as tk




def cbc(tex):
    return lambda : callback(tex)

def callback(tex):
    
    s = RAM, '\n'
    tex.insert(tk.END, s)
    tex.see(tk.END)            

top = tk.Tk()
tex = tk.Text(master=top)
tex.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)

button = tk.Button(bop, text="View RAM", command=cbc(tex))
button.pack()

tk.Button(bop, text='Exit', command=top.destroy).pack()
top.mainloop()
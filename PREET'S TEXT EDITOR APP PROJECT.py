# PREET'S TEXT EDITOR APPLICATION


import tkinter as tk
from tkinter import filedialog,messagebox

#--------------MAIN WINDOW------------------------
root=tk.Tk()
root.title("Preet's Text Editor")
root.geometry("800x600")

#-------------TEXT AREA--------------------------
text=tk.Text(root,wrap=tk.WORD,font=("Arial",18))
text.pack(expand=True,fill=tk.BOTH)

#------------FILE FUNCTIONS---------------------

#function to create new file
def new_file():
    text.delete(1.0,tk.END)
    root.title("Untitled -Preet's Text Editor")

#function to open existing file
def open_file():
    #open filedialog to select a text file
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents","*.txt"),("All files","*.*")]
        )
    if file_path:
        try:
            with open(file_path,"r")as file:
                text.delete(1.0,tk.END)
                text.insert(tk.END,file.read())
                root.title(f"{file_path}-Preet's Text Editor")
        except exception as e :
            messagebox.showerror("Error",f"could not open file :{e}")

#function to save file
def save_file():
    #open save filedialog
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents",".txt"),("All files","*.*")]
        )
    if file_path:
        try:
            with open(file_path,"w")as file:
             file.write(text.get(1.0,tk.END))
             root.title(f"{file_path}-Preet's Text Editor")
             messagebox.showinfo("Info","File saved successfully")
        except exception as e:
            messagebox.showerror("Error",f"could not save file:{e}")
#function to exit app
def exit_app():
    if messagebox.askokcancel("Quit","Do you want to quit?"):
        root.destroy()

#--------------MENU BAR-----------------------------
#create menu bar
menu_bar=tk.Menu(root)
#create filemenu & dropdown under file menu
file_menu=tk.Menu(menu_bar)
#Add filemenu to menubar
menu_bar.add_cascade(label="File",menu=file_menu)
#add new option to file menu
file_menu.add_command(label="New",command=new_file)
#add open option
file_menu.add_command(label="Open",command=open_file)
#add save option
file_menu.add_command(label="Save",command=save_file)
#add separtaor line in menu
file_menu.add_separator()
#add exit option to close the app
file_menu.add_command(label="Exit",command=exit_app)
root.config(menu=menu_bar)

#----------------RUN APPLICATION-------------------
root.mainloop()


        
        
                
            

# Import tkinter as tk for creating graphical user interface
import tkinter as tk
# Import tkinter.messagebox for displaying warning messages
import tkinter.messagebox  
# Import pickle for saving and loading tasks in a file
import pickle  

# Create the root window of the app
root  = tk.Tk()
# Set the title of the window
root.title("To-Do list @wambaforestin")

# Define a function to add a task to the listbox
def addtask():
    # Get the task from the entry widget
    task = entrytask.get()
    # If the task is not empty, insert it at the end of the listbox
    if task !=" ":
        taskbox.insert(tk.END, task)
        # Clear the entry widget
        entrytask.delete(0,tk.END)
    # If the task is empty, show a warning message
    else:
        tk.messagebox.showwarning(title="Warning!!",message="You must enter a task.")

# Define a function to delete a task from the listbox
def deletetask():
    try:
        # Get the index of the selected task in the listbox
        taskindex = taskbox.curselection()[0]
        # Delete the task from the listbox
        taskbox.delete(taskindex)
    # If no task is selected, show a warning message
    except:
         tk.messagebox.showwarning(title="Warning!!",message="You must select a task.")

# Define a function to load tasks from a file
def loadtask():
   try:
       # Load tasks from a file using pickle
        tasks = pickle.load(open("tasks.txt" , "rb")) 
        # Clear the listbox
        taskbox.delete(0,tk.END)
        # Insert each task in the listbox
        for task in tasks:
            taskbox.insert(tk.END, task)
   # If the file is not found or invalid, show a warning message
   except:
       tk.messagebox.showwarning(title="Warning!!",message="Unknown file!")

# Define a function to save tasks to a file
def savetask():
    # Get all the tasks from the listbox as a tuple
    tasks = taskbox.get(0,taskbox.size())
    # Save tasks to a file using pickle
    pickle.dump(tasks , open("tasks.txt","wb"))

# Create a frame for adding tasks and displaying them in a scrollable box
framefortask = tk.Frame(root)
framefortask.pack()   

# Create a listbox for displaying tasks
taskbox = tk.Listbox(framefortask,height=5,width=50)
taskbox.pack(side='left' )

# Create a scrollbar for scrolling through tasks
scrollbar = tk.Scrollbar(framefortask)
scrollbar.config(command=taskbox.yview)#binding scrollbar to y axis of taskbox 
scrollbar.pack(side='right',fill='y')

# Create an entry widget for entering tasks
entrytask = tk.Entry(root, width=35,borderwidth=5)
entrytask.pack()
 
# Create a button for adding tasks and bind it to the addtask function
addbutton = tk.Button(root, text="Add Task" ,width=48,command=addtask, bg="darkblue",fg="white",borderwidth=4)
addbutton.pack()

# Create a button for deleting tasks and bind it to the deletetask function
addbutton = tk.Button(root, text="Delete Task" ,width=48,command=deletetask, bg="darkblue",fg="white",borderwidth=4)
addbutton.pack()

# Create a button for loading tasks and bind it to the loadtask function
addbutton = tk.Button(root, text="load Task" ,width=48,command=loadtask, bg="darkblue",fg="white",borderwidth=4)
addbutton.pack()

# Create a button for saving tasks and bind it to the savetask function
addbutton = tk.Button(root, text="Save Task" ,width=48,command=savetask, bg="darkblue",fg="white",borderwidth=4)
addbutton.pack()

# Start the main loop of the app
root.mainloop()

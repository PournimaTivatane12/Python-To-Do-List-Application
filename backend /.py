from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('650x410+300+150')

        # Title Label
        self.label = Label(self.root, text='To-Do-List App', 
                           font=('Arial', 25, 'bold'), width=20, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        # Add Task Label
        self.label2 = Label(self.root, text='Add Task', 
                            font=('Arial', 18, 'bold'), width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        # Tasks Label
        self.label3 = Label(self.root, text='Tasks', 
                            font=('Arial', 18, 'bold'), width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        # Task Listbox
        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font=('Arial', 20, 'italic', 'bold'))
        self.main_text.place(x=280, y=100)

        # Textbox to Add New Task
        self.text = Text(self.root, bd=5, height=2, width=30, font=('Arial', 10, 'bold'))
        self.text.place(x=20, y=120)

        # Load tasks from file when initializing
        self.load_tasks()

        # Add Task Button
        self.button = Button(self.root, text="Add", font=('Sarif', 20, 'bold', 'italic'),
                             width=10, bd=5, bg='orange', fg='black', command=self.add)
        self.button.place(x=30, y=180)

        # Delete Task Button
        self.button2 = Button(self.root, text="Delete", font=('Sarif', 20, 'bold', 'italic'),
                              width=10, bd=5, bg='orange', fg='black', command=self.delete)
        self.button2.place(x=30, y=280)

    # Add task method
    def add(self):
        content = self.text.get("1.0", END).strip()
        if content:  # Only add if the content is not empty
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + "\n")
            self.text.delete(1.0, END)

    # Delete task method
    def delete(self):
        try:
            selected_task_index = self.main_text.curselection()[0]
            selected_task = self.main_text.get(selected_task_index)

            self.main_text.delete(selected_task_index)
            self.update_file(selected_task)

        except IndexError:
            # No item selected, ignore the delete command
            pass

    # Method to update file after deleting a task
    def update_file(self, task_to_delete):
        with open('data.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip("\n") != task_to_delete:
                    file.write(line)
            file.truncate()

    # Load tasks from file on startup
    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    self.main_text.insert(END, line.strip())
        except FileNotFoundError:
            # If the file doesn't exist, we simply ignore it.
            pass

# Main function to run the application
def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()

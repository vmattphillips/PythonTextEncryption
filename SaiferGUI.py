import sys
import os
import saifer

# Half working attempt at making a GUI to interface with the saifer.py backend

sai = saifer

class Globals:
    key_path = ""
    txt_path = ""
    saifertxt_path = ""

def reset_Globals():
    Globals.key_path = "-No File Selected-"
    Globals.txt_path = "-No File Selected-"
    Globals.saifertxt_path = "-No File Selected-"


def valid_path(path):
    return os.path.exists(path)

def newKey_Click():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user to enter a name
    name = tk.simpledialog.askstring("Enter Name", "Please enter a name for the key:\t\t", )

    # Display the name entered by the user
    if name:
        path = sai.makeKey(name)
        tk.messagebox.showinfo("Success", f"Key saved at: {path}")
    else:
        tk.messagebox.showerror("Error", "Name cannot be empty")
        return

def encrypt_Click():
    if (valid_path(Globals.key_path) and valid_path(Globals.txt_path)):
        print("doing stuff")
    else:
        tk.messagebox.showerror("Error", "One or more paths provided do not exist")

def decrypt_Click():
    if (valid_path(Globals.key_path) and valid_path(Globals.saifertxt_path)):
        print("doing stuff")
    else:
        tk.messagebox.showerror("Error", "One or more paths provided do not exist")
        return

def select_Key():
    # Create a Tkinter root window
    key_window = tk.Tk()
    key_window.withdraw()  # Hide the root window

    # Open a file dialog for selecting a key file
    key_file_path = filedialog.askopenfilename(initialdir=os.getcwd()+"/Keys", title="Select Key",
                                           filetypes=[("Saifer Keys", "*.saiferkey")])

    # Check if a file was selected
    if (key_file_path and valid_path(key_file_path)):
        Globals.key_path = key_file_path
        key_path_var.set(Globals.key_path)
    else:
        tk.messagebox.showerror("Error", "One or more paths provided do not exist")
    
    root.update()

# Create the main window
root = tk.Tk()
root.title("Saifer GUI")
root.geometry("600x600")

reset_Globals()

#TK Variables
key_path_var = tk.StringVar()
key_path_var.trace_add("write", update_label)
key_path_var.set(Globals.key_path)

update_label()
  
# Row 0
new_key = tk.Button(root, text="New Key", command=newKey_Click, width=15, height=3, font=("Arial", 12))
new_key.grid(row=0, column=0, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_Click, width=15, height=3, font=("Arial", 12))
encrypt_button.grid(row=0, column=1, padx=5, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_Click, width=15, height=3, font=("Arial", 12))
decrypt_button.grid(row=0, column=2, padx=5, pady=5)

# Row 1
label = tk.Label(root, text="Use the buttons below to select the files you'd like to encrypt or decrypt:", font=('Arial', 12))
label.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

# Row 2
label = tk.Label(root, text="Key:", font=('Arial', 12))
label.grid(row=2, column=0, padx=10, pady=10)

label = tk.Label(root, text=f"{key_path_var.get()}", font=('Arial', 10))
label.grid(row=2, column=1, padx=10, pady=10)

key_select = tk.Button(root, text="Select File", command=select_Key, width=10, height=1, font=("Arial", 12))
key_select.grid(row=2, column=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
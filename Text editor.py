from customtkinter import *
from CTkMenuBar import *
from tkinter.filedialog import *

root = CTk()

root.title("Notepad")
root.geometry("600x600")
root.configure(border=2, borderwidth=2)

menu = CTkMenuBar(master=root)
b1 = menu.add_cascade("File")

def save_as():
    filepath = asksaveasfilename(filetypes=[("Text File", "*.txt"), ("Python File", "*.py"),
                                            ("Java", "*.java"), ("C", "*.c"), ("C++", "*.cpp"), ("C#", "*.cs"),
                                            ("JavaScript", "*.js"), ("HTML", "*.html"), ("CSS", "*.css"),
                                            ("PHP", "*.php"), ("Ruby", "*.rb"), ("Swift", "*.swift"),
                                            ("Kotlin", "*.kt"), ("Perl", "*.pl"), ("SQL", "*.sql"), ("R", "*.r"),
                                            ("Matlab", "*.m"), ("GO", "*.go"), ("Assembly", "*.asm"),
                                            ("Scala", "*.scala"), ("TypeScript", "*.ts"), ("Rust", "*.rs"),
                                            ("Haskell", "*.hs"), ("Dart", "*.dart"), ("All Files", "*.*")],
                                 defaultextension=".txt")

    if filepath:
        with open(filepath, "w") as file:
            content = text.get("1.0", END)
            file.write(content)


def open_o():
    filepath = askopenfilename(filetypes=[("Text File", "*.txt"), ("Python File", "*.py"), ("Java", "*.java"),
                                          ("C", "*.c"), ("C++", "*.cpp"), ("C#", "*.cs"), ("JavaScript", "*.js"),
                                          ("HTML", "*.html"), ("CSS", "*.css"), ("PHP", "*.php"), ("Ruby", "*.rb"),
                                          ("Swift", "*.swift"), ("Kotlin", "*.kt"), ("Perl", "*.pl"), ("SQL", "*.sql"),
                                          ("R", "*.r"), ("Matlab", "*.m"), ("GO", "*.go"), ("Assembly", "*.asm"),
                                          ("Scala", "*.scala"), ("TypeScript", "*.ts"), ("Rust", "*.rs"),
                                          ("Haskell", "*.hs"), ("Dart", "*.dart"), ("All Files", "*.*")],
                               defaultextension=".txt")

    if filepath:
        with open(filepath, "r") as file:
            content = file.read()
            text.delete("1.0", "end")
            text.insert("1.0", content)


d1 = CustomDropdownMenu(widget=b1)
d1.add_option("Open", command=open_o)
d1.add_option("Save", command=save_as)
d1.add_option("Exit", command=root.destroy)


text = CTkTextbox(root, font=("Ariel", 18, "bold"), border_color="Brown", border_width=2)
text.pack(fill=BOTH, expand=True)

root.mainloop()

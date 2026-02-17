import tkinter as tk

root = tk.Tk()

text = tk.Text(root, height=5, width=20)
text.insert(tk.END, "Line 1\nLine 2")
text.configure(state="disabled")
text.pack()

root.mainloop()

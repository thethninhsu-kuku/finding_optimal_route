import tkinter as tk

class RoundedFrame(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.configure(bg='white', highlightthickness=0)
        self.rounded_rectangle(10, 10, 200, 100, radius=20, fill='lightblue', outline='black')

    def rounded_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        self.create_arc(x1, y1, x1 + radius * 2, y1 + radius * 2, start=90, extent=90, **kwargs)
        self.create_arc(x2 - radius * 2, y1, x2, y1 + radius * 2, start=0, extent=90, **kwargs)
        self.create_arc(x2 - radius * 2, y2 - radius * 2, x2, y2, start=-90, extent=90, **kwargs)
        self.create_arc(x1, y2 - radius * 2, x1 + radius * 2, y2, start=180, extent=90, **kwargs)
        self.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
        self.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)

root = tk.Tk()
root.geometry("300x200")

frame = RoundedFrame(root)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

label = tk.Label(frame, text="This is a label with rounded borders", bg='lightblue')
label.pack(padx=20, pady=20)

root.mainloop()


import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from mycollection import *
import networkx as nx
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import ImageTk, Image

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        print(args)
        self.nav_frame=Frame(self)
        self.nav_frame.pack(side='top',fill='x', anchor=NW, padx=10,pady=0)
        # Display it within a label.
        img=Image.open("image/myanmar.png")
        img = img.resize((int(3/4*600), 600))
        image = ImageTk.PhotoImage(img)

        # Create a label to display the image
        label = Label(self, image=image)
        label.image = image
        # Pack the label to fill the window
        label.pack(side='left')
        self.name=Frame(self,pady=150,padx=50)
        self.name.pack(side='top',anchor='w')
        label = tk.Label(self.name, text="Finding Optimal Route",font=('Arial 20'), justify=LEFT, anchor="w",width=30)
        label.pack(side="top", pady=20)
        label = tk.Label(self.name, text="for Travelling around MYANMAR ",font=('Arial 20'), justify=LEFT, anchor="w",width=30)
        label.pack(side="top", pady=20)
        label = tk.Label(self.name, text="Using Dijkstra’s Algorithm",font=('Arial 20'), justify=LEFT, anchor="w",width=30)
        label.pack(side="top", pady=20)
        print('grgrgh')
        label = Label(text ='')

        # Center the label widget
        #label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    def add_page(self,page):
        self.page2=page
        b1 = tk.Button(self.name, text="Start", command=self.page2.show,width=20,height=2,font=('Arial ',12,'bold'), bg='gray70',activebackground='gray40')
        b1.pack(side="left",pady=40)

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        self.nav_frame=Frame(self)
        self.nav_frame.pack(side='top',fill='x', anchor=NW, padx=10,pady=0)
        input_frame=Frame(self,width=100,height=100,highlightbackground="black",highlightthickness=2)
        input_frame.pack(side='top',fill='x',padx=50,pady=20)
        self.display_frame=Frame(self,width=100,height=100,highlightbackground="black",highlightthickness=0)
        self.display_frame.pack(side='top',padx=50,pady=10)
        
        
        label=Label(input_frame)
        label.grid(row=0,column=0,pady=0)
        label=Label(input_frame,text='Source',activebackground='blue',font=('Arial 10'))
        label.grid(row=1,column=0,padx=80,sticky='E')
        label=Label(input_frame,text='Destination',font=('Arial 10'))
        label.grid(row=3,column=0,padx=80,pady=10,sticky='W')
        label=Label(input_frame,text='Avoid Cities',font=('Arial 10'))
        label.grid(row=1,column=3,padx=(80,0))

        cities=get_cities()
        self.city=cities
        numbers=Entry(input_frame,width=20,font=('Arial ',15),validate='key')
        #numbers.grid(row=1,column=1)
        self.froms = ttk.Combobox(input_frame,values=self.city,font=('Arial ',13),width=20)
        self.froms.grid(row=1,column=1,sticky="W")
        def update_combobox(event):
            # Get the current text in the combobox
            value = self.froms.get()
            print(value)
            if value == '':
                self.froms['values'] = self.city  # Show all data if input is empty
            else:
                filtered_data = [item for item in self.city if value.lower() in item.lower()]
                self.froms['values'] = filtered_data
        self.froms.bind('<KeyRelease>', update_combobox)
        self.to = ttk.Combobox(input_frame,values=self.city,font=('Arial ',13),width=20)
        self.to.grid(row=3,column=1,sticky="W")
        def update_combobox2(event):
            # Get the current text in the combobox
            value = self.to.get()
            print(value)
            if value == '':
                self.to['values'] = self.city  # Show all data if input is empty
            else:
                filtered_data = [item for item in self.city if value.lower() in item.lower()]
                self.to['values'] = filtered_data
        self.to.bind('<KeyRelease>', update_combobox2)
        self.avoid = ttk.Combobox(input_frame,values=self.city,font=('Arial ',13),width=20)
        self.avoid.grid(row=1,column=4)
        def update_combobox3(event):
            # Get the current text in the combobox
            value = self.avoid.get()
            print(value)
            if value == '':
                self.avoid['values'] = self.city  # Show all data if input is empty
            else:
                filtered_data = [item for item in self.city if value.lower() in item.lower()]
                self.avoid['values'] = filtered_data
        self.avoid.bind('<KeyRelease>', update_combobox3)
        
        generate=Button(input_frame,text='Search Route',width=20,height=2,font=('Arial ',12,'bold'),bg='gray70',activebackground='gray40',command=self.search_route)#, bg='PaleGreen4'
        generate.grid(row=3,column=4,padx=50,pady=15)

        self.res=Label(self.display_frame,text='', anchor="w",width=20,activebackground='blue',font=('Arial 15'))
        self.res.grid(row=0,column=0,pady=20)
        self.res2=Label(self.display_frame,text='', anchor="w",width=20,activebackground='blue',font=('Arial 15'))
        self.res2.grid(row=1,column=0,pady=20)
        self.result=Label(self.display_frame,text='', justify=LEFT, anchor="w",width=80,activebackground='blue',font=('Arial 13'))
        self.result.grid(row=0,column=1)
        self.result2=Label(self.display_frame,text='', justify=LEFT, anchor="w",width=80,activebackground='blue',font=('Arial 13'))
        self.result2.grid(row=1,column=1)
        #self.display_plot2()
    def root(self,root):
        self.root=root
        print('SLEF>ROOT',self.root)
        #self.openNewWindow()
    def search_route(self):
        print('Searching route........')
        print(self.froms.get(),self.to.get(),self.avoid.get())
        source=self.froms.get().strip()
        destination=self.to.get().strip()
        avoid=self.avoid.get().strip()
        
        cities=get_cities()
        sms=''
        if not source:  sms='Please select Source City!'
        elif source not in cities:    sms='Source : Invalid City Name!'
        elif not destination:  sms='Please select Destination City!'
        elif destination not in cities: sms='Destination : Invalid City Name!'
        elif source==destination:   sms='Source and Destination are the same!'
        elif avoid not in cities and avoid:   sms='Avoid City : Invalid City Name!'
        elif avoid==source:   sms='Avoid City should not be the same with Source City!'
        elif avoid==destination:   sms='Avoid City should not be the same with destination City!'
        if sms:
            messagebox.showwarning("Warning", sms) 
        else:
            path=dijkstra(source=source,destination=destination,avoid=avoid)
            print('NODE RESULT',nodes_result(path.nodes),nodes_result2(path.costs,path.total_cost))
            self.res['text']='Optimal Route : '
            self.res2['text']='Total Distance: '
            self.result['text']=nodes_result(path.nodes)
            self.result2['text']=nodes_result2(path.costs,path.total_cost)
            self.vp=Button(self.display_frame,text='View Plot',width=20,height=2,font=('Arial ',12,'bold'),bg='gray70',activebackground='gray40',command=self.openNewWindow)#, bg='cornflower blue'
            self.vp.grid(row=2,column=1,pady=20)
            self.path=path
            self.avoid_city=avoid
    def openNewWindow(self):
        self.newWindow = Toplevel(self.root)
        self.newWindow.title("Optimal Route Plot Network")
    
        # sets the geometry of toplevel
        self.newWindow.geometry("700x1000")
        
        self.plot_frame=Frame(self.newWindow,width=100,height=100,highlightbackground="black",highlightthickness=0)
        self.plot_frame.pack(side='top',padx=50,pady=10)
        print('plot_frame',self.plot_frame)
        self.display_plot(plot_f=self.plot_frame)
        # A Label widget to show in toplevel
        Label(self.newWindow, text ="This is a new window").pack()
    def display_plot(self,plot_f):
        # the figure that will contain the plot 
        print('PATH',self.path)
        edgelist=create_edge(self.path.nodes)
        fig = Figure(figsize = (50, 50), dpi = 60) 
        # adding the subplot 
        plot1 = fig.add_subplot(111) 
        
        
        # plotting the graph 
        datas=get_datas()
        #print('DF',datas)
        G = nx.Graph()
        for x in datas:
            G.add_edge(x[1],x[2],weight= "{:.1f}".format(x[7]))#int(x[7])
        '''
        G.add_edge(1, 2,weight=1)
        G.add_edge(2, 3,weight=2)
        G.add_edge(3, 4,weight=3)
        G.add_edge(1, 4,weight=4)
        G.add_edge(1, 5,weight=5)
        '''
        left_node=left_nodes(self.path.nodes,self.avoid_city,get_cities())
        filtered_left_node = {node: node for node in left_node}
        print('LEFT NODE',left_node)
        print(filtered_left_node)
        # Set node positions (optional, choose a layout algorithm)
        pos = nx.spring_layout(G,seed=657)
        pos=node_pos(pos)
        print('POS',pos)
        lb_pos=label_pos(pos)
        print("POS",pos)
        print(lb_pos)
        filtered_path = {node: node for node in self.path.nodes}
        #lal_pos=label_pos(pos)
        #pos={1: [0, 0],2: [-0.42076278, -0.04737344],3: [-0.79518388, -0.40322521],4: [-0.11764776, -0.22362193],5: [1.        , 0.48875428]}
        #edge_colors = ['blue', 'red', 'green', 'purple']
        #node_colors = ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
        nx.draw(G, pos, with_labels=True)
        # Draw the graph with node and edge colors
        nx.draw_networkx_nodes(G,
                            pos, 
                            node_color='#4d94ff',node_size=180,
                            ax=plot1)
        nx.draw_networkx_edges(G,
                            pos,
                            edge_color='blue',
                            ax=plot1)
        nx.draw_networkx_labels(G, lb_pos, labels=filtered_left_node,
                                font_size=10,font_color='black',ax=plot1)
        nx.draw_networkx_labels(G, lb_pos, font_weight='bold', labels=filtered_path,
                                font_size=12,font_color='#004d00',ax=plot1)
        
        nx.draw_networkx_nodes(G,
                            pos, 
                            node_color='#47d147',node_size=180,
                            nodelist=self.path.nodes,
                            ax=plot1)
        if self.avoid_city:
            nx.draw_networkx_nodes(G,
                                pos,
                                node_color='red',node_size=180,
                                nodelist=[self.avoid_city],
                                ax=plot1)
            nx.draw_networkx_labels(G, lb_pos, labels={self.avoid_city:self.avoid_city},
                                    font_size=12,font_weight='bold',font_color='black',ax=plot1)
        nx.draw_networkx_edges(G,
                            pos,
                            edge_color='green',width=2,
                            edgelist=edgelist,
                            ax=plot1)
        nx.draw_networkx_nodes(G,
                            pos,
                            node_color='#006600',node_size=180,
                            nodelist=[self.path.nodes[0],self.path.nodes[-1]],
                            ax=plot1)

        '''
        nx.draw_networkx_edges(G,
                            pos,
                            edge_color='blue',
                            edgelist=[(1,2),(2,3)],ax=plot1)
        nx.draw_networkx_labels(G, pos, labels={1:'YGN',2:'PTN',3:'MDY',4:'MKN',5:'TG'},
                                font_size=12,font_color='black',ax=plot1)
        nx.draw_networkx_nodes(G,
                                pos, 
                                node_color='green',
                                nodelist=[4,5],ax=plot1)
        nx.draw_networkx_edges(G,
                            pos,
                            edge_color='orange',
                            edgelist=[(3,4),(1,4),(1,5)],ax=plot1)
        '''
        edge_labels = nx.get_edge_attributes(G, "weight")
        #print('edge_labels ',edge_labels)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,ax=plot1)
        # creating the Tkinter canvas 
        # containing the Matplotlib figure 
        canvas = FigureCanvasTkAgg(fig, master = self.newWindow)

        canvas.draw()
        # placing the canvas on the Tkinter window 
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        # creating the Matplotlib toolbar 
        toolbar = NavigationToolbar2Tk(canvas, plot_f)
        toolbar.update() 
            
        # placing the toolbar on the Tkinter window 
        canvas.get_tk_widget().pack()
    
    def display_plot3(self,plot_f):
        print('plot_frame',plot_f)
        # the figure that will contain the plot 
        fig = Figure(figsize = (5, 5), 
                        dpi = 100) 
        
        # list of squares 
        
        # adding the subplot 
        plot1 = fig.add_subplot(111) 
        
        # plotting the graph 
        
        G = nx.Graph()
        
        G.add_edge(1, 2,weight=2)
        G.add_edge(2, 3,weight=2)
        G.add_edge(3, 4,weight=3)
        G.add_edge(1, 4,weight=4)
        G.add_edge(1, 5,weight=5)
        
        # Set node positions (optional, choose a layout algorithm)
        pos = nx.spring_layout(G,seed=657)
        #pos={1: [0, 0],2: [-0.42076278, -0.04737344],3: [-0.79518388, -0.40322521],4: [-0.11764776, -0.22362193],5: [1.        , 0.48875428]}
        edge_colors = ['blue', 'red', 'green', 'purple']
        node_colors = ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
        
        # Draw the graph with node and edge colors
        nx.draw_networkx_nodes(G,
                            pos,
                            node_color='red',
                            nodelist=[1,2,3] ,ax=plot1)
        nx.draw_networkx_nodes(G,
                                pos,
                                node_color='green',
                                nodelist=[4,5],ax=plot1)
        nx.draw_networkx_labels(G, pos, labels={1:'YGN',2:'PTN',3:'MDY',4:'MKN',5:'TG'},
                                font_size=12,font_color='black',ax=plot1)
        nx.draw_networkx_edges(G,
                            pos,
                            edge_color='blue',
                            edgelist=[(1,2),(2,3)],ax=plot1)
        nx.draw_networkx_edges(G,
                            pos,
                            edge_color='orange',
                            edgelist=[(3,4),(1,4),(1,5)],ax=plot1)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels,ax=plot1)
        # creating the Tkinter canvas 
        # containing the Matplotlib figure 
        canvas = FigureCanvasTkAgg(fig, master = plot_f)
        canvas.draw() 
            
        # placing the canvas on the Tkinter window 
        canvas.get_tk_widget().pack() 
        # creating the Matplotlib toolbar 

        toolbar = NavigationToolbar2Tk(canvas, plot_f) 
        toolbar.update() 
            
        # placing the toolbar on the Tkinter window 
        canvas.get_tk_widget().pack()
    def display_plot2(self):
        # the figure that will contain the plot 
        fig = Figure(figsize = (5, 5), 
                        dpi = 100) 
        
        # list of squares 
        y = [i**2 for i in range(101)] 
        
        # adding the subplot 
        plot1 = fig.add_subplot(111) 
        
        # plotting the graph 
        
        G = nx.Graph()
        
        G.add_edge(1, 2,weight=2)
        G.add_edge(2, 3,weight=2)
        G.add_edge(3, 4,weight=3)
        G.add_edge(1, 4,weight=4)
        G.add_edge(1, 5,weight=5)
        
        # Set node positions (optional, choose a layout algorithm)
        pos = nx.spring_layout(G,seed=657)
        #pos={1: [0, 0],2: [-0.42076278, -0.04737344],3: [-0.79518388, -0.40322521],4: [-0.11764776, -0.22362193],5: [1.        , 0.48875428]}

        
        # Draw the graph with node and edge colors
        nx.draw_networkx_nodes(G,
                            pos, 
                            node_color='red',
                            nodelist=[1,2,3] ,ax=plot1)
        nx.draw_networkx_nodes(G,
                                pos, 
                                node_color='green',
                                nodelist=[4,5],ax=plot1)
        nx.draw_networkx_labels(G, pos, labels={1:'YGN',2:'PTN',3:'MDY',4:'MKN',5:'TG'},
                                font_size=12,font_color='black',ax=plot1)
        nx.draw_networkx_edges(G,
                            pos,
                            edge_color='blue',
                            edgelist=[(1,2),(2,3)],ax=plot1)
        nx.draw_networkx_edges(G,
                            pos,
                            edge_color='orange',
                            edgelist=[(3,4),(1,4),(1,5)],ax=plot1)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels,ax=plot1)
        # creating the Tkinter canvas 
        # containing the Matplotlib figure 
        canvas = FigureCanvasTkAgg(fig, master = self.display_frame) 
        canvas.draw() 
            
        # placing the canvas on the Tkinter window 
        canvas.get_tk_widget().pack() 
        # creating the Matplotlib toolbar 
        toolbar = NavigationToolbar2Tk(canvas, self.display_frame)
        toolbar.update() 
            
        # placing the toolbar on the Tkinter window 
        canvas.get_tk_widget().pack()
    def add_page(self,page,page3):
        b1 = tk.Button(self.nav_frame, text="< Back", command=page.show,width=15,height=2,font=('Arial ',8,'bold'),bg='gray70')
        b1.pack(side="left")
        b2 = tk.Button(self.nav_frame, text="Cities Info", command=page3.show,width=15,height=2,font=('Arial ',8,'bold'),bg='gray70')
        b2.pack(side="right")

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.nav_frame=Frame(self)
        self.nav_frame.pack(side='top',fill='x', anchor=NW, padx=10,pady=0)
        self.display_frame=Frame(self,width=100,height=100,highlightbackground="black",highlightthickness=1,)
        self.display_frame.pack(side='top',fill='both',padx=50,pady=10)


        '''
        for x in range(10):
            for y in range(5):
                ll=Label(display_frame,text=str(x)+str(y),width=20,height=4)
                ll.grid(row=x,column=y)
    '''
    def root(self,root):
        self.root=root
        self.display_data()
    def display_data(self):
        print('SLEF>ROOT',self.root)
        self.container = ttk.Frame(self.display_frame)
        self.canvas = tk.Canvas(self.container, width=900, height=600, background='grey')
        self.vscrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.hscrollbar = ttk.Scrollbar(self.container, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window(0, 0, window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.vscrollbar.set)
        self.canvas.configure(xscrollcommand=self.hscrollbar.set)

        df=get_cities_info()
        print('DATA Frame')
        print(list(df.columns))
        table_headers = list(df.columns)
        for i in range(len(table_headers)):
            current_entry = tk.Entry(self.scrollable_frame, width=[21,8][i==0], justify='center',font=('Arial ',10,'bold'))
            current_entry.insert(0, str(table_headers[i]))
            current_entry.configure(state='disabled', disabledforeground='blue')
            current_entry.grid(row=0, column=i)
        for i in range(0, 69):
            for header_to_create in table_headers:
                current_entry = tk.Entry(self.scrollable_frame, width=[23,10][header_to_create=='No'], justify='center')
                current_entry.insert(0, str(df._get_value(i, header_to_create)))
                current_entry.configure(state='disabled', disabledforeground='blue')
                current_entry.grid(row=i+1, column=table_headers.index(header_to_create))

        self.container.pack()
        self.canvas.grid()
        self.vscrollbar.grid(row=0, column=1, sticky="ns")
        self.hscrollbar.grid(row=1, column=0, sticky="ew")
    def add_page(self,page):
            self.page2=page
            b1 = tk.Button(self.nav_frame, text="< Back", command=self.page2.show,width=15,height=2,font=('Arial ',8,'bold'),bg='gray70')
            b1.pack(side="left",pady=0)
    
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        print('ARgs',args,type(args),type(args[0]))
        p3 = Page3(self)    #citi info
        p1 = Page1(self)    #intro page
        p2 = Page2(self)    #main page
        p2.root(args[0])
        p1.add_page(p2)
        p3.add_page(p2)
        p2.add_page(p1,p3)
        p3.root(args[0])

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
#bj//
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b2 = tk.Button(buttonframe, text="App", command=p2.show,width=15,height=2,font=('Arial ',8,'bold'))
        
        #b2.pack(side="left")
        #b3.pack(side="left")
        p2.show()

root = tk.Tk()
main = MainView(root)
main.pack(side="top", fill="both", expand=True)
root.title('Finding Optimal Route for Travelling arounnd Myanmar')
root.wm_geometry('1100x700')
root.mainloop()
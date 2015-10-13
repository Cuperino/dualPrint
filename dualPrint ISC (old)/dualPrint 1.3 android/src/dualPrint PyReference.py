#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gobject
import random
import os
import sys
import gtk
import math
import platform
import webbrowser
#EndImports

# Pyperclip v1.3 (Extract, only copy functions have been implemented to use with dualPrint.)
# A cross-platform clipboard module for Python.
# By Al Sweigart al@coffeeghost.net

# On Mac, this module makes use of the pbcopy and pbpaste commands, which should come with the os.
# On Linux, this module makes use of the xclip command, which should come with the os. Otherwise run "sudo apt-get install xclip"

# Copyright (c) 2010, Albert Sweigart
# All rights reserved.
#
# BSD-style license:
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# * Neither the name of the pyperclip nor the
# names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY Albert Sweigart "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Albert Sweigart BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Change Log:
# 1.2 Use the platform module to help determine OS.
# 1.3 Changed ctypes.windll.user32.OpenClipboard(None) to ctypes.windll.user32.OpenClipboard(0), after some people ran into some TypeError

def winSetClipboard(text):
    GMEM_DDESHARE = 0x2000
    ctypes.windll.user32.OpenClipboard(0)
    ctypes.windll.user32.EmptyClipboard()
    try:
        # works on Python 2 (bytes() only takes one argument)
        hCd = ctypes.windll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(bytes(text))+1)
    except TypeError:
        # works on Python 3 (bytes() requires an encoding)
        hCd = ctypes.windll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(bytes(text, 'ascii'))+1)
    pchData = ctypes.windll.kernel32.GlobalLock(hCd)
    try:
        # works on Python 2 (bytes() only takes one argument)
        ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pchData), bytes(text))
    except TypeError:
        # works on Python 3 (bytes() requires an encoding)
        ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pchData), bytes(text, 'ascii'))
    ctypes.windll.kernel32.GlobalUnlock(hCd)
    ctypes.windll.user32.SetClipboardData(1,hCd)
    ctypes.windll.user32.CloseClipboard()

def macSetClipboard(text):
    outf = os.popen('pbcopy', 'w')
    outf.write(text)
    outf.close()

def gtkSetClipboard(text):
    cb = gtk.Clipboard()
    cb.set_text(text)
    cb.store()

def qtSetClipboard(text):
    cb.setText(text)

def xclipSetClipboard(text):
    outf = os.popen('xclip -selection c', 'w')
    outf.write(text)
    outf.close()

def xselSetClipboard(text):
    outf = os.popen('xsel -i', 'w')
    outf.write(text)
    outf.close()

if os.name == 'nt' or platform.system() == 'Windows':
    import ctypes
    setcb = winSetClipboard
elif os.name == 'mac' or platform.system() == 'Darwin':
    setcb = macSetClipboard
elif os.name == 'posix' or platform.system() == 'Linux':
    xclipExists = os.system('which xclip') == 0
    if xclipExists:
        setcb = xclipSetClipboard
    else:
        xselExists = os.system('which xsel') == 0
        if xselExists:
            setcb = xselSetClipboard
        try:
            setcb = gtkSetClipboard
        except:
            try:
                import PyQt4.QtCore
                import PyQt4.QtGui
                app = QApplication([])
                cb = PyQt4.QtGui.QApplication.clipboard()
                setcb = qtSetClipboard
            except:
                raise Exception('Pyperclip requires the gtk or PyQt4 module installed, or the xclip command.')
copy = setcb

#Continue dualPrint...

class iscApp1:
 iscVcapApple = 5000
 iscVn8 = 8
 iscVn6 = 6
 iscVn4 = 4
 iscVn0 = 0
 iscVn2m = 2
 iscVnm1 = 1
 iscVparImpTest = ""
 iscVcapAndro = 78
 iscVlink_pHelp_Loc = "redirect.html"
 iscVwAbout = 0
 iscVlink_license = "http://www.opensource.org/licenses/MIT"
 iscVlink_web = "http://www.dualPrint.org/"
 iscVNotifyOSD_Par = "notify-send \'dualPrint: Even Copy\' \'The seccond print set has been copied to the clipboard. You may paste it in the print dialog.\'"
 iscVNotifyOSD_Imp = "notify-send \'dualPrint: Odd Copy\' \'The first print set has been copied to the clipboard. You may paste it in the print dialog.\'"
 iscVn2 = 2
 iscVcoma = ","
 iscVguion = "-"
 iscVn = 12
 iscVsl = 4
 iscVstart = 1
 iscVcount = 0
 iscVnText = "12"
 iscVslText = "4"
 iscVstartText = "1"
 iscVwPar = ""
 iscVwrite = "write"
 iscVn1 = 1
 iscVcountText = "countText"
 iscVqTest = 0
 iscVqDifference = 0
 iscVwImpar = ""
 iscVlink = ""
 iscVnullText = ""
 iscVlink_pHelp_M = "http://www.dualprint.org/"
 iscVtotal = "Total: "
 iscVtotalPages = ""
 iscWindow2browse1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow2browse1Fixed = gtk.Fixed()
 iscWindow2return0 = gtk.Button("Return to dualPrint")

 iscWindow3about1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow3about1Fixed = gtk.Fixed()
 iscWindow3icon0 = gtk.Image()
 iscWindow3info0 =gtk.Label("dualPrint is a multi-platform application to")
 iscWindow3rights0 =gtk.Label("Copyright © 2012-2013 Javier O. Cordero Pérez")
 iscWindow3close0 = gtk.Button("Close")
 iscWindow3web0 = gtk.Button("Website")
 iscWindow3MIT0 =gtk.Label("This software is under the MIT License")
 iscWindow3version0 =gtk.Label("1.3")
 iscWindow3dualprint0 =gtk.Label("dualPrint")
 iscWindow3license0 = gtk.Button("License")
 iscWindow3illumination0 =gtk.Label("Built using Illumination Software Creator")
 iscWindow3info10 =gtk.Label("save sheets of paper by helping you do")
 iscWindow3info20 =gtk.Label("milti-sided printing.")
 iscWindow3MIT10 =gtk.Label("For more information press License.")

 iscWindow1main1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow1main1Fixed = gtk.Fixed()
 iscWindow1nQ0 =gtk.Label("Which would be the last page to print?")
 iscWindow1slidesQ0 =gtk.Label("How many slides or pages per side?")
 iscWindow1n0 = gtk.Entry()
 iscWindow1sl0 = gtk.Entry()
 iscWindow1bStart0 = gtk.Button("Generate Print Sets")
 iscWindow1inicioQ0 =gtk.Label("Which would be the first page to print?")
 iscWindow1start0 = gtk.Entry()
 iscWindow1infoImpar0 =gtk.Label("Odd, set of pages to print first.")
 iscWindow1wImpar0 = gtk.Entry()
 iscWindow1parInfo0 =gtk.Label("Even, set of pages to print on the back.")
 iscWindow1wPar0 = gtk.Entry()
 iscWindow1CI0 = gtk.Image()
 iscWindow1CP0 = gtk.Image()
 iscWindow1about0 = gtk.Button("About dualPrint")
 iscWindow1paper0 = gtk.Button("Printing help")
 iscWindow1header0 = gtk.Image()

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()



#EndOfClass

def iscWindow2():
 thisiscApp1.iscWindow2return0 = gtk.Button("Return to dualPrint")
 thisiscApp1.iscWindow2browse1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow2browse1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow2browse1.set_title("Mobile Browser")
 thisiscApp1.iscWindow2browse1.set_default_size(320, 460)
 thisiscApp1.iscWindow2browse1.add(thisiscApp1.iscWindow2browse1Fixed)
 thisiscApp1.iscWindow2browse1Fixed.width = 320
 thisiscApp1.iscWindow2browse1Fixed.height = 460
 thisiscApp1.iscWindow2browse1.connect("delete_event", iscWindow2Closed)
 thisiscApp1.iscWindow2browse1.set_resizable(False)
 thisiscApp1.iscWindow2browse1Fixed.show()
 thisiscApp1.iscWindow2browse1Fixed.put(thisiscApp1.iscWindow2return0, 0, 420)
 thisiscApp1.iscWindow2return0.set_size_request(320, 40)
 thisiscApp1.iscWindow2return0.connect("clicked", iscWindow2returnClicked)
 thisiscApp1.iscWindow2return0.show()
 thisiscApp1.iscWindow2browse1.show()
 iscSetWebBrowser42()
 #iscWindow2Opened
 #iscWindow2Done


def iscWindow2Closed(self, other):
 pass
 #iscWindow2Closed


def iscWindow2returnClicked(self):
 pass
 iscIfThen41()
 #iscWindow2returnClicked


def iscWindow3():
 thisiscApp1.iscWindow3icon0 = gtk.Image()
 thisiscApp1.iscWindow3info0 =gtk.Label("dualPrint is a multi-platform application to")
 thisiscApp1.iscWindow3rights0 =gtk.Label("Copyright © 2012-2013 Javier O. Cordero Pérez")
 thisiscApp1.iscWindow3close0 = gtk.Button("Close")
 thisiscApp1.iscWindow3web0 = gtk.Button("Website")
 thisiscApp1.iscWindow3MIT0 =gtk.Label("This software is under the MIT License")
 thisiscApp1.iscWindow3version0 =gtk.Label("1.3")
 thisiscApp1.iscWindow3dualprint0 =gtk.Label("dualPrint")
 thisiscApp1.iscWindow3license0 = gtk.Button("License")
 thisiscApp1.iscWindow3illumination0 =gtk.Label("Built using Illumination Software Creator")
 thisiscApp1.iscWindow3info10 =gtk.Label("save sheets of paper by helping you do")
 thisiscApp1.iscWindow3info20 =gtk.Label("milti-sided printing.")
 thisiscApp1.iscWindow3MIT10 =gtk.Label("For more information press License.")
 thisiscApp1.iscWindow3about1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow3about1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow3about1.set_title("About dualPrint")
 thisiscApp1.iscWindow3about1.set_default_size(320, 380)
 thisiscApp1.iscWindow3about1.add(thisiscApp1.iscWindow3about1Fixed)
 thisiscApp1.iscWindow3about1Fixed.width = 320
 thisiscApp1.iscWindow3about1Fixed.height = 380
 thisiscApp1.iscWindow3about1.connect("delete_event", iscWindow3Closed)
 thisiscApp1.iscWindow3about1.set_resizable(False)
 thisiscApp1.iscWindow3about1Fixed.show()
 iscWindow3icon0EventBox = gtk.EventBox()
 iscWindow3icon0EventBox.set_size_request(90, 90)
 iscWindow3icon0EventBox.connect("button_press_event", iscWindow3iconClicked)
 thisiscApp1.iscWindow3icon0.set_size_request(90, 90)
 iscWindow3icon0EventBox.add(thisiscApp1.iscWindow3icon0)
 thisiscApp1.iscWindow3about1Fixed.put(iscWindow3icon0EventBox, 115, 12)
 thisiscApp1.iscWindow3icon0.show()
 iscWindow3icon0EventBox.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3info0, 10, 154)
 thisiscApp1.iscWindow3info0.set_size_request(300, 20)
 thisiscApp1.iscWindow3info0.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3rights0, 10, 225)
 thisiscApp1.iscWindow3rights0.set_size_request(300, 20)
 thisiscApp1.iscWindow3rights0.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3close0, 234, 330)
 thisiscApp1.iscWindow3close0.set_size_request(80, 45)
 thisiscApp1.iscWindow3close0.connect("clicked", iscWindow3closeClicked)
 thisiscApp1.iscWindow3close0.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3web0, 8, 330)
 thisiscApp1.iscWindow3web0.set_size_request(90, 45)
 thisiscApp1.iscWindow3web0.connect("clicked", iscWindow3webClicked)
 thisiscApp1.iscWindow3web0.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3MIT0, 10, 284)
 thisiscApp1.iscWindow3MIT0.set_size_request(300, 20)
 thisiscApp1.iscWindow3MIT0.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3version0, 120, 130)
 thisiscApp1.iscWindow3version0.set_size_request(80, 20)
 thisiscApp1.iscWindow3version0.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3dualprint0, 120, 108)
 thisiscApp1.iscWindow3dualprint0.set_size_request(80, 20)
 thisiscApp1.iscWindow3dualprint0.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3license0, 103, 330)
 thisiscApp1.iscWindow3license0.set_size_request(90, 45)
 thisiscApp1.iscWindow3license0.connect("clicked", iscWindow3licenseClicked)
 thisiscApp1.iscWindow3license0.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3illumination0, 10, 255)
 thisiscApp1.iscWindow3illumination0.set_size_request(300, 20)
 thisiscApp1.iscWindow3illumination0.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3info10, 10, 175)
 thisiscApp1.iscWindow3info10.set_size_request(300, 20)
 thisiscApp1.iscWindow3info10.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3info20, 10, 196)
 thisiscApp1.iscWindow3info20.set_size_request(300, 20)
 thisiscApp1.iscWindow3info20.show()
 thisiscApp1.iscWindow3about1Fixed.put(thisiscApp1.iscWindow3MIT10, 10, 305)
 thisiscApp1.iscWindow3MIT10.set_size_request(300, 20)
 thisiscApp1.iscWindow3MIT10.show()
 thisiscApp1.iscWindow3about1.show()
 iscSetCanvasPicture169()
 #iscWindow3Opened
 #iscWindow3Done


def iscWindow3Closed(self, other):
 pass
 iscSetNumber173()
 #iscWindow3Closed


def iscWindow3iconClicked(widget, event):
 pass
 #iscWindow3iconClicked


def iscWindow3closeClicked(self):
 pass
 iscTargetIs134()
 #iscWindow3closeClicked


def iscWindow3webClicked(self):
 pass
 iscSetText170()
 #iscWindow3webClicked


def iscWindow3licenseClicked(self):
 pass
 iscSetText171()
 #iscWindow3licenseClicked


def iscFloat_to_integer5():
  #Using a function to integer
  thisiscApp1.iscVqDifference = math.floor(thisiscApp1.iscVqDifference)
#iscFloat_to_integer5Done

def iscSetText6():
 thisiscApp1.iscVlink = thisiscApp1.iscVlink_pHelp_M
 iscTargetIs166()
 #iscSetText6Done


def iscSetText7():
 thisiscApp1.iscVlink = thisiscApp1.iscVlink_pHelp_Loc
 iscTargetIs166()
 #iscSetText7Done


def iscConvertNumberToText8():
 thisiscApp1.iscVtotalPages = str(thisiscApp1.iscVqDifference)
 iscCombineText9()
 #iscConvertNumberToText8Done


def iscCombineText9():
 thisiscApp1.iscVtotalPages = thisiscApp1.iscVtotal + thisiscApp1.iscVtotalPages
 iscSetButton158()
 #iscCombineText9Done


def iscPortalDestination10():
 iscSubtract14()
 iscDivide12()
 iscDivide11()
 iscAdd13()
 iscTargetIs157()
 iscConvertNumberToText8()
 #iscPortalDestination10Arrived


def iscDivide11():
 thisiscApp1.iscVqDifference = thisiscApp1.iscVqDifference / thisiscApp1.iscVn2
 #iscDivide11Done


def iscDivide12():
 thisiscApp1.iscVqDifference = thisiscApp1.iscVqDifference / thisiscApp1.iscVsl
 #iscDivide12Done


def iscAdd13():
 thisiscApp1.iscVqDifference = thisiscApp1.iscVqDifference + thisiscApp1.iscVn1
 #iscAdd13Done


def iscSubtract14():
 thisiscApp1.iscVqDifference = thisiscApp1.iscVn - thisiscApp1.iscVstart
 #iscSubtract14Done


def iscClipboard_Copy16():
 copy(thisiscApp1.iscVwPar)
 #iscClipboard_Copy16Done

def iscRunShellScript18():
 os.system(thisiscApp1.iscVNotifyOSD_Par)
 #iscRunShellScript18Done


def iscIf_Linux20():
 if os.name == 'posix' or platform.system() == 'Linux':
  OS = "Linux"
  iscRunShellScript18()
 if os.name == 'posix' or platform.system() == 'Linux':
  OS = "Linux"
  #iscIf_Linux20Linux
 else:
  OS = "Other"
  #iscIf_Linux20Else

def iscPortalDeparture21():
 iscPortalDestination147()
 #iscPortalDeparture21Done


def iscIfThen22():
 if thisiscApp1.iscVqTest > thisiscApp1.iscVn:
  iscPortalDeparture21()
  #iscIfThen22True

  pass
 else:
  iscPortalDeparture29()
  #iscIfThen22False

  pass

def iscIfThen26():
 if thisiscApp1.iscVqTest == thisiscApp1.iscVn:
  iscPortalDeparture27()
  iscPortalDeparture155()
  #iscIfThen26True

  pass
 else:
  iscDivide28()
  iscIfThen31()
  iscPortalDeparture155()
  #iscIfThen26False

  pass

def iscPortalDeparture27():
 iscPortalDestination97()
 #iscPortalDeparture27Done


def iscDivide28():
 thisiscApp1.iscVqDifference = thisiscApp1.iscVn / thisiscApp1.iscVn2
 #iscDivide28Done


def iscPortalDeparture29():
 iscPortalDestination131()
 #iscPortalDeparture29Done


def iscIfThen31():
 if thisiscApp1.iscVqTest < thisiscApp1.iscVqDifference:
  iscPortalDeparture29()
  #iscIfThen31True

  pass
 else:
  iscIfThen60()
  #iscIfThen31False

  pass

def iscDoWhile33():
 while thisiscApp1.iscVcount < thisiscApp1.iscVn:
  iscCombineText135()
  iscConvertNumberToText51()
  iscCombineText128()
  iscAdd139()
  iscAdd140()
  #iscDoWhile33Loop

 iscSetText44()
 iscConvertTextToNumber150()
 iscPortalDeparture155()
 #iscDoWhile33Finished


def iscDoWhile34():
 while thisiscApp1.iscVcount < thisiscApp1.iscVn:
  iscCombineText135()
  iscConvertNumberToText51()
  iscCombineText128()
  iscAdd139()
  iscAdd140()
  #iscDoWhile34Loop

 iscSetText49()
 iscAdd139()
 iscAdd140()
 iscDoWhile33()
 #iscDoWhile34Finished


def iscMessageBox35():
 message = "The starting page should be lower than the total of pages to print."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox35Open
 dialog.destroy()
 #iscMessageBox35Closed

def iscRunShellScript36():
 os.system(thisiscApp1.iscVNotifyOSD_Imp)
 #iscRunShellScript36Done


def iscIf_Linux38():
 if os.name == 'posix' or platform.system() == 'Linux':
  OS = "Linux"
  iscRunShellScript36()
 if os.name == 'posix' or platform.system() == 'Linux':
  OS = "Linux"
  #iscIf_Linux38Linux
 else:
  OS = "Other"
  #iscIf_Linux38Else

def iscAdd39():
 thisiscApp1.iscVqTest = thisiscApp1.iscVqTest + thisiscApp1.iscVsl
 #iscAdd39Done


def iscAdd40():
 thisiscApp1.iscVcount = thisiscApp1.iscVcount + thisiscApp1.iscVqDifference
 #iscAdd40Done


def iscIfThen41():
 if thisiscApp1.iscVwAbout == thisiscApp1.iscVn1:
  iscWindow3()
  #iscIfThen41True

  pass
 else:
  iscWindow1()
  #iscIfThen41False

  pass

def iscSetWebBrowser42():
 thisiscApp1.iscWindow2WebBrowser0.set_text(thisiscApp1.iscVlink)
 #iscSetWebBrowser42Done


def iscMessageBox43():
 message = "You should print at least 1 page per side."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox43Open
 dialog.destroy()
 #iscMessageBox43Closed

def iscSetText44():
 thisiscApp1.iscVwPar = thisiscApp1.iscVwrite
 iscSetTextBox77()
 iscSetTextBox101()
 iscTargetIs163()
 #iscSetText44Done


def iscTargetIs45():
  iscSetText7()
  #iscTargetIs45Python

  pass

def iscSubtract46():
 thisiscApp1.iscVqTest = thisiscApp1.iscVqTest - thisiscApp1.iscVn1
 #iscSubtract46Done


def iscSubtract47():
 thisiscApp1.iscVqDifference = thisiscApp1.iscVqTest - thisiscApp1.iscVn
 iscSubtract48()
 #iscSubtract47Done


def iscSubtract48():
 thisiscApp1.iscVqDifference = thisiscApp1.iscVsl - thisiscApp1.iscVqDifference
 iscAdd40()
 #iscSubtract48Done


def iscSetText49():
 thisiscApp1.iscVwImpar = thisiscApp1.iscVwrite
 iscAdd125()
 #iscSetText49Done


def iscAdd50():
 thisiscApp1.iscVqTest = thisiscApp1.iscVqTest + thisiscApp1.iscVn1
 #iscAdd50Done


def iscConvertNumberToText51():
 thisiscApp1.iscVcountText = str(thisiscApp1.iscVcount)
 #iscConvertNumberToText51Done


def iscMessageBox52():
 message = "Please fill all boxes first."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox52Open
 dialog.destroy()
 #iscMessageBox52Closed

def iscIfThen53():
 if thisiscApp1.iscVsl == thisiscApp1.iscVn1:
  iscPortalDeparture56()
  iscSetCanvasPicture54()
  #iscIfThen53True

  pass
 else:
  iscTargetIs167()
  #iscIfThen53False

  pass

def iscSetCanvasPicture54():
 thisiscApp1.iscWindow1header0.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/header.jpg") #iscSetCanvasPicture54Done


def iscPortalDestination55():
 iscAdd132()
 iscSubtract46()
 iscIfThen130()
 #iscPortalDestination55Arrived


def iscPortalDeparture56():
 iscPortalDestination142()
 #iscPortalDeparture56Done


def iscMessageBox57():
 message = "The sum of the starting page and the pages per side should be less than or equal to the total of pages to print."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox57Open
 dialog.destroy()
 #iscMessageBox57Closed

def iscIfThen59():
 if thisiscApp1.iscVqTest > thisiscApp1.iscVn:
  iscMessageBox57()
  #iscIfThen59True

  pass
 else:
  iscIfThen53()
  #iscIfThen59False

  pass

def iscIfThen60():
 if thisiscApp1.iscVqTest == thisiscApp1.iscVqDifference:
  iscPortalDeparture29()
  #iscIfThen60True

  pass
 else:
  iscAdd62()
  iscAdd39()
  iscIfThen22()
  #iscIfThen60False

  pass

def iscMessageBox61():
 message = "The number of pages per side should be less than the total of pages to print."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox61Open
 dialog.destroy()
 #iscMessageBox61Closed

def iscAdd62():
 thisiscApp1.iscVqTest = thisiscApp1.iscVstart + thisiscApp1.iscVsl
 #iscAdd62Done


def iscCombineText64():
 thisiscApp1.iscVwrite = thisiscApp1.iscVwrite + thisiscApp1.iscVguion
 #iscCombineText64Done


def iscSetCanvasPicture66():
 thisiscApp1.iscWindow1CP0.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/copy.jpg") #iscSetCanvasPicture66Done


def iscSetCanvasPicture67():
 thisiscApp1.iscWindow1CI0.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/copy.jpg") #iscSetCanvasPicture67Done


def iscAppQuit68():
 thisiscApp1.destroy(None,None)
 #iscAppQuit68Done


def iscPortalDeparture69():
 iscPortalDestination71()
 #iscPortalDeparture69Done


def iscPortalDeparture70():
 iscPortalDestination55()
 #iscPortalDeparture70Done


def iscPortalDestination71():
 iscAdd139()
 iscAdd140()
 iscConvertNumberToText51()
 iscCombineText128()
 iscPortalDeparture70()
 #iscPortalDestination71Arrived


def iscSetTextBox77():
 thisiscApp1.iscWindow1wImpar0.set_text(thisiscApp1.iscVwImpar)
 #iscSetTextBox77Done


def iscIfThen78():
 if thisiscApp1.iscVqTest == thisiscApp1.iscVn:
  iscCombineText64()
  iscAdd139()
  iscSubtract127()
  iscConvertNumberToText51()
  iscCombineText128()
  #iscIfThen78True

  pass
 else:
  iscCombineText64()
  iscSubtract47()
  iscSubtract127()
  iscConvertNumberToText51()
  iscConvertNumberToText51()
  iscCombineText128()
  #iscIfThen78False

  pass

def iscIfThen79():
 if thisiscApp1.iscVqTest == thisiscApp1.iscVn:
  iscCombineText135()
  iscAdd139()
  iscAdd140()
  iscConvertNumberToText51()
  iscCombineText128()
  #iscIfThen79True

  pass
 else:
  #iscIfThen79False

  pass

def iscMessageBox95():
 message = "The document must have 2 pages at least."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox95Open
 dialog.destroy()
 #iscMessageBox95Closed

def iscMessageBox96():
 message = "Your print should start from page 1 forward."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox96Open
 dialog.destroy()
 #iscMessageBox96Closed

def iscPortalDestination97():
 iscSetNumber136()
 iscCombineText64()
 iscPortalDeparture143()
 iscSetText49()
 iscSetText44()
 #iscPortalDestination97Arrived


def iscIfThen98():
 if thisiscApp1.iscVstart < thisiscApp1.iscVn:
  iscIfThen102()
  #iscIfThen98True

  pass
 else:
  iscMessageBox35()
  #iscIfThen98False

  pass

def iscIfThen99():
 if thisiscApp1.iscVstart < thisiscApp1.iscVn1:
  iscMessageBox96()
  #iscIfThen99True

  pass
 else:
  iscIfThen117()
  #iscIfThen99False

  pass

def iscSetTextBox101():
 thisiscApp1.iscWindow1wPar0.set_text(thisiscApp1.iscVwPar)
 #iscSetTextBox101Done


def iscIfThen102():
 if thisiscApp1.iscVsl < thisiscApp1.iscVn:
  iscAdd62()
  iscIfThen59()
  #iscIfThen102True

  pass
 else:
  iscMessageBox61()
  #iscIfThen102False

  pass

def iscPortalDestination103():
 iscPortalDeparture143()
 iscSetText49()
 iscCombineText64()
 iscPortalDeparture143()
 iscSetText44()
 #iscPortalDestination103Arrived


def iscPortalDeparture104():
 iscPortalDestination103()
 #iscPortalDeparture104Done


def iscIfThen114():
 if thisiscApp1.iscVstartText == thisiscApp1.iscVnullText:
  iscMessageBox52()
  #iscIfThen114True

  pass
 else:
  iscIfThen115()
  #iscIfThen114False

  pass

def iscIfThen115():
 if thisiscApp1.iscVnText == thisiscApp1.iscVnullText:
  iscMessageBox52()
  #iscIfThen115True

  pass
 else:
  iscIfThen151()
  #iscIfThen115False

  pass

def iscIfThen116():
 if thisiscApp1.iscVn < thisiscApp1.iscVn2:
  iscMessageBox95()
  #iscIfThen116True

  pass
 else:
  iscIfThen99()
  #iscIfThen116False

  pass

def iscIfThen117():
 if thisiscApp1.iscVsl < thisiscApp1.iscVn1:
  iscMessageBox43()
  #iscIfThen117True

  pass
 else:
  iscIfThen98()
  #iscIfThen117False

  pass

def iscGetTextBox118():
 thisiscApp1.iscVstartText = thisiscApp1.iscWindow1start0.get_text()
 iscGetTextBox119()
 #iscGetTextBox118Done


def iscGetTextBox119():
 thisiscApp1.iscVslText = thisiscApp1.iscWindow1sl0.get_text()
 iscGetTextBox120()
 #iscGetTextBox119Done


def iscGetTextBox120():
 thisiscApp1.iscVnText = thisiscApp1.iscWindow1n0.get_text()
 iscIfThen114()
 #iscGetTextBox120Done


def iscOpen_in_Web_Browser122():
 url=(thisiscApp1.iscVlink)
 webbrowser.open(url)
 #iscOpen_in_Web_Browser122Done

def iscAdd125():
 thisiscApp1.iscVcount = thisiscApp1.iscVstart + thisiscApp1.iscVsl
 iscConvertNumberToText148()
 #iscAdd125Done


def iscSubtract127():
 thisiscApp1.iscVcount = thisiscApp1.iscVcount - thisiscApp1.iscVn1
 #iscSubtract127Done


def iscCombineText128():
 thisiscApp1.iscVwrite = thisiscApp1.iscVwrite + thisiscApp1.iscVcountText
 #iscCombineText128Done


def iscIfThen129():
 if thisiscApp1.iscVqTest < thisiscApp1.iscVn:
  iscCombineText135()
  iscPortalDeparture69()
  #iscIfThen129True

  pass
 else:
  iscIfThen79()
  #iscIfThen129False

  pass

def iscIfThen130():
 if thisiscApp1.iscVqTest < thisiscApp1.iscVn:
  iscCombineText64()
  iscPortalDeparture143()
  #iscIfThen130True

  pass
 else:
  iscIfThen78()
  #iscIfThen130False

  pass

def iscPortalDestination131():
 iscSetNumber136()
 iscCombineText64()
 iscPortalDeparture104()
 #iscPortalDestination131Arrived


def iscAdd132():
 thisiscApp1.iscVqTest = thisiscApp1.iscVcount + thisiscApp1.iscVsl
 #iscAdd132Done


def iscIfThen133():
 if thisiscApp1.iscVwAbout == thisiscApp1.iscVn1:
  #iscIfThen133True

  pass
 else:
  iscSetNumber168()
  #iscIfThen133False

  pass

def iscTargetIs134():
  iscSetNumber173()
  iscCloseWindow172()
  #iscTargetIs134Python

  pass

def iscCombineText135():
 thisiscApp1.iscVwrite = thisiscApp1.iscVwrite + thisiscApp1.iscVcoma
 #iscCombineText135Done


def iscSetNumber136():
 thisiscApp1.iscVqTest = 0
 iscSetNumber137()
 #iscSetNumber136Done


def iscSetNumber137():
 thisiscApp1.iscVqDifference = 0
 iscSetNumber138()
 #iscSetNumber137Done


def iscSetNumber138():
 thisiscApp1.iscVcount = thisiscApp1.iscVstart
 iscConvertNumberToText148()
 #iscSetNumber138Done


def iscAdd139():
 thisiscApp1.iscVcount = thisiscApp1.iscVcount + thisiscApp1.iscVsl
 #iscAdd139Done


def iscAdd140():
 thisiscApp1.iscVcount = thisiscApp1.iscVcount + thisiscApp1.iscVn1
 #iscAdd140Done


def iscAdd141():
 thisiscApp1.iscVn = thisiscApp1.iscVn + thisiscApp1.iscVn1
 #iscAdd141Done


def iscPortalDestination142():
 iscSetNumber136()
 iscAdd139()
 iscAdd140()
 iscAdd141()
 iscDoWhile34()
 #iscPortalDestination142Arrived


def iscPortalDeparture143():
 iscPortalDestination144()
 #iscPortalDeparture143Done


def iscPortalDestination144():
 iscAdd139()
 iscSubtract127()
 iscConvertNumberToText51()
 iscCombineText128()
 iscPortalDeparture145()
 #iscPortalDestination144Arrived


def iscPortalDeparture145():
 iscPortalDestination146()
 #iscPortalDeparture145Done


def iscPortalDestination146():
 iscAdd132()
 iscAdd50()
 iscIfThen129()
 #iscPortalDestination146Arrived


def iscPortalDestination147():
 iscSetNumber136()
 iscCombineText64()
 iscPortalDeparture143()
 iscSetText49()
 iscCombineText64()
 iscAdd132()
 iscSubtract46()
 iscSubtract47()
 iscSubtract127()
 iscConvertNumberToText51()
 iscCombineText128()
 iscSetText44()
 #iscPortalDestination147Arrived


def iscConvertNumberToText148():
 thisiscApp1.iscVwrite = str(thisiscApp1.iscVcount)
 #iscConvertNumberToText148Done


def iscConvertTextToNumber149():
 try:
  thisiscApp1.iscVstart = int(thisiscApp1.iscVstartText)
 except ValueError:
  thisiscApp1.iscVstart = 0
 #iscConvertTextToNumber149Done


def iscConvertTextToNumber150():
 try:
  thisiscApp1.iscVn = int(thisiscApp1.iscVnText)
 except ValueError:
  thisiscApp1.iscVn = 0
 #iscConvertTextToNumber150Done


def iscIfThen151():
 if thisiscApp1.iscVslText == thisiscApp1.iscVnullText:
  iscMessageBox52()
  #iscIfThen151True

  pass
 else:
  iscConvertTextToNumber149()
  iscConvertTextToNumber150()
  iscConvertTextToNumber152()
  iscIfThen116()
  #iscIfThen151False

  pass

def iscConvertTextToNumber152():
 try:
  thisiscApp1.iscVsl = int(thisiscApp1.iscVslText)
 except ValueError:
  thisiscApp1.iscVsl = 0
 #iscConvertTextToNumber152Done


def iscGetTextBox153():
 thisiscApp1.iscVwImpar = thisiscApp1.iscWindow1wImpar0.get_text()
 iscTargetIs159()
 #iscGetTextBox153Done


def iscGetTextBox154():
 thisiscApp1.iscVwPar = thisiscApp1.iscWindow1wPar0.get_text()
 iscTargetIs160()
 #iscGetTextBox154Done


def iscPortalDeparture155():
 iscPortalDestination10()
 #iscPortalDeparture155Done


def iscTargetIs157():
  #iscTargetIs157Python

  pass

def iscSetButton158():
 thisiscApp1.iscWindow1bStart0.set_label(thisiscApp1.iscVtotalPages)
 #iscSetButton158Done


def iscTargetIs159():
  iscClipboard_Copy165()
  iscIf_Linux38()
  #iscTargetIs159Python

  pass

def iscTargetIs160():
  iscClipboard_Copy16()
  iscIf_Linux20()
  #iscTargetIs160Python

  pass

def iscMessageBox161():
 message = "The copy button is not available for this platform."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox161Open
 dialog.destroy()
 #iscMessageBox161Closed

def iscMessageBox162():
 message = "The copy button is not available for this platform yet. You must copy manually at the moment."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox162Open
 dialog.destroy()
 #iscMessageBox162Closed

def iscTargetIs163():
  iscClipboard_Copy165()
  iscIf_Linux38()
  #iscTargetIs163Python

  pass

def iscClipboard_Copy165():
 copy(thisiscApp1.iscVwImpar)
 #iscClipboard_Copy165Done

def iscTargetIs166():
  iscOpen_in_Web_Browser122()
  #iscTargetIs166Python

  pass

def iscTargetIs167():
  iscIfThen26()
  #iscTargetIs167Python

  pass

def iscSetNumber168():
 thisiscApp1.iscVwAbout = 1
 iscWindow3()
 #iscSetNumber168Done


def iscSetCanvasPicture169():
 thisiscApp1.iscWindow3icon0.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/dualprint.jpg") #iscSetCanvasPicture169Done


def iscSetText170():
 thisiscApp1.iscVlink = thisiscApp1.iscVlink_web
 iscTargetIs166()
 #iscSetText170Done


def iscSetText171():
 thisiscApp1.iscVlink = thisiscApp1.iscVlink_license
 iscTargetIs166()
 #iscSetText171Done


def iscCloseWindow172():
 thisiscApp1.iscWindow3about1.destroy()
 #iscCloseWindow172Done


def iscSetNumber173():
 thisiscApp1.iscVwAbout = 0
 #iscSetNumber173Done


def iscIfThen175():
 if thisiscApp1.iscVqDifference > thisiscApp1.iscVcapAndro:
  #iscIfThen175True

  pass
 else:
  iscIfThen26()
  iscSetCanvasPicture54()
  #iscIfThen175False

  pass

def iscIfThen176():
 if thisiscApp1.iscVqDifference > thisiscApp1.iscVcapApple:
  #iscIfThen176True

  pass
 else:
  iscIfThen26()
  #iscIfThen176False

  pass

def iscWindow1():
 thisiscApp1.iscWindow1nQ0 =gtk.Label("Which would be the last page to print?")
 thisiscApp1.iscWindow1slidesQ0 =gtk.Label("How many slides or pages per side?")
 thisiscApp1.iscWindow1n0 = gtk.Entry()
 thisiscApp1.iscWindow1sl0 = gtk.Entry()
 thisiscApp1.iscWindow1bStart0 = gtk.Button("Generate Print Sets")
 thisiscApp1.iscWindow1inicioQ0 =gtk.Label("Which would be the first page to print?")
 thisiscApp1.iscWindow1start0 = gtk.Entry()
 thisiscApp1.iscWindow1infoImpar0 =gtk.Label("Odd, set of pages to print first.")
 thisiscApp1.iscWindow1wImpar0 = gtk.Entry()
 thisiscApp1.iscWindow1parInfo0 =gtk.Label("Even, set of pages to print on the back.")
 thisiscApp1.iscWindow1wPar0 = gtk.Entry()
 thisiscApp1.iscWindow1CI0 = gtk.Image()
 thisiscApp1.iscWindow1CP0 = gtk.Image()
 thisiscApp1.iscWindow1about0 = gtk.Button("About dualPrint")
 thisiscApp1.iscWindow1paper0 = gtk.Button("Printing help")
 thisiscApp1.iscWindow1header0 = gtk.Image()
 thisiscApp1.iscWindow1main1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow1main1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow1main1.set_title("dualPrint")
 thisiscApp1.iscWindow1main1.set_default_size(320, 438)
 thisiscApp1.iscWindow1main1.add(thisiscApp1.iscWindow1main1Fixed)
 thisiscApp1.iscWindow1main1Fixed.width = 320
 thisiscApp1.iscWindow1main1Fixed.height = 438
 thisiscApp1.iscWindow1main1.connect("delete_event", iscWindow1Closed)
 thisiscApp1.iscWindow1main1.set_resizable(False)
 thisiscApp1.iscWindow1main1Fixed.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1nQ0, 10, 125)
 thisiscApp1.iscWindow1nQ0.set_size_request(300, 18)
 thisiscApp1.iscWindow1nQ0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1slidesQ0, 10, 180)
 thisiscApp1.iscWindow1slidesQ0.set_size_request(300, 18)
 thisiscApp1.iscWindow1slidesQ0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1n0, 40, 148)
 thisiscApp1.iscWindow1n0.set_text("12")
 thisiscApp1.iscWindow1n0.set_size_request(90, 24)
 thisiscApp1.iscWindow1n0.connect("changed", iscWindow1nChanged)
 thisiscApp1.iscWindow1n0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1sl0, 40, 202)
 thisiscApp1.iscWindow1sl0.set_text("4")
 thisiscApp1.iscWindow1sl0.set_size_request(90, 24)
 thisiscApp1.iscWindow1sl0.connect("changed", iscWindow1slChanged)
 thisiscApp1.iscWindow1sl0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1bStart0, 48, 235)
 thisiscApp1.iscWindow1bStart0.set_size_request(250, 32)
 thisiscApp1.iscWindow1bStart0.connect("clicked", iscWindow1bStartClicked)
 thisiscApp1.iscWindow1bStart0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1inicioQ0, 10, 71)
 thisiscApp1.iscWindow1inicioQ0.set_size_request(300, 18)
 thisiscApp1.iscWindow1inicioQ0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1start0, 40, 94)
 thisiscApp1.iscWindow1start0.set_text("1")
 thisiscApp1.iscWindow1start0.set_size_request(90, 24)
 thisiscApp1.iscWindow1start0.connect("changed", iscWindow1startChanged)
 thisiscApp1.iscWindow1start0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1infoImpar0, 4, 275)
 thisiscApp1.iscWindow1infoImpar0.set_size_request(316, 18)
 thisiscApp1.iscWindow1infoImpar0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1wImpar0, 56, 299)
 thisiscApp1.iscWindow1wImpar0.set_text("")
 thisiscApp1.iscWindow1wImpar0.set_size_request(245, 26)
 thisiscApp1.iscWindow1wImpar0.connect("changed", iscWindow1wImparChanged)
 thisiscApp1.iscWindow1wImpar0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1parInfo0, 4, 334)
 thisiscApp1.iscWindow1parInfo0.set_size_request(316, 18)
 thisiscApp1.iscWindow1parInfo0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1wPar0, 57, 358)
 thisiscApp1.iscWindow1wPar0.set_text("")
 thisiscApp1.iscWindow1wPar0.set_size_request(245, 26)
 thisiscApp1.iscWindow1wPar0.connect("changed", iscWindow1wParChanged)
 thisiscApp1.iscWindow1wPar0.show()
 iscWindow1CI0EventBox = gtk.EventBox()
 iscWindow1CI0EventBox.set_size_request(32, 32)
 iscWindow1CI0EventBox.connect("button_press_event", iscWindow1CIClicked)
 thisiscApp1.iscWindow1CI0.set_size_request(32, 32)
 iscWindow1CI0EventBox.add(thisiscApp1.iscWindow1CI0)
 thisiscApp1.iscWindow1main1Fixed.put(iscWindow1CI0EventBox, 15, 297)
 thisiscApp1.iscWindow1CI0.show()
 iscWindow1CI0EventBox.show()
 iscWindow1CP0EventBox = gtk.EventBox()
 iscWindow1CP0EventBox.set_size_request(32, 32)
 iscWindow1CP0EventBox.connect("button_press_event", iscWindow1CPClicked)
 thisiscApp1.iscWindow1CP0.set_size_request(32, 32)
 iscWindow1CP0EventBox.add(thisiscApp1.iscWindow1CP0)
 thisiscApp1.iscWindow1main1Fixed.put(iscWindow1CP0EventBox, 14, 355)
 thisiscApp1.iscWindow1CP0.show()
 iscWindow1CP0EventBox.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1about0, 166, 395)
 thisiscApp1.iscWindow1about0.set_size_request(136, 30)
 thisiscApp1.iscWindow1about0.connect("clicked", iscWindow1aboutClicked)
 thisiscApp1.iscWindow1about0.show()
 thisiscApp1.iscWindow1main1Fixed.put(thisiscApp1.iscWindow1paper0, 18, 395)
 thisiscApp1.iscWindow1paper0.set_size_request(136, 30)
 thisiscApp1.iscWindow1paper0.connect("clicked", iscWindow1paperClicked)
 thisiscApp1.iscWindow1paper0.show()
 iscWindow1header0EventBox = gtk.EventBox()
 iscWindow1header0EventBox.set_size_request(320, 68)
 iscWindow1header0EventBox.connect("button_press_event", iscWindow1headerClicked)
 thisiscApp1.iscWindow1header0.set_size_request(320, 68)
 iscWindow1header0EventBox.add(thisiscApp1.iscWindow1header0)
 thisiscApp1.iscWindow1main1Fixed.put(iscWindow1header0EventBox, 0, 0)
 thisiscApp1.iscWindow1header0.show()
 iscWindow1header0EventBox.show()
 thisiscApp1.iscWindow1main1.show()
 iscSetCanvasPicture67()
 iscSetCanvasPicture66()
 iscSetCanvasPicture54()
 #iscWindow1Opened
 #iscWindow1Done


def iscWindow1Closed(self, other):
 pass
 iscAppQuit68()
 #iscWindow1Closed


def iscWindow1nChanged(self):
 pass
 #iscWindow1nChanged


def iscWindow1slChanged(self):
 pass
 #iscWindow1slChanged


def iscWindow1bStartClicked(self):
 pass
 iscGetTextBox118()
 #iscWindow1bStartClicked


def iscWindow1startChanged(self):
 pass
 #iscWindow1startChanged


def iscWindow1wImparChanged(self):
 pass
 iscSetTextBox77()
 #iscWindow1wImparChanged


def iscWindow1wParChanged(self):
 pass
 iscSetTextBox101()
 #iscWindow1wParChanged


def iscWindow1CIClicked(widget, event):
 pass
 iscGetTextBox153()
 #iscWindow1CIClicked


def iscWindow1CPClicked(widget, event):
 pass
 iscGetTextBox154()
 #iscWindow1CPClicked


def iscWindow1aboutClicked(self):
 pass
 iscIfThen133()
 #iscWindow1aboutClicked


def iscWindow1paperClicked(self):
 pass
 iscTargetIs45()
 #iscWindow1paperClicked


def iscWindow1headerClicked(widget, event):
 pass
 #iscWindow1headerClicked


#EndOfFunctions

thisiscApp1 = iscApp1()

iscWindow1()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()

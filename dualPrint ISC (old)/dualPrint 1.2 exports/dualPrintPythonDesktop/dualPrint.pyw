#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dualPrint v1.2
# A multi-platform aplication that generates print sets for multiple pages per sheet, two-sided, printing.
# By Javier Oscar Cordero Pérez javier.cordero@upr.edu, http://www.sourceforge.net/projects/dualprint

import pygtk
pygtk.require('2.0')
import gobject
import random
import os
import platform
import sys
import gtk
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
 iscVwImpar = ""
 iscVqDifference = 0
 iscVqTest = 0
 iscVcountText = "countText"
 iscVn1 = 1
 iscVwrite = "write"
 iscVwPar = ""
 iscVstartText = "1"
 iscVslText = "4"
 iscVnText = "12"
 iscVcount = 0
 iscVstart = 1
 iscVsl = 4
 iscVn = 12
 iscVguion = "-"
 iscVcoma = ","
 iscVn2 = 2
 iscVNotifyOSD_Imp = "notify-send \'dualPrint: Odd Copy\' \'The first print set has been copied to the clipboard. You may paste it in the print dialog.\'"
 iscVNotifyOSD_Par = "notify-send \'dualPrint: Even Copy\' \'The seccond print set has been copied to the clipboard. You may paste it in the print dialog.\'"
 iscVlink_web = "http://sourceforge.net/projects/dualprint/"
 iscVlink_license = "http://www.opensource.org/licenses/MIT"
 iscVwAbout = 0
 iscVlink_pHelp = "redirect.html"
 iscWindow151main1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow151main1Fixed = gtk.Fixed()
 iscWindow151nQ0 =gtk.Label("Which would be the last page to print?")
 iscWindow151slidesQ0 =gtk.Label("How many slides or pages per side?")
 iscWindow151n0 = gtk.Entry()
 iscWindow151sl0 = gtk.Entry()
 iscWindow151bStart0 = gtk.Button("Generate Print Sets")
 iscWindow151inicioQ0 =gtk.Label("Which would be the first page to print?")
 iscWindow151start0 = gtk.Entry()
 iscWindow151infoImpar0 =gtk.Label("Odd, set of pages to print first.")
 iscWindow151wImpar0 = gtk.Entry()
 iscWindow151parInfo0 =gtk.Label("Even, set of pages to print on the back.")
 iscWindow151wPar0 = gtk.Entry()
 iscWindow151CI0 = gtk.Image()
 iscWindow151CP0 = gtk.Image()
 iscWindow151about0 = gtk.Button("About dualPrint")
 iscWindow151paper0 = gtk.Button("Printing help")
 iscWindow151header0 = gtk.Image()

 iscWindow1about1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow1about1Fixed = gtk.Fixed()
 iscWindow1icon0 = gtk.Image()
 iscWindow1info0 =gtk.Label("dualPrint is a multi-platform application that")
 iscWindow1rights0 =gtk.Label("Copyright © 2012 Javier O. Cordero Pérez")
 iscWindow1close0 = gtk.Button("Close")
 iscWindow1web0 = gtk.Button("Website")
 iscWindow1MIT0 =gtk.Label("This software is under the MIT License")
 iscWindow1version0 =gtk.Label("1.2")
 iscWindow1dualprint0 =gtk.Label("dualPrint")
 iscWindow1license0 = gtk.Button("License")
 iscWindow1illumination0 =gtk.Label("Built in Illumination Software Creator")
 iscWindow1info10 =gtk.Label("generates print sets for multiple pages per")
 iscWindow1info20 =gtk.Label("sheet, two-sided, printing.")
 iscWindow1MIT10 =gtk.Label("For more information click License.")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()

#EndOfClass

def iscTargetIs3():
  iscIf_Linux122()
  #iscTargetIs3Python

  pass

def iscTargetIs4():
  iscIf_Linux113()
  #iscTargetIs4Python

  pass

def iscIfThen5():
 if thisiscApp1.iscVwAbout == thisiscApp1.iscVn1:
  #iscIfThen5True

  pass
 else:
  iscSetNumber139()
  #iscIfThen5False

  pass

def iscTargetIs6():
  iscClipboard_Copy118()
  #iscTargetIs6Python

  pass

def iscTargetIs7():
  iscClipboard_Copy118()
  #iscTargetIs7Python

  pass

def iscTargetIs8():
  iscClipboard_Copy120()
  #iscTargetIs8Python

  pass

def iscPortalDestination9():
 iscSetNumber69()
 iscAdd132()
 iscAdd130()
 iscAdd138()
 iscDoWhile10()
 #iscPortalDestination9Arrived


def iscDoWhile10():
 while thisiscApp1.iscVcount < thisiscApp1.iscVn:
  iscCombineText97()
  iscConvertNumberToText133()
  iscCombineText64()
  iscAdd132()
  iscAdd130()
  #iscDoWhile10Loop

 iscSetText100()
 iscAdd132()
 iscAdd130()
 iscDoWhile11()
 #iscDoWhile10Finished


def iscDoWhile11():
 while thisiscApp1.iscVcount < thisiscApp1.iscVn:
  iscCombineText97()
  iscConvertNumberToText133()
  iscCombineText64()
  iscAdd132()
  iscAdd130()
  #iscDoWhile11Loop

 iscSetText61()
 #iscDoWhile11Finished


def iscPortalDeparture12():
 iscPortalDestination31();
 #iscPortalDeparture12Done


def iscIfThen13():
 if thisiscApp1.iscVqTest > thisiscApp1.iscVn:
  iscPortalDeparture12()
  #iscIfThen13True

  pass
 else:
  iscPortalDeparture14()
  #iscIfThen13False

  pass

def iscPortalDeparture14():
 iscPortalDestination33();
 #iscPortalDeparture14Done


def iscIfThen15():
 if thisiscApp1.iscVqTest == thisiscApp1.iscVqDifference:
  iscPortalDeparture14()
  #iscIfThen15True

  pass
 else:
  iscAdd136()
  iscAdd137()
  iscIfThen13()
  #iscIfThen15False

  pass

def iscIfThen16():
 if thisiscApp1.iscVqTest < thisiscApp1.iscVqDifference:
  iscPortalDeparture14()
  #iscIfThen16True

  pass
 else:
  iscIfThen15()
  #iscIfThen16False

  pass

def iscPortalDeparture17():
 iscPortalDestination32();
 #iscPortalDeparture17Done


def iscIfThen18():
 if thisiscApp1.iscVqTest == thisiscApp1.iscVn:
  iscPortalDeparture17()
  #iscIfThen18True

  pass
 else:
  iscDivide145()
  iscIfThen16()
  #iscIfThen18False

  pass

def iscPortalDeparture19():
 iscPortalDestination9()
 #iscPortalDeparture19Done


def iscIfThen20():
 if thisiscApp1.iscVsl == thisiscApp1.iscVn1:
  iscPortalDeparture19()
  #iscIfThen20True

  pass
 else:
  iscIfThen18()
  #iscIfThen20False

  pass

def iscIfThen21():
 if thisiscApp1.iscVqTest > thisiscApp1.iscVn:
  iscMessageBox53()
  #iscIfThen21True

  pass
 else:
  iscIfThen20()
  #iscIfThen21False

  pass

def iscIfThen22():
 if thisiscApp1.iscVsl < thisiscApp1.iscVn:
  iscAdd136()
  iscIfThen21()
  #iscIfThen22True

  pass
 else:
  iscMessageBox54()
  #iscIfThen22False

  pass

def iscIfThen23():
 if thisiscApp1.iscVn < thisiscApp1.iscVn2:
  iscMessageBox58()
  #iscIfThen23True

  pass
 else:
  iscIfThen24()
  #iscIfThen23False

  pass

def iscIfThen24():
 if thisiscApp1.iscVstart < thisiscApp1.iscVn1:
  iscMessageBox57()
  #iscIfThen24True

  pass
 else:
  iscIfThen25()
  #iscIfThen24False

  pass

def iscIfThen25():
 if thisiscApp1.iscVsl < thisiscApp1.iscVn1:
  iscMessageBox56()
  #iscIfThen25True

  pass
 else:
  iscIfThen26()
  #iscIfThen25False

  pass

def iscIfThen26():
 if thisiscApp1.iscVstart < thisiscApp1.iscVn:
  iscIfThen22()
  #iscIfThen26True

  pass
 else:
  iscMessageBox55()
  #iscIfThen26False

  pass

def iscPortalDestination27():
 iscAdd127()
 iscSubtract128()
 iscIfThen142()
 #iscPortalDestination27Arrived


def iscPortalDeparture28():
 iscPortalDestination27()
 #iscPortalDeparture28Done


def iscPortalDestination29():
 iscAdd132()
 iscAdd130()
 iscConvertNumberToText133()
 iscCombineText64()
 iscPortalDeparture28()
 #iscPortalDestination29Arrived


def iscPortalDeparture30():
 iscPortalDestination29()
 #iscPortalDeparture30Done


def iscPortalDestination31():
 iscSetNumber69()
 iscCombineText78()
 iscPortalDeparture37()
 iscSetText100()
 iscCombineText78()
 iscAdd127()
 iscSubtract128()
 iscSubtract123()
 iscSubtract131()
 iscConvertNumberToText133()
 iscCombineText64()
 iscSetText61()
 #iscPortalDestination31Arrived


def iscPortalDestination32():
 iscSetNumber69()
 iscCombineText78()
 iscPortalDeparture37()
 iscSetText100()
 iscSetText61()
 #iscPortalDestination32Arrived


def iscPortalDestination33():
 iscSetNumber69()
 iscCombineText78()
 iscPortalDeparture39()
 #iscPortalDestination33Arrived


def iscPortalDestination34():
 iscAdd127()
 iscAdd126()
 iscIfThen141()
 #iscPortalDestination34Arrived


def iscPortalDestination35():
 iscAdd132()
 iscSubtract131()
 iscConvertNumberToText133()
 iscCombineText64()
 iscPortalDeparture36()
 #iscPortalDestination35Arrived


def iscPortalDeparture36():
 iscPortalDestination34()
 #iscPortalDeparture36Done


def iscPortalDeparture37():
 iscPortalDestination35()
 #iscPortalDeparture37Done


def iscPortalDestination38():
 iscPortalDeparture37()
 iscSetText100()
 iscCombineText78()
 iscPortalDeparture37()
 iscSetText61()
 #iscPortalDestination38Arrived


def iscPortalDeparture39():
 iscPortalDestination38()
 #iscPortalDeparture39Done


def iscOpen_in_Web_Browser41():
 url=(thisiscApp1.iscVlink_license)
 webbrowser.open(url)
 #iscOpen_in_Web_Browser41Done

def iscOpen_in_Web_Browser43():
 url=(thisiscApp1.iscVlink_web)
 webbrowser.open(url)
 #iscOpen_in_Web_Browser43Done

def iscOpen_in_Web_Browser45():
 url=(thisiscApp1.iscVlink_pHelp)
 webbrowser.open(url)
 #iscOpen_in_Web_Browser45Done

def iscRunShellScript47():
 os.system(thisiscApp1.iscVNotifyOSD_Par)
 #iscRunShellScript47Done


def iscAdd48():
 thisiscApp1.iscVcount = thisiscApp1.iscVstart + thisiscApp1.iscVsl
 iscConvertNumberToText49()
 #iscAdd48Done


def iscConvertNumberToText49():
 thisiscApp1.iscVwrite = str(thisiscApp1.iscVcount)
 #iscConvertNumberToText49Done


def iscConvertTextToNumber50():
 try:
  thisiscApp1.iscVn = int(thisiscApp1.iscVnText)
 except ValueError:
  thisiscApp1.iscVn = 0
 iscConvertTextToNumber51()
 #iscConvertTextToNumber50Done


def iscConvertTextToNumber51():
 try:
  thisiscApp1.iscVsl = int(thisiscApp1.iscVslText)
 except ValueError:
  thisiscApp1.iscVsl = 0
 iscConvertTextToNumber52()
 #iscConvertTextToNumber51Done


def iscConvertTextToNumber52():
 try:
  thisiscApp1.iscVstart = int(thisiscApp1.iscVstartText)
 except ValueError:
  thisiscApp1.iscVstart = 0
 iscIfThen23()
 #iscConvertTextToNumber52Done


def iscMessageBox53():
 message = "The sum of the starting page and the pages per side should be less than or equal to the total of pages to print."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox53Open
 dialog.destroy()
 #iscMessageBox53Closed

def iscMessageBox54():
 message = "The number of pages per side should be less than the total of pages to print."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox54Open
 dialog.destroy()
 #iscMessageBox54Closed

def iscMessageBox55():
 message = "The starting page should be lower than the total of pages to print."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox55Open
 dialog.destroy()
 #iscMessageBox55Closed

def iscMessageBox56():
 message = "You should print at least 1 page per side."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox56Open
 dialog.destroy()
 #iscMessageBox56Closed

def iscMessageBox57():
 message = "Your print should start from page 1 forward."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox57Open
 dialog.destroy()
 #iscMessageBox57Closed

def iscMessageBox58():
 message = "The document must have 2 pages at least."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox58Open
 dialog.destroy()
 #iscMessageBox58Closed

def iscAppQuit60():
 thisiscApp1.destroy(None,None)
 #iscAppQuit60Done


def iscSetText61():
 thisiscApp1.iscVwPar = thisiscApp1.iscVwrite
 iscSetTextBox62()
 iscSetTextBox96()
 iscTargetIs6()
 #iscSetText61Done


def iscSetTextBox62():
 thisiscApp1.iscWindow151wImpar0.set_text(thisiscApp1.iscVwImpar)
 #iscSetTextBox62Done


def iscCombineText64():
 thisiscApp1.iscVwrite = thisiscApp1.iscVwrite + thisiscApp1.iscVcountText
 #iscCombineText64Done


def iscSetNumber69():
 thisiscApp1.iscVqTest = 0
 iscSetNumber135()
 #iscSetNumber69Done


def iscSetText77():
 thisiscApp1.iscVwrite = thisiscApp1.iscVstartText
 #iscSetText77Done


def iscCombineText78():
 thisiscApp1.iscVwrite = thisiscApp1.iscVwrite + thisiscApp1.iscVguion
 #iscCombineText78Done


def iscGetTextBox90():
 thisiscApp1.iscVstartText = thisiscApp1.iscWindow151start0.get_text()
 iscConvertTextToNumber50()
 #iscGetTextBox90Done


def iscGetTextBox93():
 thisiscApp1.iscVnText = thisiscApp1.iscWindow151n0.get_text()
 iscGetTextBox94()
 #iscGetTextBox93Done


def iscGetTextBox94():
 thisiscApp1.iscVslText = thisiscApp1.iscWindow151sl0.get_text()
 iscGetTextBox90()
 #iscGetTextBox94Done


def iscSetTextBox96():
 thisiscApp1.iscWindow151wPar0.set_text(thisiscApp1.iscVwPar)
 #iscSetTextBox96Done


def iscCombineText97():
 thisiscApp1.iscVwrite = thisiscApp1.iscVwrite + thisiscApp1.iscVcoma
 #iscCombineText97Done


def iscGetTextBox98():
 thisiscApp1.iscVwImpar = thisiscApp1.iscWindow151wImpar0.get_text()
 iscTargetIs7()
 #iscGetTextBox98Done


def iscGetTextBox99():
 thisiscApp1.iscVwPar = thisiscApp1.iscWindow151wPar0.get_text()
 iscTargetIs8()
 #iscGetTextBox99Done


def iscSetText100():
 thisiscApp1.iscVwImpar = thisiscApp1.iscVwrite
 iscAdd48()
 #iscSetText100Done


def iscIf_Linux113():
 if os.name == 'posix' or platform.system() == 'Linux':
  OS = "Linux"
  iscRunShellScript47()
  #iscIf_Linux113Linux
 else:
  OS = "Other"
  #iscIf_Linux113Else

def iscRunShellScript114():
 os.system(thisiscApp1.iscVNotifyOSD_Imp)
 #iscRunShellScript114Done


def iscMessageBox115():
 message = "Select the text with the mouse, right click on it and select Copy."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox115Open
 dialog.destroy()
 #iscMessageBox115Closed

def iscMessageBox116():
 message = "The copy function is not yet available for the mobile version of dualPrint."
 dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_NONE, message)
 dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
 dialog.run()
 #iscMessageBox116Open
 dialog.destroy()
 #iscMessageBox116Closed

def iscClipboard_Copy118():
 pyperclip.copy(thisiscApp1.iscVwImpar)
 iscTargetIs3()
 pyperclip.copy(thisiscApp1.iscVwImpar)
 #iscClipboard_Copy118Done
def iscClipboard_Copy120():
 pyperclip.copy(thisiscApp1.iscVwPar)
 iscTargetIs4()
 pyperclip.copy(thisiscApp1.iscVwPar)
 #iscClipboard_Copy120Done
def iscIf_Linux122():
 if os.name == 'posix' or platform.system() == 'Linux':
  OS = "Linux"
  iscRunShellScript114()
  #iscIf_Linux122Linux
 else:
  OS = "Other"
  #iscIf_Linux122Else

def iscSubtract123():
 thisiscApp1.iscVqDifference = thisiscApp1.iscVqTest - thisiscApp1.iscVn
 iscSubtract124()
 #iscSubtract123Done


def iscSubtract124():
 thisiscApp1.iscVqDifference = thisiscApp1.iscVsl - thisiscApp1.iscVqDifference
 iscAdd125()
 #iscSubtract124Done


def iscAdd125():
 thisiscApp1.iscVcount = thisiscApp1.iscVcount + thisiscApp1.iscVqDifference
 #iscAdd125Done


def iscAdd126():
 thisiscApp1.iscVqTest = thisiscApp1.iscVqTest + thisiscApp1.iscVn1
 #iscAdd126Done


def iscAdd127():
 thisiscApp1.iscVqTest = thisiscApp1.iscVcount + thisiscApp1.iscVsl
 #iscAdd127Done


def iscSubtract128():
 thisiscApp1.iscVqTest = thisiscApp1.iscVqTest - thisiscApp1.iscVn1
 #iscSubtract128Done


def iscAdd130():
 thisiscApp1.iscVcount = thisiscApp1.iscVcount + thisiscApp1.iscVn1
 #iscAdd130Done


def iscSubtract131():
 thisiscApp1.iscVcount = thisiscApp1.iscVcount - thisiscApp1.iscVn1
 #iscSubtract131Done


def iscAdd132():
 thisiscApp1.iscVcount = thisiscApp1.iscVcount + thisiscApp1.iscVsl
 #iscAdd132Done


def iscConvertNumberToText133():
 thisiscApp1.iscVcountText = str(thisiscApp1.iscVcount)
 #iscConvertNumberToText133Done


def iscSetNumber134():
 thisiscApp1.iscVcount = thisiscApp1.iscVstart
 iscSetText77()
 #iscSetNumber134Done


def iscSetNumber135():
 thisiscApp1.iscVqDifference = 0
 iscSetNumber134()
 #iscSetNumber135Done


def iscAdd136():
 thisiscApp1.iscVqTest = thisiscApp1.iscVstart + thisiscApp1.iscVsl
 #iscAdd136Done


def iscAdd137():
 thisiscApp1.iscVqTest = thisiscApp1.iscVqTest + thisiscApp1.iscVsl
 #iscAdd137Done


def iscAdd138():
 thisiscApp1.iscVn = thisiscApp1.iscVn + thisiscApp1.iscVn1
 #iscAdd138Done


def iscSetNumber139():
 thisiscApp1.iscVwAbout = 1
 iscWindow1()
 #iscSetNumber139Done


def iscSetNumber140():
 thisiscApp1.iscVwAbout = 0
 #iscSetNumber140Done


def iscIfThen141():
 if thisiscApp1.iscVqTest < thisiscApp1.iscVn:
  iscCombineText97()
  iscPortalDeparture30()
  #iscIfThen141True

  pass
 else:
  iscIfThen143()
  #iscIfThen141False

  pass

def iscIfThen142():
 if thisiscApp1.iscVqTest < thisiscApp1.iscVn:
  iscCombineText78()
  iscPortalDeparture37()
  #iscIfThen142True

  pass
 else:
  iscIfThen144()
  #iscIfThen142False

  pass

def iscIfThen143():
 if thisiscApp1.iscVqTest == thisiscApp1.iscVn:
  iscCombineText97()
  iscAdd132()
  iscAdd130()
  iscConvertNumberToText133()
  iscCombineText64()
  #iscIfThen143True

  pass
 else:
  #iscIfThen143False

  pass

def iscIfThen144():
 if thisiscApp1.iscVqTest == thisiscApp1.iscVn:
  iscCombineText78()
  iscAdd132()
  iscSubtract131()
  iscConvertNumberToText133()
  iscCombineText64()
  #iscIfThen144True

  pass
 else:
  iscCombineText78()
  iscSubtract123()
  iscSubtract131()
  iscConvertNumberToText133()
  iscConvertNumberToText133()
  iscCombineText64()
  #iscIfThen144False

  pass

def iscDivide145():
 thisiscApp1.iscVqDifference = thisiscApp1.iscVn / thisiscApp1.iscVn2
 #iscDivide145Done


def iscSetCanvasPicture146():
 thisiscApp1.iscWindow151header0.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/header.jpg") #iscSetCanvasPicture146Done


def iscSetCanvasPicture147():
 thisiscApp1.iscWindow151CP0.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/copy.gif") #iscSetCanvasPicture147Done


def iscSetCanvasPicture148():
 thisiscApp1.iscWindow151CI0.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/copy.gif") #iscSetCanvasPicture148Done


def iscCloseWindow149():
 thisiscApp1.iscWindow1about1.destroy()
 iscSetNumber140()
 #iscCloseWindow149Done


def iscSetCanvasPicture150():
 thisiscApp1.iscWindow1icon0.set_from_file(os.path.dirname(sys.argv[0]) + "/ISCimages/dualprint.gif") #iscSetCanvasPicture150Done


def iscWindow151():
 thisiscApp1.iscWindow151nQ0 =gtk.Label("Which would be the last page to print?")
 thisiscApp1.iscWindow151slidesQ0 =gtk.Label("How many slides or pages per side?")
 thisiscApp1.iscWindow151n0 = gtk.Entry()
 thisiscApp1.iscWindow151sl0 = gtk.Entry()
 thisiscApp1.iscWindow151bStart0 = gtk.Button("Generate Print Sets")
 thisiscApp1.iscWindow151inicioQ0 =gtk.Label("Which would be the first page to print?")
 thisiscApp1.iscWindow151start0 = gtk.Entry()
 thisiscApp1.iscWindow151infoImpar0 =gtk.Label("Odd, set of pages to print first.")
 thisiscApp1.iscWindow151wImpar0 = gtk.Entry()
 thisiscApp1.iscWindow151parInfo0 =gtk.Label("Even, set of pages to print on the back.")
 thisiscApp1.iscWindow151wPar0 = gtk.Entry()
 thisiscApp1.iscWindow151CI0 = gtk.Image()
 thisiscApp1.iscWindow151CP0 = gtk.Image()
 thisiscApp1.iscWindow151about0 = gtk.Button("About dualPrint")
 thisiscApp1.iscWindow151paper0 = gtk.Button("Printing help")
 thisiscApp1.iscWindow151header0 = gtk.Image()
 thisiscApp1.iscWindow151main1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow151main1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow151main1.set_title("dualPrint")
 thisiscApp1.iscWindow151main1.set_default_size(320, 438)
 thisiscApp1.iscWindow151main1.add(thisiscApp1.iscWindow151main1Fixed)
 thisiscApp1.iscWindow151main1Fixed.width = 320
 thisiscApp1.iscWindow151main1Fixed.height = 438
 thisiscApp1.iscWindow151main1.connect("delete_event", iscWindow151Closed)
 thisiscApp1.iscWindow151main1Fixed.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151nQ0, 10, 125)
 thisiscApp1.iscWindow151nQ0.set_size_request(300, 18)
 thisiscApp1.iscWindow151nQ0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151slidesQ0, 10, 180)
 thisiscApp1.iscWindow151slidesQ0.set_size_request(300, 18)
 thisiscApp1.iscWindow151slidesQ0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151n0, 40, 148)
 thisiscApp1.iscWindow151n0.set_text("12")
 thisiscApp1.iscWindow151n0.set_size_request(90, 24)
 thisiscApp1.iscWindow151n0.connect("changed", iscWindow151nChanged)
 thisiscApp1.iscWindow151n0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151sl0, 40, 202)
 thisiscApp1.iscWindow151sl0.set_text("4")
 thisiscApp1.iscWindow151sl0.set_size_request(90, 24)
 thisiscApp1.iscWindow151sl0.connect("changed", iscWindow151slChanged)
 thisiscApp1.iscWindow151sl0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151bStart0, 48, 235)
 thisiscApp1.iscWindow151bStart0.set_size_request(250, 32)
 thisiscApp1.iscWindow151bStart0.connect("clicked", iscWindow151bStartClicked)
 thisiscApp1.iscWindow151bStart0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151inicioQ0, 10, 71)
 thisiscApp1.iscWindow151inicioQ0.set_size_request(300, 18)
 thisiscApp1.iscWindow151inicioQ0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151start0, 40, 94)
 thisiscApp1.iscWindow151start0.set_text("1")
 thisiscApp1.iscWindow151start0.set_size_request(90, 24)
 thisiscApp1.iscWindow151start0.connect("changed", iscWindow151startChanged)
 thisiscApp1.iscWindow151start0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151infoImpar0, 4, 275)
 thisiscApp1.iscWindow151infoImpar0.set_size_request(316, 18)
 thisiscApp1.iscWindow151infoImpar0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151wImpar0, 56, 299)
 thisiscApp1.iscWindow151wImpar0.set_text("")
 thisiscApp1.iscWindow151wImpar0.set_size_request(245, 26)
 thisiscApp1.iscWindow151wImpar0.connect("changed", iscWindow151wImparChanged)
 thisiscApp1.iscWindow151wImpar0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151parInfo0, 4, 334)
 thisiscApp1.iscWindow151parInfo0.set_size_request(316, 18)
 thisiscApp1.iscWindow151parInfo0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151wPar0, 57, 358)
 thisiscApp1.iscWindow151wPar0.set_text("")
 thisiscApp1.iscWindow151wPar0.set_size_request(245, 26)
 thisiscApp1.iscWindow151wPar0.connect("changed", iscWindow151wParChanged)
 thisiscApp1.iscWindow151wPar0.show()
 iscWindow151CI0EventBox = gtk.EventBox()
 iscWindow151CI0EventBox.set_size_request(32, 32)
 iscWindow151CI0EventBox.connect("button_press_event", iscWindow151CIClicked)
 thisiscApp1.iscWindow151CI0.set_size_request(32, 32)
 iscWindow151CI0EventBox.add(thisiscApp1.iscWindow151CI0)
 thisiscApp1.iscWindow151main1Fixed.put(iscWindow151CI0EventBox, 15, 297)
 thisiscApp1.iscWindow151CI0.show()
 iscWindow151CI0EventBox.show()
 iscWindow151CP0EventBox = gtk.EventBox()
 iscWindow151CP0EventBox.set_size_request(32, 32)
 iscWindow151CP0EventBox.connect("button_press_event", iscWindow151CPClicked)
 thisiscApp1.iscWindow151CP0.set_size_request(32, 32)
 iscWindow151CP0EventBox.add(thisiscApp1.iscWindow151CP0)
 thisiscApp1.iscWindow151main1Fixed.put(iscWindow151CP0EventBox, 14, 355)
 thisiscApp1.iscWindow151CP0.show()
 iscWindow151CP0EventBox.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151about0, 166, 395)
 thisiscApp1.iscWindow151about0.set_size_request(136, 30)
 thisiscApp1.iscWindow151about0.connect("clicked", iscWindow151aboutClicked)
 thisiscApp1.iscWindow151about0.show()
 thisiscApp1.iscWindow151main1Fixed.put(thisiscApp1.iscWindow151paper0, 18, 395)
 thisiscApp1.iscWindow151paper0.set_size_request(136, 30)
 thisiscApp1.iscWindow151paper0.connect("clicked", iscWindow151paperClicked)
 thisiscApp1.iscWindow151paper0.show()
 iscWindow151header0EventBox = gtk.EventBox()
 iscWindow151header0EventBox.set_size_request(320, 68)
 iscWindow151header0EventBox.connect("button_press_event", iscWindow151headerClicked)
 thisiscApp1.iscWindow151header0.set_size_request(320, 68)
 iscWindow151header0EventBox.add(thisiscApp1.iscWindow151header0)
 thisiscApp1.iscWindow151main1Fixed.put(iscWindow151header0EventBox, 0, 0)
 thisiscApp1.iscWindow151header0.show()
 iscWindow151header0EventBox.show()
 thisiscApp1.iscWindow151main1.show()
 iscSetCanvasPicture148()
 iscSetCanvasPicture147()
 iscSetCanvasPicture146()
 #iscWindow151Opened
 #iscWindow151Done


def iscWindow151Closed(self, other):
 pass
 iscAppQuit60()
 #iscWindow151Closed


def iscWindow151nChanged(self):
 pass
 #iscWindow151nChanged


def iscWindow151slChanged(self):
 pass
 #iscWindow151slChanged


def iscWindow151bStartClicked(self):
 pass
 iscGetTextBox93()
 #iscWindow151bStartClicked


def iscWindow151startChanged(self):
 pass
 #iscWindow151startChanged


def iscWindow151wImparChanged(self):
 pass
 iscSetTextBox62()
 #iscWindow151wImparChanged


def iscWindow151wParChanged(self):
 pass
 iscSetTextBox96()
 #iscWindow151wParChanged


def iscWindow151CIClicked(widget, event):
 pass
 iscGetTextBox98()
 #iscWindow151CIClicked


def iscWindow151CPClicked(widget, event):
 pass
 iscGetTextBox99()
 #iscWindow151CPClicked


def iscWindow151aboutClicked(self):
 pass
 iscIfThen5()
 #iscWindow151aboutClicked


def iscWindow151paperClicked(self):
 pass
 iscOpen_in_Web_Browser45()
 #iscWindow151paperClicked


def iscWindow151headerClicked(widget, event):
 pass
 #iscWindow151headerClicked


def iscWindow1():
 thisiscApp1.iscWindow1icon0 = gtk.Image()
 thisiscApp1.iscWindow1info0 =gtk.Label("dualPrint is a multi-platform application that")
 thisiscApp1.iscWindow1rights0 =gtk.Label("Copyright © 2012 Javier O. Cordero Pérez")
 thisiscApp1.iscWindow1close0 = gtk.Button("Close")
 thisiscApp1.iscWindow1web0 = gtk.Button("Website")
 thisiscApp1.iscWindow1MIT0 =gtk.Label("This software is under the MIT License")
 thisiscApp1.iscWindow1version0 =gtk.Label("1.2")
 thisiscApp1.iscWindow1dualprint0 =gtk.Label("dualPrint")
 thisiscApp1.iscWindow1license0 = gtk.Button("License")
 thisiscApp1.iscWindow1illumination0 =gtk.Label("Built in Illumination Software Creator")
 thisiscApp1.iscWindow1info10 =gtk.Label("generates print sets for multiple pages per")
 thisiscApp1.iscWindow1info20 =gtk.Label("sheet, two-sided, printing.")
 thisiscApp1.iscWindow1MIT10 =gtk.Label("For more information click License.")
 thisiscApp1.iscWindow1about1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow1about1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow1about1.set_title("About dualPrint")
 thisiscApp1.iscWindow1about1.set_default_size(310, 380)
 thisiscApp1.iscWindow1about1.add(thisiscApp1.iscWindow1about1Fixed)
 thisiscApp1.iscWindow1about1Fixed.width = 310
 thisiscApp1.iscWindow1about1Fixed.height = 380
 thisiscApp1.iscWindow1about1.connect("delete_event", iscWindow1Closed)
 thisiscApp1.iscWindow1about1Fixed.show()
 iscWindow1icon0EventBox = gtk.EventBox()
 iscWindow1icon0EventBox.set_size_request(90, 90)
 iscWindow1icon0EventBox.connect("button_press_event", iscWindow1iconClicked)
 thisiscApp1.iscWindow1icon0.set_size_request(90, 90)
 iscWindow1icon0EventBox.add(thisiscApp1.iscWindow1icon0)
 thisiscApp1.iscWindow1about1Fixed.put(iscWindow1icon0EventBox, 115, 12)
 thisiscApp1.iscWindow1icon0.show()
 iscWindow1icon0EventBox.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1info0, 10, 155)
 thisiscApp1.iscWindow1info0.set_size_request(300, 20)
 thisiscApp1.iscWindow1info0.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1rights0, 10, 225)
 thisiscApp1.iscWindow1rights0.set_size_request(300, 20)
 thisiscApp1.iscWindow1rights0.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1close0, 212, 340)
 thisiscApp1.iscWindow1close0.set_size_request(80, 27)
 thisiscApp1.iscWindow1close0.connect("clicked", iscWindow1closeClicked)
 thisiscApp1.iscWindow1close0.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1web0, 18, 340)
 thisiscApp1.iscWindow1web0.set_size_request(80, 27)
 thisiscApp1.iscWindow1web0.connect("clicked", iscWindow1webClicked)
 thisiscApp1.iscWindow1web0.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1MIT0, 10, 285)
 thisiscApp1.iscWindow1MIT0.set_size_request(300, 20)
 thisiscApp1.iscWindow1MIT0.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1version0, 120, 130)
 thisiscApp1.iscWindow1version0.set_size_request(80, 20)
 thisiscApp1.iscWindow1version0.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1dualprint0, 120, 108)
 thisiscApp1.iscWindow1dualprint0.set_size_request(80, 20)
 thisiscApp1.iscWindow1dualprint0.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1license0, 110, 340)
 thisiscApp1.iscWindow1license0.set_size_request(80, 27)
 thisiscApp1.iscWindow1license0.connect("clicked", iscWindow1licenseClicked)
 thisiscApp1.iscWindow1license0.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1illumination0, 10, 255)
 thisiscApp1.iscWindow1illumination0.set_size_request(300, 20)
 thisiscApp1.iscWindow1illumination0.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1info10, 10, 175)
 thisiscApp1.iscWindow1info10.set_size_request(300, 20)
 thisiscApp1.iscWindow1info10.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1info20, 10, 195)
 thisiscApp1.iscWindow1info20.set_size_request(300, 20)
 thisiscApp1.iscWindow1info20.show()
 thisiscApp1.iscWindow1about1Fixed.put(thisiscApp1.iscWindow1MIT10, 10, 305)
 thisiscApp1.iscWindow1MIT10.set_size_request(300, 20)
 thisiscApp1.iscWindow1MIT10.show()
 thisiscApp1.iscWindow1about1.show()
 iscSetCanvasPicture150()
 #iscWindow1Opened
 #iscWindow1Done


def iscWindow1Closed(self, other):
 pass
 iscSetNumber140()
 #iscWindow1Closed


def iscWindow1iconClicked(widget, event):
 pass
 #iscWindow1iconClicked


def iscWindow1closeClicked(self):
 pass
 iscCloseWindow149()
 #iscWindow1closeClicked


def iscWindow1webClicked(self):
 pass
 iscOpen_in_Web_Browser43()
 #iscWindow1webClicked


def iscWindow1licenseClicked(self):
 pass
 iscOpen_in_Web_Browser41()
 #iscWindow1licenseClicked


#EndOfFunctions

thisiscApp1 = iscApp1()

iscWindow151()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()

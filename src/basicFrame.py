__author__="dmarques"
__date__ ="$Mar 27, 2014 3:38:30 PM$"

import wx

class firstFrame(wx.Frame):
    def __init__ (self, parent, id):
        wx.Frame.__init__(self,parent,id,'Frame aka Window', size=(300,200))

if __name__ == '__main__':
    app=wx.PySimpleApp()
    frame=firstFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()



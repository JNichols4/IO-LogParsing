# Starting this file in the hopes that I will be able to create a graphical user interface that incorporates the
# ability to change the files imported.
#
# TODO: Create a GUI that allows for file selection, single (or multiple) files for parsing.
# TODO: Create a GUI option that allows for directory scanning, "new" file parsing, and mass data generation.
#
# Making sure to push to git so that this file is available online.

from Tkinter import *
import Tkinter as tk
import tkFileDialog
import os
import errno


def checkdir(cdpath):
    if not os.path.exists(cdpath):
        try:
            os.makedirs(cdpath)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise


class App(tk.Frame):
    def __init__(self, master, frameSize):
        tk.Frame.__init__(self,master)
        self.defDir = os.getcwd() + '\\defaults\\'

        #STATES
        self.rb1 = tk.IntVar()
        self.rb2 = tk.IntVar()
        self.rb3 = tk.IntVar()
        self.rb4 = tk.IntVar()
        self.rb5 = tk.IntVar()
        self.rb6 = tk.IntVar()

        #Framing constituents
        self.fs = frameSize.split('x')
        checkdir(self.defDir)

        wheight = float(self.fs[1])
        wwidth = float(self.fs[0])


        # FRAMES

        # TODO: Make the frames resizeable or make the window a static size.
        # MAIN FRAMES
        self.browseFrame = tk.Frame(master, height=.2*wheight, bd=1, relief=SUNKEN)
        self.browseFrame.pack(fill=X, padx=5)

        self.optionFrame = tk.Frame(master, height=.6*wheight, bd=1)
        self.optionFrame.pack(fill=X, padx=5)

        self.bottomFrame = tk.Frame(master, height=.2*wheight, bd=1, relief=SUNKEN)
        self.bottomFrame.pack(fill=X, padx=5)

        # TODO: Make the sizes of these frames dependent on the size of the mother frame that they are in.
        # 1 LEVEL SUBFRAMES
        self.bbuttonFrame = tk.Frame(self.browseFrame, height=.2*wheight, width=.25*wwidth, bd=1, relief=SUNKEN)
        self.bbuttonFrame.pack(side=LEFT)

        self.binputFrame = tk.Frame(self.browseFrame, height=.2*wheight, width=.75*wwidth, bd=1, relief=SUNKEN)
        self.binputFrame.pack(side=LEFT)

        self.optCheckbox = tk.Frame(self.optionFrame, height=.6*wheight, width=.25*wwidth, bd=1, relief=SUNKEN)
        self.optCheckbox.pack(side=LEFT)

        self.centerCheckbox = tk.Frame(self.optionFrame, height=.6*wheight, width=.75*wwidth, bd=1, relief=SUNKEN)
        self.centerCheckbox.pack(side=LEFT)

        # 2 LEVEL SUBFRAMES
        self.pullCheckbox = tk.Frame(self.optCheckbox, height=.3*.6*wheight, width=.25*wwidth)
        self.pullCheckbox.pack(side=TOP)

        self.dataOutpbox = tk.Frame(self.optCheckbox, height=.7*.6*wheight, width=.25*wwidth)
        self.dataOutpbox.pack(side=TOP)

        # TODO: Align these panels with the top left of the parent frame. The grid should extend from there, not the center.
        self.iosCheckbox = tk.Frame(self.centerCheckbox, height=.3*.6*wheight, width=.375*wwidth)
        self.iosCheckbox.grid(row=0, column=0, sticky=NW)

        self.respTimebox = tk.Frame(self.centerCheckbox, height=.3*.6*wheight, width=.375*wwidth)
        self.respTimebox.grid(row=1, column=0)

        self.genMenu = tk.Frame(self.centerCheckbox, height=.3*.6*wheight, width=.375*wwidth)
        self.genMenu.grid(row=0, column=1)

        self.genMenu2 = tk.Frame(self.centerCheckbox, height=.3*.6*wheight, width=.375*wwidth)
        self.genMenu2.grid(row=1, column=1)


        #Resize flags
        self.browseFrame.pack_propagate(FALSE)
        self.optionFrame.pack_propagate(FALSE)
        self.bottomFrame.pack_propagate(FALSE)
        self.bbuttonFrame.pack_propagate(FALSE)
        self.binputFrame.pack_propagate(FALSE)
        self.optCheckbox.pack_propagate(FALSE)
        self.centerCheckbox.pack_propagate(FALSE)
        self.pullCheckbox.pack_propagate(FALSE)
        self.dataOutpbox.pack_propagate(FALSE)
        self.iosCheckbox.pack_propagate(FALSE)
        self.respTimebox.pack_propagate(FALSE)
        self.genMenu.pack_propagate(FALSE)
        self.genMenu2.pack_propagate(FALSE)


        # Buttons, entries, and check boxes
        self.browseButton = tk.Button(self.bbuttonFrame, text='Browse for File', command=self.fileBrowser)
        self.browseButton.pack(fill=X, anchor=CENTER)

        self.browseButton1 = tk.Button(self.bbuttonFrame, text='Browse for Directory', command=self.fileBrowser1)
        self.browseButton1.pack(fill=X, anchor=CENTER)

        self.importEntry = tk.Entry(self.binputFrame, bd=2)
        self.importEntry.pack(fill=X, ipady=3, anchor=CENTER)

        self.importEntry1 = tk.Entry(self.binputFrame, bd=2)
        self.importEntry1.pack(fill=X, ipady=3, anchor=CENTER)


        # PULL OPTIONS AND CHECK BOXES
        self.CB1 = tk.Radiobutton(self.pullCheckbox, variable=self.rb1, value=1, bd=1, text='Pull Single File')
        self.CB1.pack(anchor=NW)

        self.CB2 = tk.Radiobutton(self.pullCheckbox, variable=self.rb1, value=2, bd=1, text='Pull Directory')
        self.CB2.pack(anchor=NW)

        self.CB3 = tk.Radiobutton(self.dataOutpbox, variable=self.rb2, value=1, bd=1, text='Generate CSV')
        self.CB3.pack(anchor=NW)

        self.CB4 = tk.Radiobutton(self.dataOutpbox, variable=self.rb2, value=2, bd=1, text='Generate TXT')
        self.CB4.pack(anchor=NW)

        self.CB5 = tk.Radiobutton(self.iosCheckbox, variable = self.rb3, value=1, text='IO Parsing')
        self.CB6 = tk.Radiobutton(self.iosCheckbox, variable = self.rb3, value=0, text='None')
        self.CB5.pack(anchor=NW)
        self.CB6.pack(anchor=NW)

        self.CB7 = tk.Radiobutton(self.respTimebox, variable = self.rb4, value=1, text='Time Parsing')
        self.CB8 = tk.Radiobutton(self.respTimebox, variable = self.rb4, value=0, text='None')
        self.CB7.pack(anchor=NW)
        self.CB8.pack(anchor=NW)

        self.CB9 = tk.Radiobutton(self.genMenu, variable = self.rb5, value=1, text='GUI element1')
        self.CB10 = tk.Radiobutton(self.genMenu, variable = self.rb5, value=0, text='None')
        self.CB9.pack(anchor=NW)
        self.CB10.pack(anchor=NW)

        self.CB11 = tk.Radiobutton(self.genMenu2, variable = self.rb6, value=1, text='GUI element2')
        self.CB12 = tk.Radiobutton(self.genMenu2, variable = self.rb6, value=0, text='None')
        self.CB11.pack(anchor=NW)
        self.CB12.pack(anchor=NW)

    def fileBrowser(self):
            filename = tkFileDialog.askopenfilename(prent=rootWindow, title="Browse for import file")
            if filename is '':
                return 0
            elif filename is not '':
                #This needs to be a Tkinter import entry widget
                self.importEntry.delete(0, 'end')
                self.importEntry.insert(0, filename)

    def fileBrowser1(self):
            filename = tkFileDialog.askopenfilename(prent=rootWindow, title="Browse for import file")
            if filename is '':
                return 0
            elif filename is not '':
                #This needs to be a Tkinter import entry widget
                self.importEntry1.delete(0, 'end')
                self.importEntry1.insert(0, filename)




if __name__ == "__main__":
    rootWindow = tk.Tk()
    # TODO: Make the window a static size and not resizeable
    frameSize = "500x300"
    rootWindow.title('IO LOG PARSER')
    rootWindow.geometry(frameSize)
    app = App(rootWindow, frameSize)
    app.mainloop()
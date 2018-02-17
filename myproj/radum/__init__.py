import gtk
import gtk.glade
import numpy as np
import matplotlib.pyplot as plt
import csv
import gobject
import pango
import os
from subprocess import Popen, PIPE
import fcntl
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

wnd = gtk.Window()
wnd.set_default_size(400, 400)
wnd.connect("destroy", gtk.main_quit)
textview = gtk.TextView()
fontdesc = pango.FontDescription("monospace")
textview.modify_font(fontdesc)
scroll = gtk.ScrolledWindow()
scroll.add(textview)
exp = gtk.Expander("Details")
exp.add(scroll)
wnd.add(exp)
wnd.show_all()
df = pd.read_csv('/home/linuxlite/Desktop/sursa2.csv')
m = ols('An ~ Procent',df).fit()
#textview.get_buffer().insert_at_cursor(df.describe().to_string())
print m.summary()
#sub_proc = Popen('/home/linuxlite/Desktop/child.py', stdout=PIPE, shell=True)
#sub_outp = ""

builder=gtk.Builder()
builder.add_from_file("interfata.glade")    
window=builder.get_object("window1")
filename="/home/linuxlite/Desktop/sursa2.csv"

def main():
    signals={"on_window1_destroy":on_window1_destroy, "on_button1_clicked":on_button1_clicked, "on_button2_clicked":on_button2_clicked, "on_button3_clicked":on_button3_clicked, "on_imagemenuitem5_activate":on_imagemenuitem5_activate, "on_imagemenuitem2_activate":on_imagemenuitem2_activate}
    builder.connect_signals(signals)
    window.show()
    #gobject.timeout_add(100, update_terminal)
    gtk.main()

def on_window1_destroy(self):
    print "destroy signal occurred"
    gtk.main_quit()
    
def on_imagemenuitem5_activate(self):
    print "destroy signal occurred"
    gtk.main_quit()
    
def on_imagemenuitem2_activate(self):
    from Tkinter import Tk
    from tkFileDialog import askopenfilename
    Tk().withdraw() 
    global filename
    filename = askopenfilename() 
    #print(filename)
    
def on_button1_clicked(self):
    from sklearn.decomposition import PCA
    from sklearn.datasets import load_digits
    digits = load_digits()
    pca = PCA(n_components=2)
    proj = pca.fit_transform(digits.data)
    plt.scatter(proj[:, 0], proj[:, 1], c=digits.target) 
    
    plt.colorbar() 
    plt.show()
    
def on_button2_clicked(self):
    x = []
    y = []

    with open(filename,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(float(row[1])))
    
    plt.plot(x,y, label='Incarcat din fisierul sursa2.csv!')
    plt.xlabel('Ani')
    plt.ylabel('%')
    plt.title('Grad de cuprindere in invatamant a populatiei de varsta scolara')
    plt.legend()
    plt.show()

def on_button3_clicked(self):    
    print "destroy signal occurred"
    gtk.main_quit()
    
def non_block_read(output):
    fd = output.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    try:
        return output.read()
    except:
        return ''


#def update_terminal():
   # textview.get_buffer().insert_at_cursor(non_block_read(sub_proc.stdout))
   # return sub_proc.poll() is None

main()


import gtk
import gtk.glade
import numpy as np
import matplotlib.pyplot as plt
import csv

builder=gtk.Builder()
builder.add_from_file("interfata.glade")
window=builder.get_object("window1")
filename="/home/linuxlite/Desktop/sursa.csv"

def main():
    signals={"on_window1_destroy":on_window1_destroy, "on_button1_clicked":on_button1_clicked, "on_button2_clicked":on_button2_clicked, "on_button3_clicked":on_button3_clicked, "on_imagemenuitem5_activate":on_imagemenuitem5_activate, "on_imagemenuitem2_activate":on_imagemenuitem2_activate}
    builder.connect_signals(signals)
    window.show()
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
            y.append(int(row[1]))
    
    plt.plot(x,y, label='Loaded from file!')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

def on_button3_clicked(self):    
    print "destroy signal occurred"
    gtk.main_quit()

main()


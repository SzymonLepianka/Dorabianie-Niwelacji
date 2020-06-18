from tkinter import filedialog
from tkinter import *
import ni2
import tkinter.font as tkFont


def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))


def _on_mousewheel(self, event):
    self.canvas.yview_scroll(-1 * (event.delta / 120), "units")


def on_mousewheel(event):
    shift = (event.state & 0x1) != 0
    scroll = -1 if event.delta > 0 else 1
    if shift:
        canvas.xview_scroll(scroll, "units")
    else:
        canvas.yview_scroll(scroll, "units")


root = Tk()
canvas = Canvas(root)
canvas.bind_all("<MouseWheel>", on_mousewheel)
main_frame = Frame(canvas)
vsb_y = Scrollbar(root, orient="vertical", command=canvas.yview)
vsb_x = Scrollbar(root, orient="horizontal", command=canvas.xview)
canvas.configure(yscrollcommand=vsb_y.set)
canvas.configure(xscrollcommand=vsb_x.set)

vsb_y.pack(side="right", fill="y")
vsb_x.pack(side="bottom", fill="x")
canvas.pack(side="left", fill="both", expand=True)
canvas_frame = canvas.create_window((0, 0), window=main_frame, anchor="nw")  # tags="frame")
root.geometry('1000x800')  # po plusach położenie początkowe okienka
root.iconbitmap('DN.ico')
labels_pos1 = [0] * 10000
labels_pos2 = [0] * 10000

# def onCanvasConfigure(e):
#     canvas.itemconfig('frame', height=canvas.winfo_height(), width=canvas.winfo_width())
#
#     print(str("c: " + str(canvas.winfo_height())) + " " + str(canvas.winfo_width()))
# print(type(main_frame))
# main_frame.pack(anchor=W, fill=Y, expand=False, side=LEFT)
# print(type(main_frame))
main_frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
# canvas.bind("<Configure>", onCanvasConfigure)
root.title('Dorabianie Niwelacji')  # tytuł okienka
# main_frame.place(x=0, y=0, width=1000, height=1000, expand=True)

frame_pos_list = []
for i in range(100):
    frame_pos_list.append(Frame(root).place(x=2000, y=2000))


def populate(main_frame):
    for row in range(550):
        t = "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "
        Label(main_frame, text=t).pack()


dane_o_posrednich1 = [[0] * 100 for i in range(100)]
dane_o_posrednich2 = [[0] * 100 for i in range(100)]
for a in range(100):
    for b in range(100):
        dane_o_posrednich1[a][b] = StringVar()
        dane_o_posrednich2[a][b] = StringVar()


def punkty(sv1, iterator):
    number1 = sv1.get()
    global frame_pos_list
    if frame_pos_list[iterator]:
        frame_pos_list[iterator].destroy()
    frame_pos_list[iterator] = Frame(main_frame)
    frame_pos_list[iterator].place(x=430, y=130 + iterator * 80, height=60, width=8500)
    for j in range(iterator * 100, iterator * 100 + 100):
        labels_pos1[j] = 0
        labels_pos2[j] = 0
    for x in range(iterator * 100, iterator * 100 + 100):
        labels_pos1[x] = 0
        labels_pos2[x] = 0
    for i in range(int(number1)):
        if i == 0:
            Label(frame_pos_list[iterator], text="Nazwa:").place(x=18, y=20)
            Label(frame_pos_list[iterator], text="Wysokość:").place(x=10, y=40)
        Label(frame_pos_list[iterator], text="Pośredni nr " + str(i + 1) + ":").place(x=75 + i * 80, y=0)
        Entry(frame_pos_list[iterator], width=12, textvariable=dane_o_posrednich1[int(iterator)][i]).place(
            x=75 + i * 80, y=20)
        Entry(frame_pos_list[iterator], width=12, textvariable=dane_o_posrednich2[int(iterator)][i]).place(
            x=75 + i * 80, y=40)


frame = Frame(root).place(x=2000, y=2000)
frame2 = Frame(root).place(x=2000, y=2000)

labels = []
labels2 = []
labels3 = []
labels4 = []
labels5 = []
labels6 = []
dane_o_stanowiskach = [[0] * 3 for i in range(100)]
for a in range(100):
    for b in range(3):
        dane_o_stanowiskach[a][b] = StringVar()
        if b == 2:
            dane_o_stanowiskach[a][2].set("0")
populate(main_frame)

# print(str(main_frame.winfo_width()) + " " + str(main_frame.winfo_vrootheight()))

ile_do_rp2 = StringVar()
reper2_nazwa = StringVar()
reper2_wys = StringVar()
fontStyle = tkFont.Font(size=12)


def posrednie(ile_na_osi):
    number = ile_na_osi.get()
    if number > 100:
        ile_na_osi.set("100")
    global frame
    global frame2
    global gdzie
    if frame:
        frame.destroy()
    if frame2:
        frame2.destroy()
    frame = Frame(main_frame)
    szerokosc_pojedynczego = 80
    frame.place(x=0, y=130, height=szerokosc_pojedynczego * number, width=425)

    del labels[:]
    del labels2[:]
    del labels3[:]
    del labels4[:]
    del labels5[:]
    del labels6[:]
    for a in range(int(ile_na_osi.get()), 100):
        dane_o_stanowiskach[a][2].set("0")
    for i in range(number):
        labels.append(
            Label(frame, text="NR " + str(i + 1) + ": ", font=fontStyle).place(x=30, y=20 + i * szerokosc_pojedynczego))
        labels.append(
            Label(frame, text="ilość stanowisk żeby dojść do niego:").place(x=100, y=0 + i * szerokosc_pojedynczego))
        labels3.append(Label(frame, text="wysokość:").place(x=100, y=20 + i * szerokosc_pojedynczego))

        labels5.append(Label(frame, text="liczba punktów pośrednich: ").place(x=100, y=40 + i * szerokosc_pojedynczego))
        labels2.append(
            Entry(frame, textvariable=dane_o_stanowiskach[i][0]).place(x=300, y=0 + i * szerokosc_pojedynczego))
        labels4.append(
            Entry(frame, textvariable=dane_o_stanowiskach[i][1]).place(x=300, y=20 + i * szerokosc_pojedynczego))

        dane_o_stanowiskach[i][2].trace("w",
                                        lambda name, index, mode, var=dane_o_stanowiskach[i][2], var2=i: punkty(var,
                                                                                                                var2))
        labels6.append(
            Entry(frame, textvariable=dane_o_stanowiskach[i][2]).place(x=300, y=40 + i * szerokosc_pojedynczego))
        canvas3 = Canvas(frame, width=500, height=10)
        canvas3.create_line(5, 5, 425, 5)
        canvas3.place(x=0, y=65 + szerokosc_pojedynczego * i)
    frame2 = Frame(main_frame)
    gdzie = 130 + 80 * number
    frame2.place(x=0, y=gdzie, height=500, width=500)

    labelNum8 = Label(frame2, text="ilość stanowisk żeby dojść do reperu nr 2:").place(x=0, y=0)
    labelNum9 = Label(frame2, text="Reper nr 2:").place(x=0, y=20)
    labelNum10 = Label(frame2, text="Wysokość reperu nr 2:").place(x=0, y=40)
    entryNum8 = Entry(frame2, textvariable=ile_do_rp2).place(x=250, y=0)
    entryNum9 = Entry(frame2, textvariable=reper2_nazwa).place(x=250, y=20)
    entryNum10 = Entry(frame2, textvariable=reper2_wys).place(x=250, y=40)

    btn_oblicz = Button(frame2, text="OBLICZ", command=lambda: obliczanie(gdzie)).place(x=10, y=65)

    def kontakt():
        top = Toplevel()
        top.iconbitmap('DN.ico')
        fontStyle = tkFont.Font(size=14)
        treść = "W razie pojawienia się jakichś problemów przy instalacji \n" \
                "czy działaniu programu proszę o kontakt mailowy. Proszę opisać \n" \
                "na czym polega problem i na jakim systemie operacyjnym wystąpił \n" \
                "(wersja, 32 czy 64 bit) oraz jaki zainstalowany był program antywirusowy. \n" \
                "Można ewentualnie załączyć jakieś printscreeny czy pliki .niw  \n" \
                "jeśli chodzi o obliczenia"
        treść2 = "Adres do kontaktu:\n Szymon Lepianka  \nslepianka@wp.pl "
        Label(top, text=treść).pack()
        Label(top, text=treść2, font=fontStyle).pack()
        btn2 = Button(top, text="Zamknij", command=top.destroy).pack()

    btn = Button(frame2, text="KONTAKT", command=kontakt).place(x=80, y=65)

    def instrukcja():
        top = Toplevel()
        top.iconbitmap('DN.ico')
        fontStyle = tkFont.Font(size=14)
        tytuł = "INSTRUKCJA:"
        Label(top, text=tytuł, font=fontStyle).pack()
        treść = "Program \"Dorabianie niwelacji\" służy do zautomatyzowania procesu tworzenia niwelacji technicznej. \n" \
                "Działanie programu było testowane przy wczytywaniu pliku stworzonego przez ten program do C-GEO. \n" \
                "Zalecane jest wskazanie ścieżki projektu w C-GEO za pomocą przycinku \"Wskaż ścieżkę\" (ułatwi \n" \
                "to później podczytanie pliku). Domyślnie plik zapisze się w tym samym miejscu na komputerze, \n" \
                "w którym znajduje się program \"Dorabianie niwelacji\". Wysokości (reperów, stanowisk, \n" \
                "punktów) należy wprowadzać w formie bez ',' oraz '.'. Ma być 6 cyfr! Przykład: 213450. \n"
        treść2 = "Adres do kontaktu:\n Szymon Lepianka  \nslepianka@wp.pl "
        Label(top, text=treść).pack()
        Label(top, text=treść2, font=fontStyle).pack()
        # my_img = ImageTk.PhotoImage(Image.open("zdjecie.jpg"))
        # my_label = Label(top, image=my_img).pack()
        btn2 = Button(top, text="Zamknij", command=top.destroy).pack()

    btn = Button(frame2, text="INSTRUKCJA", command=instrukcja).place(x=160, y=65)


def obliczanie(gdzie):
    global gdzie_zapisac, nazwa_reper1, wys_reper1, ile_na_osi, dane_o_stanowiskach, dane_o_posrednich1, dane_o_posrednich2, ile_do_rp2, reper2_nazwa, reper2_wys
    dane_o_posrednich1_final = []
    dane_o_posrednich2_final = []
    dane_o_stanowiskach_final = [[0] * 3 for i in range(ile_na_osi.get())]
    for a in range(ile_na_osi.get()):
        dane_o_posrednich1_final.append([0] * int(dane_o_stanowiskach[a][2].get()))
        dane_o_posrednich2_final.append([0] * int(dane_o_stanowiskach[a][2].get()))
    for a in range(ile_na_osi.get()):
        for b in range(int(dane_o_stanowiskach[a][2].get())):
            dane_o_posrednich1_final[a][b] = dane_o_posrednich1[a][b].get()
            dane_o_posrednich2_final[a][b] = dane_o_posrednich2[a][b].get()
    for a in range(ile_na_osi.get()):
        for b in range(3):
            dane_o_stanowiskach_final[a][b] = dane_o_stanowiskach[a][b].get()
    ni2.liczenie(gdzie_zapisac.get(), nazwa_reper1.get(), wys_reper1.get(), ile_na_osi.get(), dane_o_stanowiskach_final,
                 dane_o_posrednich1_final,
                 dane_o_posrednich2_final, ile_do_rp2.get(), reper2_nazwa.get(), reper2_wys.get())
    canvas3 = Canvas(main_frame, width=900, height=2000)
    max_wys = max(wys_reper1.get(), reper2_wys.get())
    min_wys = min(wys_reper1.get(), reper2_wys.get())
    for a in range(ile_na_osi.get()):
        max_wys = max(max_wys, dane_o_stanowiskach_final[a][1])
        min_wys = min(min_wys, dane_o_stanowiskach_final[a][1])
    zakres = int((int(max_wys) - int(min_wys)) / 5000)
    fontStyle = tkFont.Font(size=8)
    start = int(int(min_wys) / 5000) * 5000
    for i in range(zakres + 3):
        Label(canvas3, text=start + (zakres + 2) * 5000 - 5000 * i, font=fontStyle).place(x=5, y=10 + 100 * i)
        canvas3.create_line(5, 30 + 100 * i, 800, 30 + 100 * i)
        if i == zakres + 2:
            break
        for j in range(4):
            canvas3.create_line(5, 50 + 100 * i + j * 20, 800, 50 + 100 * i + 20 * j, dash=(5, 5))
    start = int(int(min_wys) / 5000) * 5000
    skok_x = int(800 / len(ni2.a_i_b))
    y1 = int(wys_reper1.get()) - start
    c = 0
    for i in range(len(ni2.a_i_b)):
        if i % 2 == 0:
            y2 = y1 + ni2.a_i_b[i]
        else:
            y2 = y1 - ni2.a_i_b[i]
        if ni2.a_b_r[i] == "a":
            canvas3.create_line(5 + skok_x * i, 30 + (zakres + 2) * 100 - int(y1 / 50), 5 + skok_x * (i + 1), 30 + (zakres + 2) * 100 - int(y2 / 50), fill="yellow")
        elif ni2.a_b_r[i] == "b":
            canvas3.create_line(5 + skok_x * i, 30 + (zakres + 2) * 100 - int(y1 / 50), 5 + skok_x * (i + 1), 30 + (zakres + 2) * 100 - int(y2 / 50), fill="red")
        elif ni2.a_b_r[i] == "r":
            canvas3.create_line(5 + skok_x * i, 30 + (zakres + 2) * 100 - int(y1 / 50), 5 + skok_x * (i + 1), 30 + (zakres + 2) * 100 - int(y2 / 50), fill="green")
            if c < ile_na_osi.get():
                canvas3.create_oval(skok_x * (i + 1),25 + (zakres + 2) * 100 - int((int(dane_o_stanowiskach_final[c][1]) - start) / 50), 10 + skok_x * (i + 1),
                                    35 + (zakres + 2) * 100 - int((int(dane_o_stanowiskach_final[c][1]) - start) / 50))
                c += 1
        else:
            canvas3.create_line(5 + skok_x * i, 30 + (zakres + 2) * 100 - int(y1 / 50), 5 + skok_x * (i + 1),30 + (zakres + 2) * 100 - int(y2 / 50))
        y1 = y2
    canvas3.place(x=0, y=gdzie + 100)
    ni2.a_i_b.clear()
    ni2.a_b_r.clear()


def open():
    global gdzie_zapisac
    ftypes = [('Niwelacja', '.niw'), ('All files', '*')]
    root.filename2 = filedialog.asksaveasfilename(filetypes=ftypes, initialdir=".", initialfile="niw1.niw",
                                                  defaultextension='.niw')
    gdzie_zapisac.set(root.filename2)


btn_wskaz_sciezke = Button(main_frame, text="Wskaż ścieżkę", command=open).place(x=600, y=0)

nazwa_reper1 = StringVar()
wys_reper1 = StringVar()
number7 = StringVar()
number8 = StringVar()
number9 = StringVar()
number10 = StringVar()

labelNum1 = Label(main_frame, text="Nazwa pliku do zapisu: ").place(x=0, y=0)
labelNum2 = Label(main_frame, text="Reper nr 1:").place(x=0, y=20)
labelNum3 = Label(main_frame, text="Wysokość reperu nr 1:").place(x=0, y=40)
labelNum6 = Label(main_frame, text="Ilość stanowisk potrzebnych do pomiaru punktów pośrednich:").place(x=0, y=60)
canvas1 = Canvas(main_frame, width=600, height=10)
canvas1.create_line(5, 5, 470, 5)
canvas1.place(x=0, y=80)
fontStyle = tkFont.Font(size=12)
labelNum6 = Label(main_frame, text="Stanowiska do pomiaru punktów pośrednich:", font=fontStyle).place(x=50, y=90)
canvas2 = Canvas(main_frame, width=500, height=10)
canvas2.create_line(5, 5, 425, 5)
canvas2.place(x=0, y=114)


def sciezka(gdzie_zapisac):
    global btn_wskaz_sciezke
    btn_wskaz_sciezke = Button(main_frame, text="Wskaż ścieżkę", command=open).place(x=600, y=0)


gdzie_zapisac = StringVar()
gdzie_zapisac.set("niw1.niw")
gdzie_zapisac.trace("w", lambda name, index, mode, gdzie_zapisac=gdzie_zapisac: sciezka(gdzie_zapisac))
entryNum1 = Entry(main_frame, textvariable=gdzie_zapisac, width=40).place(x=345, y=0)
entryNum2 = Entry(main_frame, textvariable=nazwa_reper1).place(x=345, y=20)
entryNum3 = Entry(main_frame, textvariable=wys_reper1).place(x=345, y=40)
ile_na_osi = IntVar()
ile_na_osi.set("1")
posrednie(ile_na_osi)
ile_na_osi.trace("w", lambda name, index, mode, ile_na_osi=ile_na_osi: posrednie(ile_na_osi))
entryNum6 = Entry(main_frame, textvariable=ile_na_osi).place(x=345, y=60)

root.mainloop()

import tkinter

main_window = tkinter.Tk()
def even_tekan():    
    label2 = tkinter.Label(main_window,text = 'Lanjutkan !')
    label2.pack()


label = tkinter.Label(main_window,text='Ini adalah : \n GUI pertama menggunakan \n Python')
tombol = tkinter.Button(main_window,text = 'Lanjutkan',command = even_tekan)

label.pack()
tombol.pack()

main_window.mainloop()
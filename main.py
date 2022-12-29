from qrcode import QRCode
from tkinter import *
from tkinter import ttk


win = Tk()
win.geometry('400x380')
win.title('QRCode')
win.config(bg = 'white')


var_version = StringVar()
var_box_size = StringVar()
var_border = StringVar()
var_data = StringVar()
var_name = StringVar()


def fun_create():
    qr = QRCode(version = var_version.get(), box_size = var_box_size.get(), border = var_border.get())


    data = var_data.get()
    qr.add_data(data)

    qr.make(fit = True)
    img = qr.make_image(fill = 'black', back_color = str(combo_color.get()))

    if var_name.get() == '':
        img.save('QRCode.png')
    else:
        img.save(str(var_name.get())+'.png')



lb_data = Label(text = 'Data:', fg = 'red', bg = 'white').pack()
input_data = ttk.Entry(textvariable = var_data, width = 45).pack()

lb_name = Label(text = 'Name:', fg = 'red', bg = 'white').pack()
input_name = ttk.Entry(textvariable = var_name, width = 30).pack()



lb_version = Label(text = 'Complicity:', fg = 'red', bg = 'white').pack()
slider_version = Scale(variable = var_version, from_ = 1, to = 50, orient = HORIZONTAL).pack()

lb_box_size = Label(text = 'Size:', fg = 'red', bg = 'white').pack()
slider_box_size = Scale(variable = var_box_size, from_ = 1, to = 50, orient = HORIZONTAL).pack()

lb_border = Label(text = 'Border Size:', fg = 'red', bg = 'white').pack()
slider_border = Scale(variable = var_border, from_ = 1, to = 50, orient = HORIZONTAL).pack()



lb_background_color = Label(text = 'Background Color', fg = 'red', bg = 'white').pack()
combo_color = ttk.Combobox(values = ['white', 'red', 'blue', 'yellow', 'green', 'pink'])
combo_color.current(0)
combo_color.pack()


bt_create = ttk.Button(text = 'Create!', command = fun_create).pack()



win.mainloop()
from tkinter import *
from tkinter import messagebox

toolbox = {'Heading': 'h1',
           'Subheading': 'h2',
           'Body': 'b'
           }

components = {}


def add_menu():
    title_var = StringVar()

    def create():
        if add_list.curselection():
            tmp_title = title_var.get()
            tmp_num = 1
            selected = add_list.get(add_list.curselection()[0])
            tmp = {'type': selected, 'content': content.get(1.0, 'end-1c')}
            print(selected)
            # tmp['type'] = selected
            # tmp['content'] = content.get(1.0, 'end-1c')
            print(tmp)
            if tmp_title in components:
                while tmp_title + ' ' + str(tmp_num) in components:
                    tmp_num += 1
                tmp_title = tmp_title + ' ' + str(tmp_num)
            components[tmp_title] = tmp
            print(components)
            overview.insert(END, tmp_title)
            menu.destroy()
            menu.update()

    menu = Toplevel()
    menu.title('Add menu')
    add_list = Listbox(menu)
    for x in range(0, len(toolbox)):
        add_list.insert(END, list(toolbox.keys())[x])
    add_list.grid(row=0, column=1)
    Entry(menu, width=20, textvariable=title_var).grid(row=0, column=0, sticky=N)
    title_var.set('Component name')
    content = Text(menu, height=9, width=20)
    content.insert(END, 'Put text here')
    content.grid(row=0, column=0, sticky=S)
    continue_button = Button(menu, text='Create', command=create)
    continue_button.grid(row=2, column=1, sticky=SE)


def delcomponent():
    if overview.curselection():
        components.pop(overview.get(overview.curselection()))
        components.keys()
        components.update()
        overview.delete(overview.curselection())
        print(components)


def edit_menu():
    if overview.curselection():
        title_var = StringVar()
        type_var = StringVar()
        editing = overview.get(overview.curselection()[0])

        def save_component():
            tmp = {'content': content.get(1.0, 'end-1c')}
            components[overview.get(overview.curselection()[0])] = tmp
            print(components)
            menu.destroy()
            menu.update()

        print(editing)
        menu = Toplevel()
        menu.title('Edit menu')
        Entry(menu, width=20, textvariable=title_var, state=DISABLED).grid(row=0, column=0, sticky=N)
        title_var.set(editing)
        Entry(menu, width=20, textvariable=type_var, state=DISABLED).grid(row=0, column=1)
        type_var.set(components[editing]['type'])
        content = Text(menu, height=9, width=20)
        content.insert(END, components[editing]['content'])
        content.grid(row=1, column=0, sticky=S)
        continue_button = Button(menu, text='Create', command=save_component)
        continue_button.grid(row=2, column=1, sticky=SE)


def export():
    if messagebox.askokcancel('Continue?', 'This will wipe index.html and write the current site to it!'):
        generate()
        f = open('index.html', 'w')
        f.write(generated)
        f.close()
        messagebox.showinfo('Success', 'Export complete')
    else:
        messagebox.showinfo('Canceled', 'Export was cancelled')


def generate():
    global generated
    generated = '<!DOCTYPE html>\n<html>\n<head></head>\n<body>\n'
    for x in range(0, len(components)):
        tmp = components[list(components)[x]]
        print('lol')
        generated = generated + '<' + toolbox[tmp['type']] + '>' + tmp['content'] + '</' + toolbox[tmp['type']] + '>\n'
    generated = generated + '</body>\n</html>'
    print(generated)


r = Tk()
r.title('Website Builder')
addButton = Button(r, text='+', command=add_menu, width=4) \
    .grid(row=0, column=0, sticky=W)  # Button for adding components
remButton = Button(r, text='-', command=delcomponent, width=4) \
    .grid(row=0, column=0, sticky='')  # Button for removing components
detButton = Button(r, text='>', command=edit_menu, width=4) \
    .grid(row=0, column=0, sticky=E)
overview = Listbox(r)
overview.grid(row=1, column=0)  # Listbox overview of all components
export_button = Button(r, text='Export', command=export, state=NORMAL).grid(row=2, column=1, sticky=E)
r.mainloop()

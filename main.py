import customtkinter as ctk

def main():
    ctk.set_appearance_mode('System')
    ctk.set_default_color_theme('blue')

    root = ctk.CTk()
    root.title('Modern CustomTkinter GUI')
    root.geometry('400x300')

    label = ctk.CTkLabel(root, text='Hello World from CustomTkinter & UV!', font=('Arial', 16))
    label.pack(pady=60)

    button = ctk.CTkButton(root, text='Close Window', command=root.destroy)
    button.pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()

from turtledemo.sorting_animate import show_text

import customtkinter as ctk

# Configuração aparência
ctk.set_appearance_mode('dark')

# Criação das funções de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'piter' and senha == '123456':
        resultado_login.configure(text='Login Sucessful!', text_color='green')
    else:
        resultado_login.configure(text='Login Failed!', text_color='red')

# Criação da Janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

# Criação dos campos
label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)

# Iniciar a aplicação
app.mainloop()

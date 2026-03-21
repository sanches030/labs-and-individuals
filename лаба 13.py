import tkinter as tk
from tkinter import messagebox

def check_readiness():
    obj_type = obj_type_var.get()
    condition = condition_var.get()
    documents = documents_var.get()
    is_urgent = urgent_var.get()

    if not obj_type or not condition or not documents:
        messagebox.showwarning("Не всі дані", "Будь ласка, заповніть усі параметри.")
        return
    ready = True
    issues = []
    if condition == "bad":
        ready = False
        issues.append("потребує ремонту")
    elif condition == "average":
        issues.append("бажано освіжити вигляд")
    if documents == "partial":
        ready = False
        issues.append("неповний пакет документів")
    elif documents == "none":
        ready = False
        issues.append("документи відсутні")

    result = f"Об'єкт: {obj_type}\n"
    if ready:
        result += "✅ Стан та документи в порядку.\n"
        if is_urgent:
            result += "⚠️ Терміново! Можна показувати вже зараз."
        else:
            result += "Рекомендується запланувати показ."
    else:
        result += "❌ До показу не готовий.\nПроблеми:\n• " + "\n• ".join(issues) + "\n"
        if is_urgent:
            result += "Терміново виправте вказані недоліки перед показом!"
        else:
            result += "Виправте недоліки та призначте показ."

    result_label.config(text=result)
# Головне вікно
root = tk.Tk()
root.title("Рієлторський помічник")
root.geometry("500x580")
root.configure(bg="#FDF8F0")  

header_bg = "#2C3E5C"      
frame_bg = "#F5F0E6"        
button_bg = "#E67E22"  
button_fg = "#FFFFFF"
result_bg = "#FFFFFF"        

# Стилі шрифтів
title_font = ("Segoe UI", 13, "bold")
label_font = ("Segoe UI", 10)
result_font = ("Segoe UI", 10)

# Заголовок
header = tk.Label(root, text="Помічник оцінки готовності об'єкта",
                  font=("Segoe UI", 14, "bold"), bg="#FDF8F0", fg=header_bg)
header.pack(pady=15)

type_frame = tk.LabelFrame(root, text="Тип об'єкта", font=title_font,
                           bg=frame_bg, fg=header_bg, padx=10, pady=5)
type_frame.pack(pady=5, padx=20, fill="x")

obj_type_var = tk.StringVar(value="")
types = [("Квартира", "квартира"), ("Будинок", "будинок"), ("Комерція", "комерційне приміщення")]
for text, val in types:
    tk.Radiobutton(type_frame, text=text, variable=obj_type_var, value=val,
                   bg=frame_bg, font=label_font).pack(anchor="w", pady=2)

condition_frame = tk.LabelFrame(root, text="Стан об'єкта", font=title_font,
                                bg=frame_bg, fg=header_bg, padx=10, pady=5)
condition_frame.pack(pady=5, padx=20, fill="x")

condition_var = tk.StringVar(value="")
conditions = [("Відмінний (після ремонту)", "good"),
              ("Задовільний (косметичний ремонт)", "average"),
              ("Потребує ремонту", "bad")]
for text, val in conditions:
    tk.Radiobutton(condition_frame, text=text, variable=condition_var, value=val,
                   bg=frame_bg, font=label_font).pack(anchor="w", pady=2)

docs_frame = tk.LabelFrame(root, text="Документи", font=title_font,
                           bg=frame_bg, fg=header_bg, padx=10, pady=5)
docs_frame.pack(pady=5, padx=20, fill="x")

documents_var = tk.StringVar(value="")
docs = [("Повний пакет", "full"),
        ("Частково (є ризики)", "partial"),
        ("Відсутні", "none")]
for text, val in docs:
    tk.Radiobutton(docs_frame, text=text, variable=documents_var, value=val,
                   bg=frame_bg, font=label_font).pack(anchor="w", pady=2)
urgent_var = tk.BooleanVar()
urgent_check = tk.Checkbutton(root, text="Терміновий показ (клієнт чекає)", variable=urgent_var,
                              bg="#FDF8F0", font=label_font)
urgent_check.pack(pady=10)
check_btn = tk.Button(root, text="Оцінити готовність", command=check_readiness,
                      bg=button_bg, fg=button_fg, font=("Segoe UI", 10, "bold"),
                      relief="flat", padx=15, pady=5, cursor="hand2", bd=0)
check_btn.pack(pady=10)
result_label = tk.Label(root, text="", font=result_font, bg=result_bg, fg="#2C3E5C",
                        justify="left", wraplength=450, relief="solid", bd=1,
                        padx=10, pady=10)
result_label.pack(pady=15, padx=20, fill="both", expand=True)

root.mainloop()
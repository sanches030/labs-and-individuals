import tkinter as tk
from tkinter import messagebox, Spinbox

def calculate_mortgage():
    try:
        loan_amount = float(loan_entry.get().strip())
        if loan_amount <= 0: raise ValueError
        years = int(years_spin.get())
        if years <= 0: raise ValueError
        annual_rate = rate_scale.get() / 100.0
        exchange_rate = exchange_scale.get()
        if exchange_rate <= 0: raise ValueError
    except:
        messagebox.showerror("Помилка", "Введіть коректні дані")
        return

    months = years * 12
    monthly_rate = annual_rate / 12
    fixed_principal = loan_amount / months

    balance = loan_amount
    total_interest = 0
    payments = [] 

    for month in range(1, months + 1):
        interest = balance * monthly_rate
        payment = fixed_principal + interest
        if month == months:
            principal = balance
            payment = balance + interest
        else:
            principal = fixed_principal
        balance -= principal
        payments.append((payment, interest, principal, balance))
        total_interest += interest

    total_paid = loan_amount + total_interest
    first_payment = payments[0][0]

    result_main.config(
        text=f" Сума кредиту: {loan_amount:.2f} USD\n"
             f" Тіло кредиту: {fixed_principal:.2f} USD (не змінюється)\n"
             f" Загальна переплата (відсотки): {total_interest:.2f} USD\n"
             f" Всього: {total_paid:.2f} USD"
    )

    global payment_data
    payment_data = {
        "payments": payments,
        "months": months,
        "exchange_rate": exchange_rate,
        "fixed_principal": fixed_principal
    }
    month_scale.config(to=months, state="normal")
    month_scale.set(1)
    update_month_info()

def update_month_info(*args):
    if not payment_data:
        return
    try:
        month = int(month_scale.get())
        if month < 1 or month > payment_data["months"]:
            return
        payment, interest, principal, balance = payment_data["payments"][month-1]
        exchange = payment_data["exchange_rate"]
        fixed_principal = payment_data["fixed_principal"]
        result_month.config(
            text=f"Місяць {month}:\n"
                 f" Тіло кредиту: {fixed_principal:.2f} USD / {fixed_principal*exchange:.2f} UAH\n"
                 f" Відсотки за місяць: {interest:.2f} USD / {interest*exchange:.2f} UAH\n"
                 f" Загальний щомісячний платіж: {payment:.2f} USD / {payment*exchange:.2f} UAH\n"
                 f" Залишок: {balance:.2f} USD / {balance*exchange:.2f} UAH"
        )
        month_value_label.config(text=f"Місяць {month}")
    except:
        pass

# Головне вікно
root = tk.Tk()
root.title("Іпотечний калькулятор")
root.configure(bg="#FDF8F0")
root.minsize(550, 720)

header_bg = "#2C3E5C"
frame_bg = "#F5F0E6"
button_bg = "#E67E22"
button_fg = "#FFFFFF"
result_bg = "#FFFFFF"

tk.Label(root, text="Калькулятор іпотеки",
         font=("Segoe UI", 12, "bold"), bg="#FDF8F0", fg=header_bg).pack(pady=15)

frame_loan = tk.Frame(root, bg=frame_bg, relief="groove", bd=1, padx=10, pady=5)
frame_loan.pack(pady=5, padx=20, fill="x")
tk.Label(frame_loan, text="Сума кредиту USD:", font=("Segoe UI",10), bg=frame_bg).pack(anchor="w")
loan_entry = tk.Entry(frame_loan, font=("Segoe UI",10), width=20)
loan_entry.insert(0, "") 
loan_entry.pack(anchor="w", pady=2)

frame_years = tk.Frame(root, bg=frame_bg, relief="groove", bd=1, padx=10, pady=5)
frame_years.pack(pady=5, padx=20, fill="x")
tk.Label(frame_years, text="Термін (років):", font=("Segoe UI",10), bg=frame_bg).pack(anchor="w")
years_spin = Spinbox(frame_years, from_=0, to=30, font=("Segoe UI",10), width=10)
years_spin.delete(0, tk.END)
years_spin.insert(0, "0") 
years_spin.pack(anchor="w", pady=2)

frame_rate = tk.Frame(root, bg=frame_bg, relief="groove", bd=1, padx=10, pady=5)
frame_rate.pack(pady=5, padx=20, fill="x")
tk.Label(frame_rate, text="Річна відсоткова ставка (%):", font=("Segoe UI",10), bg=frame_bg).pack(anchor="w")
rate_scale = tk.Scale(frame_rate, from_=0, to=30, orient="horizontal", length=300, tickinterval=5, resolution=0.1, bg=frame_bg)
rate_scale.set(0)  # нуль
rate_scale.pack(fill="x", pady=2)

frame_exch = tk.Frame(root, bg=frame_bg, relief="groove", bd=1, padx=10, pady=5)
frame_exch.pack(pady=5, padx=20, fill="x")
tk.Label(frame_exch, text="Курс USD/UAH:", font=("Segoe UI",10), bg=frame_bg).pack(anchor="w")
exchange_scale = tk.Scale(frame_exch, from_=0, to=50, orient="horizontal", length=300, tickinterval=5, resolution=0.5, bg=frame_bg)
exchange_scale.set(0)  
exchange_scale.pack(fill="x", pady=2)

btn_calc = tk.Button(root, text="Розрахувати", command=calculate_mortgage, bg=button_bg, fg=button_fg, font=("Segoe UI",10,"bold"), relief="flat", padx=15, pady=5)
btn_calc.pack(pady=10)

result_main = tk.Label(root, text="", font=("Segoe UI",10), bg=result_bg, justify="left", wraplength=500, relief="solid", bd=1, padx=10, pady=10)
result_main.pack(pady=10, padx=20, fill="x")

frame_month = tk.Frame(root, bg=frame_bg, relief="groove", bd=1, padx=10, pady=5)
frame_month.pack(pady=5, padx=20, fill="x")
tk.Label(frame_month, text="Щомісячний платіж:", font=("Segoe UI",10), bg=frame_bg).pack(anchor="w")
month_control = tk.Frame(frame_month, bg=frame_bg)
month_control.pack(fill="x", pady=2)
month_scale = tk.Scale(month_control, from_=1, to=12, orient="horizontal", length=300, tickinterval=0, resolution=1, bg=frame_bg, state="disabled")
month_scale.pack(side="left", fill="x", expand=True)
month_value_label = tk.Label(month_control, text="Місяць 1", width=15, bg=frame_bg)
month_value_label.pack(side="right", padx=5)
month_scale.configure(command=lambda x: update_month_info())

result_month = tk.Label(root, text="", font=("Segoe UI",10), bg=result_bg, justify="left", wraplength=500, relief="solid", bd=1, padx=10, pady=10)
result_month.pack(pady=10, padx=20, fill="x")
payment_data = {}
root.mainloop()
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from .parser import Parser
from .interpreter import Interpreter


def create_editor():
    def run_code():
        code = text_area.get("1.0", tk.END).strip()
        try:
            parsed_code = Parser.parse(code)
            interpreter = Interpreter()
            result = interpreter.execute(parsed_code)
            output_area.config(state=tk.NORMAL)
            output_area.delete("1.0", tk.END)
            output_area.insert(tk.END, result)
            output_area.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"Execution failed: {e}")

    def clear_code():
        text_area.delete("1.0", tk.END)

    def clear_output():
        output_area.config(state=tk.NORMAL)
        output_area.delete("1.0", tk.END)
        output_area.config(state=tk.DISABLED)

    def save_code():
        content = text_area.get("1.0", tk.END).strip()
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def load_code():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                text_area.delete("1.0", tk.END)
                text_area.insert("1.0", content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    root = tk.Tk()
    root.title("Custom Language Editor")

    # Меню
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=load_code)
    file_menu.add_command(label="Save", command=save_code)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menu_bar)

    # Поле для ввода кода
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
    text_area.pack(padx=10, pady=10)

    # Кнопки управления
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    run_button = tk.Button(button_frame, text="Run", command=run_code)
    run_button.grid(row=0, column=0, padx=5)

    clear_code_button = tk.Button(button_frame, text="Clear Code", command=clear_code)
    clear_code_button.grid(row=0, column=1, padx=5)

    clear_output_button = tk.Button(button_frame, text="Clear Output", command=clear_output)
    clear_output_button.grid(row=0, column=2, padx=5)

    # Поле для вывода результата
    output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, state=tk.DISABLED)
    output_area.pack(padx=10, pady=10)

    root.mainloop()

import tkinter as tk
import customtkinter as ctk
from tkinter import simpledialog, messagebox
import threading

# @author quantam
# @date 2024-05-30

def brainfuck_interpreter(code, input_callback):
    """
    Interprets and executes Brainfuck code.
    """
    code = ''.join(filter(lambda x: x in ['<', '>', '+', '-', '.', ',', '[', ']'], code))
    tape = [0] * 30000
    ptr = 0
    code_ptr = 0
    output = ''
    loop_stack = []

    while code_ptr < len(code):
        command = code[code_ptr]
        if command == '>':
            ptr += 1
        elif command == '<':
            ptr -= 1
        elif command == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif command == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif command == '.':
            output += chr(tape[ptr])
        elif command == ',':
            user_input = input_callback()
            if user_input:
                tape[ptr] = ord(user_input[0]) % 256
        elif command == '[':
            if tape[ptr] == 0:
                open_brackets = 1
                while open_brackets:
                    code_ptr += 1
                    if code[code_ptr] == '[':
                        open_brackets += 1
                    elif code[code_ptr] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(code_ptr)
        elif command == ']':
            if tape[ptr] != 0:
                code_ptr = loop_stack[-1]
            else:
                loop_stack.pop()

        code_ptr += 1

    return output

def run_brainfuck():
    """
    Retrieves the code from the text editor, runs it in a separate thread, and displays the output.
    """
    code = text_editor.get("1.0", tk.END).strip()
    threading.Thread(target=execute_brainfuck, args=(code,)).start()

def execute_brainfuck(code):
    """
    Executes the Brainfuck code and updates the output display.
    """
    try:
        output = brainfuck_interpreter(code, get_user_input)
        output_display.delete("1.0", tk.END)
        output_display.insert(tk.END, output)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def get_user_input():
    """
    Prompts the user to enter a single character for the Brainfuck ',' command.
    """
    return simpledialog.askstring("Input", "Enter a single character:")

def show_author_info():
    """
    Displays the author information.
    """
    messagebox.showinfo("Author Info", "Brainfuck Compiler & IDE\nAuthor: quantam\nContact: quantamphysic [on Discord]")

def setup_ui(root):
    """
    Sets up the UI components.
    """
    global text_editor, output_display

    # Configure root window
    root.title("Brainfuck Compiler | v1.0 | @quantam")
    root.geometry("800x600")
    root.resizable(False, False)
    root.iconbitmap("assets/bfuck.ico")  # Set the app icon

    # Text editor for Brainfuck code
    text_editor = ctk.CTkTextbox(root, width=780, height=300)
    text_editor.pack(pady=20)

    # Placeholder text
    placeholder_text = "Enter your Brainfuck code here..."
    text_editor.insert("1.0", placeholder_text)
    text_editor.bind("<FocusIn>", lambda event: on_focus_in(event, placeholder_text))
    text_editor.bind("<FocusOut>", lambda event: on_focus_out(event, placeholder_text))

    # Frame for buttons
    button_frame = ctk.CTkFrame(root)
    button_frame.pack(pady=10)

    # Run button
    run_button = ctk.CTkButton(button_frame, text="Run", command=run_brainfuck)
    run_button.pack(side=tk.LEFT, padx=10)

    # Info button
    info_button = ctk.CTkButton(button_frame, text="i", width=30, command=show_author_info)
    info_button.pack(side=tk.LEFT, padx=10)

    # Output display
    output_display = ctk.CTkTextbox(root, width=780, height=200)
    output_display.pack(pady=20)

def on_focus_in(event, placeholder_text):
    """
    Clears the placeholder text when the text editor gains focus.
    """
    if text_editor.get("1.0", tk.END).strip() == placeholder_text:
        text_editor.delete("1.0", tk.END)
        text_editor.config(fg="black")

def on_focus_out(event, placeholder_text):
    """
    Restores the placeholder text if the text editor is empty when it loses focus.
    """
    if not text_editor.get("1.0", tk.END).strip():
        text_editor.insert("1.0", placeholder_text)
        text_editor.config(fg="gray")

if __name__ == "__main__":
    app = ctk.CTk()
    setup_ui(app)
    app.mainloop()

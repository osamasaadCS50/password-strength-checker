import re
import tkinter as tk
from tkinter import messagebox, ttk
import secrets
import string

def check_password_strength(password):
    """Check the strength of a password based on defined criteria."""
    score = 0
    feedback = []

    # Criterion 1: Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Criterion 2: Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Criterion 3: Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Criterion 4: Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Criterion 5: Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

def generate_strong_password(length=12):
    """Generate a strong random password using secrets module."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def on_check_password():
    """Handle the password check button click."""
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, feedback = check_password_strength(password)
    result_text = f"Password Strength: {strength}\n\nFeedback:\n"
    result_text += "\n".join(f"- {item}" for item in feedback) if feedback else "Perfect! Your password meets all criteria."
    label_result.config(text=result_text)

def on_generate_password():
    """Generate and display a strong password."""
    new_password = generate_strong_password()
    entry_password.delete(0, tk.END)
    entry_password.insert(0, new_password)
    label_result.config(text="Generated a strong password. Click 'Check Password' to evaluate.")

def toggle_password_visibility():
    """Toggle password visibility based on checkbox state."""
    if show_password_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

# Create GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x400")  # Adjusted for desktop screens
root.configure(bg="#f0f0f0")  # Light gray background

# Style configuration
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
style.configure("TCheckbutton", font=("Helvetica", 10), background="#f0f0f0")

# Main frame for better organization
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Password Entry
ttk.Label(main_frame, text="Enter Password:").grid(row=0, column=0, sticky=tk.W, pady=10)
entry_password = ttk.Entry(main_frame, show="*", width=40, font=("Helvetica", 12))
entry_password.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=10)

# Show Password Checkbox
show_password_var = tk.BooleanVar()
ttk.Checkbutton(main_frame, text="Show Password", variable=show_password_var, command=toggle_password_visibility).grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=5)

# Buttons
ttk.Button(main_frame, text="Check Password", command=on_check_password).grid(row=2, column=0, columnspan=2, pady=10)
ttk.Button(main_frame, text="Generate Strong Password", command=on_generate_password).grid(row=3, column=0, columnspan=2, pady=10)

# Result Label
label_result = ttk.Label(main_frame, text="", wraplength=500, justify="left", font=("Helvetica", 11))
label_result.grid(row=4, column=0, columnspan=2, pady=20)

# Configure grid weights for responsiveness
main_frame.columnconfigure(1, weight=1)

# Start the GUI
root.mainloop()
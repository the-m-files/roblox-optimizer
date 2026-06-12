import tkinter as tk
from tkinter import ttk

# -----------------------------
# Window Setup
# -----------------------------
root = tk.Tk()
root.title("Roblox Performance Analyzer v2.4")
root.geometry("550x250")
root.resizable(False, False)

# -----------------------------
# User Input Screen
# -----------------------------
title = tk.Label(
    root,
    text="Roblox Performance Analyzer v2.4",
    font=("Segoe UI", 14, "bold"),
    anchor="w",
    justify="left"
)
title.pack(fill="x", padx=15, pady=(10, 5))

form_frame = tk.Frame(root)
form_frame.pack(fill="x", padx=15)

# Nickname row
name_row = tk.Frame(form_frame)
name_row.pack(fill="x", pady=5)

tk.Label(name_row, text="Nickname:", width=15, anchor="w").pack(side="left")
name_entry = tk.Entry(name_row, width=30)
name_entry.pack(side="left", fill="x", expand=True)

# Age row
age_row = tk.Frame(form_frame)
age_row.pack(fill="x", pady=5)

tk.Label(age_row, text="Age:", width=15, anchor="w").pack(side="left")
age_entry = tk.Entry(age_row, width=10)
age_entry.pack(side="left")

info = tk.Label(
    root,
    text="This analysis may take several minutes.",
    anchor="w",
    justify="left"
)
info.pack(fill="x", padx=15, pady=(10, 10))

start_button = tk.Button(
    root,
    text="Begin Analysis",
    width=20
)
start_button.pack(anchor="w", padx=15)
# -----------------------------
# Analysis Screen
# -----------------------------
status_label = tk.Label(root, text="", font=("Consolas", 10))
progress = ttk.Progressbar(root, length=500, mode="determinate")

messages = [
    "Verifying Roblox installation...",
    "Checking graphics settings...",
    "Testing network latency...",
    "Measuring frame consistency...",
    "Benchmarking hardware...",
    "Analyzing cache usage...",
    "Reviewing performance profile...",
    "Counting pixels...",
    "Re-counting pixels...",
    "Pixel count discrepancy detected...",
    "Resolving pixel dispute...",
    "Pixel dispute resolved peacefully...",
    "Testing avatar integrity...",
    "Avatar appears intact...",
    "Measuring grass exposure...",
    "WARNING: Grass exposure below recommended levels...",
    "Compensating...",
    "Detecting gamer posture...",
    "Detecting gamer posture again because we didn't believe it...",
    "Contacting optimization servers...",
    "Optimization servers confused...",
    "Running advanced AI analysis...",
    "AI requested a break...",
    "Break approved...",
    "AI has returned...",
    "Consulting highly trained hamster...",
    "Hamster approved recommendations...",
    "Consulting backup hamster...",
    "Backup hamster agrees...",
    "Cross-referencing Roblox statistics...",
    "Cross-referencing snack consumption...",
    "Cross-referencing gravitational alignment...",
    "Checking if user has touched grass recently...",
    "Search returned no results...",
    "Generating report..."
]

index = 0
user_name = ""
user_age = ""

# -----------------------------
# Final Report
# -----------------------------
def show_report():
    root.geometry("900x700")

    for widget in root.winfo_children():
        widget.destroy()

    report = f"""
═══════════════════════════════════════════════════════════════
ROBLOX PERFORMANCE ANALYSIS REPORT
═══════════════════════════════════════════════════════════════

SUBJECT INFORMATION

Name:
{user_name}

Age:
{user_age}

Analysis Duration:
9 Minutes 27 Seconds

═══════════════════════════════════════════════════════════════

SYSTEM STATUS

CPU ................ PASS
GPU ................ PASS
RAM ................ PASS
Internet ........... QUESTIONABLE
Chair .............. PASS

═══════════════════════════════════════════════════════════════

PLAYER PROFILE

Curiosity .......... EXTREMELY HIGH
Patience ........... SURPRISINGLY HIGH
Decision Making .... UNDER REVIEW

═══════════════════════════════════════════════════════════════

ADVANCED ROBLOX METRICS

Estimated Oofs:
12,487

Estimated "One More Round":
734

Estimated Avatar Adjustments:
4,391

Estimated Hours Looking At Skins:
CLASSIFIED

═══════════════════════════════════════════════════════════════

GRASS EXPOSURE REPORT

Current Exposure:
0.02%

Recommended Exposure:
Literally Any Amount

Status:
CRITICAL

═══════════════════════════════════════════════════════════════

BEHAVIORAL FINDINGS

• Clicked every button presented.

• Waited through every loading screen.

• Followed every instruction.

• Questioned absolutely nothing.

═══════════════════════════════════════════════════════════════

OFFICIAL CLASSIFICATION

ELITE PROFESSIONAL OOF ENGINEER

═══════════════════════════════════════════════════════════════

FINAL CONCLUSION

Your computer was already fine.

The optimization was never real.

We simply wanted to determine
how far you would go.

The answer:

Way farther than expected.

Thank you for participating in the
2026 International Patience Study.

Your results have been forwarded to:

✓ NASA
✓ Grandma

Grandma was the most concerned.
"""

    text = tk.Text(root, font=("Consolas", 11))
    text.pack(fill="both", expand=True)

    text.insert("1.0", report)
    text.config(state="disabled")


# -----------------------------
# Fake 99% Delay
# -----------------------------
def fake_99_sequence():
    sequence = [
        "99% - Generating report...",
        "99% - Double-checking report...",
        "99% - Triple-checking report...",
        "99% - Removing unnecessary professionalism...",
        "99% - Re-adding professionalism...",
        "99% - Verifying hamster approval..."
    ]

    def step(i):
        if i < len(sequence):
            status_label.config(text=sequence[i])
            root.after(2500, lambda: step(i + 1))
        else:
            progress["value"] = 100
            show_report()

    step(0)


# -----------------------------
# Analysis Progress
# -----------------------------
def update_analysis():
    global index

    if index < len(messages):
        status_label.config(text=messages[index])

        value = (index + 1) / len(messages) * 98
        progress["value"] = value

        index += 1
        root.after(1400, update_analysis)

    else:
        fake_99_sequence()


# -----------------------------
# Start Button
# -----------------------------
def start_analysis():
    global user_name, user_age

    user_name = name_entry.get().strip() or "Unknown Subject"
    user_age = age_entry.get().strip() or "Classified"

    title.pack_forget()
    form_frame.pack_forget()   # <-- THIS FIXES BOTH NAME + AGE ROWS
    info.pack_forget()
    start_button.pack_forget()

    status_label.pack(pady=15)
    progress.pack(pady=10)

    update_analysis()

start_button.config(command=start_analysis)

root.mainloop()

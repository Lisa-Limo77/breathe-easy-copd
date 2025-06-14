import tkinter as tk

def draw_lungs_tk(risk_score):
    root = tk.Tk()
    root.title("Breathe-Easy: Lung Visualization")
    root.geometry("400x400")
    root.configure(bg="lightblue")

    canvas = tk.Canvas(root, width=400, height=400, bg="lightblue")
    canvas.pack()

    if risk_score <= 1:
        lung_color = "lightgreen"
    elif risk_score == 2:
        lung_color = "yellow"
    else:
        lung_color = "red"

    canvas.create_oval(100, 150, 180, 300, fill=lung_color, outline="black")
    canvas.create_oval(220, 150, 300, 300, fill=lung_color, outline="black")
    canvas.create_rectangle(185, 80, 215, 150, fill="gray", outline="black")
    canvas.create_text(200, 350, text="Close window to exit", font=("Arial", 14))

    root.mainloop()

# For testing alone:
if __name__ == "__main__":
    draw_lungs_tk(1)  # change number to test colors

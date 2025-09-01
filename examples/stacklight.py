import tkinter as tk
import tk_tools

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("StackLight Example")

    sl = tk_tools.StackLight(root, colors=("red", "yellow", "green","orange"),width=20,height=60)
    sl.pack(padx=20, pady=20)

    # Demo cycle
    def demo():
        sl.set_state("red", "on")
        root.after(1000, lambda: sl.set_state("yellow", "blink"))
        root.after(3000, lambda: sl.set_state("green", "on"))
        root.after(5000, lambda: sl.set_state("red", "off"))
        root.after(7000, lambda: sl.set_state("yellow", "off"))
        root.after(9000, lambda: sl.set_state("green", "off"))

    root.after(1000, demo)
    root.mainloop()

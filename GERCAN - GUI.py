import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

class WorldClockApp:
    def __init__(self, master):
        self.master = master
        self.master.title("World Clock")
                
        self.country_label = ttk.Label(master, text="Select a country:")
        self.country_label.pack(padx=20, pady=5)

        self.country_combo = ttk.Combobox(master, values=["United States", "United Kingdom"])
        self.country_combo.pack(padx=20, pady=5)
        self.country_combo.set("Philippines")
        self.country_combo.bind("<<ComboboxSelected>>", self.update_time)

        self.label = tk.Label(master, font=('Helvetica', 8))
        self.label.pack(padx=20, pady=20)

        self.update_time()

    def update_time(self, event=None):
        current_time = datetime.now()
        time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

        # Get the selected country
        selected_country = self.country_combo.get()

        # Display time for different time zones based on the selected country
        if selected_country == "United States":
            local_timezone = pytz.timezone('America/New_York')
        elif selected_country == "United Kingdom":
            local_timezone = pytz.timezone('Europe/London')
        else:
            local_timezone = pytz.timezone('Asia/Manila')  # Default to Philippines if country not found

        local_time = pytz.utc.localize(current_time).astimezone(local_timezone)

        time_display = f"Local Time ({selected_country}): {local_time.strftime('%Y-%m-%d %H:%M:%S')}"

        self.label.config(text=time_display)
        self.master.after(1000, self.update_time)

def main():
    root = tk.Tk()
    app = WorldClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

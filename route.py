import tkinter as tk
from tkinter import messagebox


# Dummy function to simulate fetching flight routes
def get_flight_routes(source, destination):
    # Here you would typically fetch data from an API
    # For simplicity, let's just return a stIatic list
    return [("LHE", "Jakarta"),("Peshawar", "Chicago"), ("ISB", "New York"), ("KHI", "Sydney"),("KHI", "Dubai"),("LHR", "Washington")]


def find_routes():
    source = entry_source.get()
    destination = entry_destination.get()

    if not source or not destination:
        messagebox.showerror("Error", "Please enter source and destination airports.")
        return

    routes = get_flight_routes(source, destination)

    if routes:
        route_str = "\n".join([f"{route[0]} -> {route[1]}" for route in routes])
        messagebox.showinfo("Routes", f"Available Routes:\n{route_str}")
    else:
        messagebox.showinfo("Routes", "No routes available for the given airports.")


# Create main window
root = tk.Tk()
root.title("Airline Route Planner")

# Create and place widgets
label_source = tk.Label(root, text="Source Airport:")
label_source.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_source = tk.Entry(root)
entry_source.grid(row=0, column=1, padx=10, pady=5)

label_destination = tk.Label(root, text="Destination Airport:")
label_destination.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_destination = tk.Entry(root)
entry_destination.grid(row=1, column=1, padx=10, pady=5)

btn_find_routes = tk.Button(root, text="Find Routes", command=find_routes)
btn_find_routes.grid(row=2, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()

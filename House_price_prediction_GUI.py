
import tkinter as tk
from tkinter import ttk
import pickle
import pandas as pd
# import numpy as np

font_select = ('Arial', 14, 'bold')


win = tk.Tk()
win.title("House Rate Prediction")
win.geometry("800x600")
win.config(bg='#f0f0f0')  # Light gray background

# Load the data from model and csv file
data = pd.read_csv("Cleaned_data.csv")
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))
locations = sorted(data['location'].unique())


card = tk.LabelFrame(win, text="House Rate Prediction", bg='#ffffff', width=600, height=400,
                     font=("Arial", 18, "bold"), bd=2, relief=tk.GROOVE)
card.pack(pady=20)

label_frame = tk.LabelFrame(card, text='', bg='#ffffff')
label_frame.pack(padx=20, pady=20)

# Create labels and entry boxes for user input
location_label = tk.Label(label_frame, text="Select Your location:    ", font=font_select, bg="#ffffff")
location_label.grid(row=0, column=0, padx=10, pady=10)

location_var = tk.StringVar()
Location_combobox = ttk.Combobox(label_frame, values=locations, textvariable=location_var, width=20, font=font_select)
Location_combobox.grid(row=0, column=1, padx=10, pady=10)
Location_combobox.set(locations[0])

bhk_label = tk.Label(label_frame, text="Enter the BHK:         ", font=font_select, bg="#ffffff")
bhk_label.grid(row=1, column=0, padx=10, pady=10)

bhk_var = tk.IntVar()
bhk = tk.Entry(label_frame, textvariable=bhk_var, font=font_select)
bhk.grid(row=1, column=1, padx=10, pady=10)

bathroom_label = tk.Label(label_frame, text="Enter the No. Bathroom:", font=font_select, bg="#ffffff")
bathroom_label.grid(row=2, column=0, padx=10, pady=10)

bathroom_var = tk.IntVar()
bathroom = tk.Entry(label_frame, textvariable=bathroom_var, font=font_select)
bathroom.grid(row=2, column=1, padx=10, pady=10)

square_feet_label = tk.Label(label_frame, text="Enter the Square feet:  ", font=font_select, bg="#ffffff")
square_feet_label.grid(row=3, column=0, padx=10, pady=10)

square_feet_var = tk.IntVar()
square_feet = tk.Entry(label_frame, textvariable=square_feet_var, font=font_select)
square_feet.grid(row=3, column=1, padx=10, pady=10)


# Function to predict the house rate
def predict_model():
    if bhk_var.get() == 0 or square_feet_var.get() == 0 or bathroom_var.get() == 0:
        prediction_label.config(text="Please enter correct details")
    else:
        input_data = pd.DataFrame([[location_var.get(), square_feet_var.get(), bathroom_var.get(), bhk_var.get()]],
                                  columns=['location', 'total_sqft', 'bath', 'bhk'])
        prediction_value = pipe.predict(input_data)[0] * 100000
        prediction_label.config(text=f"Prediction: ₹{prediction_value:.2f}", foreground='green')


prediction_label = tk.Label(label_frame, text="Prediction:", font=('Arial', 18, 'bold'), bg="#ffffff")
prediction_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Button to trigger prediction
submit_btn = tk.Button(label_frame, text="Predict Price", command=predict_model, font=font_select, bg='#4CAF50',
                       fg='#ffffff', bd=2, relief=tk.RAISED)
submit_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

win.mainloop()

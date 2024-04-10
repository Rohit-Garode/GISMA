# Carbon Footprint Monitoring Tool

This program is designed to help users monitor and analyze their carbon footprint based on various factors such as energy usage, waste generation, and business travel. The program provides a user-friendly interface to input relevant data and generates a detailed report along with suggestions for reducing carbon emissions.

## Features

- **User Input Fields**: Users can input data related to their electricity, natural gas, and fuel bills, waste generation, recycling percentage, business travel distance, and average fuel efficiency.
  
- **Generate Report**: Upon clicking the "Generate Report" button, the program calculates the carbon footprint based on the provided inputs. It checks if the calculated values exceed certain limits (provided by the user) and suggests actions to reduce the carbon footprint if necessary.

- **PDF Report Generation**: The program generates a PDF report containing:
  - A text page with the current date and time, along with a summary of carbon footprint details and suggestions.
  - Pie charts illustrating the breakdown of energy usage, waste, and business travel.
  - A bar graph comparing actual values to set limits. The PDF report is saved locally and opened in the default web browser.

- **Error Handling**: Basic error handling is implemented to ensure that users input numeric values only.

- **Tkinter GUI**: The graphical interface is created using Tkinter, a standard GUI toolkit for Python.

## Getting Started

To run the program, follow these steps:

1. Ensure you have Python installed on your system.

2. Clone this repository to your local machine:
   ```
   git clone https://github.com/Rohit-Garode/M602A_Computer_Programming_WS0124.git
   ```

3. Install the required dependencies:
   ```
   pip3 install -r requirements.txt
   ```

4. Run the program:
   ```
   python3 carbon_footprint_monitoring.py
   ```

5. Enter the required data in the input fields and click on the "Generate Report" button to generate the carbon footprint report.

   ![Screenshot 2024-04-10 153354](https://github.com/Rohit-Garode/GISMA/assets/76519295/364f5863-0cdc-438e-87c4-214d9cb1dfeb)



## Requirements

- Python 3.x
- Tkinter
- Matplotlib

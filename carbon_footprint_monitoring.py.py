import tkinter as tk
import webbrowser
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import datetime


def calculate_energy_usage(electricity_bill, natural_gas_bill, fuel_bill):
    return (electricity_bill * 12 * 0.0005) + (natural_gas_bill * 12 * 0.0053) + (fuel_bill * 12 * 2.32)


def calculate_waste(total_waste_generated_per_month, recycling_percentage):
    return total_waste_generated_per_month * 12 * (0.57 - (recycling_percentage / 100))


def calculate_business_travel(total_kilometers_traveled_per_year, average_fuel_efficiency):
    return total_kilometers_traveled_per_year / (average_fuel_efficiency / 100) * 2.31


def generate_report(energy_usage, waste, business_travel, suggestions=None):
    report = f"Energy Usage: {energy_usage:.2f} kgCO2e\n"
    report += f"Waste: {waste:.2f} kgCO2e\n"
    report += f"Business Travel: {business_travel:.2f} kgCO2e\n\n"
    report += "The report includes two graphs to help you understand your carbon footprint \nbreakdown:\n\n"
    report += ("- Pie Chart: This chart divides your footprint into each sections, reflects \nthe relative impact of "
               "each aspect on your overall footprint.\n")
    report += ("- Bar Graph: It compares actual values to your set limits, allowing you to \nsee if your footprint "
               "exceeds them in any category.\n\n")

    if suggestions:
        report += "Suggestions for reducing carbon footprints:\n\n"
        for suggestion in suggestions:
            report += f"- {suggestion}\n"
    return report


def generate_and_save_pdf(energy_usage, waste, business_travel,
                          energy_limit, waste_limit, business_travel_limit,
                          electricity_bill, natural_gas_bill, fuel_bill,
                          total_waste_generated_per_month, recycling_percentage,
                          total_kilometers_traveled_per_year, average_fuel_efficiency,
                          suggestions=None):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    current_month_date = datetime.datetime.now().strftime("%B %d, %Y - %H:%M:%S")
    pdf_path = f"carbon_footprint_report_{current_time}.pdf"
    with PdfPages(pdf_path) as pdf:

        # Add a text page at the beginning of the PDF
        plt.figure(figsize=(8.27, 11.69))  # A4 size
        plt.text(0.5, 0.9, current_month_date, horizontalalignment='center', fontsize=12)
        plt.text(0.5, 0.8, "Carbon Footprint Report", horizontalalignment='center', fontsize=16, weight='bold')
        report = generate_report(energy_usage, waste, business_travel, suggestions)
        plt.text(0, 0.7, report, verticalalignment='top', fontsize=12, horizontalalignment='left')
        plt.axis('off')
        pdf.savefig()
        plt.close()

        # Generating pie charts for input element values
        plt.figure(figsize=(8.27, 11.69))  # A4 size
        plt.subplot(3, 1, 1)
        labels_energy = [f'Electricity Bill: {electricity_bill}',
                         f'Natural Gas Bill: {natural_gas_bill}',
                         f'Fuel Bill: {fuel_bill}']
        sizes_energy = [electricity_bill, natural_gas_bill, fuel_bill]
        plt.pie(sizes_energy, labels=labels_energy, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title('Energy Usage')
        plt.gca().set_aspect('equal')

        plt.subplot(3, 1, 2)
        labels_waste = [f'Total Waste Generated: {total_waste_generated_per_month}',
                        f'Recycling Percentage: {recycling_percentage}%']
        sizes_waste = [total_waste_generated_per_month, recycling_percentage]
        plt.pie(sizes_waste, labels=labels_waste, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title('Waste')
        plt.gca().set_aspect('equal')

        plt.subplot(3, 1, 3)
        labels_travel = [f'Total Km Traveled: {total_kilometers_traveled_per_year}',
                         f'Avg Fuel Efficiency: {average_fuel_efficiency}']
        sizes_travel = [total_kilometers_traveled_per_year, average_fuel_efficiency]
        plt.pie(sizes_travel, labels=labels_travel, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title('Business Travel')
        plt.gca().set_aspect('equal')

        plt.suptitle('Carbon Footprint Input Values')
        plt.tight_layout(rect=(0, 0.03, 1, 0.95))
        pdf.savefig()
        plt.close()

        # Generating bar graph for actual values and limits
        plt.figure(figsize=(8.27, 11.69))  # A4 size

        categories = ['Energy Usage', 'Waste', 'Business Travel']
        actual_values = [energy_usage, waste, business_travel]
        limit_values = [energy_limit, waste_limit, business_travel_limit]

        bar_width = 0.35
        index = range(len(categories))

        plt.bar(index, actual_values, bar_width, color='blue', label='Actual Values')
        plt.bar([i + bar_width for i in index], limit_values, bar_width, color='red', label='Limit Values')

        # Check if any values exceed limits and provide suggestions
        for i in range(len(categories)):
            if actual_values[i] > limit_values[i]:
                plt.text(i, actual_values[i], f"Exceeds limit by {actual_values[i] - limit_values[i]:.2f}",
                         ha='center', va='bottom', color='red')

        plt.xlabel('Categories')
        plt.ylabel('CO2e (kg)')
        plt.title('Carbon Footprint Actual vs. Limits')
        plt.xticks([i + bar_width / 2 for i in index], categories)
        plt.legend()

        pdf.savefig()
        plt.close()

    # Open the PDF file in the default web browser
    webbrowser.open(pdf_path)


def handle_generate_report():
    try:
        electricity_bill = float(electricity_bill_entry.get())
        natural_gas_bill = float(natural_gas_bill_entry.get())
        fuel_bill = float(fuel_bill_entry.get())
        total_waste_generated_per_month = float(total_waste_generated_per_month_entry.get())
        recycling_percentage = float(recycling_percentage_entry.get())
        total_kilometers_traveled_per_year = float(total_kilometers_traveled_per_year_entry.get())
        average_fuel_efficiency = float(average_fuel_efficiency_entry.get())
        energy_limit = float(energy_limit_entry.get())
        waste_limit = float(waste_limit_entry.get())
        business_travel_limit = float(business_travel_limit_entry.get())

        energy_usage = calculate_energy_usage(electricity_bill, natural_gas_bill, fuel_bill)
        waste = calculate_waste(total_waste_generated_per_month, recycling_percentage)
        business_travel = calculate_business_travel(total_kilometers_traveled_per_year, average_fuel_efficiency)

        suggestions = []
        if energy_usage > energy_limit:
            suggestions.append(
                "Reduce energy consumption by using energy-efficient appliances and turning off \nunused devices.")
        if waste > waste_limit:
            suggestions.append("Increase recycling efforts and reduce waste generation by using reusable items.")
        if business_travel > business_travel_limit:
            suggestions.append(
                "Encourage telecommuting, carpooling, or using public transportation for business \ntravel.")

        report = generate_report(energy_usage, waste, business_travel, suggestions)
        report_textbox.delete(1.0, tk.END)
        report_textbox.insert(tk.END, report)

        generate_and_save_pdf(energy_usage, waste, business_travel, energy_limit, waste_limit, business_travel_limit,
                              electricity_bill, natural_gas_bill, fuel_bill, total_waste_generated_per_month,
                              recycling_percentage, total_kilometers_traveled_per_year, average_fuel_efficiency,
                              suggestions=suggestions)

        messagebox.showinfo("Success", "Report generated successfully!")

    except ValueError:
        messagebox.showerror("Error", "Please enter numeric values only.")


# Create the main window
root = tk.Tk()
root.title("Carbon Footprint Monitoring Program")

# Create labels and entry fields for input
tk.Label(root, text="Electricity Bill ($):").grid(row=0, column=0, sticky="e")
electricity_bill_entry = tk.Entry(root)
electricity_bill_entry.grid(row=0, column=1)

tk.Label(root, text="Natural Gas Bill ($):").grid(row=1, column=0, sticky="e")
natural_gas_bill_entry = tk.Entry(root)
natural_gas_bill_entry.grid(row=1, column=1)

tk.Label(root, text="Fuel Bill ($):").grid(row=2, column=0, sticky="e")
fuel_bill_entry = tk.Entry(root)
fuel_bill_entry.grid(row=2, column=1)

tk.Label(root, text="Total Waste Generated per Month (kg):").grid(row=3, column=0, sticky="e")
total_waste_generated_per_month_entry = tk.Entry(root)
total_waste_generated_per_month_entry.grid(row=3, column=1)

tk.Label(root, text="Recycling/Composting Percentage (%):").grid(row=4, column=0, sticky="e")
recycling_percentage_entry = tk.Entry(root)
recycling_percentage_entry.grid(row=4, column=1)

tk.Label(root, text="Total Kilometers Traveled per Year for Business Purposes:").grid(row=5, column=0, sticky="e")
total_kilometers_traveled_per_year_entry = tk.Entry(root)
total_kilometers_traveled_per_year_entry.grid(row=5, column=1)

tk.Label(root, text="Average Fuel Efficiency (L/100km):").grid(row=6, column=0, sticky="e")
average_fuel_efficiency_entry = tk.Entry(root)
average_fuel_efficiency_entry.grid(row=6, column=1)

tk.Label(root, text="Energy Usage Limit (kgCO2e):").grid(row=7, column=0, sticky="e")
energy_limit_entry = tk.Entry(root)
energy_limit_entry.grid(row=7, column=1)

tk.Label(root, text="Waste Limit (kgCO2e):").grid(row=8, column=0, sticky="e")
waste_limit_entry = tk.Entry(root)
waste_limit_entry.grid(row=8, column=1)

tk.Label(root, text="Business Travel Limit (kgCO2e):").grid(row=9, column=0, sticky="e")
business_travel_limit_entry = tk.Entry(root)
business_travel_limit_entry.grid(row=9, column=1)

# Create a button to generate report
generate_report_button = tk.Button(root, text="Generate Report", command=handle_generate_report)
generate_report_button.grid(row=10, columnspan=2, pady=10)

# Create a textbox to display the report
report_textbox = tk.Text(root, height=10, width=50)
report_textbox.grid(row=11, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()

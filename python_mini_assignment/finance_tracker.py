import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class FinanceTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")

        self.income_type_var = tk.StringVar()
        self.income_amount = tk.StringVar()
        self.expense_category_var = tk.StringVar()
        self.expense_amount = tk.StringVar()

        self.expenses = {"Groceries": 0, "Utilities": 0, "Entertainment": 0}
        self.incomes = {"Regular": 0, "Additional": 0}

        self.weekly_var = tk.StringVar()
        self.weekly_expense_amount = tk.StringVar()
        self.weekly_expenses = {"week1": 0, "week2": 0, "week3": 0, "week4": 0}

        self.create_input_frame()
        self.visualization_frame_for_income()
        self.visualization_frame_for_expense()
        self.visualization_frame_for_savings()

    def create_input_frame(self):
        """
        This function will create the frame which holds the input values of
        incomes and expenses
        """
        input_frame = ttk.LabelFrame(self.root, text="Input Expenses and Incomes")
        input_frame.grid(row=1, column=0, padx=10, pady=10,columnspan=2)

        # Income input
        ttk.Label(input_frame, text="Income Type:").grid(row=0, column=0, padx=5, pady=5)
        income_type_combobox = ttk.Combobox(input_frame, textvariable=self.income_type_var,
                                            values=list(self.incomes.keys()))
        income_type_combobox.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Income Amount:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.income_amount).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(input_frame, text="Add Income", command=self.add_income).grid(row=2, column=0, columnspan=2, pady=3)

        # Expense input
        ttk.Label(input_frame, text="Expense Category:").grid(row=3, column=0, padx=3, pady=3)
        expense_category_combobox = ttk.Combobox(input_frame, textvariable=self.expense_category_var,
                                                 values=list(self.expenses.keys()))
        expense_category_combobox.grid(row=3, column=1, padx=3, pady=3)

        ttk.Label(input_frame, text="Expense Amount:").grid(row=4, column=0, padx=3, pady=3)
        ttk.Entry(input_frame, textvariable=self.expense_amount).grid(row=4, column=1, padx=3, pady=3)

        ttk.Button(input_frame, text="Add Expense", command=self.add_expense).grid(row=5, column=0, columnspan=2,
                                                                                   pady=3)
        # weekly expenses
        #ghjkl
        ttk.Label(input_frame, text="select week:").grid(row=1, column=6, padx=3, pady=3)
        income_type_combobox = ttk.Combobox(input_frame, textvariable=self.weekly_var,
                                            values=list(self.weekly_expenses.keys()))
        income_type_combobox.grid(row=1, column=7, padx=3, pady=3)

        ttk.Label(input_frame, text="weekly expenses amount:").grid(row=2, column=6, padx=3, pady=3)
        ttk.Entry(input_frame, textvariable=self.weekly_expense_amount).grid(row=2, column=7, padx=3, pady=3)

        ttk.Button(input_frame, text="Add weekly expenses amount", command=self.add_weekly_expense).grid(row=3, column=6,
                                                                                                        columnspan=2,
                                                                                                        pady=3)

    def visualization_frame_for_income(self):
        """
            Generates the frame which contain a basic figure
        """
        income_frame = ttk.LabelFrame(self.root, text="Income")
        income_frame.grid(row=0, column=0, padx=5, pady=5)

        # Create a figure for the pie chart
        self.figure, self.ax_income = plt.subplots()

        # embed the figure to tkinter canvas
        self.canvas_income = FigureCanvasTkAgg(self.figure, master=income_frame)
        self.canvas_income.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        ttk.Button(income_frame, text="Generate income Report", command=self.generate_report_for_income).pack(pady=1)

    def visualization_frame_for_expense(self):
        """
            Generates the frame which contain a basic figure
        """
        expense_frame = ttk.LabelFrame(self.root, text="Expenses")
        expense_frame.grid(row=0, column=1, padx=5, pady=5)

        self.figure, self.ax_expense = plt.subplots()
        self.canvas_expense = FigureCanvasTkAgg(self.figure, master=expense_frame)
        self.canvas_expense.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        ttk.Button(expense_frame, text="Generate expenses Report", command=self.generate_report_for_expense).pack(pady=1)
        ttk.Button(expense_frame, text="Generate weekly expenses Report",
                   command=self.generate_report_for_weekly_expenses).pack(pady=1)

    def visualization_frame_for_savings(self):
        """
            Generates the frame which contain a basic figure
        """
        savings_frame = ttk.LabelFrame(self.root, text="Savings")
        savings_frame.grid(row=0, column=2, padx=5, pady=5)

        self.figure, self.ax_savings = plt.subplots()
        self.canvas_savings = FigureCanvasTkAgg(self.figure, master=savings_frame)
        self.canvas_savings.draw()
        self.canvas_savings.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        ttk.Button(savings_frame, text="Generate Bar Chart", command=self.generate_report_savings).pack(pady=1)

    def add_expense(self):
        """
        This function will add the all the expenses entered
         in input field to  dictionary with respect to expenses category
        """
        try:
            amount = float(self.expense_amount.get())
            category = self.expense_category_var.get()
            self.expenses[category] += amount

            # Clear entry fields
            self.expense_amount.set("")
            self.expense_category_var.set("")

        except ValueError as e:
            print(f"Invalid amount {e}")

    def add_income(self):
        """
            This function will add the all the income entered
            in input field to  dictionary with respect to income category
        """
        try:
            amount = float(self.income_amount.get())
            income_type = self.income_type_var.get()
            self.incomes[income_type] += amount

            # Clear entry fields
            self.income_amount.set("")
            self.income_type_var.set("")

        except ValueError as e:
            print(f"Invalid amount {e}")

    def add_weekly_expense(self):
        """
            This function will add the all the expenses entered
            in input field to  dictionary with respect to weekly expenses
        """
        try:
            amount = float(self.weekly_expense_amount.get())
            week = self.weekly_var.get()
            self.weekly_expenses[week] += amount

            # Clear entry fields
            self.weekly_expense_amount.set("")
            self.weekly_var.set("")
        except ValueError as e:
            print(f"Invalid amount {e}")

    def generate_report_for_income(self):
        """
            This function will generate the pie chart
            based on income amount w.r.t income category
        """
        try:
            labels = list(self.incomes.keys())
            values = list(self.incomes.values())

            # Plotting a pie chart
            self.ax_income.clear()
            self.ax_income.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
            self.ax_income.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle

            # Draw the pie chart on the Tkinter canvas
            self.canvas_income.draw()
        except Exception as e:
            print(f"error while generating pie chart:{e}")

    def generate_report_for_expense(self):
        """
            This function will generate the pie chart
            based on expense amount w.r.t expense category
        """
        try:
            labels = list(self.expenses.keys())
            values = list(self.expenses.values())

            # Plotting a pie chart
            self.ax_expense.clear()
            self.ax_expense.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
            self.ax_expense.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle

            # Draw the pie chart on the Tkinter canvas
            self.canvas_expense.draw()
        except Exception as e:
            print(f"error while generating pie chart:{e}")

    def generate_report_for_weekly_expenses(self):
        """
            This function will generate the bar chart
            based on expense amount w.r.t weekly expenses
        """
        try:
            labels = list(self.weekly_expenses.keys())
            values = list(self.weekly_expenses.values())
            weekly_amount_list = [float(amount) for amount in values]

            self.ax_expense.clear()

            # Plotting a bar chart
            self.ax_expense.bar(labels, weekly_amount_list)
            self.ax_expense.set_ylabel('Amount')
            self.ax_expense.set_title('Weekly Expense Report')

            # Draw the bar chart on the Tkinter canvas
            self.canvas_expense.draw()
        except Exception as e:
            print(f"error while generating bar chart:{e}")

    def generate_report_savings(self):
        """
            This function will generate the bar chart
            based on income, expense amount given and calculates
            savings
        """
        try:
            income_list = list(self.incomes.values())
            expense_list = list(self.expenses.values())

            total_income = sum([int(income) for income in income_list])
            total_expense = sum([int(expense) for expense in expense_list])
            total_savings = total_income - total_expense
            self.ax_savings.clear()

            categories = ['Income', 'Expense', 'Savings']
            values = [total_income, total_expense, total_savings]

            # Plot the bar chart
            self.ax_savings.bar(categories, values, color=['green', 'red', 'blue'])
            self.ax_savings.set_ylabel('Amount')
            self.ax_savings.set_title('Income, Expense, and Savings')

            # Draw the updated chart on the Tkinter canvas
            self.canvas_savings.draw()
        except Exception as e:
            print(f"error while generating bar chart:{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTrackerApp(root)
    root.mainloop()


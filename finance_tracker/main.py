import questionary
from features.transactions.transactions import add_expense, add_income, list_transactions, balance_command
from features.budgets.budgets import set_budget, view_budgets
from features.analytics.analytics import monthly_summary, category_wise_spending
from features.smart_assistant.smart_assistant import spending_analysis, savings_suggestions, budget_optimization, financial_tips
from features.data_management.data_management import export_data, reset_data
from rich.console import Console

console = Console()

def main():
    console.print("[bold magenta]Welcome to Personal Finance Tracker CLI![/bold magenta]")
    console.print("[italic]Your command-line companion for managing finances.[/italic]\n")
    while True:
        console.print("[bold magenta]Personal Finance Tracker CLI[/bold magenta]")
        choice = questionary.select(
            "What do you want to do?",
            choices=[
                "Add Expense",
                "Add Income",
                "List Transactions",
                "View Balance",
                "Set Budget",
                "View Budgets",
                "Monthly Summary",
                "Category-wise Spending",
                "Spending Analysis",
                "Savings Suggestions",
                "Budget Optimization",
                "Financial Tips",
                "Export Data",
                "Reset Data",
                "Exit"
            ]
        ).ask()

        if choice == "Add Expense":
            add_expense()
        elif choice == "Add Income":
            add_income()
        elif choice == "List Transactions":
            list_transactions()
        elif choice == "View Balance":
            balance_command()
        elif choice == "Set Budget":
            set_budget()
        elif choice == "View Budgets":
            view_budgets()
        elif choice == "Monthly Summary":
            monthly_summary()
        elif choice == "Category-wise Spending":
            category_wise_spending()
        elif choice == "Spending Analysis":
            spending_analysis()
        elif choice == "Savings Suggestions":
            savings_suggestions()
        elif choice == "Budget Optimization":
            budget_optimization()
        elif choice == "Financial Tips":
            financial_tips()
        elif choice == "Export Data":
            export_data()
        elif choice == "Reset Data":
            reset_data()
        elif choice == "Exit":
            console.print("[bold green]Exiting. Goodbye![/bold green]")
            break

if __name__ == "__main__":
    main()
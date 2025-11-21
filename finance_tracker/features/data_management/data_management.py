import os
import csv
import questionary
from rich.console import Console
from features.transactions.transactions import TRANSACTIONS_FILE, _read_transactions
from features.budgets.budgets import BUDGETS_FILE

console = Console()

def export_data():
    """Exports all transaction and budget data to a CSV file."""
    console.print("[bold blue]\n--- Export Data ---[/bold blue]")

    filename = questionary.text(
        "Enter filename for export (e.g., finance_data.csv):",
        default="finance_data.csv",
        instruction="Data will be saved in CSV format."
    ).ask()
    if filename is None: return

    try:
        with open(filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Type", "Date", "Amount", "Category/Source", "Description"]) # Header

            # Export Transactions
            transactions = _read_transactions()
            for t in transactions:
                csv_writer.writerow([
                    t["type"],
                    t["date"].strftime("%Y-%m-%d"),
                    f"{(t['amount'] / 100):.2f}",
                    t["category"],
                    t["description"]
                ])
            
            # Export Budgets
            if os.path.exists(BUDGETS_FILE):
                with open(BUDGETS_FILE, "r") as f:
                    for line in f:
                        parts = line.strip().split("|")
                        if len(parts) == 3:
                            csv_writer.writerow(["budget", parts[2], f"{(int(parts[1]) / 100):.2f}", parts[0], "N/A"])
        console.print(f"[bold green]Data exported successfully to '{filename}'![/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error exporting data: {e}[/bold red]")

def reset_data():
    """Resets all transaction and budget data."""
    console.print("[bold red]\n--- Reset Data ---[/bold red]")

    confirm = questionary.confirm(
        "Are you absolutely sure you want to reset ALL data? This action cannot be undone.",
        default=False
    ).ask()
    if confirm is None or not confirm:
        console.print("[yellow]Data reset cancelled. Your data is safe.[/yellow]")
        return

    try:
        if os.path.exists(TRANSACTIONS_FILE):
            with open(TRANSACTIONS_FILE, "w") as f:
                f.write("") # Clear file content
            console.print(f"[green]Cleared {TRANSACTIONS_FILE}[/green]")
        else:
            console.print(f"[yellow]{TRANSACTIONS_FILE} does not exist, no transactions to clear.[/yellow]")

        if os.path.exists(BUDGETS_FILE):
            with open(BUDGETS_FILE, "w") as f:
                f.write("") # Clear file content
            console.print(f"[green]Cleared {BUDGETS_FILE}[/green]")
        else:
            console.print(f"[yellow]{BUDGETS_FILE} does not exist, no budgets to clear.[/yellow]")

        console.print("[bold green]All transaction and budget data has been successfully reset![/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error resetting data: {e}[/bold red]")

from rich import print
from rich.console import Console
from rich.table import Table

print("[bold green]Hello, students![/bold green]")

table = Table(title="Student Grades")
table.add_column("Name")
table.add_column("Grade")

table.add_row("Alice", "5")
table.add_row("Bob", "4")
table.add_row("Charlie", "5")

Console().print(table)

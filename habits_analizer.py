import csv
from datetime import datetime
from typing import List, Dict, Optional

# Constantes
DATA_FILE = "habits_data.csv"
HEADERS = ["date", "habit", "duration_min", "completed"]


def init_data_file() -> None:
    """Inicializa el archivo CSV con headers si no existe."""
    try:
        with open(DATA_FILE, "x", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
    except FileExistsError:
        pass


def log_habit(habit: str, duration_min: int, completed: bool) -> None:
    """Registra un hábito en el archivo CSV."""
    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writerow({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "habit": habit,
            "duration_min": duration_min,
            "completed": completed
        })


if __name__ == "__main__":
    init_data_file()
    print("¡Bienvenido al Analizador de Hábitos!")

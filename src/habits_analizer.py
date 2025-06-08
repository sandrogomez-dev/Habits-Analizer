import csv
from datetime import datetime
from typing import List, Dict, Any
from collections import defaultdict


class HabitTracker:
    def __init__(self, data_file: str = "data/habits_data.csv") -> None:
        self.data_file = data_file
        self.headers = ["date", "habit", "duration_min", "completed"]
        self._init_data_file()

    def _init_data_file(self) -> None:
        """Inicializa el archivo CSV con headers si no existe."""
        try:
            with open(self.data_file, "x", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
        except FileExistsError:
            pass

    def log_habit(self, habit: str, duration_min: int, completed: bool) -> None:
        """Registra un hábito en el CSV."""
        with open(self.data_file, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writerow({
                "date": datetime.now().strftime("%Y-%m-%d"),
                "habit": habit,
                "duration_min": duration_min,
                "completed": completed
            })

    def get_habits(self) -> List[Dict[str, str]]:
        """Retorna todos los hábitos registrados."""
        with open(self.data_file, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def analyze_habits(self) -> Dict[str, Dict[str, float]]:
        """
        Analiza hábitos y devuelve:
        - Tasa de completitud (%).
        - Duración promedio (minutos).
        """
        habits = self.get_habits()
        if not habits:
            return {}

        analysis: Dict[str, Dict[str, float]] = defaultdict(
            lambda: {"total": 0, "completed": 0, "total_duration": 0.0}
        )

        for entry in habits:
            habit = entry["habit"]
            analysis[habit]["total"] += 1
            analysis[habit]["completed"] += int(entry["completed"] == "True")
            analysis[habit]["total_duration"] += float(entry["duration_min"])

        # Calcular métricas
        for habit, stats in analysis.items():
            stats["completion_rate"] = (
                stats["completed"] / stats["total"]) * 100
            stats["avg_duration"] = stats["total_duration"] / stats["total"]

        return dict(analysis)


if __name__ == "__main__":
    # Ejemplo de uso
    tracker = HabitTracker()

    # Registrar algunos hábitos (simulación)
    habits_to_log = [
        ("Meditación", 10, True),
        ("Ejercicio", 30, True),
        ("Leer", 20, False),
        ("Meditación", 15, True)
    ]

    for habit, duration, completed in habits_to_log:
        tracker.log_habit(habit, duration, completed)

    # Análisis
    analysis = tracker.analyze_habits()
    print("Análisis de Hábitos:")
    for habit, stats in analysis.items():
        print(
            f"Hábito: {habit}\n"
            f"  - Completitud: {stats['completion_rate']:.2f}%\n"
            f"  - Duración Promedio: {stats['avg_duration']:.2f} min\n"
        )

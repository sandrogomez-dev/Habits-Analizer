class HabitTracker:
    def __init__(self, data_file: str = "habits_data.csv"):
        self.data_file = data_file
        self.headers = ["date", "habit", "duration_min", "completed"]
        self._init_data_file()

    def _init_data_file(self) -> None:
        """Inicializa el archivo CSV."""
        try:
            with open(self.data_file, "x", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
        except FileExistsError:
            pass

    def log_habit(self, habit: str, duration_min: int, completed: bool) -> None:
        """Registra un hábito."""
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


if __name__ == "__main__":
    tracker = HabitTracker()
    tracker.log_habit("Meditación", 10, True)
    print("Hábitos registrados:", tracker.get_habits())

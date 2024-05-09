from tkinter import *
from calendar import monthrange


class Calendar(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.master.title("Мой календарь")
        self.current_month = 1
        self.current_year = 2024

        self.create_widgets()
        self.display_calendar()

    def create_widgets(self):
        self.left_month_button = Button(root, text='<--', command=self.left_month)
        self.left_month_button.grid(row=0, column=0, padx=5, pady=5)

        self.right_month_button = Button(root, text='-->', command=self.right_month)
        self.right_month_button.grid(row=0, column=2, padx=5, pady=5)

        self.month_label = Label(root, text=f'{self.month_name(self.current_month)}, {self.current_year}')
        self.month_label.grid(row=0, column=1, padx=5, pady=5)

        self.weekdays_frame = Frame(self)
        self.weekdays_frame.grid(row=1, column=0, columnspan=4)

        for i, day in enumerate(["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]):
            weekday_label = Label(self.weekdays_frame, text=day)
            weekday_label.grid(row=0, column=i)

        self.days_frame = Frame(root)
        self.days_frame.grid(row=2, column=0, columnspan=4)

    def display_calendar(self):
        for widget in self.days_frame.winfo_children():
            widget.destroy()

        first_weekday, num_days = monthrange(self.current_year, self.current_month)
        row = 0
        col = 0

        for i in range(1, num_days + 1):
            if (i + first_weekday - 1) % 7 == 0:
                row += 1
                col = 0

            day_button = Button(self.days_frame, text=str(i))
            day_button.grid(row=row, column=col)
            col += 1

    def left_month(self):
        self.current_month -= 1

        if self.current_month < 1:
            self.current_month = 12
            self.current_year -= 1
        self.update_month_label()

    def right_month(self):
        self.current_month += 1

        if self.current_month >= 12:
            self.current_month = 1
            self.current_year += 1
        self.update_month_label()

    def update_month_label(self):
        self.month_label.config(text=f"{self.month_name(self.current_month)} {self.current_year}")

    def month_name(self, month):
        months = ["Январь", "Февраль", "Март", "Апрель", 'Май','Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                  'Ноябрь', 'Декабрь']
        return months[month - 1]


if __name__ == "__main__":
    root = Tk()
    # Запустить приложение посередине экрана
    # Получаем ширину и высоту экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Вычисляем координаты для центрирования окна
    window_width = 170
    window_height = 170
    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)

    # Устанавливаем размер и положение окна
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    app = Calendar(root)
    app.mainloop()



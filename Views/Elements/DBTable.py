from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.Qt import Qt

from datetime import date
from calendar import monthrange


class DBTable(QTableWidget):

    def __init__(self, parent):
        QTableWidget.__init__(self, parent=parent)
        self.source = None

    def set_source(self, db):
        self.source = db
        pass


class DBTableClients(DBTable):

    def __init__(self, parent):
        DBTable.__init__(self, parent=parent)

    def set_source(self, db):
        super().set_source(db)
        titles = ["№", "Дата вылета", "Вылет", "Страна", "Статус", "Виза", "Тур Оператор",
                  "Дата прилета", "Партнер", "Бронирование", "Покупатель",
                  "Депозит", "Профит"]

        data = db.get_all_clients()
        self.setRowCount(len(data)+1)
        self.setColumnCount(len(titles))

        for i in range(len(titles)):
            self.setItem(0, i, QTableWidgetItem(titles[i]))

        for i in range(len(data)):
            for item in range(0, len(data[i])):
                self.setItem(i+1, item, QTableWidgetItem(str(data[i][item])))


class DBTablePartners(DBTable):

    def __init__(self, parent):
        DBTable.__init__(self, parent=parent)

    def set_source(self, db):
        super().set_source(db)
        titles = ["ID", "Название", "Финансы", "Контакты", "Доступ", "Бренд", "%",
                  "Депозит"]

        data = db.get_all_partners()
        self.setRowCount(len(data)+1)
        self.setColumnCount(len(titles))

        for i in range(len(titles)):
            self.setItem(0, i, QTableWidgetItem(titles[i]))

        for i in range(len(data)):
            for item in range(0, len(data[i])):
                self.setItem(i+1, item, QTableWidgetItem(str(data[i][item])))


class CalendarDBTable(DBTable):

    def __init__(self, parent):
        DBTable.__init__(self, parent=parent)

    def update_values(self, month, year):
        self.setRowCount(0)
        self.setColumnCount(0)
        days_in_month = monthrange(year, month)[1]

        month_to_word = {1: "января",
                         2: "февраля",
                         3: "марта",
                         4: "апреля",
                         5: "мая",
                         6: "июня",
                         7: "июля",
                         8: "августа",
                         9: "сентября",
                         10: "октября",
                         11: "ноября",
                         12: "декабря"}

        if days_in_month == 28:
            self.setColumnCount(7)
            self.setRowCount(4)

        else:
            self.setColumnCount(7)
            self.setRowCount(5)
            for i in range(6, 6-(35-days_in_month), -1):
                self.setItem(4, i, QTableWidgetItem("XXXX"))

        for i in range(0, self.rowCount()):
            broken = False
            for j in range(0, 7):
                current_day = i*7 + j+1
                self.setItem(i, j, QTableWidgetItem(f"{current_day} {month_to_word[month]}\n"))
                if current_day == days_in_month:
                    broken = True
                    break
            if broken:
                break

        try:
            res = self.source.get_flights_on(month, year)
            messages = {}
            for flight in res[0]:
                day = flight[1].day
                if day % 7 == 0:
                    row = (day // 7) - 1
                    column = 6
                else:
                    row = day // 7
                    column = (day % 7) - 1
                message = f"Дата вылета клиента №{flight[0]}"
                if f"{row}_{column}" not in messages.keys():
                    messages[f"{row}_{column}"] = []
                messages[f"{row}_{column}"].append(message)

            for flight in res[1]:
                day = flight[1].day
                if day % 7 == 0:
                    row = (day // 7) - 1
                    column = 6
                else:
                    row = day // 7
                    column = (day % 7) - 1
                message = f"Дата прилета клиента №{flight[0]}"
                if f"{row}_{column}" not in messages.keys():
                    messages[f"{row}_{column}"] = []
                messages[f"{row}_{column}"].append(message)

            for i in messages.keys():
                row, column = [int(j) for j in i.split("_")]
                new_message = '\n'.join(messages[i])
                res = f"{self.item(row, column).text()}{new_message}"
                self.setItem(row, column, QTableWidgetItem(res))
        except Exception as e:
            print(e)




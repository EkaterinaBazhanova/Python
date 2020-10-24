class Data:
    @classmethod
    def set_data(cls, datastring):
        datalist = [int(el) for el in datastring.split("-")]
        return datalist

    @staticmethod
    def data_valid(obj):
        if obj[0] < 1 or obj[0] > 31:
            return f"Ошибка в записи дня"
        if obj[1] < 1 or obj[1] > 12:
            return f"Ошибка в записи месяца"
        return f"Установлена дата: {obj[0]} день, {obj[1]} месяц, {obj[2]} год"

data = input("Введите дату в формате 'dd-mm-yyyy': ")
print(Data.data_valid(Data.set_data(data)))

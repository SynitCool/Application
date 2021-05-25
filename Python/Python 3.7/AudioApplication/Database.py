import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.file = None

        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.data = {}
        for line in self.file:
            email, path, created = line.strip().split(";")
            self.data[email] = (path, created)

        self.file.close()

    def add_data(self, name, path):
        if name.strip() not in self.data:
            self.data[name.strip()] = (path.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Data Already Exist")
            return -1

    def save(self):
        with open(self.filename, 'w') as f:
            for line in self.data:
                f.write(f"{line};{self.data[line][0]};{self.data[line][1]}\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
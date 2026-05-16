# Lesson: using oops concept using json
import json


class DictToJson:

    def __init__(self, name, Id, salary):
        self.name = name
        self.Id = Id
        self.salary = salary

    def print_info(self):
        print("Name:", self.name)
        print("Id:", self.Id)
        print("Salary:", self.salary)



    def save_to_json(self, filepath):
        my_dict = {
            "employee": [
                {
                    "name": self.name,
                    "id": self.Id,
                    "salary": self.salary
                }
            ]
        }
        with open(filepath, 'a') as file:
            json.dump(my_dict, file)
        return my_dict


employee1 = DictToJson("bishal koirala", 12, 1300000)
employee1.print_info()
employee1.save_to_json("jsonfiles/my_data_json.json")
employee1.addEmployee()

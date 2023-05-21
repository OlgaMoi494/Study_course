from datetime import datetime


class Veterinary:

    def __init__(self, name):
        self.name = name

    def conduct_examination(self, animal):
        return f"Veterinarian {self.name} is conducting examination " \
               f"of the {animal.__class__.__name__.lower()} {animal.name}."
    @staticmethod
    def making_vet_report(animal):
        report_text = input("Please type the result of the vet examination: ")
        created_at = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        report_name = f'report_{animal.__class__.__name__.lower()}_{animal.name}_{created_at}.txt'
        with open('reports/'+report_name, 'w', encoding='utf-8') as report_file:
            report_file.write(report_text)

from modules import Dog, Cat, Horse, Veterinary

dog_rex = Dog('Rex', 'brown', weight=45)
dog_sheila = Dog('Sheila', 'white', weight=35)

puppy_dog = dog_rex.reproduce(dog_sheila)

cat_chili = Cat('Chili', "red")

horse_meteor = Horse('Meteor', 'in gray apples')

animal_lst = [dog_rex, dog_sheila, puppy_dog, cat_chili, horse_meteor]

for animal in animal_lst:
    print(animal.important_info())
print()

for animal in animal_lst:
    print(animal.move())
print()

for animal in animal_lst:
    print(animal.bite())

veterinary_pavel = Veterinary("Pavel Anatolievich")

veterinary_pavel.conduct_examination(dog_sheila)

veterinary_pavel.making_vet_report(dog_sheila)

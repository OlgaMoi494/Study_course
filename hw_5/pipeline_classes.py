from modules.animal_classes import Animal, Dog, Cat, Horse


description = '''
        It looks like a giant crocodile with dragon wings.
        It lives in tropical forests and feeds on small animals and birds.
        He can fly and swim, but he doesn’t walk very well on the ground.
        He’s dangerous to humans, but he’s not aggressive if you don’t touch him.
'''

animal_krocodragon = Animal("Krocodragon", 'purple_green', 5535, description=description)


dog_puppy = Dog('Puppy', 'brown')

cat_chili = Cat('Chili', "red")

horse_meteor = Horse('Meteor', 'in gray apples')

animal_lst = [animal_krocodragon, dog_puppy, cat_chili, horse_meteor]

for animal in animal_lst:
    print('\n', animal.important_info())

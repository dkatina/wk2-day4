

#-----Character Creator ----------


class Character():

    def __init__(self):
        self.name = ''
        self.race = ''
        self.outfit = {
            'helmet' : '',
            'Chestplate' :'',
            'Pants': '', 
            'Boots': ''
        }


    def get_info(self, name, race):
        self.name = name
        self.race = race

    def change_boots(self, boots):
        self.outfit['Boots'] = boots

    def change_pants(self, pants):
        self.outfit['Pants'] = pants

    def change_helm(self, helm):
        print('changing helm')
        self.outfit['helmet'] = helm

    def change_chest(self, chest):
        self.outfit['Chestplate'] = chest

    def display_outfit(self):
        print('You are currently wearing:')
        for key, value in self.outfit.items():
            print(f'{key}: {value}')
        

    def runner(self):
        print('----Welcome to the Character Builder ----')
        name = input('What\'s  your name traveler: ')
        race = input('What race are you? (Human/Elf/Orc/Dwarf): ')
        self.get_info(name, race)

        print(f'---Welcome {self.name}---')
        print('Lets customize your gear')
        while True:
            response = input('Would you like to view/edit/save your fit: ')
            if response.lower() == 'view':
                self.display_outfit()
            elif response.lower() == 'edit':
                piece = input('What would you like to edit Helm/Chest/Pants/Boots: ')
                if piece.lower() == 'helm':
                    helm = input('What helm would you like to wear?: ')
                    self.change_helm(helm)
                elif piece.lower() == 'chest':
                    chest = input('What chest would you like to wear?: ')
                    self.change_chest(chest)
                elif piece.lower() == 'pants':
                    pants = input('What pants would you like to wear?: ')
                    self.change_pants(pants)
                elif piece.lower() == 'boots':
                    boots = input('What boots would you like to wear?: ')
                    self.change_boots(boots)
            elif response == 'save':
                break

        print('Character successfully Built!')


dylan = Character()

dylan.runner()


#VY 2nd classes for upgraded rpg manager


#DataVizualization class (use Matplotlib and/or Pandas)


#StatisticalAnalyzer class (use Matplotlib)


#RandomGenerator class (use Faker)


#Characters class (parent class)


#Character class (for character creation and character object management)
class Character:
    def __init__(self, char_info, race, role, inventory=None):  #using "role" as a substitute word for "class"
        self.char_info = char_info  #when a character is created, char_info should be a dictionary with keys "name", "description", "backstory", and "persona_traits"
        self.level = 1  #level should stay 1 since it's a new character
        self.race = race.strip().lower()
        self.role = role.strip().lower()
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
        #set all stats to 0
        self.stats = {
            'strength': 0,
            'dexterity': 0,
            'resilience': 0,
            'magic': 0
        }
        #empty set for skills
        self.skills = set()
        #automatically gives three skill points
        self.skill_points = 3

        #give racial bonuses and specific-skills based on race
        if self.race == "human":
            self.stats = {
                'strength': 1,
                'dexterity': 1,
                'resilience': 1,
                'magic': 1
            }
        elif self.race == "orc":
            self.stats = {
                'strength': 2,
                'dexterity': 0,
                'resilience': 1,
                'magic': 0
            }
            self.skills = {'physical attack'}
        elif self.race == "elf":
            self.stats = {
                'strength': 0,
                'dexterity': 2,
                'resilience': 0,
                'magic': 1,
            }
            self.skills = {'buff magic'}
        elif self.race == "dwarf":
            self.stats = {
                'strength': 1,
                'dexterity': 0,
                'resilience': 2,
                'magic': 0
            }
            self.skills = {'defense boost'}

        #give different skills based on class
        if self.role == "cleric":
            pass
        elif self.role == "wizard":
            pass
        elif self.role == "fighter":
            pass
        elif self.role == "rogue":
            pass


    #method to level up
    def level_up(self):
        pass


    #method to add a new skill/ability
    def add_skill(self):
        pass


    #method to reset skill points
    def reset_skill_pts(self):
        pass


    #method to edit the inventory
    def edit_inventory(self):
        pass


    #method to edit the personal information for the character (name, description, backstory, and persona_traits)
    def edit_info(self):
        pass


    #method to print out the information of the character (will be used in the "view character" option of the menu)
    def __str__(self):
        pass
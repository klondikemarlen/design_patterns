## (Unofficial) Head First Design Patterns - in Python!

### Notes:
This is a 'work in progress' that doesn't include many extra exercises.

Run any package by doing C:\>`python3 example_package` (Windows) or $`python3 -m example_package` (Ubuntu) (or just 'python example_package' if you only have one python). This will run the file called '\_\_main\_\_' in that package. NOTE: a python package is just a folder that contains a '\_\_init\_\_.py' file. This file can be (and often is) blank.

Note on get/set methods in Python:
- you don't need them in the simplest use case in Python.
- for a more complex use case you can combined the semi-private '_' + 'example_var' -> '_example_var' combined with '@property' and/or 'get'/'set' where it seems appropriate.

e.g.
When adding a Quest object to the Journal of a Hero object. You want the quest to become active when it is added to the Hero's Journal.
```python
class Hero:
    def __init__(self):
        self.journal = None

class Quest:
    def __init__(self, name):
        self.name = name
        self.active = False

    def __repr__(self):
        return "<Quest: {}, active:{}>".format(self.name, self.active)

class Journal:
    def __init__(self):
        self._quests = []  # semi-private _

    def add_quest(self, quest):  # complex use case requiring set style
        """quests 'set' method."""
        quest.active = True
        self._quests.append(quest)

    @property
    def quests(self):  # simple get, using sem-private @property
        """Unmodifiable get 'quests' attribute."""
        return self._quests

    def get_active_quests(self):  # fancy get
        """Returns only active quests."""
        return [quest for quest in self._quests if quest.active]

    def get_inactive_quests(self):  # fancy get
        """Returns only inactive quests."""
        return [quest for quest in self._quests if not quest.active]


hero = Hero()
journal = Journal()
hero.journal = journal

quest1 = Quest("Find a Bug")
quest2 = Quest("Write an issue in GitHub")
quest3 = Quest("Fix an issue from GitHub")

journal.add_quest(quest1)
journal.add_quest(quest2)
journal.add_quest(quest3)

print(journal.quests)

quest1.active = False
print(hero.journal.get_active_quests())

quest2.active = False
print(hero.journal.get_inactive_quests())
```

### More notes:
While you could put all the code for every pattern in just one file, I decided to use python package style. It is easy to use and breaks up large files full of code, into lots of smaller files with just a little code. I have been told by those wiser than myself ... and noticed in my own practice that this saves a great deal of effort in the long run. On a personal note I tend to write in a single file ... then migrate it to packages and modules as a tidying up process. NOTE: a module is just a python file.

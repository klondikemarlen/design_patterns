## (Unofficial) Head First Design Patterns - in Python!

Work in progress that doesn't include many extra exercises.

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
        self._quests = []

    def add_quest(self, quest):
        """quests 'set' method."""
        quest.active = True
        self._quests.append(quest)

    @property
    def quests(self):
        """Unmodifiable 'quests' attribute."""
        return self._quests

    def get_active_quests(self):
        """Returns only active quests."""
        return [quest for quest in self._quests if quest.active]

    def get_inactive_quests(self):
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


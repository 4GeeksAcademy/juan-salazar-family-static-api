from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": 14157599,
                "first_name": "jhon",
                "last_name": "last.name",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 61333910,
                "first_name": "jane",
                "last_name": "last.name",
                "age": 33,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 24072010,
                "first_name": "jimmy",
                "last_name": "last.name",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        new_member = {
            "id": member.get("id", self._generateId()),
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }
        self._members.append(new_member)
        print(f"Added member: {new_member}")
        print(f"lista de usuarios {self._members}")
        return new_member

    def delete_member(self, id):
        print(f"Deleting member with id: {id}")
        for index, member in enumerate(self._members):
            print(f"Checking member with id: {member['id']}")
            if member["id"] == id:
                del self._members[index]
                print(f"Member with id: {id} deleted.")
                print(f"Members after delete: {self._members}")
                return True
        print(f"Member with id: {id} not found.")
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def update_member(self, id, member):
        print(f"Updating member with id: {id}")
        for index, current_member in enumerate(self._members):
            print(f"Checking member with id: {current_member['id']}")
            if current_member["id"] == id:
                self._members[index] = {
                    "id": id,
                    "first_name": member.get("first_name", current_member["first_name"]),
                    "last_name": member.get("last_name", current_member["last_name"]),
                    "age": member.get("age", current_member["age"]),
                    "lucky_numbers": member.get("lucky_numbers", current_member["lucky_numbers"])
                }
                print(f"Member with id: {id} updated.")
                print(f"Members after update: {self._members}")
                return True
        print(f"Member with id: {id} not found.")
        return False

    def get_all_members(self):
        return self._members
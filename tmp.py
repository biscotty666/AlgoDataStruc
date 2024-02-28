from dataclasses import dataclass

@dataclass
class User:
    name: str
    username: str

user = User('Bob', 'bob')
print(f"User(): {user}")
print(f"User.name: {user.name}")

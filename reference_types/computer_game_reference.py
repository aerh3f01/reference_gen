# reference_types/computer_game_reference.py
from .base_reference import BaseReference

class ComputerGameReference(BaseReference):
    def fields(self):
        return [
            ("Title", "title"),
            ("Developer", "developer"),
            ("Year", "year"),
            ("Edition (if applicable)", "edition"),
            ("Platform", "platform"),
        ]

    def cite_in_text(self, data):
        return f"({data['title']}, {data['year']})"

    def full_reference(self, data):
        ref = f"{data['developer']} ({data['year']}) {data['title']} ({data.get('edition', 'Standard')}). {data['platform']} [Computer game]."
        return ref

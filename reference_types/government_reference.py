# reference_types/government_reference.py
from .base_reference import BaseReference
from datetime import datetime

class GovernmentReference(BaseReference):
    def fields(self):
        return [
            ("Department Name", "department"),
            ("Year", "year"),
            ("Title", "title"),
            ("URL", "url"),
        ]

    def cite_in_text(self, data):
        return f"({data['department']}, {data['year']})"

    def full_reference(self, data):
        ref = f"{data['department']} ({data['year']}) {data['title']}. Available at: {data['url']} (Accessed: {datetime.today().strftime('%d %B %Y')})."
        return ref

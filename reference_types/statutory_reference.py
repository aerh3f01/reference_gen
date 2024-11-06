# reference_types/statutory_reference.py
from .base_reference import BaseReference
from datetime import datetime

class StatutoryReference(BaseReference):
    def fields(self):
        return [
            ("Title of Regulation", "title"),
            ("SI Number and Year", "si_number_year"),
            ("URL", "url"),
        ]

    def cite_in_text(self, data):
        return f"({data['title']}, {data['si_number_year']})"

    def full_reference(self, data):
        ref = f"{data['title']} ({data['si_number_year']}). Available at: {data['url']} (Accessed: {datetime.today().strftime('%d %B %Y')})."
        return ref

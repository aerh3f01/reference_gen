# reference_types/website_reference.py
from .base_reference import BaseReference
from datetime import datetime

class WebsiteReference(BaseReference):
    def fields(self):
        return [
            ("Author or Organization", "author"),
            ("Year", "year"),
            ("Title", "title"),
            ("URL", "url"),
        ]

    def cite_in_text(self, data):
        return f"({data['author']}, {data['year']})"

    def full_reference(self, data):
        ref = f"{data['author']} ({data['year']}) {data['title']}. Available at: {data['url']} (Accessed: {datetime.today().strftime('%d %B %Y')})."
        return ref

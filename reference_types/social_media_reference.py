# reference_types/social_media_reference.py
from .base_reference import BaseReference
from datetime import datetime

class SocialMediaReference(BaseReference):
    def fields(self):
        return [
            ("Author/Organization", "author"),
            ("Year", "year"),
            ("Title of Post", "title"),
            ("Platform (e.g., Facebook)", "platform"),
            ("Date of Post", "date"),
            ("URL", "url"),
        ]

    def cite_in_text(self, data):
        return f"({data['author']}, {data['year']})"

    def full_reference(self, data):
        ref = f"{data['author']} ({data['year']}) '{data['title']}', [{data['platform']}], {data['date']}. Available at: {data['url']} (Accessed: {datetime.today().strftime('%d %B %Y')})."
        return ref

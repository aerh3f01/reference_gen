# reference_types/podcast_reference.py
from .base_reference import BaseReference
from datetime import datetime

class PodcastReference(BaseReference):
    def fields(self):
        return [
            ("Presenter", "presenter"),
            ("Year", "year"),
            ("Title of Episode", "episode_title"),
            ("Podcast Title", "podcast_title"),
            ("Date of Episode", "episode_date"),
            ("URL", "url"),
        ]

    def cite_in_text(self, data):
        return f"({data['presenter']}, {data['year']})"

    def full_reference(self, data):
        ref = f"{data['presenter']} ({data['year']}) '{data['episode_title']}', {data['podcast_title']} [Podcast]. {data['episode_date']}. Available at: {data['url']} (Accessed: {datetime.today().strftime('%d %B %Y')})."
        return ref

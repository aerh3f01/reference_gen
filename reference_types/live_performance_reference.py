# reference_types/live_performance_reference.py
from .base_reference import BaseReference

class LivePerformanceReference(BaseReference):
    def fields(self):
        return [
            ("Title", "title"),
            ("Author (e.g., playwright, composer)", "author"),
            ("Year", "year"),
            ("Director (if applicable)", "director"),
            ("Location and Date of Performance", "location_date"),
        ]

    def cite_in_text(self, data):
        return f"({data['title']}, {data['year']})"

    def full_reference(self, data):
        ref = f"{data['title']} by {data['author']} ({data['year']}) Directed by {data.get('director', 'Unknown')} [{data['location_date']}]."
        return ref

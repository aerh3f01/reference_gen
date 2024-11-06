# reference_types/ai_reference.py
from .base_reference import BaseReference

class AIReference(BaseReference):
    def fields(self):
        return [
            ("AI Tool Name", "ai_tool"),
            ("Year", "year"),
            ("Receiver of Communication (e.g., your name)", "receiver"),
            ("Date (day/month)", "date"),
        ]

    def cite_in_text(self, data):
        return f"({data['ai_tool']}, {data['year']})"

    def full_reference(self, data):
        ref = f"{data['ai_tool']} ({data['year']}) {data['ai_tool']} [AI] response to {data['receiver']}. {data['date']}"
        return ref

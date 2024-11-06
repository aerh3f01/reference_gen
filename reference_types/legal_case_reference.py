# reference_types/legal_case_reference.py
from .base_reference import BaseReference

class LegalCaseReference(BaseReference):
    def fields(self):
        return [
            ("Case Name", "case_name"),
            ("Year", "year"),
            ("Volume Number", "volume_number"),
            ("Report Name", "report_name"),
            ("First Page of Report", "first_page"),
            ("URL (if available)", "url"),
        ]

    def cite_in_text(self, data):
        return f"({data['case_name']}, {data['year']})"

    def full_reference(self, data):
        ref = f"{data['case_name']} ({data['year']}) {data['volume_number']} {data['report_name']} {data['first_page']}."
        if data.get("url"):
            ref += f" Available at: {data['url']} (Accessed: today)."
        return ref

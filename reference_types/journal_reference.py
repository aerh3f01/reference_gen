# reference_types/journal_reference.py
from .base_reference import BaseReference

class JournalReference(BaseReference):
    def fields(self):
        return [
            ("Authors (Last name, First name; separate by semicolons)", "authors"),
            ("Year", "year"),
            ("Article Title", "article_title"),
            ("Journal Title", "journal_title"),
            ("Volume", "volume"),
            ("Issue", "issue"),
            ("Pages", "pages"),
            ("DOI (optional)", "doi"),
            ("URL (optional)", "url"),
        ]

    def cite_in_text(self, data):
        authors = self.format_authors(data["authors"], in_text=True)
        return f"({authors}, {data['year']})"

    def full_reference(self, data):
        authors = self.format_authors(data["authors"])
        ref = f"{authors} ({data['year']}) '{data['article_title']}', {data['journal_title']}, {data['volume']}({data['issue']}), pp. {data['pages']}."
        if data.get("doi"):
            ref += f" doi:{data['doi']}."
        elif data.get("url"):
            ref += f" Available at: {data['url']} (Accessed: {data.get('accessed', 'today')})."
        return ref

# reference_types/book_reference.py
from .base_reference import BaseReference

class BookReference(BaseReference):
    def fields(self):
        return [
            ("Authors (Last name, First name; separate by semicolons)", "authors"),
            ("Year", "year"),
            ("Title", "title"),
            ("Publisher", "publisher"),
            ("Place of Publication", "place"),
            ("Edition (optional)", "edition"),
        ]

    def cite_in_text(self, data):
        authors = self.format_authors(data["authors"], in_text=True)
        return f"({authors}, {data['year']})"

    def full_reference(self, data):
        authors = self.format_authors(data["authors"])
        ref = f"{authors} ({data['year']}) {data['title']}. "
        if data.get("edition"):
            ref += f"{data['edition']} edn. "
        if data.get("place"):
            ref += f"{data['place']}: "
        ref += f"{data['publisher']}."
        return ref

    def format_authors(self, authors_text, in_text=False):
        authors = [author.strip() for author in authors_text.split(';')]
        if in_text:
            if len(authors) > 3:
                first_author_last_name = authors[0].split(',')[0].strip()
                return f"{first_author_last_name} et al."
            else:
                return ', '.join([author.split(',')[0].strip() for author in authors])
        else:
            formatted_authors = []
            for author in authors:
                last_name, first_name = author.split(',')[:2]
                initials = ''.join([name[0] + '.' for name in first_name.strip().split()])
                formatted_authors.append(f"{last_name.strip()}, {initials}")
            return ', '.join(formatted_authors)

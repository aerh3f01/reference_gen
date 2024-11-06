import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QTextEdit
from reference_types import (BookReference, JournalReference, WebsiteReference, LivePerformanceReference,
                             AIReference, ComputerGameReference, StatutoryReference, PodcastReference,
                             LegalCaseReference, GovernmentReference, SocialMediaReference)

REFERENCE_TYPES = {
    "Book": BookReference,
    "Journal Article": JournalReference,
    "Website": WebsiteReference,
    "Live Performance": LivePerformanceReference,
    "Generative AI (e.g., ChatGPT)": AIReference,
    "Computer Game": ComputerGameReference,
    "Statutory Instrument": StatutoryReference,
    "Podcast": PodcastReference,
    "Legal Case": LegalCaseReference,
    "Government Publication": GovernmentReference,
    "Social Media Post": SocialMediaReference,
}

class ReferenceGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("USW Harvard Reference Generator")
        self.resize(500, 600)
        
        # Dropdown to select reference type
        self.ref_type_label = QLabel("Select Reference Type:")
        self.ref_type_dropdown = QComboBox()
        self.ref_type_dropdown.addItems(REFERENCE_TYPES.keys())
        self.ref_type_dropdown.currentTextChanged.connect(self.display_fields)

        # Layout for input fields and output
        self.fields_layout = QVBoxLayout()
        self.generate_button = QPushButton("Generate Reference")
        self.generate_button.clicked.connect(self.generate_reference)
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.ref_type_label)
        main_layout.addWidget(self.ref_type_dropdown)
        main_layout.addLayout(self.fields_layout)
        main_layout.addWidget(self.generate_button)
        main_layout.addWidget(self.output_box)
        self.setLayout(main_layout)
        
        self.current_ref_type = None
        self.display_fields()

    def display_fields(self):
        # Clear existing fields
        for i in reversed(range(self.fields_layout.count())):
            widget = self.fields_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Get the selected reference type class
        ref_type = self.ref_type_dropdown.currentText()
        self.current_ref_type = REFERENCE_TYPES[ref_type]()
        
        # Display fields for the selected reference type
        for label_text, field_name in self.current_ref_type.fields():
            label = QLabel(label_text)
            field = QLineEdit()
            field.setObjectName(field_name)
            self.fields_layout.addWidget(label)
            self.fields_layout.addWidget(field)

    def generate_reference(self):
        # Gather input values
        data = {self.fields_layout.itemAt(i).widget().objectName(): 
                self.fields_layout.itemAt(i).widget().text() for i in range(1, self.fields_layout.count(), 2)}

        # Generate in-text citation and full reference
        if self.current_ref_type:
            citation = self.current_ref_type.cite_in_text(data)
            full_reference = self.current_ref_type.full_reference(data)
            self.output_box.setText(f"In-Text Citation:\n{citation}\n\nFull Reference:\n{full_reference}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReferenceGenerator()
    window.show()
    sys.exit(app.exec())

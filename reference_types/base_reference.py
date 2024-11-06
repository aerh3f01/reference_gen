# reference_types/base_reference.py
class BaseReference:
    def fields(self):
        """Return a list of field labels and field names specific to this reference type."""
        raise NotImplementedError("Subclasses should implement this method.")

    def cite_in_text(self, data):
        """Generate an in-text citation."""
        raise NotImplementedError("Subclasses should implement this method.")

    def full_reference(self, data):
        """Generate a full reference entry."""
        raise NotImplementedError("Subclasses should implement this method.")

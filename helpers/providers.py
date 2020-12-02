
class FieldNameProvider:
    """Provides the function to return a display-friendly name for the error summary in the View"""    
    def __init__(self):
        self.names = {
            "first-name" : "First Name",
            "second-name" : "Second Name",
            "country" : "Country"
        }
    
    def get_name(self, field_name):
        return self.names[field_name]
    
    def __str__(self):
        return "A dictionary of display-friendly field names, use get_name([field_name]) to access"

    def __repr__(self):
        return "FieldNameProvider()"

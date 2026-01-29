from allauth.account.forms import SignupForm, LoginForm
from django import forms


class CustomSignupForm(SignupForm):
    """Custom signup form with Bootstrap styling"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field.label:
                field.widget.attrs['placeholder'] = str(field.label)


class CustomLoginForm(LoginForm):
    """Custom login form with Bootstrap styling"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field.label:
                field.widget.attrs['placeholder'] = str(field.label)

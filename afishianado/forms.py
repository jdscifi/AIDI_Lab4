from django import forms

SPECIES = [("Bream", "Bream"), ("Roach", "Roach"), ("Whitefish", "Whitefish"), ("Parkki", "Parkki"), ("Perch", "Perch"),
           ("Pike", "Pike"), ("Smelt", "Smelt")]


# creating a form
class InputForm(forms.Form):
    species = forms.ChoiceField(choices=SPECIES)
    vertical_length = forms.DecimalField(decimal_places=2)
    diagnal_length = forms.DecimalField(decimal_places=2)
    cross_length = forms.DecimalField(decimal_places=2)
    height = forms.DecimalField(decimal_places=2)
    width = forms.DecimalField(decimal_places=2)

from django import forms
from .models import Post

class NameForm(ModelForm):
    def __init__(self, *args, **kwargs):
          super(NameForm, self).__init__(*args, **kwargs)
          self.fields['name'].error_messages['required'] = 'Testing'

    class Meta:
        model = Player
        fields = ['name']
        widgets = {'name': forms.TextInput(
                     attrs={'id': 'player_name', 'required': True, 'placeholder': 'Player name...','value':'player1','title':'write here your name'})}

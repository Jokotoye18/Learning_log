from django import forms
from .models import Topic, Entry

class NewLogForm(forms.ModelForm):
    entry = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your entry'}), max_length=2000, help_text='2000 character max')
    class Meta:
        model = Topic
        fields = ['topic', 'entry']
        widgets = {'topic':forms.TextInput(attrs={'placeholder':'Topic'})}


class NewEntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['entry']
        widgets = {'entry':forms.Textarea(attrs={'placeholder':'Entry'})}
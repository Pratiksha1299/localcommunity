from django import forms
from .models import Post

class SearchForm(forms.Form):
    search = forms.CharField(required=False,min_length=3)
    search_in= forms.ChoiceField(required=False,
                                choices=(
                                        ("name","Name"),
                                         ("provider","Provider")
                                    ))
class ServiceForm(forms.ModelForm):
    cover=forms.ImageField(help_text="Upload Image",required=False)
    class Meta:
        model= Post
        fields = ['name','provider','provider_contact','slug','price','cover']



class ContactForm(forms.Form):
    from_mail=forms.EmailField(required=True)
    subject= forms.CharField(required=True)
    message= forms.CharField(widget=forms.Textarea,required=True)






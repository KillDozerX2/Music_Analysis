from django import forms


from models import Request,Author_request,Song


class Request_form(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            "Song_name",
            "Artist",
            "Message",
        ]


class Author_request_form(forms.ModelForm):
    class Meta:
        model = Author_request
        fields = [
            "Name",
            "Email",
        ]


class Song_form(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            "Artist",
            "Genre",
            "Album",
            "Title",
            "Image_src",
            "IntroDetails",
            "Verse1Details",
            "Verse2Details",
            "OutroDetails",
        ]
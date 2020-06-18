from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label='name', max_length=16,
                           error_messages={'required': "So mysterious", 'max_length': "too long"})

    email = forms.CharField(label='email', error_messages={'required': "Please provide your email addr",
                                                           'invalid': 'Wrong format'})

    content = forms.CharField(label='content', error_messages={'required': 'Please write your comment',
                                                               'max_length': 'too long'})

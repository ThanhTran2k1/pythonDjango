from django import forms

class registerForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class loginForm(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "class" : "form-input",
        "placeholder" : "Tên đăng nhập"
    }))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        "class" : "form-input",
        "placeholder" : "Mật khẩu"
    }))



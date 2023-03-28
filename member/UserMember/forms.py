from django import forms

class registerForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        "class": "form-control form-label",
        "placeholder": "Tên đăng nhập"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "form-control form-label",
        "placeholder": "Email"
    }))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        "type": "password",
        "id": "form3Example4c",
        "class": "form-control form-label ",
        "placeholder": "Mật khẩu"
    }))
    repeatPass = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        "type": "password",
        "id": "form3Example4c",
        "class": "form-control form-label ",
        "placeholder": "Nhập lại mật khẩu"
    }))



class loginForm(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={
        "class" : "form-input tendn",
        "placeholder" : "Tên đăng nhập"

    }))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={
        "class" : "form-input recss",
        "placeholder" : "Mật khẩu"
    }))



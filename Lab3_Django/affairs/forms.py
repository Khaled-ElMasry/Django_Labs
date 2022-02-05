from django import forms

from affairs.models import Student


class InsertForm(forms.Form):
    gender = [("male", "male"),
              ("female", "female")]
    # student_id = forms.AutoField(primary_key=True)
    student_fname = forms.CharField(max_length=10, label="fname")
    student_lname = forms.CharField(max_length=10)
    student_email = forms.EmailField()
    student_gender = forms.ChoiceField(choices=gender)


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

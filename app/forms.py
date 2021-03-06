from wtforms import Form, TextField, TextAreaField, SubmitField, FileField, SelectField, validators
 
class ProfileForm(Form):
    uploadedfile = FileField("File")
    username = TextField("UserName",[validators.Required()])
    firstname = TextField("FirstName",[validators.Required()])
    lastname = TextField("LastName",[validators.Required()])
    age = TextField("Age",[validators.Required()])
    sex = SelectField("Sex",choices=[("Male","Male"),("Female","Female")])
    userbio = TextField("Bio",[validators.Required()])
    submit = SubmitField("Send")
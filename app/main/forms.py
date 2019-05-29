from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required, Length


class PostForm(FlaskForm):
    CATEGORIES=[('SALES PITCH', 'SALES PITCH'), ('BUSINESS PITCH', 'BUSINESS PITCH'), ('MUSIC PITCH', 'MUSIC PITCH'), ('ELEVATOR PITCH', 'ELEVATOR PITCH')]
    category=SelectField("Categories",choices=CATEGORIES)
    post=TextAreaField("Post",validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
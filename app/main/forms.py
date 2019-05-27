from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required, Length


class PostForm(FlaskForm):
    CATEGORIES=[('sales pitch', 'sales pitch'), ('business pitch', 'business pitch'), ('music pitch', 'music pitch'), ('elevator pitch', 'elevator pitch')]
    category=SelectField("categories",choices=CATEGORIES)
    post=TextAreaField("Post",validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    title = StringField('Comment category', validators=[Required()])
    comment = TextAreaField('Pitches comment')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
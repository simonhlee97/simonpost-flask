from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    # content = TextAreaField('Content', validators=[DataRequired()])
    pagedowncontent = PageDownField('Blog post', validators=[DataRequired()])
    submit = SubmitField('Post')
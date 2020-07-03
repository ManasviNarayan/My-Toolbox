from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField,SelectField,TextField,
                    TextAreaField,SubmitField, IntegerField, FloatField)
from wtforms.validators import DataRequired


class FormElements(FlaskForm):

    text_input = StringField()
    int_input = IntegerField()
    int_input2 = IntegerField()
    int_input3 = IntegerField()
    get = SubmitField('GET')
    check = SubmitField('CHECK')

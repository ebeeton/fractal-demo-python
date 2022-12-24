""" Forms for the application. """
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class FractalForm(FlaskForm):
    """ WTForm for fractal parameter input. """
    max_iter = IntegerField('Maximum Iterations',
                            default=100,
                            validators=[DataRequired(),
                                        NumberRange(min=10, max=1000)])
    width = IntegerField('Width (pixels)',
                         default=512,
                         validators=[DataRequired(),
                                     NumberRange(min=128, max=32768)])
    height = IntegerField('Height (pixels)',
                          default=512,
                          validators=[DataRequired(),
                                      NumberRange(min=128, max=32768)])
    submit = SubmitField('Plot')

# -*- coding: utf-8 -*-
import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd

from utils import *

from fileselect import *
from analysisselect import *
from plotinfoselect import *
from ackandcreators import *
from mylayouts import *
from myinput import *
from radioitems import *
from upload import *
from droplist import *
from button import *
from image import *

texts = {
    'title': 'Gluettery',
    'introduction': ['Welcome to the Gluettery platform.',
                    'This platform was created in order to facilitate and stimulate the production of interactive graphics of battery-related data. ',
                    'As an open source platform, all collaboration and tips are more than welcome. ',
                    '\"Obrigado e de nada\"! '],
}

def Title_and_Introduction():
    return html.Div(
        children = [
            html.Div(
                children=[TitleLeftHTML(texts['title'])],
                style={ 'width': '100%', 'height': '100%',
                'backgroundColor': colors['background'],
                'backgroundImage': 'url(https://www.everynation.org/wp-content/uploads/2018/02/Monthly-Website-Header-background.jpg)'},
            ),
            html.Div(
                children=[
                    SubTitleBoldHTML(texts['introduction'][0]),
                    SubTitleHTML(texts['introduction'][1]),
                    SubTitleHTML(texts['introduction'][2]),
                    SubTitleBoldHTML(texts['introduction'][3]),
                ], style={ 'width': '60%', 'height': '95%',
                    'marginLeft': '20%',
                    'marginRight': '20%',
                    'marginTop': '5%',
                    'borderWidth': '1px',
                    'borderStyle': 'outset',
                    'borderRadius': '5px',
                    'backgroundColor': colors['background'],
                }, 
        )],
        style = {
                'width': '100%', 'height': '100%',
        }
    )
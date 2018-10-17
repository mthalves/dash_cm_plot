# -*- coding: utf-8 -*-
import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
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
    'title': 'C&M',
    'introduction': ['Welcome to the C & M platform.',
                    'This platform was created in order to facilitate and stimulate the production of interactive graphics of battery-related data. ',
                    'As an open source platform, all collaboration and tips are more than welcome. ',
                    '\"Obrigado e de nada\"! '],
}

def Title_and_Introduction():
    return html.Div([
        html.Div(
            TitleLeftHTML(texts['title']),
            style={ 'width': '100%', 'height': '100%',
            'backgroundColor': colors['background'],
            'backgroundImage': 'url(https://purduenext.purdue.edu/sites/prdnext/files/ce.poly_.m1_header._v2.jpg)'},
        ),
        html.Div([
            SubTitleBoldHTML(texts['introduction'][0]),
            SubTitleBoldHTML(texts['introduction'][1]),
            SubTitleBoldHTML(texts['introduction'][2]),
            SubTitleBoldHTML(texts['introduction'][3]),
        ],style={ 'width': '90%', 'height': '95%',
            'marginLeft': '10%',
            'marginTop': '2.5%',
            'marginBot': '2.5%',
            'backgroundColor': colors['background'],}
            )
    ])
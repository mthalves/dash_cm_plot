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
    'section': '2. Select your analysis',
    'subseca': 'a) Data analysis',
    'subsecb': 'b) Data and Cycle Type',
}

def Select_Analysis():
    return html.Div([
        SectionHTML(texts['section']),
        SubsectionHTML(texts['subseca']),
        DroplistHTML('analysis-dropdown',
        			[{'label': 'Differential Voltage Analysis (DVA)', 'value': 'DVA'},
                    {'label': 'Coulombic Efficiency (CE)', 'value': 'CE'}],
                    'DVA'),
        SubsectionHTML(texts['subsecb']),
        RadioItemsHTML(),
    ])
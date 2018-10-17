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

def ButtonHTML(text_,id_):
    return html.Div(
            children=[html.Button(text_, 
                id=id_,
                style={
                    'height': '100%',
                    'width': '100%',
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'normal',
                    'marginTop': '35px',
                },
            ),],
            style={'textAlign': 'center'},
        )
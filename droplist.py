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

def DroplistHTML(id_,options,value):
    return html.Div([
            dcc.Dropdown(
                id= id_,
                style = {
                    'width': '100%',
                    'textAlign': 'left',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'normal',
                },
                options= options,
                value= value,
                clearable=False,
            )],
            style = {
                'textAlign': 'left',
                'width': '100%',
            },
        )
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
    'subsecb': 'b) Cycles',
    'subsecc': 'c) Data and Cycle Type',
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
        InputTextHTML('cycles-input','Select Cycles to evaluate... single: "1", multi: "1, 3, 5", range: "1-5"'),
        SystemAnswerHTML('Selected Cycles = Empty','cycles-select')
    ])

def Select_Analysis_Radio(radio_flag,radio):
    if radio_flag:
        return html.Div(
            id = 'analysis-radio',
            children = [
                SubsectionHTML(texts['subsecc']),
                RadioItemsHTML(radio_flag,radio)
            ])
    else:
        return html.Div(
            id = 'analysis-radio',
            children = [
                RadioItemsHTML(radio_flag,radio)
            ])
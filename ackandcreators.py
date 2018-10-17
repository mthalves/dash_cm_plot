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

from mylayouts import *
from myinput import *
from radioitems import *
from upload import *
from droplist import *
from button import *
from image import *

images = {
    'alana': base64.b64encode(open('img/alana.png', 'rb').read()),
    'caio': base64.b64encode(open('img/caio.png', 'rb').read()),
    'micanga': base64.b64encode(open('img/micanga.png', 'rb').read())
}

texts = {
    'bye': 'Thanks to use C&M',
    'creators': 'CREATORS',
    'alana': ['Technical expertise in Interfacial electrochemistry, Electrocatalysis, Development and Characterization of materials for energy conversion/storage. Project Design and Management.'],
    'caio': ['<TO DO>'],
    'micanga': ['Computer Science researcher currently working with Cooperative Game Theory. Diverse background and interest in the hottest areas (e.g., Data Forecasting and Problem Design).'],
}

def Acknowledgment_and_Creators():
    column1 = [ImageHTML(images['alana']),SubTitleBoldHTML('Alana Aragon Zulke'),ParagraphHTML(texts['alana'])]
    column2 = [ImageHTML(images['caio']),SubTitleBoldHTML('Caio Ferreira Bernardo'),ParagraphHTML(texts['caio'])]
    column3 = [ImageHTML(images['micanga']),SubTitleBoldHTML('Matheus Ap. do Carmo Alves'),ParagraphHTML(texts['micanga'])]
    return html.Div(style={ 'width': '100%', 'height': '100%',
            'backgroundColor': colors['background'],},
        children = [
        Title2HTML(texts['bye']),
        Title2HTML(texts['creators']),
        ThreeColumnsHTML([column1,column2,column3]),
    ])
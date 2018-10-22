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
    'bye': 'Thanks to use Anattery',
    'creators': 'CREATORS',
    'alana': ['Technical expertise in Interfacial electrochemistry, Electrocatalysis, Development and Characterization of materials for energy conversion/storage. Project Design and Management.'],
    'caio': ['<TO DO>'],
    'micanga': ['Computer Science researcher currently working with Cooperative Game Theory. Diverse background and interest in the hottest areas (e.g., Data Forecasting and Problem Design).'],
}

def Acknowledgment_and_Creators():
    column1 = [ImageHTML(images['alana']),SubTitleWhiteBoldHTML('Alana Aragon Zulke'),html.Div(ParagraphHTML(texts['alana']),style={ 'width': '90%', 'height': '90%',
                    'marginLeft': '5%',
                    'marginRight': '5%',
                    'marginTop': '5%',
                    'marginBottom': '5%',
                    'borderWidth': '1px',
                    'borderStyle': 'outset',
                    'borderRadius': '5px',
                    'backgroundColor': colors['background'],
                })]
    column2 = [ImageHTML(images['caio']),SubTitleWhiteBoldHTML('Caio Ferreira Bernardo'),html.Div(ParagraphHTML(texts['caio']),style={ 'width': '90%', 'height': '90%',
                    'marginLeft': '5%',
                    'marginRight': '5%',
                    'marginTop': '5%',
                    'marginBottom': '5%',
                    'borderWidth': '1px',
                    'borderStyle': 'outset',
                    'borderRadius': '5px',
                    'backgroundColor': colors['background'],
                })]
    column3 = [ImageHTML(images['micanga']),SubTitleWhiteBoldHTML('Matheus Ap. do Carmo Alves'),html.Div(ParagraphHTML(texts['micanga']),style={ 'width': '90%', 'height': '90%',
                    'marginLeft': '5%',
                    'marginRight': '5%',
                    'marginTop': '5%',
                    'marginBottom': '5%',
                    'borderWidth': '1px',
                    'borderStyle': 'outset',
                    'borderRadius': '5px',
                    'backgroundColor': colors['background'],
                })]
    return html.Div(style={ 'width': '100%', 'height': '100%',
            'backgroundColor': colors['background'],
            'backgroundImage': 'url(https://www.everynation.org/wp-content/uploads/2018/02/Monthly-Website-Header-background.jpg)'},
        children = [
        Title2WhiteHTML(texts['bye']),
        Title2WhiteHTML(texts['creators']),
        ThreeColumnsHTML([column1,column2,column3]),
    ])
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
    'section': '1. Select your file',
}

def Select_File():
    return html.Div(
    			[html.Div(
    				[SectionHTML(texts['section'])],
        			style={ 'width': '100%', 
        					'height': '100%',
            				'backgroundColor': colors['background'],
            				}
            		),
    			html.Div(
    				[UploadHTML()],
        			style={ 'width': '50%', 
        					'height': '100%',
            				'backgroundColor': colors['background'],
            				'marginLeft': '25%', 'marginRight': '25%'
            				}
            		)]
    			)
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

from ackandcreators import *
from mylayouts import *
from myinput import *
from radioitems import *
from upload import *
from droplist import *
from button import *
from image import *

texts = {
	'section': '3. Enter your plot information',
	'subseca': 'a) Plot Title',
	'subsecb': 'b) X Label',
	'subsecc': 'c) Y Label',
}

def Select_Plot_Information():
	column1 = [SubsectionCenterHTML(texts['subseca']),InputTextHTML('title-input','Title here...')]
	column2 = [SubsectionCenterHTML(texts['subsecb']),InputTextHTML('xlabel-input','X label here...')]
	column3 = [SubsectionCenterHTML(texts['subsecc']),InputTextHTML('ylabel-input','Y label here...')]
	return html.Div([
		SectionHTML(texts['section']),
		ThreeColumnsHTML([column1,column2,column3]),
	])
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

from myinput import *
from radioitems import *
from upload import *
from droplist import *
from button import *
from image import *

def TitleHTML(children):
	return html.H1(
            children=children,
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '64',
                'fontWeight': 'bold',
                'marginTop': '35px',
                'marginBot': '35px'
            }
		)

def Title2HTML(children):
    return html.H1(
            children=children,
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '32',
                'fontWeight': 'bold',
                'marginTop': '35px',
                'marginBot': '35px'
            }
        )

def TitleLeftHTML(children):
    return html.H1(
            children=children,
            style={
                'width': '80%', 'height': '100%',
                'textAlign': 'left',
                'color': '#FFFFFF',
                'fontFamily': 'Roboto Condensed',
                'fontSize': '100',
                'fontWeight': 'bold',
                'marginLeft': '20%',
            }
        )

def SubTitleHTML(children):
	return html.P(
            children= children, 
            style={
                'width': '90%', 'height': '100%',
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '18',
                'fontWeight': 'normal',
                'marginLeft': '5%',
                'marginRight': '5%',
            }
        )

def SubTitleBoldHTML(children):
    return html.P(
            children= children, 
            style={
                'width': '90%', 'height': '100%',
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '18',
                'fontWeight': 'bold',
                'marginLeft': '5%',
                'marginRight': '5%',
            },
        )

def SectionHTML(children):
	return html.H1(
            children= children,
            style={
                'textAlign': 'left',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '24',
                'fontWeight': 'bold',
                'marginLeft': '35px',
                'marginTop': '35px',
            }
        )

def SectionCenterHTML(children):
    return html.H1(
            children= children,
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '24',
                'fontWeight': 'bold',
                'marginTop': '35px',
            }
        )

def SubsectionHTML(children):
	return html.H1(
            children= children,
            style={
                'textAlign': 'left',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '20',
                'fontWeight': 'bold',
                'marginLeft': '35px',
                'marginTop': '15px',
            }
        )

def SubsectionCenterHTML(children):
    return html.H1(
            children= children,
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '20',
                'fontWeight': 'bold',
                'marginTop': '15px',
            }
        )

def ParagraphHTML(children):
	return html.P(
            children= children, 
            style={
                'textAlign': 'justify',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '18',
                'fontWeight': 'normal',
                'margin': '35px',
            }
        )

def ThreeColumnsHTML(children):
    return html.Div([
            html.Div(children=children[0],
                style={'textAlign': 'center','width': '33%', 'display': 'inline-block'}),
            html.Div(children=children[1],
                style={'textAlign': 'center','width': '33%', 'display': 'inline-block'}),
            html.Div(children=children[2],
                style={'textAlign': 'center','width': '33%', 'display': 'inline-block'}),
        ])
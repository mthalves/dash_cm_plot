# -*- coding: utf-8 -*-
# System and Standard Libraries
import base64
import datetime
import io
import re
from copy import deepcopy

# Dash Python - HTML Interface Libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event
import pandas as pd

# Dash Python - My HTML Interface
from header import *
from body import *
from footpage import *

# Protocols, Plots and Utils
import Novonix_Protocol

# Dash External Style Import
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Global variables
file = []
last_n_clicks = 0

# Main Layout
app.layout = html.Div(
    style={'width': '100%', 'height': '100%',
        'backgroundColor': colors['background'],
        'backgroundImage': 'url(https://i.redd.it/ev89ehtc0o2x.png)'
    }, 
    children=[
        # Header Layout
        Header(),

        # Body Layout
        BodyIntro(),
        Body(),
        
        # Footpage Layout
        FootPage(),
    ]
)

# Callbacks
def get_csv(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')),
                error_bad_lines = False)
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(
                io.BytesIO(decoded),
                error_bad_lines = False)
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    print(df)
    return df.to_dict('records')

@app.callback(Output(component_id='output-data-upload', component_property='children'),
                  [Input(component_id='upload-data', component_property='contents')],
                  [State('upload-data', 'filename'),
                   State('upload-data', 'last_modified')])
def file_callback(list_of_contents, list_of_names, list_of_dates):
    print(list_of_names)
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        
        global file
        file = get_csv(list_of_contents[0], list_of_names[0], list_of_dates[0])

        return children 

@app.callback(Output(component_id='analysis-radio',component_property='children'),
                [Input(component_id='analysis-dropdown',component_property='value')],
                [State('type-radioitems','value')],
                [Event('type-radioitems','change')])
def dropdown_callback(value,radio):
    if value == 'CE':
        return Select_Analysis_Radio(False,'A')
    elif value == 'DVA':
        return Select_Analysis_Radio(False,'A')

def regex_format(text):
    formated = ''
    for c in text:
        if c == '-' and len(formated) > 0 and formated[-1].isdigit():
            formated += c
        elif c == ',' and len(formated) > 0 and formated[-1].isdigit():
            formated += c
        elif re.match('\d',c) != None:
            formated += c
    print formated
    return formated

@app.callback(Output(component_id='cycles-select',component_property='children'),
                [Input(component_id='cycles-input',component_property='value')],
                [],
                [])
def cycles_callback(input_):
    print 'trigged', input_
    formated = regex_format(deepcopy(input_))
    print '>>',formated

    if re.match("^\s*$",input_) != None:
        return 'Selected Cycles = Empty'
    if re.match("^([\d]+\s*[\,\-]{0,1}\s*)+$",input_) != None:
        return 'Selected Cycles = ',formated
    else:
        return 'Selected Cycles = Invalid Format'


def plot_callback(dropdown,title,xlabel,ylabel,cycles):
    global file
    if dropdown == 'CE':
        return Novonix_Protocol.CoulombicEfficiency(file,title,xlabel,ylabel)
    elif dropdown == 'DVA':
        return Novonix_Protocol.DVA(file,title,xlabel,ylabel,cycles)

@app.callback(   
    Output(component_id='plot_click', component_property='children'),
    [Input('plot_button','n_clicks'),
     Input('analysis-dropdown','value'),
     Input('title-input','value'),
     Input('xlabel-input','value'),
     Input('ylabel-input','value'),
     Input('cycles-input','value')])
def refresh_callback(n_clicks,value,title,xlabel,ylabel,cycles):
    global last_n_clicks
    if n_clicks == 0:
        return None
    elif last_n_clicks != n_clicks:
        last_n_clicks = n_clicks
        return plot_callback(value,title,xlabel,ylabel,cycles)

if __name__ == '__main__':
    app.run_server(debug=True)
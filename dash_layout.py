# -*- coding: utf-8 -*-
import base64
import datetime
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event

import pandas as pd

from utils import *

from title import *
from fileselect import *
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

import Novonix_Protocol

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

file = []
last_n_clicks = 0
ratio_flag = False

app.layout = html.Div(
    style={'width': '100%', 'height': '100%',
        'backgroundColor': colors['background'],
        'backgroundImage': 'url(https://i.redd.it/ev89ehtc0o2x.png)'
    }, 
    children=[
        # Header Layout
        Title_and_Introduction(),

        # Body Layout
        html.Div(
            children = [
                Select_File(),
                Select_Analysis(),
                Select_Analysis_Ratio(ratio_flag),
                Select_Plot_Information(),
                ButtonHTML('PLOT','plot_button'),
                html.Div(id='plot_click'),
            ], style={ 'width': '60%', 'height': '95%',
                    'marginLeft': '20%',
                    'marginRight': '20%',
                    'marginTop': '5%',
                    'borderWidth': '1px',
                    'borderStyle': 'outset',
                    'borderRadius': '5px',
                    'backgroundColor': colors['background'],
                }, 
        ),
        
        # Footpage Layout
        Acknowledgment_and_Creators(),
    ]
)

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

def plot_callback(dropdown):
    global file
    if dropdown == 'CE':
        return Novonix_Protocol.CoulombicEfficiency(file)
    elif dropdown == 'DVA':
        return Novonix_Protocol.DVA(file,[5,10])

@app.callback(   
    Output(component_id='plot_click', component_property='children'),
    [Input('plot_button','n_clicks'),
     Input('analysis-dropdown','value')])
def refresh_callback(n_clicks,value):
    global last_n_clicks
    if n_clicks == 0:
        return None
    elif last_n_clicks != n_clicks:
        last_n_clicks = n_clicks
        return plot_callback(value)

if __name__ == '__main__':
    app.run_server(debug=True)
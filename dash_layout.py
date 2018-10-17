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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    style={ 'width': '100%', 'height': '100%',
            'backgroundColor': colors['background'],}, 
    children=[
        Title_and_Introduction(),
        Select_File(),
        Select_Analysis(),
        Select_Plot_Information(),
        ButtonHTML('PLOT','plot_button'),
        Acknowledgment_and_Creators(),
    ],
)

@app.callback(Output('output-data-upload', 'children'),
                  [Input('upload-data', 'contents')],
                  [State('upload-data', 'filename'),
                   State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children 

if __name__ == '__main__':
    app.run_server(debug=True)
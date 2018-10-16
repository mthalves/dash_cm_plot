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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

alana_img = base64.b64encode(open('alana.png', 'rb').read())
caio_img = base64.b64encode(open('caio.png', 'rb').read())
micanga_img = base64.b64encode(open('micanga.png', 'rb').read())

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

texts = {
    'introduction': ['Welcome to the C & M platform.',
                    'This platform was created in order to facilitate and stimulate the production of interactive graphics of battery-related data. ',
                    'As an open source platform, all collaboration and tips are more than welcome. ',
                    '\"Obrigado e de nada\"! '],
    'alana': ['Technical expertise in Interfacial electrochemistry, Electrocatalysis, Development and Characteriza- tion of materials for energy conversion/storage. Project De- sign and Management.'],
    'caio': ['<TO DO>'],
    'micanga': ['Computer Science researcher currently working with Coop- erative Game Theory. Diverse background and interest in the hottest areas (e.g., Data Fore- casting and Problem Design).'],
}

app.layout = html.Div(
    style={'backgroundColor': colors['background']}, 
    children=[
        ###########################################
        #
        # 1. TITLE
        #
        ###########################################
        html.H1(
            children='C&M',
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '64',
                'fontWeight': 'bold'
            }
        ),

        ###########################################
        #
        # 2. INTRODUCTION TEXT
        #
        ###########################################
        html.P(
            children= texts['introduction'][0], 
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '18',
                'fontWeight': 'normal'
            }
        ),
        html.P(
            children= [texts['introduction'][1]],
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '18',
                'fontWeight': 'normal'
            }
        ),
        html.P(
            children= [texts['introduction'][2]],
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '18',
                'fontWeight': 'normal'
            }
        ),
        html.P(
            children= [texts['introduction'][3]],
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '18',
                'fontWeight': 'normal'
            }
        ),

        ###########################################
        #
        # FILE SELECTION
        #
        ###########################################
        html.H1(
            children='1. Select your file',
            style={
                'textAlign': 'left',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '24',
                'fontWeight': 'bold',
                'marginLeft': '35px',
                'marginTop': '35px',
            }
        ),

        dcc.Upload(
            id='upload-data',
            children=html.Div([
                '\"Drag and Drop\" or ',
                html.A('Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'fontFamily': 'Roboto Condensed',
                'fontSize': '18',
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Div(id='output-data-upload'),

        ###########################################
        #
        # SELECT YOUR ANALYSIS
        #
        ###########################################
        html.H1(
            children='2. Select your analysis',
            style={
                'textAlign': 'left',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '24',
                'fontWeight': 'bold',
                'marginLeft': '35px',
                'marginTop': '50px',
            }
        ),


        html.H1(
            children='a) Data analysis',
            style={
                'textAlign': 'left',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '20',
                'fontWeight': 'bold',
                'marginLeft': '35px',
                'marginTop': '15px',
            }
        ),

        html.Div([
            dcc.Dropdown(
                id='analysis-dropdown',
                style = {
                    'width': '87%',
                    'textAlign': 'left',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'normal',
                    'marginLeft': '15px',
                },
                options=[
                    {'label': 'Differential Voltage Analysis (DVA)', 'value': 'DVA'},
                    {'label': 'Coulombic Efficiency (CE)', 'value': 'CE'}
                ],
                value='DVA',
                clearable=False,
            )
        ]),

        html.H1(
            children='b) Data and Cycle Type',
            style={
                'textAlign': 'left',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '20',
                'fontWeight': 'bold',
                'marginLeft': '35px',
                'marginTop': '35px',
            }
        ),
        html.Div([
            dcc.RadioItems(
                id='type-radioitems',
                style = {
                    'textAlign': 'left',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'normal',
                    'marginLeft': '35px',
                },
                options=[
                    {'label': 'Charge', 'value': 'C'},
                    {'label': 'Discharge', 'value': 'D'},
                    {'label': 'Full Cycle', 'value': 'F'},
                    {'label': 'All Data', 'value': 'A'},
                ],
                value='A',
                labelStyle={
                    'display': 'inline-block',
                    'paddingRight': '15px'
                    }
            )
        ]),

        ###########################################
        #
        # PLOT INFORMATION
        #
        ###########################################
        html.H1(
            children='3. Enter your plot information',
            style={
                'textAlign': 'left',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '24',
                'fontWeight': 'bold',
                'marginLeft': '35px',
                'marginTop': '50px',
            }
        ),

        html.Div([
            # DIV A ----------------------------------------
            html.Div([
                html.H1(
                    children='a) Plot Title',
                    style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'fontFamily': 'Roboto Condensed',
                        'fontSize': '20',
                        'fontWeight': 'bold',
                        'marginLeft': '35px',
                        'marginTop': '10px',
                    }
                ),

                dcc.Input(
                        id= 'title-input',
                        inputmode= 'latin-english',
                        minlength = 1,
                        maxlength = 30,
                        placeholder='Title here...',
                        spellcheck = True,
                        style={
                            'textAlign': 'left',
                            'color': colors['text'],
                            'fontFamily': 'Roboto Condensed',
                            'fontSize': '18',
                            'fontWeight': 'normal',
                            'marginLeft': '35px',
                        },
                        type='text',
                        value=''
                ),
            ], className='three columns'),

            # DIV B ----------------------------------------
            html.Div([
                html.H1(
                    children='b) X Label',
                    style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'fontFamily': 'Roboto Condensed',
                        'fontSize': '20',
                        'fontWeight': 'bold',
                        'marginLeft': '35px',
                        'marginTop': '10px',
                    }
                ),

                dcc.Input(
                    id= 'xlabel-input',
                    inputmode= 'latin-english',
                    minlength = 1,
                    maxlength = 30,
                    placeholder='X label here...',
                    spellcheck = True,
                    style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'fontFamily': 'Roboto Condensed',
                        'fontSize': '18',
                        'fontWeight': 'normal',
                        'marginLeft': '35px',
                    },
                    type='text',
                    value=''
                )
            ], className='three columns'),

            # DIV C ----------------------------------------
            html.Div([
                html.H1(
                    children='c) Y Label',
                    style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'fontFamily': 'Roboto Condensed',
                        'fontSize': '20',
                        'fontWeight': 'bold',
                        'marginLeft': '35px',
                        'marginTop': '10px',
                    }
                ),
            
                dcc.Input(
                    id= 'ylabel-input',
                    inputmode= 'latin-english',
                    minlength = 1,
                    maxlength = 30,
                    placeholder='Y label here...',
                    spellcheck = True,
                    style={
                        'textAlign': 'left',
                        'color': colors['text'],
                        'fontFamily': 'Roboto Condensed',
                        'fontSize': '18',
                        'fontWeight': 'normal',
                        'marginLeft': '35px',
                    },
                    type='text',
                    value=''
                ),
            ],className='three columns'),

        ], className='row'),

        ###########################################
        #
        # BUTTONS
        #
        ###########################################
        html.Div(
            children=[html.Button('Plot', 
                id='plot_button',
                style={
                    'width': '100%',
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'normal',
                    'marginTop': '35px',
                },
            ),],
            style={'textAlign': 'center'},
        ),

        ###########################################
        #
        # Contacts and Greetings
        #
        ###########################################
        html.H1(
            children=' Thanks for use C&M !',
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '32',
                'fontWeight': 'bold',
                'marginTop': '40px',
            }
        ),
        html.H1(
            children='CREATORS',
            style={
                'textAlign': 'left',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '32',
                'fontWeight': 'bold',
                'marginLeft': '100px',
            }
        ),

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Img(src='data:image/png;base64,{}'.format(alana_img)),
                        html.H1(
                            children= ['Alana Aragon Zulke'],
                            style={
                                'textAlign': 'center',
                                'color': colors['text'],
                                'fontFamily': 'Roboto Condensed',
                                'fontSize': '18',
                                'fontWeight': 'bold',
                            }
                        ),
                        html.P(
                            children= [texts['alana'][0]],
                            style={
                                'textAlign': 'justify',
                                'color': colors['text'],
                                'fontFamily': 'Roboto Condensed',
                                'fontSize': '18',
                                'fontWeight': 'normal',
                            }
                        ),
                    ],
                    className='three columns',
                ),

                html.Div(
                    children=[
                        html.Img(src='data:image/png;base64,{}'.format(caio_img)),
                        html.H1(
                            children= ['Caio Ferreira Bernardo'],
                            style={
                                'textAlign': 'center',
                                'color': colors['text'],
                                'fontFamily': 'Roboto Condensed',
                                'fontSize': '18',
                                'fontWeight': 'bold',
                            }
                        ),
                        html.P(
                            children= [texts['caio'][0]],
                            style={
                                'textAlign': 'justify',
                                'color': colors['text'],
                                'fontFamily': 'Roboto Condensed',
                                'fontSize': '18',
                                'fontWeight': 'normal',
                            }
                        ),
                    ],
                    className='three columns',
                ),

                html.Div(
                    children=[
                        html.Img(src='data:image/png;base64,{}'.format(micanga_img)),
                        html.H1(
                            children= ['Matheus Ap. do Carmo Alves'],
                            style={
                                'textAlign': 'center',
                                'color': colors['text'],
                                'fontFamily': 'Roboto Condensed',
                                'fontSize': '18',
                                'fontWeight': 'bold',
                            }
                        ),
                        html.P(
                            children= [texts['micanga'][0]],
                            style={
                                'textAlign': 'justify',
                                'color': colors['text'],
                                'fontFamily': 'Roboto Condensed',
                                'fontSize': '18',
                                'fontWeight': 'normal',
                            }
                        ),
                    ],
                    className='three columns',
                ),
            ],
            style={
                'width': '100%',
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Roboto Condensed',
                'fontSize': '32',
                'fontWeight': 'bold',
                'marginLeft': '45px',
            },
            className = 'row',
        )
    ]
)
def parse_contents(contents, filename, date):
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

    return html.Div([
        html.H5(
            children=['Opened file: ',filename],
            style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'normal',
                }
            ),
        html.H6(
            children= ['Opened at: ',datetime.datetime.fromtimestamp(date)],
            style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontFamily': 'Roboto Condensed',
                    'fontSize': '18',
                    'fontWeight': 'bold',
                }
            ),
    ])


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
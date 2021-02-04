import dash_core_components as dcc
import dash_html_components as html
import dash_table
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd
import plotly.express as px
from dash.dependencies import Output, Input, MATCH, State
from app import app
from data.og_data import get_csv_data

layout = html.Div([
    html.H1("oil gas bar chart", style={'text-align': 'center'}),
    dcc.Graph(id='og_bar_chart', figure={}),
])


@app.callback([Output(component_id='og_bar_chart', component_property='figure')],
              [Input(component_property='bar_input', component_id='value')])
def og_b_chart(bar_input):
    data = get_csv_data
    # data = data.groupby('Wl_Status')
    print(data.head())
    bar_fig = px.pie(data_frame=data, names='County', values=['Year', 'Wl_Status'], hole=0.2, template='plotly_dark',
                     title='og bar chart')
    return bar_fig

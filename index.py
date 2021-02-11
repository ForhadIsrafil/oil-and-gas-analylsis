import dash_core_components as dcc
import dash_html_components as html
import dash_table
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd
import plotly.express as px
from dash.dependencies import Output, Input, MATCH, State
import dash_auth
import plotly.graph_objs as go
# from plotly.subplots import make_subplots
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc

# see https://community.plot.ly/t/nolayoutexception-on-deployment-of-multi-page-dash-app-example-code/12463/2?u=dcomfort
# from app import server
from app import app
from flask import request
from data.og_data import get_csv_data

# see https://dash.plot.ly/external-resources to alter header, footer and favicon
# app.index_string = '''
# <!DOCTYPE html>
# <html>
#     <head>
#         {%metas%}
#         <title>New York Oil and Gas Report</title>
#         {%favicon%}
#         {%css%}
#     </head>
#     <body>
#         {%app_entry%}
#         <footer>
#             {%config%}
#             {%scripts%}
#         </footer>
#         <div>New York Oil and Gas Report</div>
#     </body>
# </html>
# '''
from plotly.validators.pie import domain

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # html.Div(dash_auth.create_logout_button(), className='two columns', style={'marginTop': 30}),
    # html.Div(id='page-content'),
    dbc.Row(children=[
        dbc.Col(children=[
            html.H4('Production Summery: 2006 to 2019', className='text-center text-white', ),
            dcc.Graph(id='og_pie_chart1', figure={}, style={'display': 'inline-block'}),
            dcc.Graph(id='og_pie_chart2', figure={}, style={'display': 'inline-block'}),
        ], )
    ],
        style={'display': 'inline-block', 'background-color': '#212529'},
    ),
    dcc.Graph(id='og_bar_chart', figure={}, ),

])


# Update page
# # # # # # # # #

@app.callback(
    [Output('og_pie_chart1', 'figure'), Output('og_pie_chart2', 'figure'), Output('og_bar_chart', 'figure'), ],
    Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/home/':
        data = get_csv_data()
        # data = data.groupby('Wl_Status', as_index=False)
        # print(data.head(10))
        group_data = data.groupby(['Year', 'Completion'], as_index=False).sum()
        pie_fig1 = px.pie(data_frame=group_data, names=['GasProd', 'WaterProd', 'OilProd'],
                          # labels=['GasProd', 'WaterProd', 'OilProd'],
                          hole=0.5,
                          template='plotly_dark',  # presentation
                          # title='Production Summery: 2006 to 2019',
                          width=370, height=400,
                          color_discrete_sequence=px.colors.sequential.Aggrnyl,
                          )

        bar_fig = go.Figure(
            [go.Bar(x=group_data['Year'], y=group_data['Completion'], )])
        return pie_fig1, pie_fig1, bar_fig
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)

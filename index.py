import dash_core_components as dcc
import dash_html_components as html
import dash_table
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd
import plotly.express as px
from dash.dependencies import Output, Input, MATCH, State
import dash_auth

# see https://community.plot.ly/t/nolayoutexception-on-deployment-of-multi-page-dash-app-example-code/12463/2?u=dcomfort
# from app import server
from app import app
from apps import og_bar_chart
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

app.layout = html.Div([
    html.H1("oil gas bar chart", style={'text-align': 'center'}),
    dcc.Location(id='url', refresh=False),
    # html.Div(dash_auth.create_logout_button(), className='two columns', style={'marginTop': 30}),
    html.Div(id='page-content'),
    dcc.Graph(id='og_bar_chart', figure={}),
])


# Update page
# # # # # # # # #
@app.callback(Output('og_bar_chart', 'figure'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/home/':
        data = get_csv_data()
        # data = data.groupby('Wl_Status')
        group_data = data.groupby(['County', 'Year', 'town'], as_index=False).mean()
        bar_fig = px.pie(data_frame=group_data, names='Year', values='County', hole=0.2,
                         template='plotly_dark',
                         title='og bar chart')
        return bar_fig
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)

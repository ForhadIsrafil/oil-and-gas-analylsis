import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as ex

import dash_auth

# see https://community.plot.ly/t/nolayoutexception-on-deployment-of-multi-page-dash-app-example-code/12463/2?u=dcomfort
# from app import server
from app import app
from apps import og_bar_chart
from flask import request


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
    dcc.Location(id='url', refresh=False),
    # html.Div(dash_auth.create_logout_button(), className='two columns', style={'marginTop': 30}),
    html.Div(id='page-content')
])


# Update page
# # # # # # # # #
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home/':
        return og_bar_chart.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)

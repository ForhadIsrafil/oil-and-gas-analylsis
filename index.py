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

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    ######-------- 1st row start ---------######
    dbc.Row([
        dbc.Col(children=[html.Img(src='assets/dash-logo.png', height=100, width=200)],
                width={'size': 4}),
        dbc.Col(children=[html.H4("New York Oil and Gas",
                                  ),
                          html.H6("Production Overview",
                                  )],
                className='text-center',style={'color': '#255464'},
                width={'size': 4}),

    ],
        style={'font-size': 10},
        className='pt-5'),
    ######-------- 1st row end ---------######

    ######-------- 2nd row start ---------######
    dbc.Row([

        dbc.Col(children=[html.H6("Filter by construction date (or select range in histogram):",
                                  ),
                          dcc.RangeSlider(
                              id='my-range-slider',
                              min=0,
                              max=20,
                              step=0.5,
                              value=[5, 10]

                          ),
                          html.H6("Filter by well status:",
                                  ),
                          dcc.RadioItems(
                              options=[
                                  {'label': 'All ', 'value': 'all'},
                                  {'label': 'Active Only ', 'value': 'active only'},
                                  {'label': 'Customize ', 'value': 'customize'}

                              ],
                              value='active only',
                              labelStyle={'display': 'inline-block'},
                              labelClassName='pr-2'
                          ),
                          dcc.Dropdown(
                              options=[
                                  {'label': 'Active', 'value': 'active'},
                                  {'label': 'Application Recieved to drill/plug/convert', 'value': 'aprdpc'},
                                  {'label': 'Cancelled', 'value': 'cancelled'},
                                  {'label': 'Drilling Completed', 'value': 'drilling completed'},
                                  {'label': 'Drilled Deeper', 'value': 'drilled deeper'},
                                  {'label': 'Drilling in progress', 'value': 'dip'},
                                  {'label': 'Expired Permit', 'value': 'ep'},
                                  {'label': 'Inactive', 'value': 'i'},
                                  {'label': 'Not Reported on AWR', 'value': 'nra'},
                                  {'label': 'Plugged and Abandoned', 'value': 'pa'},
                                  {'label': 'Permit Issued', 'value': 'pi'},
                                  {'label': 'Pluddeg Back', 'value': 'pb'},
                                  {'label': 'Plugged back Multilateral', 'value': 'pbm'},
                                  {'label': 'Refunded Fee', 'value': 'rf'},
                                  {'label': 'Released-Water Well', 'value': 'rww'},
                                  {'label': 'Shut-In', 'value': 'si'},
                                  {'label': 'temporarily Abandoned', 'value': 'ta'},
                                  {'label': 'Transferred Permit', 'value': 'tp'},
                                  {'label': 'Unknown', 'value': 'u'},
                                  {'label': 'Unknown Located', 'value': 'ul'},
                                  {'label': 'Unknown Not Found', 'value': 'unf'},
                                  {'label': 'Voided Permit', 'value': 'vp'}
                              ],
                              value=['active'],
                              multi=True
                          ),
                          dcc.Checklist(
                              options=[
                                  {'label': 'Lock camera', 'value': 'lock camera'}
                              ],
                              value=[]
                          ),

                          html.H6("Filter by well Type:",
                                  ),
                          dcc.RadioItems(
                              options=[
                                  {'label': 'All', 'value': 'all'},
                                  {'label': 'Productive Only', 'value': 'productive only'},
                                  {'label': 'Customize', 'value': 'customize'}
                              ],
                              value='productive only',
                              labelStyle={'display': 'inline-block'},
                              labelClassName='pr-2'
                          ),
                          dcc.Dropdown(
                              options=[
                                  {'label': 'Brine', 'value': 'brine'},
                                  {'label': 'Confidential', 'value': 'confidential'},
                                  {'label': 'Dry Hole', 'value': 'Dry Hole'},
                                  {'label': 'Disposal', 'value': 'Disposal'},
                                  {'label': 'Dry Wildcat', 'value': 'Dry Wildcat'},
                                  {'label': 'Gas Development', 'value': 'Gas Development'},
                                  {'label': 'Gas Extension', 'value': 'Gas Extension'},
                                  {'label': 'Gas Wildcat', 'value': 'Gas Wildcat'},
                                  {'label': 'Gas Injection', 'value': 'Gas Injection'},
                                  {'label': 'Oil Injection', 'value': 'Oil Injection'},
                                  {'label': 'Liquefied Petroleum Gas Storage',
                                   'value': 'Liquefied Petroleum Gas Storage'},
                                  {'label': 'Moritoring Brine', 'value': 'Moritoring Brine'},
                                  {'label': 'Monitoring Miscellaneous', 'value': 'Monitoring Miscellaneous'},
                                  {'label': 'Monitoring Storage', 'value': 'Monitoring Storage'},
                                  {'label': 'Not Listed', 'value': 'Not Listed'},
                                  {'label': 'Observation Well', 'value': 'Observation Well'},
                                  {'label': 'Oil Development', 'value': 'Oil Development'},
                                  {'label': 'Oil Extension', 'value': 'Oil Extension'},
                                  {'label': 'Oil Wildcat', 'value': 'Oil Wildcat'},
                                  {'label': 'Stratigraphic', 'value': 'Stratigraphic'},
                                  {'label': 'Storage', 'value': 'Storage'},
                                  {'label': 'Geothermal', 'value': 'Geothermal'},
                                  {'label': 'Unknown', 'value': 'Unknown'}
                              ],
                              id='bar_input',
                              value=['active'],
                              multi=True
                          )

                          ],
                style={'box-shadow': '2px 2px 2px lightgrey', 'background-color': '#255464'},
                width={'size': 4},
                className='card pt-4 pb-4 text-white',

                ),

        dbc.Col(dbc.Row(
            [
                html.Div(children=[html.H5('3225', id='no_wells', ), html.H6('No. of Wells')],
                         style={'box-shadow': '2px 2px 2px lightgrey', 'background': '#245c6c'},
                         className='card-body p-2 m-2 text-center border rounded text-white',),

                html.Div(children=[html.H5('425M mcf', id='no_gas', ), html.H6('Gas')],
                         style={'box-shadow': '2px 2px 2px lightgrey', 'background': '#245c6c'},
                         className='card-body p-2 m-2 text-center border rounded text-white'),

                html.Div(children=[html.H5('2M bbl', id='no_oil', ), html.H6('Oil')],
                         style={'box-shadow': '2px 2px 2px lightgrey', 'background': '#245c6c'},
                         className='card-body p-2 m-2 text-center border rounded text-white'),

                html.Div(children=[html.H5('3M bbl', id='no_water', ), html.H6('Water')],
                         style={'box-shadow': '2px 2px 2px lightgrey', 'background': '#245c6c'},
                         className='card-body p-2 m-2 text-center border rounded text-white'),
                # bar chart start
                # dbc.Col(children=[
                dcc.Graph(id='og_bar_chart', figure={}, )
                # ]),
                # bar chart end

            ], ),
        ),
    ], justify='start'),

    # pie chart start
    dbc.Row(children=[
        dbc.Col(children=[
            # html.H4('Production Summery: 2006 to 2019', className='text-center text-white', ),
            dcc.Graph(id='og_pie_chart1', figure={}, style={'display': 'inline-block'}),
            dcc.Graph(id='og_pie_chart2', figure={}, style={'display': 'inline-block'}),
        ], style={'width': 480, 'height': 546}),
        dbc.Col(children=[
            dcc.Graph(id='og_line_chart', figure={}, style={'height': 446, 'width': 480})
        ], )
    ],
        # style={'background-color': '#212529'},
    ),
    # pie chart end
], )


# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     # html.Div(dash_auth.create_logout_button(), className='two columns', style={'marginTop': 30}),
#     # html.Div(id='page-content'),
#
#     # bar chart start
#     dbc.Col(children=[
#         dcc.Graph(id='og_bar_chart', figure={})
#     ]),
#     # bar chart end
#
#     # pie chart start
#     dbc.Row(children=[
#         dbc.Col(children=[
#             html.H4('Production Summery: 2006 to 2019', className='text-center text-white', ),
#             dcc.Graph(id='og_pie_chart1', figure={}, style={'display': 'inline-block'}),
#             dcc.Graph(id='og_pie_chart2', figure={}, style={'display': 'inline-block'}),
#         ], ),
#         dbc.Col(children=[
#             dcc.Graph(id='og_line_chart', figure={}, )
#         ], )
#     ],
#         # style={'background-color': '#212529'},
#     ),
#     # pie chart end
#
# ])


# pie chart start


# Update page
# # # # # # # # #

@app.callback(
    [Output('og_bar_chart', 'figure'), Output('og_pie_chart1', 'figure'), Output('og_pie_chart2', 'figure'),
     Output('og_line_chart', 'figure'), Output('no_wells', 'children'), Output('no_gas', 'children'),
     Output('no_oil', 'children'),
     Output('no_water', 'children'), ],
    Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/home/':
        data = get_csv_data().copy()
        # data = data.groupby('Wl_Status', as_index=False)
        gas = data['GasProd'].sum()
        oil = data['OilProd'].sum()
        water = data['WaterProd'].sum()
        no_wells = gas + water + oil

        # print(data.head(10))
        # bar figure start
        bar_group = data[data['Wl_Status'] == 'AC'].groupby('Year', as_index=False).sum()
        bar_fig = px.bar(bar_group, x='Year', y='Completion', text='Completion',
                         color_discrete_sequence=px.colors.sequential.Aggrnyl, height=446)
        bar_fig.update_layout(
            title={'text': 'Completed Wells/Year', 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
            yaxis_title='')
        # bar figure end

        # pie figure start
        group_data = data.groupby(['Year', 'Completion'], as_index=False).sum()
        pie_fig1 = px.pie(data_frame=group_data, names=['GasProd', 'WaterProd', 'OilProd'],
                          # labels=['GasProd', 'WaterProd', 'OilProd'],
                          hole=0.5,
                          # template='plotly_dark',  # presentation, plotly_dark
                          # title='Production Summery: 2006 to 2019',
                          width=240,
                          color_discrete_sequence=px.colors.sequential.Aggrnyl,
                          )
        pie_fig1.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=-0.30, xanchor="left", x=0.01, ), )
        # pie figure end

        # line figure start
        line_data = data.groupby(['Year'], as_index=False).mean()
        line_fig = px.line(line_data, x='Year', y=['GasProd', 'WaterProd', 'OilProd'],
                           title='Aggregate: Oil Development', hover_name='Year',
                           labels={"y": "",
                                   "WaterProd": "Water Produced (bbl)",
                                   "OilProd": "Oil Produced (bbl)"}, )
        line_fig.update_layout(title={'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'}, yaxis_title='',
                               legend=dict(orientation="h", yanchor="bottom", y=-0.30, xanchor="left", x=0.01,
                                           title=''),
                               margin=dict(t=2, l=2, b=2, r=2))
        # line figure end

        return bar_fig, pie_fig1, pie_fig1, line_fig, no_wells, gas, oil, water
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)

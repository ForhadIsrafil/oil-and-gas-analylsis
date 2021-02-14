import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
# import pandas_datareader.data as web
import datetime

from data.og_data import get_csv_data


# https://www.bootstrapcdn.com/bootswatch/
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

# Layout section: Bootstrap (https://hackerthemes.com/bootstrap-cheatsheet/)
# ************************************************************************


app.layout = dbc.Container([
    ######-------- 1st row start ---------######
    dbc.Row([
        dbc.Col(children=[html.Img(src='assets/dash-logo.png', height=100, width=200)],
                width={'size': 4}),
        dbc.Col(children=[html.H4("New York Oil and Gas",
                                  ),
                          html.H6("Production Overview",
                                  )],
                className='text-center',
                width={'size': 4})

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
                style={'box-shadow': '2px 2px 2px lightgrey'},
                width={'size': 4},
                className='card pt-4 pb-4',

                ),

        dbc.Col(dbc.Row(
            [
                html.Div(children=[html.H4('3225'), html.H6('No. of Wells')],
                         style={'box-shadow': '2px 2px 2px lightgrey'},
                         className='card-body p-2 m-2 text-center border rounded',
                         ),
                html.Div(children=[html.H4('425M mcf'), html.H6('Gas')],
                         style={'box-shadow': '2px 2px 2px lightgrey'},

                         className='card-body p-2 m-2 text-center border rounded'),
                html.Div(children=[html.H4('2M bbl'), html.H6('Oil')],
                         style={'box-shadow': '2px 2px 2px lightgrey'},

                         className='card-body p-2 m-2 text-center border rounded'),
                html.Div(children=[html.H4('3M bbl'), html.H6('Water')],
                         style={'box-shadow': '2px 2px 2px lightgrey'},

                         className='card-body p-2 m-2 text-center border rounded')

            ],

        ),

        ),
        dbc.Row(children = [
            dcc.Graph(id='first_bar', figure={})]

        )

    ], justify='start'),
], )


@app.callback(Output('first_bar', 'figure'),
              Input('bar_input', 'value'))
def all_graph(first_bar_input):
    data = get_csv_data()
    # line figure start
    line_data = data.groupby(['Year'], as_index=False).sum()
    line_fig = px.line(line_data, x='Year', y=['GasProd', 'WaterProd', 'OilProd'],
                       title='Aggregate: Oil Development', hover_name='Year',
                       labels={"y": "",
                               "WaterProd": "Water Produced (bbl)",
                               "OilProd": "Oil Produced (bbl)"}, )
    line_fig.update_layout(title={'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
                           legend=dict(orientation="h", yanchor="bottom", y=-0.30, xanchor="left", x=0.01),
                           margin=dict(t=2, l=2, b=2, r=2))
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)

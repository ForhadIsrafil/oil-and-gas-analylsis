import dash_core_components as dcc
import dash_html_components as html
import dash_table
from components import Header, print_button
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd

# Read in Travel Report Data
df = pd.read_csv('data/performance_analytics_cost_and_ga_metrics.csv')

df.rename(columns={
    'Travel Product': 'Placement type',
    'Spend - This Year': 'Spend TY',
    'Spend - Last Year': 'Spend LY',
    'Sessions - This Year': 'Sessions - TY',
    'Sessions - Last Year': 'Sessions - LY',
    'Bookings - This Year': 'Bookings - TY',
    'Bookings - Last Year': 'Bookings - LY',
    'Revenue - This Year': 'Revenue - TY',
    'Revenue - Last Year': 'Revenue - LY',
}, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
current_year = df['Year'].max()

dt_columns = ['Placement type', 'Spend TY', 'Spend - LP', 'Spend PoP (Abs)', 'Spend PoP (%)', 'Spend LY',
              'Spend YoY (%)', \
              'Sessions - TY', 'Sessions - LP', 'Sessions - LY', 'Sessions PoP (%)', 'Sessions YoY (%)', \
              'Bookings - TY', 'Bookings - LP', 'Bookings PoP (%)', 'Bookings PoP (Abs)', 'Bookings - LY',
              'Bookings YoY (%)', 'Bookings YoY (Abs)', \
              'Revenue - TY', 'Revenue - LP', 'Revenue PoP (Abs)', 'Revenue PoP (%)', 'Revenue - LY', 'Revenue YoY (%)',
              'Revenue YoY (Abs)', ]

conditional_columns = ['Spend_PoP_abs_conditional', 'Spend_PoP_percent_conditional', 'Spend_YoY_percent_conditional',
                       'Sessions_PoP_percent_conditional', 'Sessions_YoY_percent_conditional',
                       'Bookings_PoP_abs_conditional', 'Bookings_YoY_abs_conditional',
                       'Bookings_PoP_percent_conditional', 'Bookings_YoY_percent_conditional',
                       'Revenue_PoP_abs_conditional', 'Revenue_YoY_abs_conditional', 'Revenue_PoP_percent_conditional',
                       'Revenue_YoY_percent_conditional', ]

dt_columns_total = ['Placement type', 'Spend TY', 'Spend - LP', 'Spend PoP (Abs)', 'Spend PoP (%)', 'Spend LY',
                    'Spend YoY (%)', \
                    'Sessions - TY', 'Sessions - LP', 'Sessions - LY', 'Sessions PoP (%)', 'Sessions YoY (%)', \
                    'Bookings - TY', 'Bookings - LP', 'Bookings PoP (%)', 'Bookings PoP (Abs)', 'Bookings - LY',
                    'Bookings YoY (%)', 'Bookings YoY (Abs)', \
                    'Revenue - TY', 'Revenue - LP', 'Revenue PoP (Abs)', 'Revenue PoP (%)', 'Revenue - LY',
                    'Revenue YoY (%)', 'Revenue YoY (Abs)',
                    'Spend_PoP_abs_conditional', 'Spend_PoP_percent_conditional', 'Spend_YoY_percent_conditional',
                    'Sessions_PoP_percent_conditional', 'Sessions_YoY_percent_conditional',
                    'Bookings_PoP_abs_conditional', 'Bookings_YoY_abs_conditional', 'Bookings_PoP_percent_conditional',
                    'Bookings_YoY_percent_conditional',
                    'Revenue_PoP_abs_conditional', 'Revenue_YoY_abs_conditional', 'Revenue_PoP_percent_conditional',
                    'Revenue_YoY_percent_conditional', ]

df_columns_calculated = ['Placement type', 'CPS - TY',
                         'CPS - LP', 'CPS PoP (Abs)', 'CPS PoP (%)',
                         'CPS - LY', 'CPS YoY (Abs)', 'CPS YoY (%)',
                         'CVR - TY',
                         'CVR - LP', 'CVR PoP (Abs)', 'CVR PoP (%)',
                         'CVR - LY', 'CVR YoY (Abs)', 'CVR YoY (%)',
                         'CPA - TY',
                         'CPA - LP', 'CPA PoP (Abs)', 'CPA PoP (%)',
                         'CPA - LY', 'CPA YoY (Abs)', 'CPA YoY (%)']

conditional_columns_calculated_calculated = ['CPS_PoP_abs_conditional', 'CPS_PoP_percent_conditional',
                                             'CPS_YoY_abs_conditional', 'CPS_PoP_percent_conditional',
                                             'CVR_PoP_abs_conditional', 'CVR_PoP_percent_conditional',
                                             'CVR_YoY_abs_conditional', 'CVR_YoY_percent_conditional',
                                             'CPA_PoP_abs_conditional', 'CPA_PoP_percent_conditional',
                                             'CPA_YoY_abs_conditional', 'CPA_YoY_percent_conditional']

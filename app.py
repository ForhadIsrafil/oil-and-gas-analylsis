import dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.BOOTSTRAP

]
# external_scripts = ["https://code.jquery.com/jquery-3.2.1.min.js",
#                     "https://codepen.io/bcd/pen/YaXojL.js"]
app = dash.Dash('forhad', external_stylesheets=external_stylesheets, url_base_pathname='/home/',
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
app.title = "Oil & Gas: Analysis!"
server = app.server
app.config.suppress_callback_exceptions = True

import dash_auth

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = [
    ['baset', '123'], ['forhad', '123'],
]
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

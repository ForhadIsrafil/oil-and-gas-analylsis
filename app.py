from dash import dash

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]
external_scripts = []
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=external_scripts,
                url_base_pathname='/home/')
app.title = "Avocado Analytics: Understand Your Avocados!"
server = app.server
app.config.suppress_callback_exceptions = True

import dash_auth

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = [
    ['[username]', '[password']
]
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

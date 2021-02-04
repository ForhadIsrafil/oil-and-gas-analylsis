from dash import dash

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
    "//fonts.googleapis.com/css?family=Raleway:400,300,600",
    "https://codepen.io/bcd/pen/KQrXdb.css",
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    "https://codepen.io/dmcomfort/pen/JzdzEZ.css"
]
external_scripts = ["https://code.jquery.com/jquery-3.2.1.min.js",
                    "https://codepen.io/bcd/pen/YaXojL.js"]
app = dash.Dash('forhad', external_stylesheets=external_stylesheets, external_scripts=external_scripts,
                url_base_pathname='/home/')
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

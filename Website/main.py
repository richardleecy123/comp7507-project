import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output
import base64

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

INTRODUCTION_1='<iframe src="https://connecthkuhk-my.sharepoint.com/personal/cyleeaw_connect_hku_hk/_layouts/15/Doc.aspx?sourcedoc={5eb3cfb4-c13f-4fa4-a1ca-76725f9bb443}&amp;action=embedview&amp;wdAr=1.7777777777777777" width="1000px" height="665px" frameborder="0">這是 <a target="_blank" href="https://office.com/webapps">Office</a> 提供的內嵌 <a target="_blank" href="https://office.com">Microsoft Office</a> 簡報。</iframe>'
DASH_BOARD_SOURCE_WORLD_1="<div class='tableauPlaceholder' id='viz1648361257523' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book4_16481303452280&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book4_16481303452280&#47;Dashboard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book4_16481303452280&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-CN' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648361257523');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='977px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
DASH_BOARD_SOURCE_WORLD_2="<div class='tableauPlaceholder' id='viz1648361283618' style='position: relative'><noscript><a href='#'><img alt='View Like Dislike ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book3_16481301379850&#47;ViewLikeDislike&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book3_16481301379850&#47;ViewLikeDislike' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book3_16481301379850&#47;ViewLikeDislike&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-CN' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648361283618');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='977px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
DASH_BOARD_SOURCE_WORLD_3="<div class='tableauPlaceholder' id='viz1648474158603' style='position: relative'><noscript><a href='#'><img alt='Country WC ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WordCloud_16483607091310&#47;CountryWC&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='WordCloud_16483607091310&#47;CountryWC' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WordCloud_16483607091310&#47;CountryWC&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-CN' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648474158603');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='692px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
DASH_BOARD_SOURCE_WORLD_0="<div class='tableauPlaceholder' id='viz1648361122750' style='position: relative'><noscript><a href='#'><img alt='Language ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;K6&#47;K62Z797QC&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;K62Z797QC' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;K6&#47;K62Z797QC&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-CN' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648361122750');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1127px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
DASH_BOARD_SOURCE_CATEGORY_0="<div class='tableauPlaceholder' id='viz1648301473558' style='position: relative; width: 100%; height:600px'><noscript><a href='#'><img alt='儀表板窗格 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;ProjectDashbaordP_2&#47;1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ProjectDashbaordP_2&#47;1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pr&#47;ProjectDashbaordP_2&#47;1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-TW' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648301473558');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1127px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
DASH_BOARD_SOURCE_CATEGORY_1="<div class='tableauPlaceholder' id='viz1648477495063' style='position: relative'><noscript><a href='#'><img alt='Category ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WordCloud-Cat&#47;Story2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='WordCloud-Cat&#47;Story2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WordCloud-Cat&#47;Story2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-CN' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648477495063');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='717px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
DASH_BOARD_SOURCE_CHANNEL_0="<div class='tableauPlaceholder' id='viz1648305383317' style='position: relative; width: 100%; height:600px'><noscript><a href='#'><img alt='仪表板 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ch&#47;channel-1&#47;1_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='channel-1&#47;1_1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ch&#47;channel-1&#47;1_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-CN' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648305383317');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1127px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
DASH_BOARD_SOURCE_CHANNEL_1="<div class='tableauPlaceholder' id='viz1648306461492' style='position: relative; width: 100%; height:600px'><noscript><a href='#'><img alt='故事 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;X6&#47;X6JWBNB27&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;X6JWBNB27' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;X6&#47;X6JWBNB27&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='zh-CN' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1648306461492');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='827px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"


SIDEBAR_STYLE={
    "position": "fixed",
    "backgroundColor": "black",
    "top": "45%",
    "left": "4%",
    }

CONTENT_STYLE = {
    "marginTop":"4%",
    "marginBottom":"2%",
    "backgroundColor":"black",
}



youtube_top = 'img/youtube_top.png' # replace with your own image
encoded_youtube_top = base64.b64encode(open(youtube_top, 'rb').read())
topbar = html.Img(src='data:image/png;base64,{}'.format(encoded_youtube_top.decode()),style={'width':'100%'})


youtube_bottom = 'img/youtube_bottom.png' # replace with your own image
encoded_youtube_bottom = base64.b64encode(open(youtube_bottom, 'rb').read())
bottombar = html.Img(src='data:image/png;base64,{}'.format(encoded_youtube_bottom.decode()),style={'width':'100%'})

sidebar = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavLink("Introduction", href="/", active="exact"),
                dbc.NavLink("Worldwide Status", href="/worldwide", active="exact"),
                dbc.NavLink("Video Category", href="/category", active="exact"),
                dbc.NavLink("Top Channel", href="/video", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(
    id="page-content",
    children=[],
    style=CONTENT_STYLE
)

app.layout = dbc.Container([
    dcc.Location(id="url"),
    dbc.Row([
        dbc.Col(topbar,width=12)
        ],
        className="fixed-top",
        style={"backgroundColor":"#202020"}),
    
    dbc.Row([
        dbc.Col(sidebar,width=2),
        dbc.Col(content,width=10),
        ],
        style={"backgroundColor":"black"}),


    dbc.Row([
        dbc.Col(bottombar,width=12)
        ],
        className="fixed-bottom"),
    
],fluid=True)



@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":

        cover_page = 'img/cover_page.jpg' # replace with your own image
        encoded_cover_page = base64.b64encode(open(cover_page, 'rb').read())
        coverPage = html.Img(src='data:image/jpg;base64,{}'.format(encoded_cover_page.decode()),style={'width':'80%'})
        return [coverPage, 
        html.Iframe(sandbox='allow-same-origin allow-scripts allow-popups allow-forms', srcDoc=INTRODUCTION_1, height="900", width="100%")]
    elif pathname == "/worldwide":
        return [
                html.Iframe(sandbox='allow-same-origin allow-scripts allow-popups allow-forms', srcDoc=DASH_BOARD_SOURCE_WORLD_0, height="900", width="100%"),
                html.Iframe(sandbox='allow-same-origin allow-scripts allow-popups allow-forms', srcDoc=DASH_BOARD_SOURCE_WORLD_1, height="900", width="100%"),
                #html.Iframe(sandbox='allow-same-origin allow-scripts allow-popups allow-forms', srcDoc=DASH_BOARD_SOURCE_WORLD_2, height="900", width="100%"),
                html.Iframe(sandbox='allow-same-origin allow-scripts allow-popups allow-forms', srcDoc=DASH_BOARD_SOURCE_WORLD_3, height="900", width="100%"),
                ]
    elif pathname == "/category":
        return [html.Iframe(sandbox='allow-same-origin allow-scripts allow-popups allow-forms', srcDoc=DASH_BOARD_SOURCE_CATEGORY_0, height="900", width="100%"),
                html.Iframe(sandbox='allow-same-origin allow-scripts allow-popups allow-forms', srcDoc=DASH_BOARD_SOURCE_CATEGORY_1, height="900", width="100%")
                ]

    elif pathname == "/video":
        return [html.Iframe(sandbox='allow-same-origin allow-scripts allow-popups allow-forms', srcDoc=DASH_BOARD_SOURCE_CHANNEL_0, height="900", width="100%"),
                html.Iframe(sandbox='allow-same-origin allow-scripts allow-popups allow-forms', srcDoc=DASH_BOARD_SOURCE_CHANNEL_1, height="900", width="100%"),
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )



if __name__=='__main__':
    app.run_server(debug=True, port=8051)

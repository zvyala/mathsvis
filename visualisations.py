import plotly.graph_objs as go
import numpy as np

def create_plot(x, y, y_start, y_end, unit):
    line_color = '#ffb3fb'
    title_color = '#f3d4ff'

    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', name='Function Plot', line=dict(color=line_color)))

    x_ticks = np.linspace(min(x), max(x), num=5)
    x_tickvals = x_ticks

    fig.update_layout(
        title='Function Visualisation',
        title_font=dict(color=title_color),
        xaxis_title='X Axis',
        xaxis_title_font=dict(color=title_color),
        yaxis_title='Y Axis',
        yaxis_title_font=dict(color=title_color),
        xaxis=dict(
            title='X Axis',
            autorange=True,
            tickvals=x_tickvals,
            ticktext=[f"{v:.0f}" for v in x_ticks],
            tickfont=dict(color=title_color)
        ),
        yaxis=dict(
            title='Y Axis',
            range=[y_start, y_end],
            tickfont=dict(color=title_color)
        ),
        dragmode='pan',
        autosize=True,
        margin=dict(l=0, r=0, t=30, b=0),
        hovermode='closest',
        showlegend=True,
        legend=dict(font=dict(color=title_color))
    )

    return fig.to_html(full_html=False)

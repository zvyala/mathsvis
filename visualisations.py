# visualisations.py
import plotly.graph_objs as go
import numpy as np

def create_plot(x, y, y_start, y_end, unit):
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', name='Function Graph'))

    # Handle x-axis tick labels based on the unit
    if unit == 'degrees':
        x_ticks = np.degrees(np.linspace(min(x), max(x), num=5))
        x_tickvals = np.radians(x_ticks)
    else:
        x_ticks = np.linspace(min(x), max(x), num=5)
        x_tickvals = x_ticks

    fig.update_layout(
        title='Function Visualisation',
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        xaxis=dict(
            title='X Axis',
            autorange=True,
            tickvals=x_tickvals,
            ticktext=[f"{v:.0f}" for v in x_ticks]
        ),
        yaxis=dict(
            title='Y Axis',
            range=[y_start, y_end]
        ),
        dragmode='pan',
        autosize=True,
        margin=dict(l=0, r=0, t=30, b=0),
        hovermode='closest',
        showlegend=True,
        xaxis_title_font=dict(size=14),
        yaxis_title_font=dict(size=14)
    )

    return fig.to_html(full_html=False)

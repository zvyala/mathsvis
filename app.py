from flask import Flask, render_template, request
import numpy as np
import plotly.graph_objs as go
from sympy import symbols, sympify, lambdify

app = Flask(__name__)

def create_plot(x, y, y_start, y_end, unit):
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', name='Function Plot', line=dict(color='#ffb3fb')))

    x_ticks = np.linspace(min(x), max(x), num=5)
    x_tickvals = x_ticks

    fig.update_layout(
        title='Function Visualisation',
        title_font=dict(color='#f3d4ff'),
        xaxis_title='X Axis',
        xaxis_title_font=dict(color='#f3d4ff'),
        yaxis_title='Y Axis',
        yaxis_title_font=dict(color='#f3d4ff'),
        xaxis=dict(
            title='X Axis',
            autorange=True,
            tickvals=x_tickvals,
            ticktext=[f"{v:.0f}" for v in x_ticks],
            tickfont=dict(color='#f3d4ff')
        ),
        yaxis=dict(
            title='Y Axis',
            range=[y_start, y_end],
            tickfont=dict(color='#f3d4ff')
        ),
        dragmode='pan',
        autosize=True,
        margin=dict(l=0, r=0, t=30, b=0),
        hovermode='closest',
        showlegend=True,
        legend=dict(font=dict(color='#f3d4ff'))
    )

    return fig.to_html(full_html=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    graph = None
    if request.method == 'POST':
        try:
            x_start = float(request.form['x_start'])
            x_end = float(request.form['x_end'])
            y_start = float(request.form.get('y_start', -10))
            y_end = float(request.form.get('y_end', 10))
            function = request.form.get('function')
            custom_function = request.form.get('custom_function', '')

            x_values = np.linspace(x_start, x_end, 1000)

            if custom_function:
                x = symbols('x')
                expr = sympify(custom_function)
                f = lambdify(x, expr, 'numpy')
                y_values = f(x_values)

                y_start = min(y_values) - 1 if y_start is None else y_start
                y_end = max(y_values) + 1 if y_end is None else y_end

            elif function:
                x_rad = np.radians(x_values)

                if function == 'sine':
                    y_values = np.sin(x_rad)
                elif function == 'cosine':
                    y_values = np.cos(x_rad)
                elif function == 'tangent':
                    y_values = np.tan(x_rad)
                    y_values = np.where(np.abs(y_values) > 10, np.nan, y_values)

                y_start = -1.5 if y_start is None else y_start
                y_end = 1.5 if y_end is None else y_end

            graph = create_plot(x_values, y_values, y_start, y_end, 'degrees')

        except Exception as e:
            print(f"Error: {e}")

    return render_template('index.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)

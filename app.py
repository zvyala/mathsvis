from flask import Flask, render_template, request
from visualisations import create_plot
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    graph = None
    if request.method == 'POST':
        try:
            x_start = float(request.form['x_start'])
            x_end = float(request.form['x_end'])
            y_start = float(request.form.get('y_start', -1))
            y_end = float(request.form.get('y_end', 1))
            function = request.form['function']
            x_values = np.linspace(x_start, x_end, 1000)
            x_rad = np.radians(x_values)  
            if function == 'sine':
                y_values = np.sin(x_rad)
            elif function == 'cosine':
                y_values = np.cos(x_rad)
            elif function == 'tangent':
                y_values = np.tan(x_rad)
            if function == 'tangent':
                y_values = np.where(np.abs(y_values) > 10, np.nan, y_values)
            graph = create_plot(x_values, y_values, y_start, y_end, 'degrees')
        except Exception as e:
            print(f"Error: {e}")

    return render_template('index.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)

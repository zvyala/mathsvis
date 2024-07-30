from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    graph = None
    if request.method == 'POST':
        try:
            x_start = float(request.form['x_start'])
            x_end = float(request.form['x_end'])
            y_start = float(request.form.get('y_start', -10))
            y_end = float(request.form.get('y_end', 10))
            function = request.form['function']

            x = np.linspace(np.deg2rad(x_start), np.deg2rad(x_end), 1000)
            if function == 'sine':
                y = np.sin(x)
            elif function == 'cosine':
                y = np.cos(x)
            elif function == 'tangent':
                y = np.tan(x)
                y = np.clip(y, y_start, y_end)

            fig, ax = plt.subplots()
            ax.plot(np.rad2deg(x), y)
            ax.set_xlabel('X (Degrees)')
            ax.set_ylabel('Y')
            ax.set_title(f'{function.capitalize()} Function')

            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            graph = base64.b64encode(img.getvalue()).decode('utf8')
            plt.close()
        except Exception as e:
            print(f"Error: {e}")

    return render_template('index.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

app = Flask(__name__)
app.secret_key = 'secret_key'  # Replace with a strong, random key


# Route to render the upload page
@app.route('/')
def upload():
    return render_template('upload.html')


# Route to handle the CSV file upload and process it
@app.route('/upload', methods=['POST'])
def handle_upload():
    # Retrieve the uploaded file
    file = request.files['file']

    if file and file.filename.endswith('.csv'):
        # Read the file into a pandas DataFrame
        df = pd.read_csv(file)

        # Compute the statistical summary
        summary = df.describe().to_html()

        # Store the summary in session
        session['summary'] = summary

        # Redirect to the summary page
        return redirect(url_for('summary'))
    else:
        return redirect(url_for('upload'))


# Route to display the statistical summary
@app.route('/summary')
def summary():
    summary = session.get('summary', 'No data available.')
    return render_template('summary.html', summary=summary)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong, random key


# Route to render the home screen
@app.route('/')
def home():
    return render_template('home.html')


# Route to handle product submission
@app.route('/submit_product', methods=['POST'])
def submit_product():
    # Retrieve form data
    product_name = request.form.get('product_name')
    quantity = request.form.get('quantity')

    # Store data in session
    session['order'] = {
        'product_name': product_name,
        'quantity': quantity
    }

    # Redirect to the shipping details page
    return redirect(url_for('shipping_details'))


# Route to render the shipping details form
@app.route('/shipping_details', methods=['GET', 'POST'])
def shipping_details():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        address = request.form.get('address')
        contact_number = request.form.get('contact_number')

        # Store data in session
        session['shipping_details'] = {
            'name': name,
            'address': address,
            'contact_number': contact_number
        }

        # Redirect to the order summary page
        return redirect(url_for('order_summary'))

    return render_template('shipping_details.html')


# Route to render the order summary
@app.route('/order_summary')
def order_summary():
    order = session.get('order', {})
    shipping_details = session.get('shipping_details', {})

    return render_template('order_summary.html',
                           order=order,
                           shipping_details=shipping_details)


# Route to confirm the order and return to the home screen
@app.route('/confirm_order')
def confirm_order():
    # Clear session data after confirming the order
    session.pop('order', None)
    session.pop('shipping_details', None)

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

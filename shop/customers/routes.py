from flask import render_template,session, request,redirect,url_for,flash,current_app
from shop import app,db,photos, search
from .forms import CustomerRegisterForm
import secrets
import os


@app.route('/customer/register', methods=['GET','POST'])
def customer_register():
    form = CustomerRegisterForm(request.form)
    return render_template('customer/register.html', form=form)
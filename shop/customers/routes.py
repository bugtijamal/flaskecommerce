from flask import render_template,session, request,redirect,url_for,flash,current_app
from shop import app,db,photos, search
from .forms import CustomerRegisterForm
import secrets
import os



def customer_register():
    return render_template('costomer/register.html')
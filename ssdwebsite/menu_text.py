import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('menu_text', __name__ )

"""Simple text routes and will have
no functionality in python. Their purpose is to display
desired text."""

@bp.route('/contact', methods=('GET', 'POST'))
def contact():
    return render_template('menu-pages/contact.html')

@bp.route('/media', methods=('GET', 'POST'))
def media():
    return render_template('menu-pages/media.html')

@bp.route('/ourVision', methods=('GET', 'POST'))
def vision():
    return render_template('menu-pages/ourVision.html')

@bp.route('/FAQ', methods=('GET', 'POST'))
def faq():
    return render_template('menu-pages/visions-submenu/FAQ.html')

@bp.route('/Objectives', methods=('GET', 'POST'))
def objectives():
    return render_template('menu-pages/visions-submenu/objectives.html')

@bp.route('/Intro', methods=('GET', 'POST'))
def intro():
    return render_template('menu-pages/visions-submenu/intro.html')

@bp.route('/documents', methods=('GET', 'POST'))
def documents():
    return render_template('menu-pages/contact-submenu/documents.html')

@bp.route('/volunteering', methods=('GET', 'POST'))
def volunteer():
    return render_template('menu-pages/contact-submenu/volunteer.html')

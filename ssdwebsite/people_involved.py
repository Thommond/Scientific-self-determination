import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('people_involved', __name__ )

@bp.route('/contributors', methods=('GET', 'POST'))
def contributors():
    return render_template('contribute/contributors.html')

@bp.route('/partners', methods=('GET', 'POST'))
def partners():
    return render_template('contribute/partners.html')

@bp.route('/volunteers', methods=('GET', 'POST'))
def volunteers():
    return render_template('contribute/volunters.html')

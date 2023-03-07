from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.route("/")
def main_page():
    """ Shows the main page. """
    return render_template("main_page/index.html")

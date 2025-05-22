from flask import Blueprint, render_template
from flask import flash, redirect, url_for, session, request
import logging

import data_handler

logger = logging.getLogger(__name__)

home_bp = Blueprint("home", __name__, template_folder="templates")


@home_bp.route("/")
def home_page():
    logger.info("home page hit")
    db_call = data_handler.database()
    budgets = db_call.get_budgets()
    return render_template("home.html", budgets=budgets)


@home_bp.route("/submit", methods=["POST"])
def submit_budget_name():
    budget_name = request.form.get("budgetName")
    logger.debug(request.form)
    if budget_name:
        logger.info(f"User submitted new budget name: {budget_name}")
        session["budget_name"] = budget_name
        db_call = data_handler.database()
        budget_id = db_call.add_budget_name(budget_name)
        if budget_id == 0:
            # db entry failed, throw error message
            flash("Budget Name not saved, please check the logs", "error")
            return redirect(url_for("home.home_page"))
        session["budget_id"] = budget_id
        flash("Budget name saved!", "success")
        return redirect(url_for("home.home_page"))
    else:
        flash("Please enter a budget name.", "error")
        return redirect(url_for("home.home_page"))

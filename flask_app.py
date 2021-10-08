from flask import Flask, render_template

import traceback

from work_modules.request_module import all_astros_in_space, astros_on_defined_craft
from work_modules.custom_context_manager import CustomTimerContextManager

app = Flask(__name__)


@app.route("/astro/list")
def astro_list():
    """
        shows the list of astronauts, that currently inhabit all the space crafts
    """
    with CustomTimerContextManager(function=str(traceback.extract_stack()[-1]).split()[-1][:-1]): # with help of traceback
                                                                                # we can log the function was called
        all_astros = all_astros_in_space()
        return render_template('all_astros.html', all_astros=all_astros)


@app.route("/astro/craft/<craft_name>")
def astro_list_spacecraft(craft_name):
    """
        shows the list of astronauts, that currently inhabit the defined space craft
    """
    with CustomTimerContextManager(function=str(traceback.extract_stack()[-1]).split()[-1][:-1]):
        astros_on_craft = astros_on_defined_craft()[craft_name]
        return render_template('astro_on_craft.html', astros_on_craft=astros_on_craft, craft_name=craft_name)


@app.route("/logs")
def file_logs_page():
    """
        shows the logfile
    """
    with CustomTimerContextManager(function=str(traceback.extract_stack()[-1]).split()[-1][:-1]):
        with open('logs.csv', mode='r') as file:
            f = file.readlines()
            return render_template('file_print.html', f=f, file_name='logs.csv')


@app.route("/file/<file_name>")
def file_print_page(file_name):
    """
        shows any file
    """
    with CustomTimerContextManager(function=str(traceback.extract_stack()[-1]).split()[-1][:-1]):
        with open(file_name, mode='r') as file:
            f = file.readlines()
            return render_template('file_print.html', f=f, file_name=file_name)


@app.errorhandler(404)
def not_found(error):
    with CustomTimerContextManager(function=str(traceback.extract_stack()[-1]).split()[-1][:-1]):
        return render_template('page404or500.html', error=error)


@app.errorhandler(500)
def internal_error(error):
    with CustomTimerContextManager(function=str(traceback.extract_stack()[-1]).split()[-1][:-1]):
        return render_template('page404or500.html', error=error)


if __name__ == "__main__":
    app.run(debug=False, port=10111)
# **********************************************************
# This is the Flask file that coordinates/controls activity
# between HTML requests/posts and searches in the energy database.
# It runs on the Raspberry Pi to service The Biggest Greenie game.
# v0.01 SACRIFICIAL DRAFT
# The MIT License (MIT)
#
# Copyright (c) 2018 HappyDay
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# **********************************************************
from flask import Flask, render_template, request, jsonify
import EnergyPlot as ep
import GetXaxis as gx
import testRoutines as test
# import logging
import dateutil.parser
# **********************************************************
# Logging many events to a logfile.  This way, I can get an idea
# of when/what code has been executed.
# There is no output to the console when logging is on.  This makes
# it difficult to detect if Flask has started up unless the logfile
# is opened/viewed at the same time.
# **********************************************************
# logging.basicConfig(filename='BiggestGreenie.log', level=logging.DEBUG)
# logging.basicConfig( level=logging.DEBUG)

app = Flask(__name__)
# Flask is very clever!  Each page the web browser accesses is hooked up
# To HTML and/or AJAX.  This makes it very powerful for including
# databases, sensor devices, ... things python is great with and
# HTML/CSS/Javascript/plotly/Ajax...stuff that is great for the client.
# **********************************************************


# **********************************************************
# The Biggest Greenie web client has requested to see the "main"
# (templates/index) page.
# **********************************************************
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/open_source')
def open_source():
    return render_template('open_source.html')


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/readings')
def readings():
    return render_template("readings.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/activities')
def activities():
    return render_template("activities.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/getData', methods=['POST'])
def getData():
    plot_date = request.get_json()
    if (plot_date['dateUnit'] == 'DAY'):
        # Using energy readings I generated awhile back until the hw/fw is
        # ready.
        test_day = test.get_random_date('any')
        power_values = ep.get_hour_list(test_day)
    elif (plot_date['dateUnit'] == 'WEEK'):
        test_day = test.get_random_date('Monday')
        power_values = ep.get_week_list(test_day)
    elif (plot_date['dateUnit'] == 'MONTH'):
        test_month, test_year = test.get_random_date('MONTH')
        power_values = ep.get_month_list(test_month, test_year)
    else:
        power_values = -1
    if (power_values != -1):
        # The x-axis labels differ from the others in that they vary based on
        # the month the power values are for.  Since the power_values list
        # has as many entries as there are days in the month, we use that to figure
        # out how many x-axis values there are (one for every day of the month).
        if (plot_date['dateUnit'] == 'MONTH'):
            last_day = len(power_values)
            x_axis_strs = [str(i) for i in range(1, last_day + 1)]
        else:
            # Get X-axis markers
            x_axis_strs = gx.get_x_axis(plot_date['dateUnit'])
    else:
        x_axis_strs = ['0']
    return jsonify({'power': power_values, 'x': x_axis_strs})


# When debug=True, the debug service restarts after changes are made.
# This is very handy!
# host = 0.0.0.0 when on Raspberry Pi
# app.run(debug=True, host='0.0.0.0')
# Trying to access from outside house
app.run(debug=True, use_debugger=True, host='0.0.0.0', port=5000)
# host = localhost when running on mac


# app.run(debug=True, host='localhost', port=9999)

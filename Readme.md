## What

This repository contains the files used to build the web server side
of [The Biggest Greenie](https://happyday.pagekite.me).
* **BiggestGreenie.py**

    Uses the Flask framework to connect the web client with the Energy DB and the other pages of The Biggest Greenie experience.  The
    code is currently set up in test mode, using test data stored
    earlier within the Energy DB.  Eventually, the data will be taken
    from current energy readings that were captured into the Energy DB
    by [the Energy Monitor Firmware](https://bitknitting.github.io/open_source.html).

    **Port Forwarding Challenge:**
    A challenge we faced was allowing access to the web server, which is behind our firewall.
    For the prototype, we chose to use pagekite after reading [this Hackaday](https://hackaday.com/2016/09/21/how-to-run-a-pagekite-server-to-expose-your-raspberry-pi/) article.

* **systemd files Folder**

    We use systemd on the Raspberry Pi to auto start the Flask (biggestgreenie_flask.service) and Pagekite (biggestgreenie_pagekite.service) services.
    Being self-taught on systemd for this project, we found the following helpful:

    - [Documentation](https://www.youtube.com/watch?v=AtEqbYTLHfs)

    - [Quick HOW-TO](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)   

    - [YouTube Tutorial](https://www.youtube.com/watch?v=AtEqbYTLHfs)

* **Templates Folder**

    Templates are an important concept in Flask.  We see the conceptual idea behind
    templates in Flask as the place where the HTML pages are stored.  It is used by
    Flask when routing to determine what page to load.  For example, the
    [BiggestGreenie.py](https://github.com/BitKnitting/HappyDay_BiggestGreenie_web_server/blob/master/BiggestGreenie.py) file has code such as:

    '''
    @app.route('/open_source')
    def open_source():
      return render_template('open_source.html')
    '''  

    This is where the Biggest Greenie's web client HTML is stored.

    **layout.html**

    Template file providing the common HTML used across pages.  For
    example, the HTML for the menu/navigation.

    **index.html**

    The Biggest Greenie's landing page.

    **energy_plot.html**

    HTML / Slick (widget) / JQuery / Ajax / Plotly code to plot daily/weekly/monthly/yearly energy readings.

* **static/css Folder**

    This is where the Biggest Greenie's web client CSS is stored.

    **labelpicker.css**

    Used in energy_plot.html to provide clean navigation when choosing
    between Day / Week / Month / Year.

* **EnergyReadingModel.py**       

    This file creates the Energ y database - EnergyMonitor.db -
    using the peewee object model.

* **EnergyMonitor.db**

    Database with contents used for testing.  The readings were generated using an [ATM90e26 Featherwing from WhatNick](https://bitknitting.wordpress.com/2017/10/07/trying-out-the-atm90e26-featherwing/).

* **x_axis.json**

     Dictionary in json format containing entries for "DAY","WEEK","MONTH".  This makes it easy to set
     the x-axis labels when plotting the energy readings.

* **Unit Test Folder**

     Unit tests using the unittest python library.

## Contributors

HappyDay

## License

Copyright (c) 2018 HappyDay

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.

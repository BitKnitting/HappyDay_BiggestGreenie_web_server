## What

This repository contains the files used to build the web server side
of [The Biggest Greenie](https://bitknitting.github.io/).
* **BiggestGreenie.py**

    Uses the Flask framework to connect the web client with the Energy DB and the other pages of The Biggest Greenie experience.  The
    code is currently set up in test mode, using test data stored
    earlier within the Energy DB.  Eventually, the data will be taken
    from current energy readings that were captured into the Energy DB
    by [the Energy Monitor Firmware](https://bitknitting.github.io/open_source.html).

* **Templates Folder**

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



A short snippet describing the license (MIT, Apache, etc.)

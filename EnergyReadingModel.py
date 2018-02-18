# **********************************************************
# This file creates the Energy database - EnergyMonitor.db -
# using the peewee object model.
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
import peewee
# USE full path when running as a service on the Raspberry Pi
# USE local path when running from the mac
database = peewee.SqliteDatabase("/home/pi/web_server/EnergyMonitor.db")
###############

class Reading(peewee.Model):
    addressID=peewee.IntegerField()
    v1 = peewee.FloatField()
    i1 = peewee.FloatField()
    p1 = peewee.FloatField()
    pf1 = peewee.FloatField()
    v2 = peewee.FloatField()
    i2 = peewee.FloatField()
    p2 = peewee.FloatField()
    pf2 = peewee.FloatField()
    time = peewee.TimestampField()

    class Meta:
        database = database

class Info(peewee.Model):
    addressID=peewee.IntegerField()
    message=peewee.TextField()
    time = peewee.TimestampField()

    class Meta:
        database = database

class Address(peewee.Model):
    addressID=peewee.IntegerField()
    firstName=peewee.TextField()
    lastName=peewee.TextField()
    streetAddress=peewee.TextField()
    city=peewee.TextField()
    state=peewee.TextField()
    zipCode=peewee.TextField()

    class Meta:
        database = database

###############
if __name__ == "__main__":
    try:
        database.create_tables([Reading, Info,Address])
        print("Tables have been created.")
    except peewee.OperationalError:
        print ("Tables already exists.")

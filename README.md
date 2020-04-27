# Power Sensor Installation Files

This respository contains accompanying files for the blog post that describes the connection of an ACS712 based power sensor module with a Raspberry Pi to monitor the operation of a pump.

## `current.py`

This is the Python program that reads the current value from the sensor.

## `current.service`

The service file to run the `current.py` file.

## `panel-alerting.json`

The json for the panel graph with alerting included

## `panel.json`

A **very** simple graph for the power monitoring

## `septic-exporter.py`

The custom Python exporter program to make the current measuremens available to Prometheus 

## `septic-exporter.service`

The service file to run the `septic-exporter.py` program.

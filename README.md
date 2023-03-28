# Market Analyze

This program analyzes the correlation coefficient (corr) of market data. The program automatically deletes data that does not have the same date, and the resulting correlation coefficient ranges from -1 to 1, where -1 represents a perfect negative correlation and 1 represents a perfect positive correlation.

## Requirements

- Python 3 or above
- NumPy package

## Installation

To install the NumPy package, run the following command:

``
pip install numpy
``

## Usage

Before running the program, modify the data in `arr1` and `arr2` according to your needs. For example:

```python
arr1 = [["2000-01-04","30.6020"],["2000-01-05","30.8000"]]
arr2 = [["2000-01-04","20.6020"],["2000-01-05","25.8000"]]
```

## RUN

``
python analyze.py
``
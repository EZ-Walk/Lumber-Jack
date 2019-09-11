# Lumber-Jack
app usage logging module

# Usage
- import Lumber Jack with `from lumberJack import lumberJack`
- initialize a logger with `logger_1 = lumberJack(`name for the log`, [`list of column names`])`
- to log an event do `logger_1.log([`event details in the same order as column names`])`, lumberJack will make sure that you have given it the correct amount of items to add to the log and will tell you if you did not
- to get a pandas dataframe of a log use `logger_1.export()`, the return value will be a dataframe


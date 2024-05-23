#!/usr/bin/python
""" filechnages modues

This is my solution for Live Project by Manning.com 
"Automatically Tracking File Changes with Python"
"""
import sqlite3

def connect_db(db_name):
    """ connect to sqlite db
    
    Connect to Existing Sqlite DB
    If not Exists, Create New DB
    
    Args:
        db_name(str): Sqlite Database Name will be connected or Created.
    Returns:
        sqlite3.Connection: Connection of the SQLite
    Examples:
        >>> con = connect_db("TEST")
    """
    con = sqlite3.connect(db_name)

    return con

def exec_query(con, sql):
    """ execute query to database

    Execute Arbitrary Query to the connected Database

    Args:
        con (sqlite3.Connection): Connection object instance of the target database
        sql (str): SQL Query strings.
    Returns:
        sqlite3.Cursor: Cursor object instance whitch have result of the immediately before query.
    Raises:
        sqlite3.Error: Occure when Invalid SQL Query or other Invalid SQLite Operations 
    Examples:
        >>> con = connect_db("TEST")
        >>> res = exec_quer(con, "SELECT * FROM test_table")
    """
    cursor = con.cursor()
    try:
        return cursor.execute(sql)
    except sqlite3.Error as e:
        raise e

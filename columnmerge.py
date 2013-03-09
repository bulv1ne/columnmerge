#!/usr/bin/python

class Column:
    def __init__(self, rows):
        self.locked = False
        self.rows = rows

    def __enter__(self):
        self.locked = True
    
    def __exit__(self, type, value, traceback):
        self.locked = False

def iter_column(columns):
    for column in columns:
        if column.locked:
            continue
        # Automatic lock and unlock column
        with column:
            for row in column.rows:
                yield (row,)
                for i in iter_column(columns):
                    yield (row,) + i


if __name__ == "__main__":
    
    data = [
        ['A1','A2'],
        ['B1','B2'],
        ['C1','C2']
    ]
    
    # Convert data to columns
    columns = map(Column, data)
    
    # Go over the iteration and print the result
    for x in iter_column(columns):
        print x
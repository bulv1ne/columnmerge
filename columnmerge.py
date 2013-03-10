#!/usr/bin/python

class Column:
    def __init__(self, rows):
        self.locked = False
        self.rows = rows

    def __enter__(self):
        self.locked = True
    
    def __exit__(self, type, value, traceback):
        self.locked = False

def iter_column(data):
    def _iter(columns):
        for column in columns:
            # If locked, skip this column
            if column.locked:
                continue
            # Automatic lock and unlock column
            with column:
                for row in column.rows:
                    # Return self
                    yield (row,)
                    # Get underlaying columns also
                    for i in _iter(columns):
                        # Return self + followers
                        yield (row,) + i
    # Convert data into columns
    columns = map(Column, data)
    # Return the generator
    return _iter(columns)


if __name__ == "__main__":
    
    data = [
        ['A1','A2'],
        ['B1','B2'],
        ['C1','C2']
    ]
    
    # Go over the iteration and print the result
    for x in iter_column(data):
            print ' '.join(x)


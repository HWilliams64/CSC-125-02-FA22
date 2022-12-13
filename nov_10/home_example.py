import json


class Transaction:

    def __init__(self, id: int, type: str, amount: float):
        self.id: int = id
        self.type: str = type
        self.amount: float = amount

    def __str__(self):
        return f'Transaction[{self.id}] {self.type} ${self.amount}'

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return hasattr(other, 'id') and other.id == self.id


transaction_list = [
    Transaction(1, 'a', 1),
    Transaction(1, 'b', 2),
    Transaction(2, 'c', 3),
    Transaction(2, 'd', 4),
]


def update_transactions(file_path: str, transaction_list: list):
    for transaction in transaction_list:
        json_str = json.dumps(transaction.__dict__)
        #print(json_str)


update_transactions('./transaction.json', transaction_list)


py_obj = {
            'key': "old_value",
            'other_key': "value"
          }

py_obj['new_key'] = 'value'
print(py_obj)

def swap_value(file_path: str, key: str, replacement):
    # load the file at the specified file path
    # convert the string in the file to a python object using json.loads
    old_value = py_obj[key]
    py_obj[key] = replacement
    # convert the python object to a json string using json.dumps
    # save the json string to the file_path
    return old_value


swap_value(py_obj, 'key', 'replacement')

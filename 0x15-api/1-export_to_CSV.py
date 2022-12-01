#!/usr/bin/python3
"""
    Takes an argument passed to the script to be used in an API query.
    Retrieved data is then parsed to be dumped in a CSV file.
"""
import sys
import csv
import json
import requests



if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_d = {}
        todo_l = []
        URL = 'https://jsonplaceholder.typicode.com/'
        user_resp = requests.get(URL + f'users/{sys.argv[1]}', timeout=3)
        todo_resp = requests.get(URL + f'todos?userId={sys.argv[1]}', timeout=3)
        if all([user_resp, todo_resp]) is not None:
            try:
                user_d = json.loads(user_resp.text)
                todo_l = json.loads(todo_resp.text)
            except json.JSONDecodeError:
                pass
            if isinstance(todo_l, list) and isinstance(user_d, dict) and user_d != {}:
                with open(sys.argv[1] + '.csv', 'w', newline='', encoding="utf-8") as csvfile:
                    write_file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                    for todo in todo_l:
                        line = [user_d.get('id'), user_d.get('username'),
                                todo.get('completed'), todo.get('title')]
                        write_file.writerow(line)

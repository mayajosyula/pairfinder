from flask import Flask, render_template, request, redirect
import pandas as pd
from matchings import get_matching

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST" and 'inputfile' in request.files:
        file = request.files['inputfile']
        # print(file.read())
        df = pd.read_csv(file) # works
        print(df)
        (status, matches) = get_matching(df)
        # print(df.to_json())
        print(matches)
        return render_template("results.html", status=status, matches=matches)
    return "error: file not uploaded"
     
@app.route("/submit", methods=["GET", "POST"])
def handle_data():
    if request.method == "POST":
        # data = request.form.getlist("name")
        # print(type(data)) 
        # data1 = request.form.getlist("row 1")
        # print(data1)
        test = request.form
        table_list = []
        max_len = 0
        for key in test.keys():
            name_added = False
            current_row = []
            for value in test.getlist(key):
                if not name_added:
                    # add name to list
                    current_row.append(value)
                    name_added = True
                else:
                    # add checkboxes to list
                    col = int(value.split('-')[-1])
                    set_list(current_row, col, 'x')
                # print(f'{key} : {value}')
            if len(current_row) > max_len:
                max_len = len(current_row)
            table_list.append(current_row)
        for row in table_list:
            row += [None] * (max_len - len(row))
        fields = ["Name"]
        for i in range(max_len - 1):
            fields += [f'pref {i}']
        table_list.insert(0, fields)
        df = pd.DataFrame(table_list)
        df.columns = df.iloc[0]
        df = df[1:]
        (status, matches) = get_matching(df)
        return render_template("results.html", status=status, matches=matches)
    return "error: table not filled correctly"

def set_list(l, i, v):
      try:
          l[i] = v
      except IndexError:
          for _ in range(i-len(l)+1):
              l.append(None)
          l[i] = v

if __name__ == "__main__":
    app.run(debug=True)
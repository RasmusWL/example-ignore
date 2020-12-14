from flask import Flask, request, redirect


app = Flask(__name__)


@app.route('/some/path/bad1')
def unsafe1():
    target = request.args.get('target', '')
    if "example.com" in target: # lgtm ignore
        return redirect(target)

app.run()

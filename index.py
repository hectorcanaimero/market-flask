from app import app


@app.route('/')
@app.route('/index')
def Index():
    return {"ok": True, "data": {"message": "Index"}}, 200


if __name__ == '__main__':
    app.run()

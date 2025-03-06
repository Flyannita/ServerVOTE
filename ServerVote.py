from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
Login = "Koshka"
Password = "Koshka993"
Votes = {
    "Флюня": 0,
    "Тим": 0,
    "Окси": 0,
    "Злата": 0
}

@app.route("/login", methods=["POST"])
def Check():
    Data = request.get_json()  # reguest - запрос с сайта,
    login = Data.get("login")
    password = Data.get("password")
    if not(login) or not(password):
        return jsonify({"error": "no key or value"}), 400
    else:
        if Login!=login or Password!=password:
            return jsonify({"error": "login or password don't match"}), 400
        else:
            return jsonify({"message": "Enter successful", "success": True}), 200



@app.route("/add", methods=["POST"])
def AddVote():
    Data = request.get_json()  # reguest - запрос с сайта,
    VoteName = Data.get("name")
    Votes[VoteName] += 1
    return jsonify({"message": "Vote add successful"})


@app.route("/statistic", methods=["GET"])
def GetStatistic():
    Num = Votes.values()
    Num = sum(Num)
    # я не умеб 3:(количество голосовавших)*100
    N = Votes.items()
    percentage = dict()
    for i,l in N:
        if Num==0:
            return jsonify({"message": "no votes", "Votes": Votes})
        else:
            l = round(l/Num*100)
            percentage[i] = l

    return jsonify({"message": "get successful", "Votes": percentage})


@app.route("/deleteAdmin", methods=["POST"])
def deleteAdmin():
    Data = request.get_json()
    VoteName = Data.get("name")
    Votes[VoteName] -= 1
    return jsonify({"message": "Vote delete successful", "warning":"Админ, ата-та, у вас нет права на голосование, ваш голос удален"})





if __name__=="__main__":
    app.run(debug=True)
from flask import jsonify, request, abort

people_inf = [{"name": "Lisa Simpson", "age": 43, "job": "teacher"},
              {"name": "Bart Simpson", "age": 47, "job": "skateboarder"}]


# function returns list of people as json

def people_info():
    return jsonify(people_inf)


def person_add():
    try:
        person_data = request.get_json(force=True)

        # try an
        for key_name in list(person_data.keys()):
            if key_name not in ["name", "job", "age"]:
                raise KeyError
        if len(person_data.keys()) != 3:
            raise KeyError

        people_inf.append(person_data)
    except KeyError:
        abort(400, "Did not provide acceptable input parameters")
    except Exception as e:
        print(e)
        abort(400, str(e))
    return jsonify(success=True)
    # JSON person object
    # extract data from the request
    # request.get_json(force=True)

    # get attributes: name etc
    # validation?

    # add the person to our store
    # response dict success message

    # except
    # print exception
    # reponse to client to denote failure
    # abort(status code) 400 bad request


# return person
def person_get(id: int):
    return jsonify(people_inf[id])


def person_put(id: int):
    try:
        if id >= len(people_inf):
            raise KeyError
        person_new_data = request.get_json()
        people_inf[id] = person_new_data
        return jsonify(success=True)
    except KeyError:
        abort(400, "Provided an invalid key, max id number is: {}".format(len(people_inf)))

def hello_from_two():
    return "hello from muhammad and ruxandra"


def db():
    return "Hello DB"


def hello():
    return "Hello from Flask!!!!!"


def user_profile(id):
    return "Hello person {}".format(id)

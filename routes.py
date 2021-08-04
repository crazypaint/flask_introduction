from middleware import *
from flask import jsonify

# url to function mappings
def initialise_routes(app):
    # url, text-based name for end point, function pointer
    app.add_url_rule("/api/hello/", "hello", hello, methods=['GET'])
    app.add_url_rule("/api/db/", "db", db)
    app.add_url_rule("/api/greeting/", "greeting", hello_from_two)
    app.add_url_rule("/api/people/info/", "people info", people_info)
    app.add_url_rule("/api/profile/<id>", "profile", user_profile)
    app.add_url_rule("/api/", "list_routes", list_routes, defaults={'app': app})

    app.add_url_rule("/api/person/<int:id>", "person put", person_put, methods=["PUT"])
    app.add_url_rule("/api/person/<int:id>", "person get", person_get, methods=["GET"])
    app.add_url_rule("/api/person/", "person add", person_add, methods=["POST"])


def list_routes(app):
    # app.url_map; where all the rule are living
    # url_map.iter_rules() returns an iterator

    # create an empty list called routes
    routes = []
    for route in app.url_map.iter_rules():
        print(route)
        print(route.endpoint)
        print(route.methods)
        # create a dict
        # 'Route' - cast to string
        # 'Endpoint'
        # 'Methods' - cast to a list
        # add the dict route to routes list
        routes.append({
            "Route": str(route),
            "Endpoint": route.endpoint,
            "Methods": list(route.methods)
        })


    # return dict
    # 'Routes' - list of routes
    # 'Total' - count of number of routes
    return jsonify({
        "Routes": routes,
        "Total": len(routes)
    })

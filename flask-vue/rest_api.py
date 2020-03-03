from flask_restplus import Resource, fields, Namespace

api = Namespace('rest', description='a simple rest interface')

person_model = api.model(name='Person', model={
    'name': fields.String(required=True, description='Name of the person'),
    'address': fields.List(fields.String, required=True, description='Address of the person'),
    'age': fields.Integer(required=True, description='Age of the person')
})

NEW_PERSON = {
    'name': 'David Gmeindl',
    'address': ['Austria', 'Graz', 'Hauptplatz 24'],
    'age': 31
}


@api.route('/person')
class Person(Resource):
    @api.doc('get_person')
    @api.marshal_with(person_model)
    def get(self):
        return NEW_PERSON

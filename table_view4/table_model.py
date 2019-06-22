from collections import namedtuple

from atom.api import (Atom, Unicode, Range, ContainerList, Bool)

TableSelection = namedtuple('TableSelection', "item, row, column, widget")


class Person(Atom):
    """ A simple class representing a person object.

    """
    last_name = Unicode()

    first_name = Unicode()

    age = Range(low=0)

    debug = Bool(False)

    def __repr__(self, *args, **kwargs):
        return "Person(first_name={p.first_name},last_name={p.last_name})".format(p=self)


class TableModel(Atom):
    people = ContainerList(Person)

    def add_persons(self):
        for i in range(10):
            age = len(self.people)
            person = Person(last_name='Doe-{}'.format(age), first_name='John-{}'.format(age), age=age)
            self.people.insert(0, person)

    def remove_person(self, selection_info=None):
        print(selection_info)
        if selection_info:
            for item in selection_info:
                if item in self.people:
                    self.people.remove(item)
        else:
            self.people.pop()


data_model = TableModel(people=[
    Person(last_name='Barker-%i' % i,
           first_name='Bob%i' % i,
           age=i,
           debug=bool(i & 1))
    for i in range(10000)  # 10000
])

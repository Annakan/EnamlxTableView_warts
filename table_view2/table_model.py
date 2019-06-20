from atom.api import (Atom, Unicode, Range, ContainerList, Bool)


class Person(Atom):
    """ A simple class representing a person object.

    """
    last_name = Unicode()

    first_name = Unicode()

    age = Range(low=0)

    debug = Bool(False)

    def __repr__(self, *args, **kwargs):
        return "Person(first_name={p.first_name},last_name={p.last_name})".format(p=self)


def _extract_rows_from_sel_info(sel_info, max_elems):
    return list(reversed(sorted({index for index in
                                 (s_index.row() for s_index in sel_info)
                                 if index < max_elems})))


class TableModel(Atom):
    people = ContainerList(Person)

    def add_persons(self):
        for i in range(10):
            age = len(self.people)
            person = Person(last_name='Doe-{}'.format(age), first_name='John-{}'.format(age), age=age)
            self.people.insert(0, person)

    def remove_persons(self, selection_info=None):
        rows = _extract_rows_from_sel_info(selection_info, len(self.people))
        print(f"rows : {rows}")
        if rows:
            for ix in rows:
                del self.people[ix]
        else:
            self.people.pop()


data_model = TableModel(people=[
    Person(last_name='Barker-%i'%i,
           first_name='Bob%i'%i,
           age=i,
           debug=bool(i&1))
    for i in range(10000) # 10000
])

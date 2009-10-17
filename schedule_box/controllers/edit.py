import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from schedule_box.lib.base import BaseController, render

import schedule_box.model as model
from schedule_box.model.meta import Session
import schedule_box.forms as forms

import tw.forms as twf

algorithm_form = twf.TableForm('algorithm_form', action='/edit/algorithm', children=[
    twf.TextField('Name'),
    twf.TextArea('Algorithm'),
    ])
volunteer_form = twf.TableForm('algorithm_form', action='/edit/algorithm', children=[
    twf.TextField('Name'),
    twf.TextArea('Algorithm'),
    ])

log = logging.getLogger(__name__)

class EditController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/edit.mako')
        # or, return a response
        return 'Hello World'

    def algorithm(self, id=None):
        if id:
            c.algorithm = Session.query(model.Algorithm).filter_by(id=id).first()
            if not c.algorithm:
                c.algorithm = model.Algorithm()
                c.algorithm.id = id
            c.algorithm.name = request.POST.get('name','')
            c.algorithm.code = request.POST.get('code','')
            Session.add(c.algorithm)
        else:
            c.algorithm = None
        c.form = algorithm_form
        return render('algorithm.mako')

    def volunteer(self, id=None):
        if id:
            c.volunteer = Session.query(model.Volunteer).filter_by(id=id).first()
            if not c.volunteer:
                c.volunteer = model.Volunteer()
                c.volunteer.id = id
        else:
            c.volunteer = None
        c.volunteer.name = request.POST.getone('name')
        c.volunteer.schedule = request.POST.getone('schedule')
        c.volunteer.preferred_number_of_hours = request.POST.getone('preferred_number_of_hours')
        Session.add(c.volunteer)
        return render('volunteer.mako')

    def dataset(self, id=None):
        if id:
            c.dataset = Session.query(model.Dataset).filter_by(id=id).first()
            if not c.dataset:
                c.dataset = model.Dataset()
                c.dataset.id = id
        else:
            c.volunteer = None
        c.dataset.name = request.POST.get('name','')
        volunteer_ids = request.POST.get('volunteers',[])
        for volunteer_id in volunteer_ids:
            volunteer = Session.query(model.Volunteer).filter_by(id=volunteer_id).first()
            if volunteer:
                c.dataset.volunteers.append(volunteer)
        Session.add(c.dataset)
        c.volunteers = Session.query(model.Volunteer).all()
        return render('dataset.mako')

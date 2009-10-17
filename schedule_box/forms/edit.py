import tw.forms as twf

algorithm_form = twf.TableForm('algorithm_form', action='/edit/algorithm', children=[
    twf.TextField('Name'),
    twf.TextArea('Algorithm'),
    ])

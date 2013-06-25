import web

my_form = web.form.Form(web.form.Textbox('', class_='textfield', id='textfield'),)
                
def make_text(string):
    return string

def POST(self):
    form = my_form()
    form.validates()
    s = form.value['textfield']
    return make_text(s)
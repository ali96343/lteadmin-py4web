from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from py4web.core import Template
from . common import db, session, T, cache, auth



@action('index')
#@action.uses('index.html', )
@action.uses(Template('index.html', delimiters='[Z[ ]]'))
def index():
    message= "index.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('register')
#@action.uses('register.html', )
@action.uses(Template('register.html', delimiters='[Z[ ]]'))
def register():
    message= "register.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('pace')
#@action.uses('pace.html', )
@action.uses(Template('pace.html', delimiters='[Z[ ]]'))
def pace():
    message= "pace.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('buttons')
#@action.uses('buttons.html', )
@action.uses(Template('buttons.html', delimiters='[Z[ ]]'))
def buttons():
    message= "buttons.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('mailbox')
#@action.uses('mailbox.html', )
@action.uses(Template('mailbox.html', delimiters='[Z[ ]]'))
def mailbox():
    message= "mailbox.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('flot')
#@action.uses('flot.html', )
@action.uses(Template('flot.html', delimiters='[Z[ ]]'))
def flot():
    message= "flot.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('topXnav')
#@action.uses('top-nav.html', )
@action.uses(Template('top-nav.html', delimiters='[Z[ ]]'))
def topXnav():
    message= "top-nav.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('data')
#@action.uses('data.html', )
@action.uses(Template('data.html', delimiters='[Z[ ]]'))
def data():
    message= "data.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('widgets')
#@action.uses('widgets.html', )
@action.uses(Template('widgets.html', delimiters='[Z[ ]]'))
def widgets():
    message= "widgets.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('X404')
#@action.uses('404.html', )
@action.uses(Template('404.html', delimiters='[Z[ ]]'))
def X404():
    message= "404.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('simple')
#@action.uses('simple.html', )
@action.uses(Template('simple.html', delimiters='[Z[ ]]'))
def simple():
    message= "simple.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('boxed')
#@action.uses('boxed.html', )
@action.uses(Template('boxed.html', delimiters='[Z[ ]]'))
def boxed():
    message= "boxed.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('fixed')
#@action.uses('fixed.html', )
@action.uses(Template('fixed.html', delimiters='[Z[ ]]'))
def fixed():
    message= "fixed.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('timeline')
#@action.uses('timeline.html', )
@action.uses(Template('timeline.html', delimiters='[Z[ ]]'))
def timeline():
    message= "timeline.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('icons')
#@action.uses('icons.html', )
@action.uses(Template('icons.html', delimiters='[Z[ ]]'))
def icons():
    message= "icons.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('blank')
#@action.uses('blank.html', )
@action.uses(Template('blank.html', delimiters='[Z[ ]]'))
def blank():
    message= "blank.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('advanced')
#@action.uses('advanced.html', )
@action.uses(Template('advanced.html', delimiters='[Z[ ]]'))
def advanced():
    message= "advanced.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('inline')
#@action.uses('inline.html', )
@action.uses(Template('inline.html', delimiters='[Z[ ]]'))
def inline():
    message= "inline.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('login')
#@action.uses('login.html', )
@action.uses(Template('login.html', delimiters='[Z[ ]]'))
def login():
    message= "login.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('editors')
#@action.uses('editors.html', )
@action.uses(Template('editors.html', delimiters='[Z[ ]]'))
def editors():
    message= "editors.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('lockscreen')
#@action.uses('lockscreen.html', )
@action.uses(Template('lockscreen.html', delimiters='[Z[ ]]'))
def lockscreen():
    message= "lockscreen.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('chartjs')
#@action.uses('chartjs.html', )
@action.uses(Template('chartjs.html', delimiters='[Z[ ]]'))
def chartjs():
    message= "chartjs.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('general')
#@action.uses('general.html', )
@action.uses(Template('general.html', delimiters='[Z[ ]]'))
def general():
    message= "general.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('profile')
#@action.uses('profile.html', )
@action.uses(Template('profile.html', delimiters='[Z[ ]]'))
def profile():
    message= "profile.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('calendar')
#@action.uses('calendar.html', )
@action.uses(Template('calendar.html', delimiters='[Z[ ]]'))
def calendar():
    message= "calendar.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('modals')
#@action.uses('modals.html', )
@action.uses(Template('modals.html', delimiters='[Z[ ]]'))
def modals():
    message= "modals.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('invoice')
#@action.uses('invoice.html', )
@action.uses(Template('invoice.html', delimiters='[Z[ ]]'))
def invoice():
    message= "invoice.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('X500')
#@action.uses('500.html', )
@action.uses(Template('500.html', delimiters='[Z[ ]]'))
def X500():
    message= "500.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('index2')
#@action.uses('index2.html', )
@action.uses(Template('index2.html', delimiters='[Z[ ]]'))
def index2():
    message= "index2.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('sliders')
#@action.uses('sliders.html', )
@action.uses(Template('sliders.html', delimiters='[Z[ ]]'))
def sliders():
    message= "sliders.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('morris')
#@action.uses('morris.html', )
@action.uses(Template('morris.html', delimiters='[Z[ ]]'))
def morris():
    message= "morris.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('collapsedXsidebar')
#@action.uses('collapsed-sidebar.html', )
@action.uses(Template('collapsed-sidebar.html', delimiters='[Z[ ]]'))
def collapsedXsidebar():
    message= "collapsed-sidebar.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('compose')
#@action.uses('compose.html', )
@action.uses(Template('compose.html', delimiters='[Z[ ]]'))
def compose():
    message= "compose.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('readXmail')
#@action.uses('read-mail.html', )
@action.uses(Template('read-mail.html', delimiters='[Z[ ]]'))
def readXmail():
    message= "read-mail.html"
    user= "first second third"
    return dict(message=message, user=user)


@action('invoiceXprint')
#@action.uses('invoice-print.html', )
@action.uses(Template('invoice-print.html', delimiters='[Z[ ]]'))
def invoiceXprint():
    message= "invoice-print.html"
    user= "first second third"
    return dict(message=message, user=user)


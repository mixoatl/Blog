from operator import pos
from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)

from werkzeug.exceptions import abort

from myblog.models.post import Post
from myblog.models.user import User
from myblog.models.coment import Coment

from myblog.views.auth import login_required

from myblog import db

coments = Blueprint('coments', __name__)

#Obtner un ususario
def get_user(id):
    user = User.query.get_or_404(id)
    return user


@coments.route("/")
def index():
    coments = Coment.query.all()
    coments = list(reversed(coments))
    db.session.commit()
    return render_template('blog/index.html', coments = coments, get_user=get_user)

#Publicar un comentario
@coments.route('/blog/createCom', methods=('GET','POST'))
@login_required
def createCom():
    if request.method == 'POST':
        body = request.form.get('comentario')

        comentario = Coment(g.user.id, body)

        error = None

        if not body:
            error = 'Se requiere un mensaje...'
        
        if error is not None:
            flash(error)
        else:
            db.session.add(comentario)
            db.session.commit()
            return redirect(url_for('blog.index'))
        
        flash(error)
        
    return render_template('blog/createCom.html')

def get_coment(id, check_author=True):
    comentario = Coment.query.get(id)

    if comentario is None:
        abort(404, f'Id {id} del comentario no existe.')

    if check_author and comentario.author != g.user.id:
        abort(404)
    
    return comentario
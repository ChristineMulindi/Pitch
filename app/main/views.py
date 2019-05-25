
from flask_login import login_required




@main.route('/pitches/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
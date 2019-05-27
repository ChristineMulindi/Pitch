from flask import render_template, request, redirect, url_for,abort
from flask_login import login_required
from . import main
from ..models import Comment, User, Post
from .forms import CommentForm, UpdateProfile, PostForm
from flask_login import login_required,current_user
from ..import db,photos


@main.route("/",methods=["GET","POST"])
def index():
    categories=["sales pitch", "business pitch", "music pitch", "elevator pitch"]
    return render_template('index.html',categories=categories)


@main.route("/pitches/<string:category>")
def posts(category):
    posts=list(Post.query.filter_by(category=category))
    return render_template("./pitches.html",posts=posts)

@main.route("/add",methods=["GET","POST"])
@login_required
def add():
    post_form=PostForm()
    if post_form.validate_on_submit():
        print(post_form.category.data)
        post=Post(text=post_form.post.data,category=post_form.category.data,user_id=current_user.id)
        post.save_post()
        return redirect(url_for("main.index"))
    return render_template('./add.html',post_form=post_form)

@main.route("/pitch/<int:post_id>",methods=["GET","POST"])
def post(post_id):
    comment_form=CommentForm()
    if comment_form.validate_on_submit():
        comment=Comment(user_id=current_user.id,post_id=post_id,pitch_comment=comment_form.comment.data)
        comment.save_comment()
    comments=Comment.query.filter_by(post_id=comment_id)
    post=Post.query.filter_by(id=post_id).first()
    
    return render_template("./pitch.html", comment_form = comment_form)



@main.route('/pitches/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    comment = get_comment(id)

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        # Updated comment instance
        new_comment = Comment(user_id=user.id, pitches_comment=comment, user=current_user)

        # save comment method
        new_commernt.save_comment()
        return redirect(url_for('.pitches', id=comment.id))
       

    title = f'{pitches.title} comment'
    return render_template('new_comment.html', title=title, comment_form=form, pitches=pitches)



@main.route('/comment/<int:id>')
def single_comment(id):
    comment=Comment.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.pitches_comment,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('comment.html',comment = comment,format_comment=format_comment)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

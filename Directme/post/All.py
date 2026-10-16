
from flask_login import current_user,login_manager,login_required
from flask import render_template,redirect,url_for,flash,abort,request,Blueprint
from Directme.post.form import MyPost_form,Updatepost_form
from db_structure import db,Post
from Directme.post.func import save_med

posts=Blueprint('post',__name__)


@posts.route('/createpost',methods=["GET","POST"])
@login_required
def cpost():
    
    form=MyPost_form()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            if form.media.data:
                pcs=save_med(form.media.data)
                pth=pcs.split('.')
                post=Post(title=form.title.data,content=form.content.data, media_type=pcs,media_path=pth[-1], author=current_user)
                db.session.add(post)
                db.session.commit()
                print(post.media_path)
                if pth[-1].lower()=="mp3" or pth[-1].lower()=="m4a":
                    return redirect(url_for("posts.audpost"))
                elif pth[-1].lower()=="mp4"   :
                    return redirect(url_for("posts.vpost"))
                else:
                    return redirect(url_for("posts.ppost"))
        return render_template("createpost.html",form=form)

    

@posts.route('/post',methods=["GET","POST"])
def post():
    page=request.args.get('p',1,type=int)
    post=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=3)
    return render_template("post.html",post=post)

@posts.route('/mainpost/<int:id>',methods=["GET","POST"])
@login_required
def mainpost(id):
    post=Post.query.get_or_404(id) 
    nost=Post.query.all()
    if current_user.is_authenticated:
        return render_template("mainpost.html",post=post,nost=nost)

@posts.route('/editpost/<int:id>',methods=["GET","POST"])
def editpost(id):
    form=Updatepost_form()
    post=Post.query.get_or_404(id) 
    if current_user.is_authenticated:
        if post.author !=current_user:
            return abort(403)

        if form.validate_on_submit():
            post.content=form.content.data
            post.title=form.title.data
            db.session.commit()
            return redirect(url_for("posts.post"))
        form.content.data=post.content
        form.title.data=post.title
        return render_template("editpost.html",post=post,form=form)

@posts.route('/vpost',methods=["GET","POST"])
def vpost():
    if current_user.is_authenticated:
        post = Post.query.filter(Post.media_path == "mp4").all()
        return render_template("vpost.html",post=post)
    return render_template("post.html")

@posts.route('/ppost',methods=["GET","POST"])
def ppost():
    if current_user.is_authenticated:
        post = Post.query.filter(Post.media_path != "mp4").all()

        return render_template("ppost.html",post=post,photos=post)
                
    return render_template("post.html")

@posts.route('/audpost',methods=["GET","POST"])
def audpost():
    if current_user.is_authenticated:
        post = Post.query.filter(Post.media_path == "mp3").all()
        return render_template("audpost.html",post=post)
    return render_template("post.html")



@posts.route('/googlepost')
def gpost():
    if current_user.is_authenticated:
        return render_template("gpost.html")

@posts.route('/servicepost')
def srvpost():
    if current_user.is_authenticated:
        return render_template("srvpost.html")

@posts.route('/contact')
def contact():
    if current_user.is_authenticated:
        return render_template("contact.html")




@posts.route('/deletepost/<int:id>',methods=["POST"])
def deletepost(id):
    post=Post.query.get_or_404(id)  
    if current_user.is_authenticated:
        if post.author!=current_user:
            return abort(403) 
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for("posts.post"))
    return render_template("mainpost.html",post=post)

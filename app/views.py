from flask import render_template, flash, redirect, session, url_for, request, \
    g, jsonify
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from flask.ext.sqlalchemy import get_debug_queries,functools
from flask.ext.babel import gettext
from datetime import datetime
from guess_language import guessLanguage
from app import app, db, lm, oid, babel
from .forms import LoginForm, EditForm, PostForm, SearchForm
from .models import User, Post, Dolaze, Razredi, Dnevnik
from .emails import follower_notification
from .translate import microsoft_translate
from config import POSTS_PER_PAGE, MAX_SEARCH_RESULTS, LANGUAGES, \
    DATABASE_QUERY_TIMEOUT


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()
        g.search_form = SearchForm()
    g.locale = get_locale()


@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= DATABASE_QUERY_TIMEOUT:
            app.logger.warning(
                "SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" %
                (query.statement, query.parameters, query.duration,
                 query.context))
    return response


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/<int:page>', methods=['GET', 'POST'])
@login_required
def index(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('index.html',
                           title='Početna',
                           form=form,
                           posts=posts)

@app.route('/proslava', methods=['GET', 'POST'])
@login_required
def proslava(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('proslava.html',
                           title='Proslava',
                           form=form,
                           posts=posts)

@app.route('/prosirenaproslava', methods=['GET', 'POST'])
@login_required
def prosirenaproslava(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('prosirenaproslava.html',
                           title='Prosirena proslava',
                           form=form,
                           posts=posts)

@app.route('/IV01', methods=['GET', 'POST'])
@login_required
def IV01(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV01').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV01').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV01.html',
                           title='IV-01',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV02', methods=['GET', 'POST'])
@login_required
def IV02(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV02').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV02').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV02.html',
                           title='IV-02',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV03', methods=['GET', 'POST'])
@login_required
def IV03(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV03').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV03').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV03.html',
                           title='IV-03',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV04', methods=['GET', 'POST'])
@login_required
def IV04(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV04').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV04').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV04.html',
                           title='IV-04',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV05', methods=['GET', 'POST'])
@login_required
def IV05(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV05').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV05').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV05.html',
                           title='IV-05',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV06', methods=['GET', 'POST'])
@login_required
def IV06(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV06').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV06').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV06.html',
                           title='IV-06',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV07', methods=['GET', 'POST'])
@login_required
def IV07(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV07').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV07').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV07.html',
                           title='IV-07',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV08', methods=['GET', 'POST'])
@login_required
def IV08(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV08').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV08').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV08.html',
                           title='IV-08',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV09', methods=['GET', 'POST'])
@login_required
def IV09(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV09').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV09').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV09.html',
                           title='IV-09',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV10', methods=['GET', 'POST'])
@login_required
def IV10(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV10').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV10').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV10.html',
                           title='IV-10',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV11', methods=['GET', 'POST'])
@login_required
def IV11(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV11').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV11').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV11.html',
                           title='IV-11',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/IV12', methods=['GET', 'POST'])
@login_required
def IV12(page=1):
    form = PostForm()
    if form.validate_on_submit():
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, timestamp=datetime.utcnow(),
                    author=g.user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Tvoje slanje je sada živo!'))
        return redirect(url_for('index'))
    dnevnik = Dnevnik.query.filter_by(razred='IV12').order_by(Dnevnik.prezime).all()
    dolaze = Dnevnik.query.filter_by(razred='IV12').filter_by(dolazi='D').order_by(Dnevnik.prezime).all()
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('IV12.html',
                           title='IV-12',
                           dnevnik=dnevnik,
                           dolaze=dolaze,
                           form=form,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash(gettext('Invalid login. Please try again.'))
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        nickname = User.make_valid_nickname(nickname)
        nickname = User.make_unique_nickname(nickname)
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
        # make the user follow him/herself
        db.session.add(user.follow(user))
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<nickname>')
@app.route('/user/<nickname>/<int:page>')
@login_required
def user(nickname, page=1):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash(gettext('User %(nickname)s not found.', nickname=nickname))
        return redirect(url_for('index'))
    posts = user.posts.paginate(page, POSTS_PER_PAGE, False)
    return render_template('user.html',
                           user=user,
                           posts=posts)


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash(gettext('Your changes have been saved.'))
        return redirect(url_for('edit'))
    elif request.method != "POST":
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)


@app.route('/follow/<nickname>')
@login_required
def follow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    if user == g.user:
        flash(gettext('You can\'t follow yourself!'))
        return redirect(url_for('user', nickname=nickname))
    u = g.user.follow(user)
    if u is None:
        flash(gettext('Cannot follow %(nickname)s.', nickname=nickname))
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash(gettext('You are now following %(nickname)s!', nickname=nickname))
    follower_notification(user, g.user)
    return redirect(url_for('user', nickname=nickname))


@app.route('/unfollow/<nickname>')
@login_required
def unfollow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    if user == g.user:
        flash(gettext('You can\'t unfollow yourself!'))
        return redirect(url_for('user', nickname=nickname))
    u = g.user.unfollow(user)
    if u is None:
        flash(gettext('Cannot unfollow %(nickname)s.', nickname=nickname))
        return redirect(url_for('user', nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash(gettext('You have stopped following %(nickname)s.',
                  nickname=nickname))
    return redirect(url_for('user', nickname=nickname))


@app.route('/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get(id)
    if post is None:
        flash('Post not found.')
        return redirect(url_for('index'))
    if post.author.id != g.user.id:
        flash('You cannot delete this post.')
        return redirect(url_for('index'))
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted.')
    return redirect(url_for('index'))


@app.route('/search', methods=['POST'])
@login_required
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('search_results', query=g.search_form.search.data))


@app.route('/search_results/<query>')
@login_required
def search_results(query):
    results = Post.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
    return render_template('search_results.html',
                           query=query,
                           results=results)


@app.route('/translate', methods=['POST'])
@login_required
def translate():
    return jsonify({
        'text': microsoft_translate(
            request.form['text'],
            request.form['sourceLang'],
            request.form['destLang'])})

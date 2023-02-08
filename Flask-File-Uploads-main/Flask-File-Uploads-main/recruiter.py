from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

# app.register_blueprint(job_post,url_prefix="/HR1")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files/jd'

class UploadFileResume(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

# @app.route('/', methods=['GET',"POST"])
@app.route('/hr', methods=['GET',"POST"])
def home():
    form = UploadFileResume()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        return "File has been uploaded."
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
from flask import send_file, Blueprint
import shutil
import uuid
import tempfile
import os
import zipfile
from app.api.helpers.permissions import is_admin

admin_blueprint = Blueprint('admin_blueprint', __name__, url_prefix='/v1/admin')
temp_dir = tempfile.gettempdir()
translations_dir = 'app/translations'

@admin_blueprint.route('/content/translations/all', methods=['GET'])
@is_admin
def download_translations():
    """Admin Translations Downloads"""
    uuid_literal = uuid.uuid4()
    zip_file_name = "translations{}".format(uuid_literal)
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(translations_dir):
            for name in files:
                zip_file.write(os.path.join(root, name))
    # zipf = zipfile.ZipFile('../{}'.format(zip_file_name), 'w', zipfile.ZIP_DEFLATED)
    # zipdir(temp_dir, zipf)
    # zipf.close()
    zip_new_file_path = os.path.join(temp_dir, zip_file_name)
    os.rename(zip_file_name, os.path.join(temp_dir, zip_file_name))
    return send_file(os.path.join(temp_dir, zip_file_name), mimetype='application/zip')
    # zip_file_ext = zip_file+'.zip'
    # shutil.make_archive(zip_file, "zip", translations_dir)
    # shutil.move(zip_file_ext, temp_dir)
    # path_to_zip = os.path.join(temp_dir, zip_file_ext)
    # from .helpers.tasks import delete_translations
    # delete_translations.apply_async(kwargs={'zip_file_path': path_to_zip}, countdown=600)
    # return send_file(path_to_zip,  mimetype='application/zip',
    #                  as_attachment=True,
    #                  attachment_filename='translations.zip')

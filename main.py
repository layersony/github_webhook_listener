from flask import Flask, request
import git
import os
import configparser

app = Flask(__name__)

# Read configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
repo_base_path = config['DEFAULT']['RepoBasePath']

@app.route('/webhook/<repo_name>', methods=['POST'])
def webhook(repo_name):
    if request.method == 'POST':
        repo_dir = os.path.join(repo_base_path, repo_name)
        if os.path.exists(repo_dir):
            repo = git.Repo(repo_dir)
            origin = repo.remotes.origin
            origin.pull()
            return '', 200
        else:
            return 'Repo does not exist', 400
    else:
        return 'Invalid request method', 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

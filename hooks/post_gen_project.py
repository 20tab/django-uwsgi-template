# cat post_gen_project.py
import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)



def remove_dirs():
    use_ansible = "{{cookiecutter.use_ansible}}" == "y"
    use_continuous_delivery_process = "{{cookiecutter.use_continuous_delivery_process}}" == "y"
    use_uwsgi_emperor_local = "{{cookiecutter.use_uwsgi_emperor_local}}" == "y"
    use_uwsgi_emperor_remote = "{{cookiecutter.use_uwsgi_emperor_remote}}" == "y"
    use_docker = "{{cookiecutter.use_docker}}" == "y"
    use_gitlab = "{{cookiecutter.use_gitlab}}" == "y"
    use_bitbucket = "{{cookiecutter.use_bitbucket}}" == "y"

    if not use_ansible:
        # remove top-level file inside the generated folder
        remove("ansible")

    if not use_continuous_delivery_process:
        # remove absolute path to file nested inside the generated folder
        remove("deployment")

    if not use_uwsgi_emperor_local:
        remove("uwsgiconf/local")

    if not use_uwsgi_emperor_remote:
        remove("uwsgiconf/remote")

    if not use_docker:
        remove("uwsgiconf/docker.ini")
        remove(".dockerignore")
        remove("Dockerfile")

    if not use_gitlab:
        remove(".gitlab-ci.yml")

    if not use_bitbucket:
        remove("bitbucket-pipelines.yml")


remove_dirs()

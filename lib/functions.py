import platform
import os


# SYSTEM
import re


def system_is_windows():
    os_system = platform.system()
    print(os_system)
    return os_system == 'Windows'


# PATH
def project_path(folder_name):
    folder_path = os.path.abspath(os.getcwd())
    folder_path = os.path.join(folder_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def resources_project_path(folder_name):
    folder_path = os.path.join(project_path("resources"), folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


# EMAIL VALIDATION
def email_check(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    return re.search(regex, email)

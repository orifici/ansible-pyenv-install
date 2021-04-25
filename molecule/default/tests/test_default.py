import os


def test_pyenv_dependencies(host):
    """ Make sure pyenv dependencies have been installed """
    PYENV_DEPS = [
        "zlib-devel",
        "bzip2",
        "bzip2-devel",
        "readline-devel",
        "sqlite",
        "sqlite-devel",
        "openssl-devel",
        "xz",
        "xz-devel",
        "libffi-devel",
        "git",
    ]
    for p_name in PYENV_DEPS:
        assert host.package(p_name).is_installed


def test_pyenv_installation(host):
    """ Make sure the pyenv install dir has the correct perms """
    pyenv_user = 'root'
    pyenv_dir = host.file("/root/.pyenv")
    assert pyenv_dir.is_directory
    assert pyenv_dir.user == pyenv_user
    assert pyenv_dir.group == pyenv_user


def test_pyenv_bashrc_config(host):
    """ Make sure bashrc contains the pyenv config"""
    user_home = '/root'
    bashrc = host.file(os.path.join(user_home, ".bashrc"))
    assert bashrc.is_file
    rc_config = 'export PATH="$HOME/.pyenv/bin:$PATH"'
    assert rc_config in bashrc.content_string
    rc_config = 'eval "$(pyenv init -)"'
    assert rc_config in bashrc.content_string
    rc_config = 'eval "$(pyenv virtualenv-init -)"'
    assert rc_config in bashrc.content_string

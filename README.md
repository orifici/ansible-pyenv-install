# Ansible pyenv install

An Ansible role to install pyenv

## Requirements

This role needs all packages in requirements.txt

```bash
pip install -r requirements.txt
```

## Role Variables

| Variable | Type| Description  | default | required? |
| --- | --- | --- | --- | --- |
| **os_users** | dict| each dictionary of type `{username_1: {"home": "string"}, username_2: {"home": "string"}` | {} | yes |

## Example Playbook

```yaml
- hosts: all
  roles:
     - ansible-pyenv-install
```

## Running molecule
|:warning: Before running molecule make sure you have installed all packages in requirements.txt |
|: ------ : |

```bash
molecule test
```

## License

Mit License

## Author Information

https://github.com/orifici

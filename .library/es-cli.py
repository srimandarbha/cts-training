DOCUMENTATION = '''
---
module: sriman
short_description: Sriman testing module.
options:
  name:
    description:
      - Description of name value.

  arg:
    description:
      - requires bool value for arg.
'''

from ansible.module_utils.basic import AnsibleModule
from re import match

def main():
    module = AnsibleModule(
            argument_spec = dict(
                name = dict(type='string', required=True),
                action = dict(type='string', required=True, default='status')
                )
            )

    action = module.params['action']
    name = module.params['name']

    for i in module.params.keys
        if type(i) != str:
            return module.fail_json(name=action, msg="Acceptable actions are start|stop|restart|monitor|status|setup <instance-name>")

    if na == True:
        return module.exit_json(name=name, arg=arg, msg='You took true option')
    
    if arg == False:
        return module.exit_json(name=name, arg=arg, msg='You took false option')


if __name__ == '__main__':
    main()

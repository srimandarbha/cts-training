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

def main():
    module = AnsibleModule(
            argument_spec = dict(
                name = dict(required=False, default='Default'),
                arg = dict(type='bool', required=False),
                )
            )

    name = module.params['name']
    arg = module.params['arg']

    if type(arg) != bool:
        return module.fail_json(name=name, msg="Please consider only bool values")

    if arg == True:
        return module.exit_json(name=name, arg=arg, msg='You took true option')
    
    if arg == False:
        return module.exit_json(name=name, arg=arg, msg='You took false option')


if __name__ == '__main__':
    main()

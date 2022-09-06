#!/usr/bin/python
import jinja2

class renderer:
    def __init__(self, templates_path):
        loader = jinja2.FileSystemLoader(searchpath=templates_path)
        self.env = jinja2.Environment(loader=loader)

    def render(self, template_name, **kwargs):
        template = self.env.get_template(template_name)
        return template.render(**kwargs)
 
jinja2_renderer = renderer("./bin/jinja2_templates")
output = jinja2_renderer.render("simple_template.tpl", some_variable="Namik", other_variable="Mesic")
print(output)




import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListView
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.text import LabelBase
from kivy.uix.settings import SettingsWithTabbedPanel
from kivy.logger import Logger

try:
    import particlesystem as kParticles
except ImportError:
    import pyparticlesystem as kParticles

import json
import random
import common

class MainApp(App):
    def build(self):
        """
        Build and return the root widget.
        """
        # The line below is optional. You could leave it out or use one of the
        # standard options, such as SettingsWithSidebar, SettingsWithSpinner
        # etc.
        self.settings_cls = SettingsWithTabbedPanel

        with open("sample.json") as f:
            class_data = json.load(f)       

        class_picked = class_data[1]

        new_particle = kParticles.ParticleSystem(class_picked["particles"])
        #TODO: Don't use static numbers
        new_particle.pos_hint = class_picked["particles_offset"]
        
        self.root.children[-3].source = class_picked["portrait"]

        if class_picked["particles_offset"]["z"] > 0:
            self.root.add_widget(new_particle)
        else:
            self.root.children[-2].add_widget(new_particle)

        if self.config.getdefault("Graphics", "particles", "1") == "1":
            new_particle.start()
    
        for font in common.FONTS:
            LabelBase.register(**font)

        return self.root

    def build_config(self, config):
        """
        Set the default values for the configs sections.
        """
        config.setdefaults('Graphics', {
            'particles': True,
        })

    def build_settings(self, settings):
        """
        Add our custom section to the default configuration object.
        """
        settings.add_json_panel('My Label', self.config, 'settings.json')

    def on_config_change(self, config, section, key, value):
        """
        Respond to changes in the configuration.
        """
        Logger.info("main.py: App.on_config_change: {0}, {1}, {2}, {3}".format(
            config, section, key, value))

        if section == "Graphics":
            if key == "particles":
                for widget in self.root.children:
                    if isinstance(widget, kParticles.ParticleSystem):
                        if value == "1":
                            widget.start()
                        else:
                            widget.stop()

    def close_settings(self, settings):
        """
        The settings panel has been closed.
        """
        Logger.info("main.py: App.close_settings: {0}".format(settings))
        super(MainApp, self).close_settings(settings)


    #def on_start(self):
    #    self.profile = cProfile.Profile()
    #    self.profile.enable()

    #def on_stop(self):
    #    self.profile.disable()
    #    self.profile.dump_stats('myapp.profile')

    def on_pause(self):
      # Here you can save data if needed
      return True

    def on_resume(self):
      # Here you can check if any data needs replacing (usually nothing)
      pass

class MainView(GridLayout):
    '''Uses :class:`CompositeListItem` for list item views comprised by two
    :class:`ListItemButton`s and one :class:`ListItemLabel`. Illustrates how
    to construct the fairly involved args_converter used with
    :class:`CompositeListItem`.
    '''

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)

        args_converter = lambda row_index, rec: {
            'text': str(self.size) + rec['text'],
            'loyalty': rec['loyalty'],
            'loyalty_source': common.LOYALTY[rec['loyalty'][0]],
            'height': common.ABILITY_HEIGHT
        }

        integers_dict = {str(i): {'text': "This is a test ability string #%s" % str(i),
                                  'loyalty': "0",
                                  'is_selected': False} for i in range(50)}

        item_sort_list  = sorted(integers_dict.items(), key=lambda x: int(x[1]["loyalty"]))
        item_sort_list.reverse()
        item_sort_list  = [ x for x,y in item_sort_list ]

        dict_adapter = DictAdapter(sorted_keys=item_sort_list,
                                   data=integers_dict,
                                   args_converter=args_converter,
                                   selection_mode='single',
                                   allow_empty_selection=False,
                                   template='ThumbnailedListItem')

        # Use the adapter in our ListView:
        list_view = ListView(adapter=dict_adapter)

        self.add_widget(list_view)

    #def on_size(self, *args):
    #    print("woof")
    #    print(args)

if __name__ == "__main__":
    MainApp().run()


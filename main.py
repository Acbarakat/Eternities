import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListView
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.text import LabelBase
from kivy.uix.settings import SettingsWithSpinner
from kivy.logger import Logger
from kivy.core.window import Window

try:
    import particlesystem as kParticles
except ImportError:
    import pyparticlesystem as kParticles

import json
import random
import common

class MainApp(App):
    use_kivy_settings = True

    class_data = {}

    def build(self):
        """
        Build and return the root widget.
        """
        self.settings_cls = SettingsWithSpinner

        Window.size = (1920, 1080)
        Window.minimum_width = 1280
        Window.minimum_height = 800
        #Window.clearcolor = (1, 0, 0, 1)
        #Window.fullscreen = True
        print(Window.dpi)
        print(Window.size)


        with open("classes.json") as f:
            self.class_data = json.load(f)

        class_picker        = self.root.ids["class_spinner"]
        class_picker.values = self.class_data.keys()
        class_picker.bind(text=self.on_class_change)
        class_picker.text   = self.class_data.keys()[0]

        #Register custom fonts
        for font in common.FONTS:
            LabelBase.register(**font)

        return self.root

    def on_class_change(self, class_picker, text):
        class_picked = self.class_data[text]

        #Use the particle system
        new_particle = kParticles.ParticleSystem(class_picked["particles"])
        #TODO: Don't use static numbers
        new_particle.pos_hint = class_picked["particles_offset"]
        
        self.root.ids["character_portrait"].source = class_picked["portrait"]
    
        self.root.ids["background_particles"].clear_widgets()
        self.root.ids["foreground_particles"].clear_widgets()

        if class_picked["particles_offset"]["z"] > 0:
            self.root.ids["foreground_particles"].add_widget(new_particle)
        else:
            self.root.ids["background_particles"].add_widget(new_particle)

        if self.config.getdefault("Graphics", "particles", "1") == "1":
            new_particle.start()

        args_converter = lambda row_index, rec: {
            'text': rec['text'],
            'loyalty': rec['loyalty'],
            'loyalty_source': common.LOYALTY[rec['loyalty'][0]],
            'height': common.ABILITY_HEIGHT
        }

        self.root.ids["planeswalker_abilties"].adapter = ListAdapter(data=class_picked["planeswalker_abilities"],
                                                                     args_converter=args_converter,
                                                                     selection_mode='single',
                                                                     allow_empty_selection=False,
                                                                     template='ThumbnailedListItem')


    def build_config(self, config):
        """
        Set the default values for the configs sections.
        """
        config.setdefaults('Graphics', {
            'particles': True,
            'ScreenX': 1440,
            'ScreenY': 900
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
                for widget in self.root.walk():
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

if __name__ == "__main__":
    MainApp().run()


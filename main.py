import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListView
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.text import LabelBase
import particlesystem as kParticles

import common

class MainApp(App):
    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })
    
    def build(self):
        new_particle = kParticles.ParticleSystem("./assets/particles/templates/crown_light.pex")
        #TODO: Don't use static numbers
        new_particle.pos = 250, 300
        self.root.add_widget(new_particle)
        new_particle.start()
    
        for font in common.FONTS:
            LabelBase.register(**font)

        print(self.root.size)

    def on_pause(self):
        return True

class MainView(GridLayout):
    '''Uses :class:`CompositeListItem` for list item views comprised by two
    :class:`ListItemButton`s and one :class:`ListItemLabel`. Illustrates how
    to construct the fairly involved args_converter used with
    :class:`CompositeListItem`.
    '''

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)

        lHeight = self.size[0] / common.RATIO
        print(lHeight)
        

        import random

        # This is quite an involved args_converter, so we should go through the
        # details. A CompositeListItem instance is made with the args
        # returned by this converter. The first three, text, size_hint_y,
        # height are arguments for CompositeListItem. The cls_dicts list
        # contains argument sets for each of the member widgets for this
        # composite: ListItemButton and ListItemLabel.
        args_converter = lambda row_index, rec: {
            'text': str(self.height / common.RATIO) + rec['text'],
            'loyalty': rec['loyalty'],
            'loyalty_source': common.LOYALTY[rec['loyalty'][0]],
            'height': 30.0,
            #'cls_dicts': [{'cls': ListItemButton,
            #               'kwargs': {'text': rec["text"],
            #                          'markup': True}},
            #               {'cls': Image,
            #                'kwargs': {'source': "assets/loyaltyup.png",
            #                           }},
            #               {'cls': ListItemLabel,
            #                'kwargs': {'text': str(rec["loyalty"]),
            #                           'markup': True}},
            #               ]
        }

        def random_loyalty():
            x = random.randint(-10, 10)
            if x > 0:
                return "+%s" % x

            return str(x)

        integers_dict = {str(i): {'text': "This is a test ability string #%s" % str(i),
                                  'loyalty': random_loyalty(),
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

if __name__ == "__main__":
    MainApp().run()


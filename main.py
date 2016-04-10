import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListItemButton, ListItemLabel, CompositeListItem, ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.text import LabelBase  
# FIXME this shouldn't be necessary
from kivy.core.window import Window

import common

class MainApp(App):

    def build(self):

        # the root is created in pictures.kv
        #root = self.root

        #root.add_widget()
    
        #for font in common.FONTS:
        #    LabelBase.register(**font)

        self.root = MainView(cols=1)

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

        Builder.load_file("Eternities.kv")

        # This is quite an involved args_converter, so we should go through the
        # details. A CompositeListItem instance is made with the args
        # returned by this converter. The first three, text, size_hint_y,
        # height are arguments for CompositeListItem. The cls_dicts list
        # contains argument sets for each of the member widgets for this
        # composite: ListItemButton and ListItemLabel.
        args_converter = lambda row_index, rec: {
            'text': rec['text'],
            'size_hint_y': None,
            'height': 25,
            'cls_dicts': [{'cls': ListItemButton,
                           'kwargs': {#'text': '[font=Beleren]%s[/font]' % rec['text'],
                                      'text': rec["text"],
                                      'markup': True}},
                           #{'cls': ListItemLabel,
                           # 'kwargs': {'text': "Middle-{0}".format(rec['text']),
                           #            'is_representing_cls': True}},
                           ]}

        integers_dict = {str(i): {'text': "This is a test ability string #%s" % str(i), 'is_selected': False} for i in range(5)}
        item_strings  = ["{0}".format(index) for index in range(5)]

        dict_adapter = DictAdapter(sorted_keys=item_strings,
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


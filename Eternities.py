import os
from kivy.app import App
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListItemButton, ListItemLabel, CompositeListItem, ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.text import LabelBase  

FONT_FOLDER = os.path.join("assets", "font")

LabelBase.register(name="Beleren",  
                   fn_regular= os.path.join(FONT_FOLDER, "beleren-bold_P1.01.ttf"),
                   fn_bold=os.path.join(FONT_FOLDER, "beleren-bold_P1.01.ttf"))

LabelBase.register(name="Matrix",  
                   fn_regular=os.path.join(FONT_FOLDER, "MATRIX.ttf"),
                   fn_bold=os.path.join(FONT_FOLDER, "MatrixBold.ttf"))

LabelBase.register(name="MatrixSmallCaps",  
                   fn_regular=os.path.join(FONT_FOLDER, "MatrixRegularSmallCaps_0.ttf"),
                   fn_bold=os.path.join(FONT_FOLDER, "matrixbsc.ttf"))

LabelBase.register(name="MPlanti",  
                   fn_regular=os.path.join(FONT_FOLDER, "mplantin.ttf"),
                   fn_bold=os.path.join(FONT_FOLDER, "mplanti1.ttf"),
                   fn_italic=os.path.join(FONT_FOLDER, "mplantinit.ttf"))

Builder.load_file("Eternities.kv")

class MainView(GridLayout):
    '''Uses :class:`CompositeListItem` for list item views comprised by two
    :class:`ListItemButton`s and one :class:`ListItemLabel`. Illustrates how
    to construct the fairly involved args_converter used with
    :class:`CompositeListItem`.
    '''

    def __init__(self, **kwargs):
        kwargs['cols'] = 1
        super(MainView, self).__init__(**kwargs)

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
                           'kwargs': {'text': '[font=assets\font\beleren-bold_P1.01]%s[/font]' % rec['text'],
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
    from kivy.base import runTouchApp
    runTouchApp(MainView(width=800))
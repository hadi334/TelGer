#! usr/bin/python
# Python Used 3.9.0
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
from kivy.uix.popup import Popup
import json
from pathlib import Path
import kivy as kv
from datetime import datetime
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner, SpinnerOption
import openpyxl as opx


kv.require('2.0.0')


class ModifiedTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.multiline = False
        self.background_color = get_color_from_hex('#231123')
        self.font_size = 16
        self.foreground_color = get_color_from_hex('#FFFFFF')
        self.hint_text_color = get_color_from_hex('#D72638')


class AddButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        


        self.text = '[b]ADD[/b]'
        self.markup = True
        self.background_normal = ''
        self.background_down = ''
        self.bg_color = get_color_from_hex('#D72638')
        self.background_color = self.bg_color
        self.font_size = 16
        self.color = get_color_from_hex('#231123')   

    def on_press(self):
        self.background_color = get_color_from_hex('#231123') 

    def on_release(self):
        self.background_color = self.bg_color


class bg_change(FloatLayout):
    def __init__(self, clr='#6E44FF', **kwargs):
        super().__init__(**kwargs)

        self.clr = clr
        with self.canvas.before:
            Color(rgb=get_color_from_hex(self.clr))
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update, pos=self._update)

    def _update(self, wid, val):
        self.rect.pos = wid.pos
        self.rect.size = wid.size




class EntryField(FloatLayout):
    now = datetime.now()
    try:
        wb_complete_path = f"storage/{now.strftime('%Y')}/{now.strftime('%m')}/{now.strftime('%d')}.xlsx"
        
        load_wb = opx.load_workbook(wb_complete_path)
        ws = load_wb.active
        cols_list = ['Sale', 'Sale Time', 'Amount', 'Selling Price', 'Profit', 'Buying Price', 'Description']
        for i, v in enumerate(cols_list, 1):
            ws.cell(row=1, column=i, value=v)
    except:
        pass
        
        
    
            
    def __init__(self, title, grp, categories=['Alfa', 'Touch'], **kwargs):
        super().__init__(**kwargs)

        self.grp = grp
        self.categories = categories
        self.title = title
        self.label_color = '#231123'  # as same as background color

        self.title_label = Label(
            text=f'[b]{self.title.upper()}[/b]',
            pos_hint={'x': 0.5, 'y': 0.94},
            font_size=20,
            markup=True,
            color=get_color_from_hex(self.label_color),
            size_hint=(0, 0))
        self.add_widget(self.title_label)

        self.tglbox1 = BoxLayout(orientation='horizontal',
                                 pos_hint={'x': 0.005, 'y': 0.83},
                                 size_hint=(0.6, 0.06))

        self.tglbtn1 = CheckBox(group=self.grp,
                                size_hint=(0.2, 1))
        self.tglbox1.add_widget(self.tglbtn1)

        self.tglbtn1_lbl = Label(text=self.categories[0],
                                 size_hint=(0.2, 1),
                                 font_size=17)
        self.tglbox1.add_widget(self.tglbtn1_lbl)
        self.add_widget(self.tglbox1)

        self.tglbox2 = BoxLayout(orientation='horizontal',
                                 pos_hint={'x': 0.005, 'y': 0.74},
                                 size_hint=(0.6, 0.06))

        self.tglbtn2 = CheckBox(group=self.grp,
                                size_hint=(0.2, 1))
        self.tglbox2.add_widget(self.tglbtn2)

        self.tglbtn2_lbl = Label(text=self.categories[1],
                                 size_hint=(0.2, 1),
                                 font_size=17)
        self.tglbox2.add_widget(self.tglbtn2_lbl)
        self.add_widget(self.tglbox2)

        self.amt_box = BoxLayout(orientation='vertical',
                                 size_hint=(1, 0.1),
                                 pos_hint={'x': 0.02, 'y': 0.51},)

        self.amt_label = Label(text='Amount:',
                               size_hint=(0.34, 0.25))
        self.amt_box.add_widget(self.amt_label)

        self.amt_input = ModifiedTextInput(size_hint=(0.34, 0.35),
                                           input_filter='int',
                                           text='1')
        self.amt_box.add_widget(self.amt_input)
        self.add_widget(self.amt_box)

        self.price_box = BoxLayout(orientation='vertical',
                                   size_hint=(0.9, 0.1),
                                   pos_hint={'x': 0.02, 'y': 0.31})

        self.price_label = Label(text='Price:',
                                 size_hint=(0.2, 0.25))
        self.price_box.add_widget(self.price_label)

        self.price = ModifiedTextInput(hint_text='10000',
                                       size_hint=(0.55, 0.35),
                                       input_filter='int')
        self.price_box.add_widget(self.price)
        self.add_widget(self.price_box)
        
        self.cardtypes = ['Small', 'Big', 'Emergency', 'Start']
        self.card_choose = Spinner(text=self.cardtypes[0],
                                    values=self.cardtypes,
                                    pos_hint={'x': 0.02, 'y': 0.58},
                                    size_hint=(0.95, 0.08),
                                    background_normal='',
                                    background_color=get_color_from_hex('#231123'),
                                    sync_height=True,
                                    text_autoupdate=True)
        
        
        self.pft_box = BoxLayout(orientation='vertical',
                                   size_hint=(0.9, 0.1),
                                   pos_hint={'x': 0.02, 'y': 0.18})

        self.pft_label = Label(text='Profit:',
                                size_hint=(0.25, 0.25))
        self.pft_box.add_widget(self.pft_label)

        self.pft = ModifiedTextInput(hint_text='10000',
                                       size_hint=(0.55, 0.35),
                                       input_filter='int')
        self.pft_box.add_widget(self.pft)
        
        self.product_box = BoxLayout(orientation='vertical',
                                   size_hint=(0.9, 0.13),
                                   pos_hint={'x': 0.02, 'y': 0.59})

        self.product_label = Label(text='Product Name:',
                                 size_hint=(0.55, 0.25))
        self.product_box.add_widget(self.product_label)

        self.product_name = ModifiedTextInput(hint_text='Samsung S9+',
                                              size_hint=(1, 0.7))
        self.product_name.font_size = 15
        self.product_name.multiline = True
        # self.product_name.line_height = 2
        self.product_box.add_widget(self.product_name)

        self.addbtn = AddButton(pos_hint={'x': 0.3, 'y': 0},
                                size_hint=(0.35, 0.14))
        self.add_widget(self.addbtn)
        self.addbtn.bind(on_press=self.callback)
        
    def callback(self, ins):
           print(ins)
           self.add_to_sheet()
        
    def add_to_sheet(self):
        self.background_color = get_color_from_hex('#9e2020')
        self.checked_box = ''

        if self.tglbtn1._get_active():
            self.checked_box = self.categories[0]

        elif self.tglbtn2._get_active():
            self.checked_box = self.categories[1]
        
        else:
            return self.error_popup(f'Please Choose {self.categories[0].capitalize()} or {self.categories[1].capitalize()}')
            
            
        if not self.price.text:
            return self.error_popup('Fields cannot be empty')
        
        
        if self.title.lower() == 'dollars':
            
            alltext = f'{self.checked_box.lower()} {self.title.lower()}'
            existing = AmountsField.existing_amounts_dict[alltext]
            
            company_take = AmountsField.existing_amounts_dict[f'{self.checked_box.lower()} dollars taken'][1]
            existing[0] -= (float(self.amt_input.text) + company_take)
            AmountsField.labels_dict[alltext].text = f'{alltext.upper()}: {format(existing[0], ".2f")}'
            
            self.add_row(alltext.capitalize(), existing[1])
            

            
            
        elif self.title.lower() == 'days':
            ind = f'{self.checked_box.lower()} big cards'
            existing_bc = AmountsField.existing_amounts_dict[ind]
            existing_bc[0] -= int(self.amt_input.text)
            AmountsField.labels_dict[ind].text = f'{ind.upper()}: {existing_bc[0]}'
            days_price = AmountsField.existing_amounts_dict[f'{self.checked_box.lower()} {self.title.lower()}'][1]
            
            self.add_row(f'{self.checked_box.lower()} {self.title.lower()}', days_price)

            
        elif self.title.lower() == 'cards':
            type_of_card = f'{self.checked_box.lower()} {self.card_choose.text.lower()} {self.title.lower()}'
            existing_card = AmountsField.existing_amounts_dict[type_of_card]
            existing_card[0] -= int(self.amt_input.text)
            AmountsField.labels_dict[type_of_card].text = f'{type_of_card.upper()}: {existing_card[0]}'
            
            self.add_row(type_of_card, existing_card[1])
            
        
        elif self.title.lower() == 'other':
            pass
        
            
        self.load_wb.save(self.wb_complete_path)
        with open('.storage.txt', 'w') as f:
            json.dump(AmountsField.existing_amounts_dict, f)
            
    def error_popup(self, error_text):
        popup_label = Label(text=error_text,
                                font_size=22)

        return Popup(title='Error',
                     content=popup_label,
                     size_hint=(0.45, 0.4)).open()
        
    def add_row(self, name, buying_price):
        max_row = self.ws.max_row + 1
        print(max_row)
        self.ws['A'+str(max_row)] = name
        self.ws['B'+str(max_row)] = f"{datetime.now().strftime('%H: %M: %S')}"
        self.ws['C'+str(max_row)] = self.amt_input.text
        self.ws['D'+str(max_row)] = self.price.text
        self.ws['E'+str(max_row)] = int(self.price.text) - (buying_price * int(self.amt_input.text))
        self.ws['F'+str(max_row)] = buying_price
        
            
class SpinnerOptions(Button):
    pass


class TotalSelledField(FloatLayout):
    pass


class FieldofFields(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.dol = EntryField('dollars',
                              'dollars',
                              size_hint=(0.33, 1))
        self.dol.pos_hint = {'x': 0, 'y': 0}
        self.add_widget(bg_change(pos_hint=self.dol.pos_hint,
                                  size_hint=self.dol.size_hint))
        self.add_widget(self.dol)

        self.days = EntryField('days',
                               'days',
                               size_hint=(0.33, 1))
        self.days.pos_hint = {'x': 0.335, 'y': 0}
        self.add_widget(bg_change(pos_hint=self.days.pos_hint,
                                  size_hint=self.days.size_hint))
        self.add_widget(self.days)

        self.cards = EntryField('cards',
                                'cards',
                                size_hint=(0.33, 1))
        self.cards.pos_hint = {'x': 0.67, 'y': 0}
        self.add_widget(bg_change(pos_hint=self.cards.pos_hint,
                                  size_hint=self.cards.size_hint))
        self.cards.amt_box.pos_hint = {'x': 0.02, 'y': 0.45}
        self.cards.price_box.pos_hint = {'x': 0.02, 'y': 0.3}
        self.cards.add_widget(self.cards.card_choose)
        
        self.add_widget(self.cards)
        

class EditPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.size_hint = (0.45, 0.5)
        self.title = 'Edit'
        self.title_align = 'center'
        self.title_color = get_color_from_hex('#00FF00')
        self.title_size = 19
        
        self.inlayout = FloatLayout(size_hint=(1, 1),
                                    pos_hint={'x': 0, 'y': 0})
        
        self.labels = [txt.upper() for txt in AmountsField.existing_amounts_dict.keys()]
        
        self.to_be_edited = Spinner(size_hint=(0.45, 0.25),
                                    pos_hint={'x': 0.05, 'y': 0.6},
                                    values=self.labels,
                                    text=self.labels[0],
                                    sync_height=True)
        self.to_be_edited.bind(on_press=self.on_spinner_text)
        
        self.inlayout.add_widget(self.to_be_edited)
        self.add_widget(self.inlayout)
        
        # Plus Box.
        self.plus_box = BoxLayout(size_hint=(0.25, 0.1),
                                  orientation='horizontal',
                                  pos_hint={'x': 0.55, 'y': 0.77})
        
        self.plus_checkbox = CheckBox(size_hint=(0.2, 1),
                                      group='plusminus')
        self.plus_box.add_widget(self.plus_checkbox)
        
        self.plus_label = Label(text='Plus',
                                size_hint=(0.2, 1),
                                font_size=19)
        self.plus_box.add_widget(self.plus_label)
        self.inlayout.add_widget(self.plus_box)
        
        # Minus Box.
        self.minus_box = BoxLayout(size_hint=(0.25, 0.1),
                                  orientation='horizontal',
                                  pos_hint={'x': 0.55, 'y': 0.62})
        
        self.minus_checkbox = CheckBox(size_hint=(0.2, 1),
                                      group='plusminus')
        self.minus_box.add_widget(self.minus_checkbox)
        
        self.minus_label = Label(text='Minus',
                                size_hint=(0.2, 1),
                                font_size=19)
        self.minus_box.add_widget(self.minus_label)
        self.inlayout.add_widget(self.minus_box)
        
        # Price change.
        self.price_box = BoxLayout(size_hint=(0.35, 0.1),
                                  orientation='horizontal',
                                  pos_hint={'x': 0.555, 'y': 0.47})
        
        self.price_checkbox = CheckBox(size_hint=(0.2, 1),
                                      group='plusminus')
        self.price_box.add_widget(self.price_checkbox)
        
        self.price_label = Label(text='Price Change',
                                size_hint=(0.4, 1),
                                font_size=19)
        self.price_box.add_widget(self.price_label)
        self.inlayout.add_widget(self.price_box)
        
        self.input_label = Label(pos_hint={'x': 0.16, 'y': 0.33},
                                 size_hint=(0, 0),
                                 text='[b][u]Amount[/u]:[/b]',
                                 markup=True,
                                 font_size=20)
        self.inlayout.add_widget(self.input_label)
        
        self.input_num = ModifiedTextInput(input_filter='float',
                                           pos_hint={'x': 0.05, 'y': 0.15},
                                           size_hint=(0.5, 0.12))
        self.inlayout.add_widget(self.input_num)
        
        self.popup_btn = Button(pos_hint={'x': 0.7, 'y': 0.1},
                                size_hint=(0.25, 0.2),
                                text='Apply',
                                font_size=20)
        self.inlayout.add_widget(self.popup_btn)
        
        self.popup_btn.bind(on_press=self.on_popup_btn_press)
        self.tmp_num = 0
        
        self.price_checkbox.bind(on_press=self.price_cb_onpress)
        
            
    def on_spinner_text(self, spn):
        self.price_checkbox.state = 'normal'
        
        
    def price_cb_onpress(self, ins):
        self.input_num.text = str(AmountsField.existing_amounts_dict[self.to_be_edited.text.lower()][1])

        
    def on_popup_btn_press(self, btn):
        
        edited_title = self.to_be_edited.text.lower()
        current_value = AmountsField.existing_amounts_dict[edited_title]
        
        if self.minus_checkbox._get_active():
            current_value[0] -= float(self.input_num.text)
            AmountsField.labels_dict[edited_title].text = f'{edited_title.upper()}: {current_value[0]}'
        
        elif self.plus_checkbox._get_active():
            current_value[0] += float(self.input_num.text)
            AmountsField.labels_dict[edited_title].text = f'{edited_title.upper()}: {current_value[0]}'
        
        elif self.price_checkbox._get_active():
            current_value[1] = float(self.input_num.text)
            
        
        else:
            return Popup(title='Error',
                         size_hint=(0.35, 0.35),
                         content=Label(text='Please Choose [b]Minus[/b], [b]Plus[/b]\nor [b]Change Price[/b]',
                                       font_size=20,
                                       markup=True)).open()
        # self.tmp_num += 1
        # if self.tmp_num == 3: # Trial
        #     self.tmp_num = 0
        #     self.dismiss()
            
        with open('.storage.txt', 'w') as f:
            json.dump(AmountsField.existing_amounts_dict, f)
        

class AmountsField(StackLayout):
    with open('.storage.txt', 'r') as jf:
        existing_amounts_dict = json.load(jf)

    labels_dict = {} # dictionary contains label object of every sale type
    for i, v in existing_amounts_dict.items():
        if i in ['alfa days', 'touch days', "alfa dollars taken", "touch dollars taken"]:
            continue
        labels_dict[i] = Label(size_hint=(0.4, 0.2))
        if i in ['alfa dollars', 'touch dollars']:
            labels_dict[i].text = f'{i.upper()}: {format(v[0], ".2f")}'
        else:
            labels_dict[i].text = f'{i.upper()}: {v[0]}'
        
        
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'tb-lr'
            
        for v in self.labels_dict.values():
            self.add_widget(v)
            
        self.edit_btn = Button(size_hint=(0.15, 0.6),
                               text='[b]EDIT[/b]',
                               font_size=20,
                               background_normal='',
                               background_color=get_color_from_hex('#6E44FF'),
                               color=get_color_from_hex('#231123'),
                               markup=True)
        self.add_widget(self.edit_btn)
        
        self.edit_btn.bind(on_press=self.popup_open)
        
    def popup_open(self, btn):
        edit_popup = EditPopup()
        edit_popup.open()


class MainScreen(FloatLayout):
    def __init__(self):
        super().__init__()

        self.amts = AmountsField(pos_hint={'x': 0.02, 'y': 0.75},
                                 size_hint=(0.65, 0.2))
        # self.add_widget(bg_change(pos_hint=self.amts.pos_hint,
        #                           size_hint=self.amts.size_hint, # to remove later
        #                           clr='#D72638'))
        self.add_widget(self.amts)
        # self.amts.size_hint_max = (820, 300)
        # self.amts.size_hint_min = (400, 140)

        self.ddc = FieldofFields(size_hint=(0.65, 0.68),
                                 pos_hint={'x': 0.011, 'y': 0.015})
        self.add_widget(self.ddc)

        self.phone_acc = EntryField(title='other',
                                    grp='phoneacc',
                                    categories=['Phone', 'Accessory'],
                                    pos_hint={'x': 0.72, 'y': 0.015})
        self.phone_acc.size_hint = (0.22, 0.68)
        self.add_widget(bg_change(pos_hint=self.phone_acc.pos_hint,
                                  size_hint=self.phone_acc.size_hint))
        self.phone_acc.price_box.pos_hint = {'x': 0.02, 'y': 0.33}
        self.phone_acc.amt_box.pos_hint = {'x': 0.02, 'y': 0.46}
        self.phone_acc.add_widget(self.phone_acc.product_box)
        self.phone_acc.add_widget(self.phone_acc.pft_box)
        self.add_widget(self.phone_acc)


class ManagerApp(App):
    def build(self):
        now = datetime.now()
        which_day = now.strftime('%d')
        which_month = now.strftime('%m')
        which_year = now.strftime("%Y")
        Path('storage').mkdir(exist_ok=True)
        Path(f'storage/{which_year}').mkdir(exist_ok=True)
        Path(f'storage/{which_year}/{which_month}').mkdir(exist_ok=True)
        complete_path = f"storage/{which_year}/{which_month}/{which_day}.xlsx"
 
        if not Path(complete_path).is_file():
            new_wb = opx.Workbook()
            new_wb.save(complete_path)
            new_wb.close()

        self.main_screen = MainScreen()

        Window.clearcolor = get_color_from_hex('#231123')  # 230C33 101D42 DCF763
        Window.size = (950, 720)
        return self.main_screen

if __name__ == '__main__':
    myapp = ManagerApp()
    myapp.run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.button import ButtonBehavior
from productList import productList

class application(Widget):
    pass

class SM(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class CatalogScreen(Screen):
    pass

class AccountScreen(Screen):
    pass

class Scroll(ScrollView):
    pass

class ProductList(GridLayout):
    def __init__(self, **kwargs):
        super(ProductList, self).__init__(**kwargs)
        for obj in productList:
            self.add_widget(Product(obj.name, obj.type, obj.picture))
            self.bind(minimum_height=self.setter('height'))
    def Update(self, text):
        self.clear_widgets()
        for obj in productList:
            if text in obj.name.lower() or text in obj.type.lower() or text in obj.tag.lower():
                self.add_widget(Product(obj.name, obj.type, obj.picture))
                self.bind(minimum_height=self.setter('height'))
        if self.children==[]:
            self.add_widget(Label(text='По вашему запросу нияего не найдено'))

class Product(BoxLayout):
    def __init__(self, n, t, i):
        super(Product, self).__init__()
        with self.canvas:
            Color(.5, .5, .5)
            self.rect=Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_rect, size=self.update_rect)
        self.add_widget(AsyncImage(source=i))
        prod_name=BoxLayout(orientation='vertical')
        prod_name.add_widget(Label(text=n))
        prod_name.add_widget(Label(text=t))
        self.add_widget(prod_name)
    def update_rect(self, *args):
        self.rect.pos=self.pos
        self.rect.size=self.size

class CatalogButton(ButtonBehavior, BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return application()
    
if __name__=="__main__":
    MyApp().run()
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.button import ButtonBehavior
from productList import productList
from kivy.garden.mapview import MapView, MapMarker

class application(Widget):
    pass

class SM(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class CatalogScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class TagScreen(Screen):
    pass

class Scroll(ScrollView):
    pass

class Map(MapView):
    pass

class Marker(MapMarker):
    pass

class ProductScreen(Screen):
    def __init__(self, **kw):
        super(ProductScreen, self).__init__(**kw)
    def update(self,id):
        for obj in productList:
            if obj.id==id:
                self.prodName=obj.name
                self.type=obj.type
                self.img=obj.picture
                self.cost=obj.cost

class TagProductList(GridLayout):
    def __init__(self, **kwargs):
        super(TagProductList, self).__init__(**kwargs)
    def tagList(self, tag):
        self.clear_widgets()
        for obj in productList:
            if tag in obj.tag:
                self.add_widget(Product(obj.name, obj.type, obj.picture, obj.id))
                self.bind(minimum_height=self.setter('height'))

class ProductList(GridLayout):
    def __init__(self, **kwargs):
        super(ProductList, self).__init__(**kwargs)
        for obj in productList:
            self.add_widget(Product(obj.name, obj.type, obj.picture, obj.id))
            self.bind(minimum_height=self.setter('height'))
    def Update(self, text):
        self.clear_widgets()
        for obj in productList:
            if text in obj.name.lower() or text in obj.type.lower() or text in obj.tag.lower():
                self.add_widget(Product(obj.name, obj.type, obj.picture, obj.id))
                self.bind(minimum_height=self.setter('height'))
        if self.children==[]:
            self.add_widget(Label(text='По вашему запросу нияего не найдено'))

class Product(ButtonBehavior, BoxLayout):
    def __init__(self, n, t, i, idProd):
        super(Product, self).__init__()
        self.add_widget(Image(source=i))
        prod_name=BoxLayout(orientation='vertical')
        prod_name.add_widget(Label(text=n))
        prod_name.add_widget(Label(text=t))
        self.add_widget(prod_name)
        self.id=idProd

class CatalogButton(ButtonBehavior, BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return application()
    
if __name__=="__main__":
    MyApp().run()
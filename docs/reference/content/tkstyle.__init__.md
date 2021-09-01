
Back to [Reference Overview](https://github.com/pyrustic/tkstyle/blob/master/docs/reference/README.md#readme)

# tkstyle.\_\_init\_\_



<br>


```python

class Button:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Button"
    
```

<br>

```python

class Canvas:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Canvas"
    
```

<br>

```python

class Checkbutton:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Checkbutton"
    
```

<br>

```python

class Entry:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Entry"
    
```

<br>

```python

class Error:
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

```

<br>

```python

class Frame:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Frame"
    
```

<br>

```python

class Label:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Label"
    
```

<br>

```python

class LabelFrame:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Labelframe"
    
```

<br>

```python

class Listbox:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Listbox"
    
```

<br>

```python

class Menu:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Menu"
    
```

<br>

```python

class Menubutton:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Menubutton"
    
```

<br>

```python

class OptionMenu:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "OptionMenu"
    
```

<br>

```python

class PanedWindow:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Panedwindow"
    
```

<br>

```python

class Radiobutton:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Radiobutton"
    
```

<br>

```python

class Scale:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Scale"
    
```

<br>

```python

class Scrollbar:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Scrollbar"
    
```

<br>

```python

class Spinbox:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Spinbox"
    
```

<br>

```python

class Text:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Text"
    
```

<br>

```python

class Theme:
    """
    A theme is a collection of styles and... others theme.
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    @property
    def styles(self):
        """
        Get a list of styles that this theme contains
        """

    def add(self, style, pattern=None):
        """
        Add a style to this theme.
        The style is an instance of 'pyrustic.default_style._Style'.
        You don't have to directly subclass the private class '_Style'.
        Instead, subclass one of the public classes in the module 'pyrustic.default_style'.
        The scope here is an optional string.
        When you don't set the scope, the style will be applied as it.
        Example. If you add a Button style in your theme, this style will be
        applied to all buttons widgets. But you can restrict this effect to a scope.
        This scope could be by example "*Canvas*Button.", meaning all buttons
        that are living on all Canvas, are candidates for the given style.
        """

    def target(self, root):
        """
        Set this theme to master. Master here should be the root widget of your app.
        You need to set the theme to master before installing others widgets on the master.
        """

```

<br>

```python

class Toplevel:
    """
    
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    _CLASS_NAME = "Toplevel"
    
```


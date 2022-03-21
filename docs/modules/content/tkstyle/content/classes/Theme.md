Back to [All Modules](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/README.md#readme)

# Module Overview

**tkstyle**
 
No description

> **Classes:** &nbsp; [Button](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Button.md#class-button) &nbsp;&nbsp; [Canvas](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Canvas.md#class-canvas) &nbsp;&nbsp; [Checkbutton](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Checkbutton.md#class-checkbutton) &nbsp;&nbsp; [Entry](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Entry.md#class-entry) &nbsp;&nbsp; [Frame](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Frame.md#class-frame) &nbsp;&nbsp; [Label](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Label.md#class-label) &nbsp;&nbsp; [LabelFrame](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/LabelFrame.md#class-labelframe) &nbsp;&nbsp; [Listbox](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Listbox.md#class-listbox) &nbsp;&nbsp; [Menu](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Menu.md#class-menu) &nbsp;&nbsp; [Menubutton](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Menubutton.md#class-menubutton) &nbsp;&nbsp; [OptionMenu](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/OptionMenu.md#class-optionmenu) &nbsp;&nbsp; [PanedWindow](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/PanedWindow.md#class-panedwindow) &nbsp;&nbsp; [Radiobutton](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Radiobutton.md#class-radiobutton) &nbsp;&nbsp; [Scale](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Scale.md#class-scale) &nbsp;&nbsp; [Scrollbar](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Scrollbar.md#class-scrollbar) &nbsp;&nbsp; [Spinbox](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Spinbox.md#class-spinbox) &nbsp;&nbsp; [Text](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Text.md#class-text) &nbsp;&nbsp; [Theme](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Theme.md#class-theme) &nbsp;&nbsp; [Toplevel](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/Toplevel.md#class-toplevel) &nbsp;&nbsp; [\_Style](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/classes/_Style.md#class-_style)
>
> **Functions:** &nbsp; [\_get\_children](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/functions.md#_get_children) &nbsp;&nbsp; [\_populate\_option\_database](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/functions.md#_populate_option_database) &nbsp;&nbsp; [\_pull\_option\_database](https://github.com/pyrustic/tkstyle/blob/master/docs/modules/content/tkstyle/content/functions.md#_pull_option_database)
>
> **Constants:** &nbsp; None

# Class Theme
A theme is a collection of styles and... others themes.

## Base Classes
object

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|styles|getter|Get a list of styles that this theme contains||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [add](#add) &nbsp;&nbsp; [apply](#apply)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## add
Add a style to this theme.
The style is an instance of 'pyrustic.default_style._Style'.
You don't have to directly subclass the private class '_Style'.
Instead, subclass one of the public classes that mirror a widget, example: tkstyle.Button.

The pattern here is an optional string.
When you don't set the pattern, the style will be applied as it.
Example. If you add a Button style in your theme, this style will be
applied to all buttons widgets. But you can restrict this effect to a pattern.
This pattern could be by example "*Canvas*Button.", meaning all buttons
that are living on all Canvas, are candidates for the given style.



**Signature:** (self, style, pattern=None)





**Return Value:** None.

[Back to Top](#module-overview)


## apply
Set this theme to master. Master here should be the root widget of your app.
You need to set the theme to master before installing others widgets on the master.



**Signature:** (self, root)





**Return Value:** None.

[Back to Top](#module-overview)




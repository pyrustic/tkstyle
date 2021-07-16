import tkinter as tk
import copy


class Theme:
    """
    A theme is a collection of styles and... others theme.
    """
    def __init__(self):
        self._styles = dict()

    @property
    def styles(self):
        """
        Get a list of styles that this theme contains
        """
        return self._styles.copy()

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
        if not pattern:
            pattern = "*{}".format(style.class_name)
        self._styles[pattern] = style

    def target(self, root):
        """
        Set this theme to master. Master here should be the root widget of your app.
        You need to set the theme to master before installing others widgets on the master.
        """
        if not isinstance(root, tk.Tk):
            raise Error("The target of a theme should be the root Tk object")
        for pattern, style in self._styles.items():
            _populate_option_database(root, {pattern: style})


class _Style:
    _CLASS_NAME = None

    def __init__(self):
        self._styles = dict()

    @property
    def class_name(self):
        """
        Get the widget class
        """
        if self._CLASS_NAME is None:
            raise Error("The class attribute _CLASS_NAME is missing in the _Style subclass")
        return self._CLASS_NAME

    @property
    def styles(self):
        return self._styles

    def copy(self):
        """
        Get a fresh new style copied from the actual one
        """
        return copy.deepcopy(self)

    def add(self, style, pattern=None):
        if not pattern:
            pattern = "*{}".format(style.class_name)
        self._styles[pattern] = style

    def target(self, widget, ignore_error=True):
        """
        Individually apply a style to a widget
        """
        self._apply_self_style(widget, ignore_error)
        self._apply_children_styles(widget)

    def _apply_self_style(self, widget, ignore_error):
        cnf = {key.lower(): val
               for key, val in self.__dict__.items()
               if key != "_styles"}
        if ignore_error:
            for key, val in cnf.items():
                try:
                    widget.config(cnf={key: val})
                except Exception as e:
                    pass
        else:
            widget.config(cnf=cnf)

    def _apply_children_styles(self, widget):
        prefix = "*{}".format(widget.winfo_name())
        classes_and_options = _populate_option_database(widget, self._styles,
                                                        prefix=prefix)
        _pull_option_database(widget, classes_and_options)

    def __str__(self):
        cache = []
        for key, val in self.__dict__.items():
            if isinstance(val, str):
                val = "\"{}\"".format(val)
            cache.append("{}: {}".format(key, val))
        return "{}\n{}".format(repr(self),
                               "\n".join(cache))


class Button(_Style):
    _CLASS_NAME = "Button"

    def __init__(self):
        super().__init__()
        self.activeBackground = None  # "#ececec"
        self.activeForeground = None  # "#000000"
        self.anchor = None  # "center"
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 1
        self.compound = None  # "none"
        self.default = None  # "disabled"
        self.disabledForeground = None  # "#a3a3a3"
        self.font = None  # TkDefaultFont
        self.foreground = None  # "#000000"
        self.height = None  # 0
        self.highlightBackground = None  # "#d9d9d9"
        self.highlightColor = None  # "#000000"
        self.highlightThickness = None  # 1
        self.justify = None  # "center"
        self.padX = None  # 3
        self.padY = None  # 1
        self.relief = None  # "raised"
        self.repeatDelay = None  # 0
        self.repeatInterval = None  # 0
        self.state = None  # "normal"
        self.underline = None  # -1
        self.width = None  # 0
        self.wrapLength = None  # 0


class Canvas(_Style):
    _CLASS_NAME = "Canvas"

    def __init__(self):
        super().__init__()
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 0
        self.closeEnough = None  # 1
        self.confine = None  # 1
        self.height = None  # 7
        self.highlightBackground = None  # "#d9d9d9"
        self.highlightColor = None  # "#000000"
        self.highlightThickness = None  # 1
        self.insertBackground = None  # "#000000"
        self.insertBorderWidth = None  # 0
        self.insertOffTime = None  # 300
        self.insertOnTime = None  # 600
        self.insertWidth = None  # 2
        self.offset = None  # 0, 0
        self.relief = None  # "flat"
        self.selectBackground = None  # "#c3c3c3"
        self.selectBorderWidth = None  # 1
        self.selectForeground = None  # "#000000"
        self.state = None  # "normal"
        self.width = None  # 10
        self.xScrollIncrement = None  # 0
        self.yScrollIncrement = None  # 0


class Checkbutton(_Style):
    _CLASS_NAME = "Checkbutton"

    def __init__(self):
        super().__init__()
        self.activeBackground = None  # "#ececec"
        self.activeForeground = None  # "#000000"
        self.anchor = None  # "center"
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 1
        self.compound = None  # "none"
        self.disabledForeground = None  # "#a3a3a3"
        self.font = None  # TkDefaultFont
        self.foreground = None  # "#000000"
        self.height = None  # 0
        self.highlightBackground = None  # "#d9d9d9"
        self.highlightColor = None  # "#000000"
        self.highlightThickness = None  # 1
        self.indicatorOn = None  # 1
        self.justify = None  # "center"
        self.offRelief = None  # "raised"
        self.offValue = None  # 0
        self.onValue = None  # 1
        self.padX = None  # 1
        self.padY = None  # 1
        self.relief = None  # "flat"
        self.selectColor = None  # "#ffffff"
        self.state = None  # "normal"
        self.underline = None  # -1
        self.width = None  # 0
        self.wrapLength = None  # 0


class Entry(_Style):
    _CLASS_NAME = "Entry"

    def __init__(self):
        super().__init__()
        self.background = None  # "#ffffff"
        self.borderWidth = None  # 1
        self.cursor = None  # xterm
        self.disabledBackground = None  # "#d9d9d9"
        self.disabledForeground = None  # "#a3a3a3"
        self.exportSelection = None  # 1
        self.font = None  # TkTextFont
        self.foreground = None  # # 000000
        self.highlightBackground = None  # "#d9d9d9"
        self.highlightColor = None  # # 000000
        self.highlightThickness = None  # 1
        self.insertBackground = None  # "#000000"
        self.insertBorderWidth = None  # 0
        self.insertOffTime = None  # 300
        self.insertOnTime = None  # 600
        self.insertWidth = None  # 2
        self.justify = None  # left
        self.readonlyBackground = None  # "#d9d9d9"
        self.relief = None  # sunken
        self.selectBackground = None  # "#c3c3c3"
        self.selectBorderWidth = None  # 0
        self.selectForeground = None  # "#000000"
        self.state = None  # normal
        self.validate = None  # none
        self.width = None  # 20


class Frame(_Style):
    _CLASS_NAME = "Frame"

    def __init__(self):
        super().__init__()
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 0
        self.class_ = None  # Frame
        self.container = None  # 0
        self.height = None  # 0
        self.highlightBackground = None  # "#d9d9d9"
        self.highlightColor = None  # "#000000"
        self.highlightThickness = None  # 0
        self.padX = None  # 0
        self.padY = None  # 0
        self.relief = None  # flat
        self.takeFocus = None  # 0
        self.width = None  # 0


class Label(_Style):
    _CLASS_NAME = "Label"

    def __init__(self):
        super().__init__()
        self.activeBackground = None  # "#ececec"
        self.activeForeground = None  # "#000000"
        self.anchor = None  # center
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 1
        self.compound = None  # none
        self.disabledForeground = None  # "#a3a3a3"
        self.font = None  # TkDefaultFont
        self.foreground = None  # # 000000
        self.height = None  # 0
        self.highlightBackground = None  # "#d9d9d9"
        self.highlightColor = None  # "#000000"
        self.highlightThickness = None  # 0
        self.justify = None  # center
        self.padX = None  # 1
        self.padY = None  # 1
        self.relief = None  # flat
        self.state = None  # normal
        self.takeFocus = None  # 0
        self.underline = None  # -1
        self.width = None  # 0
        self.wrapLength = None  # 0


class LabelFrame(_Style):
    _CLASS_NAME = "Labelframe"

    def __init__(self):
        super().__init__()
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 2
        self.class_ = None  # Labelframe
        self.container = None  # 0
        self.font = None  # TkDefaultFont
        self.foreground = None  # "#000000"
        self.height = None  # 0
        self.highlightBackground = None  # "#d9d9d9"
        self.highlightColor = None  # "#000000"
        self.highlightThickness = None  # 0
        self.labelAnchor = None  # nw
        self.padX = None  # 0
        self.padY = None  # 0
        self.relief = None  # groove
        self.takeFocus = None  # 0
        self.width = None  # 0


class Listbox(_Style):
    _CLASS_NAME = "Listbox"

    def __init__(self):
        super().__init__()
        self.activeStyle = None  # dotbox
        self.background = None  # "#ffffff"
        self.borderWidth = None  # 1
        self.disabledForeground = None  # "#a3a3a3"
        self.exportSelection = None  # 1
        self.font = None  # TkDefaultFont
        self.foreground = None  # "#000000"
        self.height = None  # 10
        self.highlightBackground = None  # "#d9d9d9"
        self.highlightColor = None  # "#000000"
        self.highlightThickness = None  # 1
        self.justify = None  # left
        self.relief = None  # sunken
        self.selectBackground = None  # "#c3c3c3"
        self.selectBorderWidth = None  # 0
        self.selectForeground = None  # "#000000"
        self.selectMode = None  # browse
        self.setGrid = None  # 0
        self.state = None  # normal
        self.width = None  # 20


class Menu(_Style):
    _CLASS_NAME = "Menu"

    def __init__(self):
        super().__init__()
        self.activeBackground = None  # "#ececec"
        self.activeBorderWidth = None  # 1
        self.activeForeground = None  # "#000000"
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 1
        self.cursor = None  # arrow
        self.disabledForeground = None  # "#a3a3a3"
        self.font = None  # TkMenuFont
        self.foreground = None  # "#000000"
        self.relief = None  # raised
        self.selectColor = None  # "#000000"
        self.takeFocus = None  # 0
        self.tearOff = None  # 1
        self.type = None  # normal


class Menubutton(_Style):
    _CLASS_NAME = "Menubutton"

    def __init__(self):
        super().__init__()
        self.activeBackground = None  # "#ececec"
        self.activeForeground = None  # "#000000"
        self.anchor = None  # center
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 1
        self.compound = None  # none
        self.direction = None  # below
        self.disabledForeground = None  # "#a3a3a3"
        self.font = None  # TkDefaultFont
        self.foreground = None  # #000000
        self.height = None  # 0
        self.highlightBackground = None  # "#d9d9d9"
        self.highlightColor = None  # "#000000"
        self.highlightThickness = None  # 0
        self.indicatorOn = None  # 0
        self.justify = None  # center
        self.padX = None  # 4p
        self.padY = None  # 3p
        self.relief = None  # flat
        self.state = None  # normal
        self.takeFocus = None  # 0
        self.underline = None  # -1
        self.width = None  # 0
        self.wrapLength = None  # 0


class OptionMenu(_Style):
    _CLASS_NAME = "OptionMenu"

    def __init__(self):
        super().__init__()
        self.activeBackground = None  # "#ececec"
        self.activeForeground = None  # "#000000"
        self.anchor = None  # center
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 2
        self.compound = None  # none
        self.cursor = None  #
        self.direction = None  # below
        self.disabledForeground = None  # #a3a3a3
        self.font = None  # TkDefaultFont
        self.foreground = None  # #000000
        self.height = None  # 0
        self.highlightBackground = None  # #d9d9d9
        self.highlightColor = None  # #000000
        self.highlightThickness = None  # 2
        self.image = None  #
        self.indicatorOn = None  # 1
        self.justify = None  # center
        self.menu = None  # .140544366545328.menu
        self.padX = None  # 5
        self.padY = None  # 4
        self.relief = None  # raised
        self.state = None  # normal
        self.takeFocus = None  # 0
        self.text = None  #
        self.textVariable = None  # PY_VAR0
        self.underline = None  # -1
        self.width = None  # 0
        self.wrapLength = None  # 0


class PanedWindow(_Style):
    _CLASS_NAME = "Panedwindow"

    def __init__(self):
        super().__init__()
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 1
        self.handlePad = None  # 8
        self.handleSize = None  # 8
        self.opaqueResize = None  # 1
        self.orient = None  # horizontal
        self.proxyBorderWidth = None  # 2
        self.relief = None  # flat
        self.sashPad = None  # 0
        self.sashRelief = None  # flat
        self.sashWidth = None  # 3
        self.showHandle = None  # 0


class Radiobutton(_Style):
    _CLASS_NAME = "Radiobutton"

    def __init__(self):
        super().__init__()
        self.activeBackground = None  # #ececec
        self.activeForeground = None  # #000000
        self.anchor = None  # center
        self.background = None  # #d9d9d9
        self.borderWidth = None  # 1
        self.compound = None  # none
        self.disabledForeground = None  # #a3a3a3
        self.font = None  # TkDefaultFont
        self.foreground = None  # #000000
        self.height = None  # 0
        self.highlightBackground = None  # #d9d9d9
        self.highlightColor = None  # #000000
        self.highlightThickness = None  # 1
        self.indicatorOn = None  # 1
        self.justify = None  # center
        self.offRelief = None  # raised
        self.padX = None  # 1
        self.padY = None  # 1
        self.relief = None  # flat
        self.selectColor = None  # #ffffff
        self.state = None  # normal
        self.underline = None  # -1
        self.variable = None  # selectedButton
        self.width = None  # 0
        self.wrapLength = None  # 0


class Scale(_Style):
    _CLASS_NAME = "Scale"

    def __init__(self):
        super().__init__()
        self.activeBackground = None  # #ececec
        self.background = None  # #d9d9d9
        self.bigIncrement = None  # 0
        self.borderWidth = None  # 1
        self.digits = None  # 0
        self.font = None  # TkDefaultFont
        self.foreground = None  # #000000
        self.from_ = None  # 0
        self.highlightBackground = None  # #d9d9d9
        self.highlightColor = None  # #000000
        self.highlightThickness = None  # 1
        self.length = None  # 100
        self.orient = None  # vertical
        self.relief = None  # flat
        self.repeatDelay = None  # 300
        self.repeatInterval = None  # 100
        self.resolution = None  # 1
        self.showValue = None  # 1
        self.sliderLength = None  # 30
        self.sliderRelief = None  # raised
        self.state = None  # normal
        self.tickInterval = None  # 0
        self.to = None  # 100
        self.troughColor = None  # #b3b3b3
        self.width = None  # 15


class Scrollbar(_Style):
    _CLASS_NAME = "Scrollbar"

    def __init__(self):
        super().__init__()
        self.activeBackground = None  # #ececec
        self.activeRelief = None  # raised
        self.background = None  # #d9d9d9
        self.borderWidth = None  # 1
        self.elementBorderWidth = None  # -1
        self.highlightBackground = None  # #d9d9d9
        self.highlightColor = None  # #000000
        self.highlightThickness = None  # 0
        self.jump = None  # 0
        self.orient = None  # vertical
        self.relief = None  # sunken
        self.repeatDelay = None  # 300
        self.repeatInterval = None  # 100
        self.troughColor = None  # #b3b3b3
        self.width = None  # 11


class Spinbox(_Style):
    _CLASS_NAME = "Spinbox"

    def __init__(self):
        super().__init__()
        self.activeBackground = None  # #ececec
        self.background = None  # #ffffff
        self.borderWidth = None  # 1
        self.cursor = None  # xterm
        self.disabledBackground = None  # #d9d9d9
        self.disabledForeground = None  # #a3a3a3
        self.exportSelection = None  # 1
        self.font = None  # TkTextFont
        self.foreground = None  # #000000
        self.from_ = None  # 0
        self.highlightBackground = None  # #d9d9d9
        self.highlightColor = None  # #000000
        self.highlightThickness = None  # 1
        self.increment = None  # 1
        self.insertBackground = None  # #000000
        self.insertBorderWidth = None  # 0
        self.insertOffTime = None  # 300
        self.insertOnTime = None  # 600
        self.insertWidth = None  # 2
        self.justify = None  # left
        self.readonlyBackground = None  # #d9d9d9
        self.relief = None  # sunken
        self.repeatDelay = None  # 400
        self.repeatInterval = None  # 100
        self.selectBackground = None  # #c3c3c3
        self.selectBorderWidth = None  # 0
        self.selectForeground = None  # #000000
        self.state = None  # normal
        self.to = None  # 0
        self.validate = None  # none
        self.width = None  # 20
        self.wrap = None  # 0


class Text(_Style):
    _CLASS_NAME = "Text"

    def __init__(self):
        super().__init__()
        self.autoSeparators = None  # 1
        self.background = None  # "#ffffff"
        self.blockCursor = None  # 0
        self.borderWidth = None  # 1
        self.cursor = None  # xterm
        self.exportSelection = None  # 1
        self.font = None  # TkFixedFont
        self.foreground = None  # #000000
        self.height = None  # 24
        self.highlightBackground = None  # #d9d9d9
        self.highlightColor = None  # #000000
        self.highlightThickness = None  # 1
        self.inactiveSelectBackground = None  # #c3c3c3
        self.insertBackground = None  # #000000
        self.insertBorderWidth = None  # 0
        self.insertOffTime = None  # 300
        self.insertOnTime = None  # 600
        self.insertUnfocussed = None  # none
        self.insertWidth = None  # 2
        self.maxUndo = None  # 0
        self.padX = None  # 1
        self.padY = None  # 1
        self.relief = None  # sunken
        self.selectBackground = None  # #c3c3c3
        self.selectBorderWidth = None  # 0
        self.selectForeground = None  # #000000
        self.setGrid = None  # 0
        self.spacing1 = None  # 0
        self.spacing2 = None  # 0
        self.spacing3 = None  # 0
        self.state = None  # normal
        self.tabStyle = None  # tabular
        self.undo = None  # 0
        self.width = None  # 80
        self.wrap = None  # "char"


class Toplevel(_Style):
    _CLASS_NAME = "Toplevel"

    def __init__(self):
        super().__init__()
        self.background = None  # "#d9d9d9"
        self.borderWidth = None  # 0
        self.class_ = None  # "Toplevel"
        self.container = None  # 0
        self.height = None  # 0
        self.highlightBackground = None  # "#d9d9d9"
        self.highlightColor = None  # "#000000"
        self.highlightThickness = None  # 0
        self.padX = None  # 0
        self.padY = None  # 0
        self.relief = None  # "flat"
        self.takeFocus = None  # 0
        self.width = None  # 0


class Error(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ""
        super().__init__(self.message)

    def __str__(self):
        return self.message


def _get_children(widget, cache=None):
    for child in widget.winfo_children():
        try:
            cache.append(child)
        except AttributeError:
            cache = list()
            cache.append(child)
        _get_children(child, cache)
    return cache


def _populate_option_database(widget, styles,
                              prefix=None,
                              classes_and_options=None):
    for pattern, style in styles.items():
        prefix_cache = pattern if not prefix else "{}{}".format(prefix, pattern)
        for key, val in style.__dict__.items():
            if key == "_styles" or val is None:
                continue
            if classes_and_options is None:
                classes_and_options = dict()
            if not style.class_name in classes_and_options:
                classes_and_options[style.class_name] = set()
            classes_and_options[style.class_name].add(key)
            if (prefix_cache.endswith("*")
                    or prefix_cache.endswith(".")):
                cache = "{}{}".format(prefix_cache, key)
            else:
                cache = "{}.{}".format(prefix_cache, key)
            widget.option_add(cache, val)
        classes_and_options = _populate_option_database(widget, style.styles,
                                                        prefix_cache,
                                                        classes_and_options)
    return classes_and_options


def _pull_option_database(widget, classes_and_options):
    if not classes_and_options:
        return
    children = _get_children(widget)
    if not children:
        return
    for child in children:
        class_name = child.winfo_class()
        if class_name not in classes_and_options:
            continue
        for option in classes_and_options[class_name]:
            val = child.option_get(option, class_name)
            if val == "":
                continue
            child.config(cnf={option.lower(): val})

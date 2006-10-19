# -*- coding: utf-8 -*-
"""
    pygments.styles.murphy
    ~~~~~~~~~~~~~~~~~~~~~

    Murphy's style from CodeRay.

    :copyright: 2006 by Georg Brandl.
    :license: GNU LGPL, see LICENSE for more details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic


class MurphyStyle(Style):

    default_style = ""

    styles = {
        Comment:                   "#666 italic",
        Comment.Preproc:           "#579 noitalic",

        Keyword:                   "bold #289",
        Keyword.Pseudo:            "#08f",
        Keyword.Type:              "#66f",

        Operator:                  "#333",
        Operator.Word:             "bold #000",

        Name.Builtin:              "#072",
        Name.Function:             "bold #5ed",
        Name.Class:                "bold #e9e",
        Name.Namespace:            "bold #0e84b5",
        Name.Exception:            "bold #F00",
        Name.Variable:             "#036",
        Name.Variable.Instance:    "#aaf",
        Name.Variable.Class:       "#ccf",
        Name.Variable.Global:      "#f84",
        Name.Constant:             "bold #5ed",
        Name.Label:                "bold #970",
        Name.Entity:               "#800",
        Name.Attribute:            "#007",
        Name.Tag:                  "#070",
        Name.Decorator:            "bold #555",

        String:                    "bg:#e0e0ff",
        String.Char:               "#88F bg:",
        String.Doc:                "#D42 bg:",
        String.Interpol:           "bg:#eee",
        String.Escape:             "bold #666",
        String.Regex:              "bg:#e0e0ff #000",
        String.Symbol:             "#fc8 bg:",
        String.Other:              "#f88",

        Number:                    "bold #60E",
        Number.Integer:            "bold #66f",
        Number.Float:              "bold #60E",
        Number.Hex:                "bold #058",
        Number.Oct:                "bold #40E",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#00A000",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #c65d09",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "#F00 bg:#FAA"
    }

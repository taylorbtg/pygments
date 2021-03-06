# -*- coding: utf-8 -*-
"""
    pygments.lexers.web
    ~~~~~~~~~~~~~~~~~~~

    Lexers for web-related languages and markup.

    :copyright: Copyright 2006-2010 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re
import copy

from pygments.lexer import RegexLexer, ExtendedRegexLexer, bygroups, using, \
     include, this
from pygments.token import \
     Text, Comment, Operator, Keyword, Name, String, Number, Other, Punctuation
from pygments.util import get_bool_opt, get_list_opt, looks_like_xml, \
                          html_doctype_matches
from pygments.lexers.agile import RubyLexer


__all__ = ['HtmlLexer', 'XmlLexer', 'JavascriptLexer', 'CssLexer',
           'PhpLexer', 'ActionScriptLexer', 'XsltLexer', 'ActionScript3Lexer',
           'MxmlLexer', 'HaxeLexer', 'HamlLexer', 'SassLexer', 'ScssLexer',
           'ObjectiveJLexer', 'CoffeeScriptLexer']


class JavascriptLexer(RegexLexer):
    """
    For JavaScript source code.
    """

    name = 'JavaScript'
    aliases = ['js', 'javascript']
    filenames = ['*.js']
    mimetypes = ['application/x-javascript', 'text/x-javascript', 'text/javascript']

    flags = re.DOTALL
    tokens = {
        'commentsandwhitespace': [
            (r'\s+', Text),
            (r'<!--', Comment),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline)
        ],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            (r'/(\\.|[^[/\\\n]|\[(\\.|[^\]\\\n])*])+/'
             r'([gim]+\b|\B)', String.Regex, '#pop'),
            (r'(?=/)', Text, ('#pop', 'badregex')),
            (r'', Text, '#pop')
        ],
        'badregex': [
            ('\n', Text, '#pop')
        ],
        'root': [
            (r'^(?=\s|/|<!--)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            (r'\+\+|--|~|&&|\?|:|\|\||\\(?=\n)|'
             r'(<<|>>>?|==?|!=?|[-<>+*%&\|\^/])=?', Operator, 'slashstartsregex'),
            (r'[{(\[;,]', Punctuation, 'slashstartsregex'),
            (r'[})\].]', Punctuation),
            (r'(for|in|while|do|break|return|continue|switch|case|default|if|else|'
             r'throw|try|catch|finally|new|delete|typeof|instanceof|void|'
             r'this)\b', Keyword, 'slashstartsregex'),
            (r'(var|with|function)\b', Keyword.Declaration, 'slashstartsregex'),
            (r'(abstract|boolean|byte|char|class|const|debugger|double|enum|export|'
             r'extends|final|float|goto|implements|import|int|interface|long|native|'
             r'package|private|protected|public|short|static|super|synchronized|throws|'
             r'transient|volatile)\b', Keyword.Reserved),
            (r'(true|false|null|NaN|Infinity|undefined)\b', Keyword.Constant),
            (r'(Array|Boolean|Date|Error|Function|Math|netscape|'
             r'Number|Object|Packages|RegExp|String|sun|decodeURI|'
             r'decodeURIComponent|encodeURI|encodeURIComponent|'
             r'Error|eval|isFinite|isNaN|parseFloat|parseInt|document|this|'
             r'window)\b', Name.Builtin),
            (r'[$a-zA-Z_][a-zA-Z0-9_]*', Name.Other),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
        ]
    }


class ActionScriptLexer(RegexLexer):
    """
    For ActionScript source code.

    *New in Pygments 0.9.*
    """

    name = 'ActionScript'
    aliases = ['as', 'actionscript']
    filenames = ['*.as']
    mimetypes = ['application/x-actionscript', 'text/x-actionscript',
                 'text/actionscript']

    flags = re.DOTALL
    tokens = {
        'root': [
            (r'\s+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'/(\\\\|\\/|[^/\n])*/[gim]*', String.Regex),
            (r'[~\^\*!%&<>\|+=:;,/?\\-]+', Operator),
            (r'[{}\[\]();.]+', Punctuation),
            (r'(case|default|for|each|in|while|do|break|return|continue|if|else|'
             r'throw|try|catch|var|with|new|typeof|arguments|instanceof|this|'
             r'switch)\b', Keyword),
            (r'(class|public|final|internal|native|override|private|protected|'
             r'static|import|extends|implements|interface|intrinsic|return|super|'
             r'dynamic|function|const|get|namespace|package|set)\b',
             Keyword.Declaration),
            (r'(true|false|null|NaN|Infinity|-Infinity|undefined|Void)\b',
             Keyword.Constant),
            (r'(Accessibility|AccessibilityProperties|ActionScriptVersion|'
             r'ActivityEvent|AntiAliasType|ApplicationDomain|AsBroadcaster|Array|'
             r'AsyncErrorEvent|AVM1Movie|BevelFilter|Bitmap|BitmapData|'
             r'BitmapDataChannel|BitmapFilter|BitmapFilterQuality|BitmapFilterType|'
             r'BlendMode|BlurFilter|Boolean|ByteArray|Camera|Capabilities|CapsStyle|'
             r'Class|Color|ColorMatrixFilter|ColorTransform|ContextMenu|'
             r'ContextMenuBuiltInItems|ContextMenuEvent|ContextMenuItem|'
             r'ConvultionFilter|CSMSettings|DataEvent|Date|DefinitionError|'
             r'DeleteObjectSample|Dictionary|DisplacmentMapFilter|DisplayObject|'
             r'DisplacmentMapFilterMode|DisplayObjectContainer|DropShadowFilter|'
             r'Endian|EOFError|Error|ErrorEvent|EvalError|Event|EventDispatcher|'
             r'EventPhase|ExternalInterface|FileFilter|FileReference|'
             r'FileReferenceList|FocusDirection|FocusEvent|Font|FontStyle|FontType|'
             r'FrameLabel|FullScreenEvent|Function|GlowFilter|GradientBevelFilter|'
             r'GradientGlowFilter|GradientType|Graphics|GridFitType|HTTPStatusEvent|'
             r'IBitmapDrawable|ID3Info|IDataInput|IDataOutput|IDynamicPropertyOutput'
             r'IDynamicPropertyWriter|IEventDispatcher|IExternalizable|'
             r'IllegalOperationError|IME|IMEConversionMode|IMEEvent|int|'
             r'InteractiveObject|InterpolationMethod|InvalidSWFError|InvokeEvent|'
             r'IOError|IOErrorEvent|JointStyle|Key|Keyboard|KeyboardEvent|KeyLocation|'
             r'LineScaleMode|Loader|LoaderContext|LoaderInfo|LoadVars|LocalConnection|'
             r'Locale|Math|Matrix|MemoryError|Microphone|MorphShape|Mouse|MouseEvent|'
             r'MovieClip|MovieClipLoader|Namespace|NetConnection|NetStatusEvent|'
             r'NetStream|NewObjectSample|Number|Object|ObjectEncoding|PixelSnapping|'
             r'Point|PrintJob|PrintJobOptions|PrintJobOrientation|ProgressEvent|Proxy|'
             r'QName|RangeError|Rectangle|ReferenceError|RegExp|Responder|Sample|Scene|'
             r'ScriptTimeoutError|Security|SecurityDomain|SecurityError|'
             r'SecurityErrorEvent|SecurityPanel|Selection|Shape|SharedObject|'
             r'SharedObjectFlushStatus|SimpleButton|Socket|Sound|SoundChannel|'
             r'SoundLoaderContext|SoundMixer|SoundTransform|SpreadMethod|Sprite|'
             r'StackFrame|StackOverflowError|Stage|StageAlign|StageDisplayState|'
             r'StageQuality|StageScaleMode|StaticText|StatusEvent|String|StyleSheet|'
             r'SWFVersion|SyncEvent|SyntaxError|System|TextColorType|TextField|'
             r'TextFieldAutoSize|TextFieldType|TextFormat|TextFormatAlign|'
             r'TextLineMetrics|TextRenderer|TextSnapshot|Timer|TimerEvent|Transform|'
             r'TypeError|uint|URIError|URLLoader|URLLoaderDataFormat|URLRequest|'
             r'URLRequestHeader|URLRequestMethod|URLStream|URLVariabeles|VerifyError|'
             r'Video|XML|XMLDocument|XMLList|XMLNode|XMLNodeType|XMLSocket|XMLUI)\b',
             Name.Builtin),
            (r'(decodeURI|decodeURIComponent|encodeURI|escape|eval|isFinite|isNaN|'
             r'isXMLName|clearInterval|fscommand|getTimer|getURL|getVersion|'
             r'isFinite|parseFloat|parseInt|setInterval|trace|updateAfterEvent|'
             r'unescape)\b',Name.Function),
            (r'[$a-zA-Z_][a-zA-Z0-9_]*', Name.Other),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-f]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
        ]
    }

    def analyse_text(text):
        return 0.05


class ActionScript3Lexer(RegexLexer):
    """
    For ActionScript 3 source code.

    *New in Pygments 0.11.*
    """

    name = 'ActionScript 3'
    aliases = ['as3', 'actionscript3']
    filenames = ['*.as']
    mimetypes = ['application/x-actionscript', 'text/x-actionscript',
                 'text/actionscript']

    identifier = r'[$a-zA-Z_][a-zA-Z0-9_]*'

    flags = re.DOTALL | re.MULTILINE
    tokens = {
        'root': [
            (r'\s+', Text),
            (r'(function\s+)(' + identifier + r')(\s*)(\()',
             bygroups(Keyword.Declaration, Name.Function, Text, Operator),
             'funcparams'),
            (r'(var|const)(\s+)(' + identifier + r')(\s*)(:)(\s*)(' + identifier + r')',
             bygroups(Keyword.Declaration, Text, Name, Text, Punctuation, Text,
                      Keyword.Type)),
            (r'(import|package)(\s+)((?:' + identifier + r'|\.)+)(\s*)',
             bygroups(Keyword, Text, Name.Namespace, Text)),
            (r'(new)(\s+)(' + identifier + r')(\s*)(\()',
             bygroups(Keyword, Text, Keyword.Type, Text, Operator)),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'/(\\\\|\\/|[^\n])*/[gisx]*', String.Regex),
            (r'(\.)(' + identifier + r')', bygroups(Operator, Name.Attribute)),
            (r'(case|default|for|each|in|while|do|break|return|continue|if|else|'
             r'throw|try|catch|with|new|typeof|arguments|instanceof|this|'
             r'switch|import|include|as|is)\b',
             Keyword),
            (r'(class|public|final|internal|native|override|private|protected|'
             r'static|import|extends|implements|interface|intrinsic|return|super|'
             r'dynamic|function|const|get|namespace|package|set)\b',
             Keyword.Declaration),
            (r'(true|false|null|NaN|Infinity|-Infinity|undefined|void)\b',
             Keyword.Constant),
            (r'(decodeURI|decodeURIComponent|encodeURI|escape|eval|isFinite|isNaN|'
             r'isXMLName|clearInterval|fscommand|getTimer|getURL|getVersion|'
             r'isFinite|parseFloat|parseInt|setInterval|trace|updateAfterEvent|'
             r'unescape)\b', Name.Function),
            (identifier, Name),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-f]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
            (r'[~\^\*!%&<>\|+=:;,/?\\{}\[\]();.-]+', Operator),
        ],
        'funcparams': [
            (r'\s+', Text),
            (r'(\s*)(\.\.\.)?(' + identifier + r')(\s*)(:)(\s*)(' +
             identifier + r'|\*)(\s*)',
             bygroups(Text, Punctuation, Name, Text, Operator, Text,
                      Keyword.Type, Text), 'defval'),
            (r'\)', Operator, 'type')
        ],
        'type': [
            (r'(\s*)(:)(\s*)(' + identifier + r'|\*)',
             bygroups(Text, Operator, Text, Keyword.Type), '#pop:2'),
            (r'\s*', Text, '#pop:2')
        ],
        'defval': [
            (r'(=)(\s*)([^(),]+)(\s*)(,?)',
             bygroups(Operator, Text, using(this), Text, Operator), '#pop'),
            (r',?', Operator, '#pop')
        ]
    }

    def analyse_text(text):
        if re.match(r'\w+\s*:\s*\w', text): return 0.3
        return 0.1


class CssLexer(RegexLexer):
    """
    For CSS (Cascading Style Sheets).
    """

    name = 'CSS'
    aliases = ['css']
    filenames = ['*.css']
    mimetypes = ['text/css']

    tokens = {
        'root': [
            include('basics'),
        ],
        'basics': [
            (r'\s+', Text),
            (r'/\*(?:.|\n)*?\*/', Comment),
            (r'{', Punctuation, 'content'),
            (r'\:[a-zA-Z0-9_-]+', Name.Decorator),
            (r'\.[a-zA-Z0-9_-]+', Name.Class),
            (r'\#[a-zA-Z0-9_-]+', Name.Function),
            (r'@[a-zA-Z0-9_-]+', Keyword, 'atrule'),
            (r'[a-zA-Z0-9_-]+', Name.Tag),
            (r'[~\^\*!%&\[\]\(\)<>\|+=@:;,./?-]', Operator),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single)
        ],
        'atrule': [
            (r'{', Punctuation, 'atcontent'),
            (r';', Punctuation, '#pop'),
            include('basics'),
        ],
        'atcontent': [
            include('basics'),
            (r'}', Punctuation, '#pop:2'),
        ],
        'content': [
            (r'\s+', Text),
            (r'}', Punctuation, '#pop'),
            (r'url\(.*?\)', String.Other),
            (r'^@.*?$', Comment.Preproc),
            (r'(azimuth|background-attachment|background-color|'
             r'background-image|background-position|background-repeat|'
             r'background|border-bottom-color|border-bottom-style|'
             r'border-bottom-width|border-left-color|border-left-style|'
             r'border-left-width|border-right|border-right-color|'
             r'border-right-style|border-right-width|border-top-color|'
             r'border-top-style|border-top-width|border-bottom|'
             r'border-collapse|border-left|border-width|border-color|'
             r'border-spacing|border-style|border-top|border|caption-side|'
             r'clear|clip|color|content|counter-increment|counter-reset|'
             r'cue-after|cue-before|cue|cursor|direction|display|'
             r'elevation|empty-cells|float|font-family|font-size|'
             r'font-size-adjust|font-stretch|font-style|font-variant|'
             r'font-weight|font|height|letter-spacing|line-height|'
             r'list-style-type|list-style-image|list-style-position|'
             r'list-style|margin-bottom|margin-left|margin-right|'
             r'margin-top|margin|marker-offset|marks|max-height|max-width|'
             r'min-height|min-width|opacity|orphans|outline|outline-color|'
             r'outline-style|outline-width|overflow(?:-x|-y|)|padding-bottom|'
             r'padding-left|padding-right|padding-top|padding|page|'
             r'page-break-after|page-break-before|page-break-inside|'
             r'pause-after|pause-before|pause|pitch|pitch-range|'
             r'play-during|position|quotes|richness|right|size|'
             r'speak-header|speak-numeral|speak-punctuation|speak|'
             r'speech-rate|stress|table-layout|text-align|text-decoration|'
             r'text-indent|text-shadow|text-transform|top|unicode-bidi|'
             r'vertical-align|visibility|voice-family|volume|white-space|'
             r'widows|width|word-spacing|z-index|bottom|left|'
             r'above|absolute|always|armenian|aural|auto|avoid|baseline|'
             r'behind|below|bidi-override|blink|block|bold|bolder|both|'
             r'capitalize|center-left|center-right|center|circle|'
             r'cjk-ideographic|close-quote|collapse|condensed|continuous|'
             r'crop|crosshair|cross|cursive|dashed|decimal-leading-zero|'
             r'decimal|default|digits|disc|dotted|double|e-resize|embed|'
             r'extra-condensed|extra-expanded|expanded|fantasy|far-left|'
             r'far-right|faster|fast|fixed|georgian|groove|hebrew|help|'
             r'hidden|hide|higher|high|hiragana-iroha|hiragana|icon|'
             r'inherit|inline-table|inline|inset|inside|invert|italic|'
             r'justify|katakana-iroha|katakana|landscape|larger|large|'
             r'left-side|leftwards|level|lighter|line-through|list-item|'
             r'loud|lower-alpha|lower-greek|lower-roman|lowercase|ltr|'
             r'lower|low|medium|message-box|middle|mix|monospace|'
             r'n-resize|narrower|ne-resize|no-close-quote|no-open-quote|'
             r'no-repeat|none|normal|nowrap|nw-resize|oblique|once|'
             r'open-quote|outset|outside|overline|pointer|portrait|px|'
             r'relative|repeat-x|repeat-y|repeat|rgb|ridge|right-side|'
             r'rightwards|s-resize|sans-serif|scroll|se-resize|'
             r'semi-condensed|semi-expanded|separate|serif|show|silent|'
             r'slow|slower|small-caps|small-caption|smaller|soft|solid|'
             r'spell-out|square|static|status-bar|super|sw-resize|'
             r'table-caption|table-cell|table-column|table-column-group|'
             r'table-footer-group|table-header-group|table-row|'
             r'table-row-group|text|text-bottom|text-top|thick|thin|'
             r'transparent|ultra-condensed|ultra-expanded|underline|'
             r'upper-alpha|upper-latin|upper-roman|uppercase|url|'
             r'visible|w-resize|wait|wider|x-fast|x-high|x-large|x-loud|'
             r'x-low|x-small|x-soft|xx-large|xx-small|yes)\b', Keyword),
            (r'(indigo|gold|firebrick|indianred|yellow|darkolivegreen|'
             r'darkseagreen|mediumvioletred|mediumorchid|chartreuse|'
             r'mediumslateblue|black|springgreen|crimson|lightsalmon|brown|'
             r'turquoise|olivedrab|cyan|silver|skyblue|gray|darkturquoise|'
             r'goldenrod|darkgreen|darkviolet|darkgray|lightpink|teal|'
             r'darkmagenta|lightgoldenrodyellow|lavender|yellowgreen|thistle|'
             r'violet|navy|orchid|blue|ghostwhite|honeydew|cornflowerblue|'
             r'darkblue|darkkhaki|mediumpurple|cornsilk|red|bisque|slategray|'
             r'darkcyan|khaki|wheat|deepskyblue|darkred|steelblue|aliceblue|'
             r'gainsboro|mediumturquoise|floralwhite|coral|purple|lightgrey|'
             r'lightcyan|darksalmon|beige|azure|lightsteelblue|oldlace|'
             r'greenyellow|royalblue|lightseagreen|mistyrose|sienna|'
             r'lightcoral|orangered|navajowhite|lime|palegreen|burlywood|'
             r'seashell|mediumspringgreen|fuchsia|papayawhip|blanchedalmond|'
             r'peru|aquamarine|white|darkslategray|ivory|dodgerblue|'
             r'lemonchiffon|chocolate|orange|forestgreen|slateblue|olive|'
             r'mintcream|antiquewhite|darkorange|cadetblue|moccasin|'
             r'limegreen|saddlebrown|darkslateblue|lightskyblue|deeppink|'
             r'plum|aqua|darkgoldenrod|maroon|sandybrown|magenta|tan|'
             r'rosybrown|pink|lightblue|palevioletred|mediumseagreen|'
             r'dimgray|powderblue|seagreen|snow|mediumblue|midnightblue|'
             r'paleturquoise|palegoldenrod|whitesmoke|darkorchid|salmon|'
             r'lightslategray|lawngreen|lightgreen|tomato|hotpink|'
             r'lightyellow|lavenderblush|linen|mediumaquamarine|green|'
             r'blueviolet|peachpuff)\b', Name.Builtin),
            (r'\!important', Comment.Preproc),
            (r'/\*(?:.|\n)*?\*/', Comment),
            (r'\#[a-zA-Z0-9]{1,6}', Number),
            (r'[\.-]?[0-9]*[\.]?[0-9]+(em|px|\%|pt|pc|in|mm|cm|ex)', Number),
            (r'-?[0-9]+', Number),
            (r'[~\^\*!%&<>\|+=@:,./?-]+', Operator),
            (r'[\[\]();]+', Punctuation),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
            (r'[a-zA-Z][a-zA-Z0-9]+', Name)
        ]
    }


class ObjectiveJLexer(RegexLexer):
    """
    For Objective-J source code with preprocessor directives.

    *New in Pygments 1.3.*
    """

    name = 'Objective-J'
    aliases = ['objective-j', 'objectivej', 'obj-j', 'objj']
    filenames = ['*.j']
    mimetypes = ['text/x-objective-j']

    #: optional Comment or Whitespace
    _ws = r'(?:\s|//.*?\n|/[*].*?[*]/)*'

    flags = re.DOTALL | re.MULTILINE

    tokens = {
        'root': [
            include('whitespace'),

            # function definition
            (r'^(' + _ws + r'[\+-]' + _ws + r')([\(a-zA-Z_].*?[^\(])(' + _ws + '{)',
             bygroups(using(this), using(this, state='function_signature'),
                      using(this))),

            # class definition
            (r'(@interface|@implementation)(\s+)', bygroups(Keyword, Text),
             'classname'),
            (r'(@class|@protocol)(\s*)', bygroups(Keyword, Text),
             'forward_classname'),
            (r'(\s*)(@end)(\s*)', bygroups(Text, Keyword, Text)),

            include('statements'),
            ('[{\(\)}]', Punctuation),
            (';', Punctuation),
        ],
        'whitespace': [
            (r'(@import)(\s+)("(\\\\|\\"|[^"])*")',
             bygroups(Comment.Preproc, Text, String.Double)),
            (r'(@import)(\s+)(<(\\\\|\\>|[^>])*>)',
             bygroups(Comment.Preproc, Text, String.Double)),
            (r'(#(?:include|import))(\s+)("(\\\\|\\"|[^"])*")',
             bygroups(Comment.Preproc, Text, String.Double)),
            (r'(#(?:include|import))(\s+)(<(\\\\|\\>|[^>])*>)',
             bygroups(Comment.Preproc, Text, String.Double)),

            (r'#if\s+0', Comment.Preproc, 'if0'),
            (r'#', Comment.Preproc, 'macro'),

            (r'\n', Text),
            (r'\s+', Text),
            (r'\\\n', Text), # line continuation
            (r'//(\n|(.|\n)*?[^\\]\n)', Comment.Single),
            (r'/(\\\n)?[*](.|\n)*?[*](\\\n)?/', Comment.Multiline),
            (r'<!--', Comment),
        ],
        'slashstartsregex': [
            include('whitespace'),
            (r'/(\\.|[^[/\\\n]|\[(\\.|[^\]\\\n])*])+/'
             r'([gim]+\b|\B)', String.Regex, '#pop'),
            (r'(?=/)', Text, ('#pop', 'badregex')),
            (r'', Text, '#pop'),
        ],
        'badregex': [
            ('\n', Text, '#pop'),
        ],
        'statements': [
            (r'(L|@)?"', String, 'string'),
            (r"(L|@)?'(\\.|\\[0-7]{1,3}|\\x[a-fA-F0-9]{1,2}|[^\\\'\n])'",
             String.Char),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
            (r'(\d+\.\d*|\.\d+|\d+)[eE][+-]?\d+[lL]?', Number.Float),
            (r'(\d+\.\d*|\.\d+|\d+[fF])[fF]?', Number.Float),
            (r'0x[0-9a-fA-F]+[Ll]?', Number.Hex),
            (r'0[0-7]+[Ll]?', Number.Oct),
            (r'\d+[Ll]?', Number.Integer),

            (r'^(?=\s|/|<!--)', Text, 'slashstartsregex'),

            (r'\+\+|--|~|&&|\?|:|\|\||\\(?=\n)|'
             r'(<<|>>>?|==?|!=?|[-<>+*%&\|\^/])=?',
             Operator, 'slashstartsregex'),
            (r'[{(\[;,]', Punctuation, 'slashstartsregex'),
            (r'[})\].]', Punctuation),

            (r'(for|in|while|do|break|return|continue|switch|case|default|if|'
             r'else|throw|try|catch|finally|new|delete|typeof|instanceof|void|'
             r'prototype|__proto__)\b', Keyword, 'slashstartsregex'),

            (r'(var|with|function)\b', Keyword.Declaration, 'slashstartsregex'),

            (r'(@selector|@private|@protected|@public|@encode|'
             r'@synchronized|@try|@throw|@catch|@finally|@end|@property|'
             r'@synthesize|@dynamic|@for|@accessors|new)\b', Keyword),

            (r'(int|long|float|short|double|char|unsigned|signed|void|'
             r'id|BOOL|bool|boolean|IBOutlet|IBAction|SEL|@outlet|@action)\b',
             Keyword.Type),

            (r'(self|super)\b', Name.Builtin),

            (r'(TRUE|YES|FALSE|NO|Nil|nil|NULL)\b', Keyword.Constant),
            (r'(true|false|null|NaN|Infinity|undefined)\b', Keyword.Constant),
            (r'(ABS|ASIN|ACOS|ATAN|ATAN2|SIN|COS|TAN|EXP|POW|CEIL|FLOOR|ROUND|'
             r'MIN|MAX|RAND|SQRT|E|LN2|LN10|LOG2E|LOG10E|PI|PI2|PI_2|SQRT1_2|'
             r'SQRT2)\b', Keyword.Constant),

            (r'(Array|Boolean|Date|Error|Function|Math|netscape|'
             r'Number|Object|Packages|RegExp|String|sun|decodeURI|'
             r'decodeURIComponent|encodeURI|encodeURIComponent|'
             r'Error|eval|isFinite|isNaN|parseFloat|parseInt|document|this|'
             r'window)\b', Name.Builtin),

            (r'([$a-zA-Z_][a-zA-Z0-9_]*)(' + _ws + r')(?=\()',
             bygroups(Name.Function, using(this))),

            (r'[$a-zA-Z_][a-zA-Z0-9_]*', Name),
        ],
        'classname' : [
            # interface definition that inherits
            (r'([a-zA-Z_][a-zA-Z0-9_]*)(' + _ws + r':' + _ws +
             r')([a-zA-Z_][a-zA-Z0-9_]*)?',
             bygroups(Name.Class, using(this), Name.Class), '#pop'),
            # interface definition for a category
            (r'([a-zA-Z_][a-zA-Z0-9_]*)(' + _ws + r'\()([a-zA-Z_][a-zA-Z0-9_]*)(\))',
             bygroups(Name.Class, using(this), Name.Label, Text), '#pop'),
            # simple interface / implementation
            (r'([a-zA-Z_][a-zA-Z0-9_]*)', Name.Class, '#pop'),
        ],
        'forward_classname' : [
            (r'([a-zA-Z_][a-zA-Z0-9_]*)(\s*,\s*)',
             bygroups(Name.Class, Text), '#push'),
            (r'([a-zA-Z_][a-zA-Z0-9_]*)(\s*;?)',
             bygroups(Name.Class, Text), '#pop'),
        ],
        'function_signature': [
            include('whitespace'),

            # start of a selector w/ parameters
            (r'(\(' + _ws + r')'                # open paren
             r'([a-zA-Z_][a-zA-Z0-9_]+)'        # return type
             r'(' + _ws + r'\)' + _ws + r')'    # close paren
             r'([$a-zA-Z_][a-zA-Z0-9_]+' + _ws + r':)', # function name
             bygroups(using(this), Keyword.Type, using(this),
                 Name.Function), 'function_parameters'),

            # no-param function
            (r'(\(' + _ws + r')'                # open paren
             r'([a-zA-Z_][a-zA-Z0-9_]+)'        # return type
             r'(' + _ws + r'\)' + _ws + r')'    # close paren
             r'([$a-zA-Z_][a-zA-Z0-9_]+)',      # function name
             bygroups(using(this), Keyword.Type, using(this),
                 Name.Function), "#pop"),

            # no return type given, start of a selector w/ parameters
            (r'([$a-zA-Z_][a-zA-Z0-9_]+' + _ws + r':)', # function name
             bygroups (Name.Function), 'function_parameters'),

            # no return type given, no-param function
            (r'([$a-zA-Z_][a-zA-Z0-9_]+)',      # function name
             bygroups(Name.Function), "#pop"),

            ('', Text, '#pop'),
        ],
        'function_parameters': [
            include('whitespace'),

            # parameters
            (r'(\(' + _ws + ')'                 # open paren
             r'([^\)]+)'                        # type
             r'(' + _ws + r'\)' + _ws + r')+'   # close paren
             r'([$a-zA-Z_][a-zA-Z0-9_]+)',      # param name
             bygroups(using(this), Keyword.Type, using(this), Text)),

            # one piece of a selector name
            (r'([$a-zA-Z_][a-zA-Z0-9_]+' + _ws + r':)',     # function name
             Name.Function),

            # smallest possible selector piece
            (r'(:)', Name.Function),

            # var args
            (r'(,' + _ws + r'...)', using(this)),

            # param name
            (r'([$a-zA-Z_][a-zA-Z0-9_]+)', Text),
        ],
        'expression' : [
            (r'([$a-zA-Z_][a-zA-Z0-9_]*)(\()', bygroups(Name.Function,
                                                        Punctuation)),
            (r'(\))', Punctuation, "#pop"),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
            (r'[^\\"\n]+', String), # all other characters
            (r'\\\n', String), # line continuation
            (r'\\', String), # stray backslash
        ],
        'macro': [
            (r'[^/\n]+', Comment.Preproc),
            (r'/[*](.|\n)*?[*]/', Comment.Multiline),
            (r'//.*?\n', Comment.Single, '#pop'),
            (r'/', Comment.Preproc),
            (r'(?<=\\)\n', Comment.Preproc),
            (r'\n', Comment.Preproc, '#pop'),
        ],
        'if0': [
            (r'^\s*#if.*?(?<!\\)\n', Comment.Preproc, '#push'),
            (r'^\s*#endif.*?(?<!\\)\n', Comment.Preproc, '#pop'),
            (r'.*?\n', Comment),
        ]
    }

    def analyse_text(text):
        if re.search('^\s*@import\s+[<"]', text, re.MULTILINE):
            # special directive found in most Objective-J files
            return True
        return False


class HtmlLexer(RegexLexer):
    """
    For HTML 4 and XHTML 1 markup. Nested JavaScript and CSS is highlighted
    by the appropriate lexer.
    """

    name = 'HTML'
    aliases = ['html']
    filenames = ['*.html', '*.htm', '*.xhtml', '*.xslt']
    mimetypes = ['text/html', 'application/xhtml+xml']

    flags = re.IGNORECASE | re.DOTALL
    tokens = {
        'root': [
            ('[^<&]+', Text),
            (r'&\S*?;', Name.Entity),
            (r'\<\!\[CDATA\[.*?\]\]\>', Comment.Preproc),
            ('<!--', Comment, 'comment'),
            (r'<\?.*?\?>', Comment.Preproc),
            ('<![^>]*>', Comment.Preproc),
            (r'<\s*script\s*', Name.Tag, ('script-content', 'tag')),
            (r'<\s*style\s*', Name.Tag, ('style-content', 'tag')),
            (r'<\s*[a-zA-Z0-9:]+', Name.Tag, 'tag'),
            (r'<\s*/\s*[a-zA-Z0-9:]+\s*>', Name.Tag),
        ],
        'comment': [
            ('[^-]+', Comment),
            ('-->', Comment, '#pop'),
            ('-', Comment),
        ],
        'tag': [
            (r'\s+', Text),
            (r'[a-zA-Z0-9_:-]+\s*=', Name.Attribute, 'attr'),
            (r'[a-zA-Z0-9_:-]+', Name.Attribute),
            (r'/?\s*>', Name.Tag, '#pop'),
        ],
        'script-content': [
            (r'<\s*/\s*script\s*>', Name.Tag, '#pop'),
            (r'.+?(?=<\s*/\s*script\s*>)', using(JavascriptLexer)),
        ],
        'style-content': [
            (r'<\s*/\s*style\s*>', Name.Tag, '#pop'),
            (r'.+?(?=<\s*/\s*style\s*>)', using(CssLexer)),
        ],
        'attr': [
            ('".*?"', String, '#pop'),
            ("'.*?'", String, '#pop'),
            (r'[^\s>]+', String, '#pop'),
        ],
    }

    def analyse_text(text):
        if html_doctype_matches(text):
            return 0.5


class PhpLexer(RegexLexer):
    """
    For `PHP <http://www.php.net/>`_ source code.
    For PHP embedded in HTML, use the `HtmlPhpLexer`.

    Additional options accepted:

    `startinline`
        If given and ``True`` the lexer starts highlighting with
        php code (i.e.: no starting ``<?php`` required).  The default
        is ``False``.
    `funcnamehighlighting`
        If given and ``True``, highlight builtin function names
        (default: ``True``).
    `disabledmodules`
        If given, must be a list of module names whose function names
        should not be highlighted. By default all modules are highlighted
        except the special ``'unknown'`` module that includes functions
        that are known to php but are undocumented.

        To get a list of allowed modules have a look into the
        `_phpbuiltins` module:

        .. sourcecode:: pycon

            >>> from pygments.lexers._phpbuiltins import MODULES
            >>> MODULES.keys()
            ['PHP Options/Info', 'Zip', 'dba', ...]

        In fact the names of those modules match the module names from
        the php documentation.
    """

    name = 'PHP'
    aliases = ['php', 'php3', 'php4', 'php5']
    filenames = ['*.php', '*.php[345]']
    mimetypes = ['text/x-php']

    flags = re.IGNORECASE | re.DOTALL | re.MULTILINE
    tokens = {
        'root': [
            (r'<\?(php)?', Comment.Preproc, 'php'),
            (r'[^<]+', Other),
            (r'<', Other)
        ],
        'php': [
            (r'\?>', Comment.Preproc, '#pop'),
            (r'<<<(\'?)([a-zA-Z_][a-zA-Z0-9_]*)\1\n.*?\n\2\;?\n', String),
            (r'\s+', Text),
            (r'#.*?\n', Comment.Single),
            (r'//.*?\n', Comment.Single),
            # put the empty comment here, it is otherwise seen as
            # the start of a docstring
            (r'/\*\*/', Comment.Multiline),
            (r'/\*\*.*?\*/', String.Doc),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'(->|::)(\s*)([a-zA-Z_][a-zA-Z0-9_]*)',
             bygroups(Operator, Text, Name.Attribute)),
            (r'[~!%^&*+=|:.<>/?@-]+', Operator),
            (r'[\[\]{}();,]+', Punctuation),
            (r'(class)(\s+)', bygroups(Keyword, Text), 'classname'),
            (r'(function)(\s*)(?=\()', bygroups(Keyword, Text)),
            (r'(function)(\s+)(&?)(\s*)',
              bygroups(Keyword, Text, Operator, Text), 'functionname'),
            (r'(const)(\s+)([a-zA-Z_][a-zA-Z0-9_]*)',
              bygroups(Keyword, Text, Name.Constant)),
            (r'(and|E_PARSE|old_function|E_ERROR|or|as|E_WARNING|parent|'
             r'eval|PHP_OS|break|exit|case|extends|PHP_VERSION|cfunction|'
             r'FALSE|print|for|require|continue|foreach|require_once|'
             r'declare|return|default|static|do|switch|die|stdClass|'
             r'echo|else|TRUE|elseif|var|empty|if|xor|enddeclare|include|'
             r'virtual|endfor|include_once|while|endforeach|global|__FILE__|'
             r'endif|list|__LINE__|endswitch|new|__sleep|endwhile|not|'
             r'array|__wakeup|E_ALL|NULL|final|php_user_filter|interface|'
             r'implements|public|private|protected|abstract|clone|try|'
             r'catch|throw|this|use|namespace)\b', Keyword),
            ('(true|false|null)\b', Keyword.Constant),
            (r'\$\{\$+[a-zA-Z_][a-zA-Z0-9_]*\}', Name.Variable),
            (r'\$+[a-zA-Z_][a-zA-Z0-9_]*', Name.Variable),
            (r'[\\a-zA-Z_][\\a-zA-Z0-9_]*', Name.Other),
            (r"[0-9](\.[0-9]*)?(eE[+-][0-9])?[flFLdD]?|"
             r"0[xX][0-9a-fA-F]+[Ll]?", Number),
            (r"'([^'\\]*(?:\\.[^'\\]*)*)'", String.Single),
            (r'`([^`\\]*(?:\\.[^`\\]*)*)`', String.Backtick),
            (r'"', String.Double, 'string'),
        ],
        'classname': [
            (r'[a-zA-Z_][\\a-zA-Z0-9_]*', Name.Class, '#pop')
        ],
        'functionname': [
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name.Function, '#pop')
        ],
        'string': [
            (r'"', String.Double, '#pop'),
            (r'[^{$"\\]+', String.Double),
            (r'\\([nrt\"$]|[0-7]{1,3}|x[0-9A-Fa-f]{1,2})', String.Escape),
            (r'\$[a-zA-Z_][a-zA-Z0-9_]*(\[\S+\]|->[a-zA-Z_][a-zA-Z0-9_]*)?',
             String.Interpol),
            (r'(\{\$\{)(.*?)(\}\})',
             bygroups(String.Interpol, using(this, _startinline=True),
                      String.Interpol)),
            (r'(\{)(\$.*?)(\})',
             bygroups(String.Interpol, using(this, _startinline=True),
                      String.Interpol)),
            (r'(\$\{)(\S+)(\})',
             bygroups(String.Interpol, Name.Variable, String.Interpol)),
            (r'[${\\]+', String.Double)
        ],
    }

    def __init__(self, **options):
        self.funcnamehighlighting = get_bool_opt(
            options, 'funcnamehighlighting', True)
        self.disabledmodules = get_list_opt(
            options, 'disabledmodules', ['unknown'])
        self.startinline = get_bool_opt(options, 'startinline', False)

        # private option argument for the lexer itself
        if '_startinline' in options:
            self.startinline = options.pop('_startinline')

        # collect activated functions in a set
        self._functions = set()
        if self.funcnamehighlighting:
            from pygments.lexers._phpbuiltins import MODULES
            for key, value in MODULES.iteritems():
                if key not in self.disabledmodules:
                    self._functions.update(value)
        RegexLexer.__init__(self, **options)

    def get_tokens_unprocessed(self, text):
        stack = ['root']
        if self.startinline:
            stack.append('php')
        for index, token, value in \
            RegexLexer.get_tokens_unprocessed(self, text, stack):
            if token is Name.Other:
                if value in self._functions:
                    yield index, Name.Builtin, value
                    continue
            yield index, token, value

    def analyse_text(text):
        rv = 0.0
        if re.search(r'<\?(?!xml)', text):
            rv += 0.3
        if '?>' in text:
            rv += 0.1
        return rv


class XmlLexer(RegexLexer):
    """
    Generic lexer for XML (eXtensible Markup Language).
    """

    flags = re.MULTILINE | re.DOTALL

    name = 'XML'
    aliases = ['xml']
    filenames = ['*.xml', '*.xsl', '*.rss', '*.xslt', '*.xsd', '*.wsdl']
    mimetypes = ['text/xml', 'application/xml', 'image/svg+xml',
                 'application/rss+xml', 'application/atom+xml',
                 'application/xsl+xml', 'application/xslt+xml']

    tokens = {
        'root': [
            ('[^<&]+', Text),
            (r'&\S*?;', Name.Entity),
            (r'\<\!\[CDATA\[.*?\]\]\>', Comment.Preproc),
            ('<!--', Comment, 'comment'),
            (r'<\?.*?\?>', Comment.Preproc),
            ('<![^>]*>', Comment.Preproc),
            (r'<\s*[a-zA-Z0-9:._-]+', Name.Tag, 'tag'),
            (r'<\s*/\s*[a-zA-Z0-9:._-]+\s*>', Name.Tag),
        ],
        'comment': [
            ('[^-]+', Comment),
            ('-->', Comment, '#pop'),
            ('-', Comment),
        ],
        'tag': [
            (r'\s+', Text),
            (r'[a-zA-Z0-9_.:-]+\s*=', Name.Attribute, 'attr'),
            (r'/?\s*>', Name.Tag, '#pop'),
        ],
        'attr': [
            ('\s+', Text),
            ('".*?"', String, '#pop'),
            ("'.*?'", String, '#pop'),
            (r'[^\s>]+', String, '#pop'),
        ],
    }

    def analyse_text(text):
        if looks_like_xml(text):
            return 0.5


class XsltLexer(XmlLexer):
    '''
    A lexer for XSLT.

    *New in Pygments 0.10.*
    '''

    name = 'XSLT'
    aliases = ['xslt']
    filenames = ['*.xsl', '*.xslt']

    EXTRA_KEYWORDS = set([
        'apply-imports', 'apply-templates', 'attribute',
        'attribute-set', 'call-template', 'choose', 'comment',
        'copy', 'copy-of', 'decimal-format', 'element', 'fallback',
        'for-each', 'if', 'import', 'include', 'key', 'message',
        'namespace-alias', 'number', 'otherwise', 'output', 'param',
        'preserve-space', 'processing-instruction', 'sort',
        'strip-space', 'stylesheet', 'template', 'text', 'transform',
        'value-of', 'variable', 'when', 'with-param'
    ])

    def get_tokens_unprocessed(self, text):
        for index, token, value in XmlLexer.get_tokens_unprocessed(self, text):
            m = re.match('</?xsl:([^>]*)/?>?', value)

            if token is Name.Tag and m and m.group(1) in self.EXTRA_KEYWORDS:
                yield index, Keyword, value
            else:
                yield index, token, value

    def analyse_text(text):
        if looks_like_xml(text) and '<xsl' in text:
            return 0.8


class MxmlLexer(RegexLexer):
    """
    For MXML markup.
    Nested AS3 in <script> tags is highlighted by the appropriate lexer.
    """
    flags = re.MULTILINE | re.DOTALL
    name = 'MXML'
    aliases = ['mxml']
    filenames = ['*.mxml']
    mimetimes = ['text/xml', 'application/xml']

    tokens = {
            'root': [
                ('[^<&]+', Text),
                (r'&\S*?;', Name.Entity),
                (r'(\<\!\[CDATA\[)(.*?)(\]\]\>)',
                 bygroups(String, using(ActionScript3Lexer), String)),
                ('<!--', Comment, 'comment'),
                (r'<\?.*?\?>', Comment.Preproc),
                ('<![^>]*>', Comment.Preproc),
                (r'<\s*[a-zA-Z0-9:._-]+', Name.Tag, 'tag'),
                (r'<\s*/\s*[a-zA-Z0-9:._-]+\s*>', Name.Tag),
            ],
            'comment': [
                ('[^-]+', Comment),
                ('-->', Comment, '#pop'),
                ('-', Comment),
            ],
            'tag': [
                (r'\s+', Text),
                (r'[a-zA-Z0-9_.:-]+\s*=', Name.Attribute, 'attr'),
                (r'/?\s*>', Name.Tag, '#pop'),
            ],
            'attr': [
                ('\s+', Text),
                ('".*?"', String, '#pop'),
                ("'.*?'", String, '#pop'),
                (r'[^\s>]+', String, '#pop'),
            ],
        }


class HaxeLexer(RegexLexer):
    """
    For haXe source code (http://haxe.org/).
    """

    name = 'haXe'
    aliases = ['hx', 'haXe']
    filenames = ['*.hx']
    mimetypes = ['text/haxe']

    ident = r'(?:[a-zA-Z_][a-zA-Z0-9_]*)'
    typeid = r'(?:(?:[a-z0-9_\.])*[A-Z_][A-Za-z0-9_]*)'
    key_prop = r'(?:default|null|never)'
    key_decl_mod = r'(?:public|private|override|static|inline|extern|dynamic)'

    flags = re.DOTALL | re.MULTILINE

    tokens = {
        'root': [
            include('whitespace'),
            include('comments'),
            (key_decl_mod, Keyword.Declaration),
            include('enumdef'),
            include('typedef'),
            include('classdef'),
            include('imports'),
        ],

        # General constructs
        'comments': [
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'#[^\n]*', Comment.Preproc),
        ],
        'whitespace': [
            include('comments'),
            (r'\s+', Text),
        ],
        'codekeywords': [
            (r'\b(if|else|while|do|for|in|break|continue|'
             r'return|switch|case|try|catch|throw|null|trace|'
             r'new|this|super|untyped|cast|callback|here)\b',
             Keyword.Reserved),
        ],
        'literals': [
            (r'0[xX][0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r'~/([^\n])*?/[gisx]*', String.Regex),
            (r'\b(true|false|null)\b', Keyword.Constant),
        ],
        'codeblock': [
          include('whitespace'),
          include('new'),
          include('case'),
          include('anonfundef'),
          include('literals'),
          include('vardef'),
          include('codekeywords'),
          (r'[();,\[\]]', Punctuation),
          (r'(?:=|\+=|-=|\*=|/=|%=|&=|\|=|\^=|<<=|>>=|>>>=|\|\||&&|'
           r'\.\.\.|==|!=|>|<|>=|<=|\||&|\^|<<|>>|>>>|\+|\-|\*|/|%|'
           r'!|\+\+|\-\-|~|\.|\?|\:)',
           Operator),
          (ident, Name),

          (r'}', Punctuation,'#pop'),
          (r'{', Punctuation,'#push'),
        ],

        # Instance/Block level constructs
        'propertydef': [
            (r'(\()(' + key_prop + ')(,)(' + key_prop + ')(\))',
             bygroups(Punctuation, Keyword.Reserved, Punctuation,
                      Keyword.Reserved, Punctuation)),
        ],
        'new': [
            (r'\bnew\b', Keyword, 'typedecl'),
        ],
        'case': [
            (r'\b(case)(\s+)(' + ident + ')(\s*)(\()',
             bygroups(Keyword.Reserved, Text, Name, Text, Punctuation),
             'funargdecl'),
        ],
        'vardef': [
            (r'\b(var)(\s+)(' + ident + ')',
             bygroups(Keyword.Declaration, Text, Name.Variable), 'vardecl'),
        ],
        'vardecl': [
            include('whitespace'),
            include('typelabel'),
            (r'=', Operator,'#pop'),
            (r';', Punctuation,'#pop'),
        ],
        'instancevardef': [
            (key_decl_mod,Keyword.Declaration),
            (r'\b(var)(\s+)(' + ident + ')',
             bygroups(Keyword.Declaration, Text, Name.Variable.Instance),
             'instancevardecl'),
        ],
        'instancevardecl': [
            include('vardecl'),
            include('propertydef'),
        ],

        'anonfundef': [
            (r'\bfunction\b', Keyword.Declaration, 'fundecl'),
        ],
        'instancefundef': [
            (key_decl_mod, Keyword.Declaration),
            (r'\b(function)(\s+)(' + ident + ')',
             bygroups(Keyword.Declaration, Text, Name.Function), 'fundecl'),
        ],
        'fundecl': [
            include('whitespace'),
            include('typelabel'),
            include('generictypedecl'),
            (r'\(',Punctuation,'funargdecl'),
            (r'(?=[a-zA-Z0-9_])',Text,'#pop'),
            (r'{',Punctuation,('#pop','codeblock')),
            (r';',Punctuation,'#pop'),
        ],
        'funargdecl': [
            include('whitespace'),
            (ident, Name.Variable),
            include('typelabel'),
            include('literals'),
            (r'=', Operator),
            (r',', Punctuation),
            (r'\?', Punctuation),
            (r'\)', Punctuation, '#pop'),
        ],

        'typelabel': [
            (r':', Punctuation, 'type'),
        ],
        'typedecl': [
            include('whitespace'),
            (typeid, Name.Class),
            (r'<', Punctuation, 'generictypedecl'),
            (r'(?=[{}()=,a-z])', Text,'#pop'),
        ],
        'type': [
            include('whitespace'),
            (typeid, Name.Class),
            (r'<', Punctuation, 'generictypedecl'),
            (r'->', Keyword.Type),
            (r'(?=[{}(),;=])', Text, '#pop'),
        ],
        'generictypedecl': [
            include('whitespace'),
            (typeid, Name.Class),
            (r'<', Punctuation, '#push'),
            (r'>', Punctuation, '#pop'),
            (r',', Punctuation),
        ],

        # Top level constructs
        'imports': [
            (r'(package|import|using)(\s+)([^;]+)(;)',
             bygroups(Keyword.Namespace, Text, Name.Namespace,Punctuation)),
        ],
        'typedef': [
            (r'typedef', Keyword.Declaration, ('typedefprebody', 'typedecl')),
        ],
        'typedefprebody': [
            include('whitespace'),
            (r'(=)(\s*)({)', bygroups(Punctuation, Text, Punctuation),
             ('#pop', 'typedefbody')),
        ],
        'enumdef': [
            (r'enum', Keyword.Declaration, ('enumdefprebody', 'typedecl')),
        ],
        'enumdefprebody': [
            include('whitespace'),
            (r'{', Punctuation, ('#pop','enumdefbody')),
        ],
        'classdef': [
            (r'class', Keyword.Declaration, ('classdefprebody', 'typedecl')),
        ],
        'classdefprebody': [
            include('whitespace'),
            (r'(extends|implements)', Keyword.Declaration,'typedecl'),
            (r'{', Punctuation, ('#pop', 'classdefbody')),
        ],
        'interfacedef': [
            (r'interface', Keyword.Declaration,
             ('interfacedefprebody', 'typedecl')),
        ],
        'interfacedefprebody': [
            include('whitespace'),
            (r'(extends)', Keyword.Declaration, 'typedecl'),
            (r'{', Punctuation, ('#pop', 'classdefbody')),
        ],

        'typedefbody': [
          include('whitespace'),
          include('instancevardef'),
          include('instancefundef'),
          (r'>', Punctuation, 'typedecl'),
          (r',', Punctuation),
          (r'}', Punctuation, '#pop'),
        ],
        'enumdefbody': [
          include('whitespace'),
          (ident, Name.Variable.Instance),
          (r'\(', Punctuation, 'funargdecl'),
          (r';', Punctuation),
          (r'}', Punctuation, '#pop'),
        ],
        'classdefbody': [
          include('whitespace'),
          include('instancevardef'),
          include('instancefundef'),
          (r'}', Punctuation, '#pop'),
          include('codeblock'),
        ],
    }

    def analyse_text(text):
        if re.match(r'\w+\s*:\s*\w', text): return 0.3


def _indentation(lexer, match, ctx):
    indentation = match.group(0)
    yield match.start(), Text, indentation
    ctx.last_indentation = indentation
    ctx.pos = match.end()

    if hasattr(ctx, 'block_state') and ctx.block_state and \
            indentation.startswith(ctx.block_indentation) and \
            indentation != ctx.block_indentation:
        ctx.stack.append(ctx.block_state)
    else:
        ctx.block_state = None
        ctx.block_indentation = None
        ctx.stack.append('content')

def _starts_block(token, state):
    def callback(lexer, match, ctx):
        yield match.start(), token, match.group(0)

        if hasattr(ctx, 'last_indentation'):
            ctx.block_indentation = ctx.last_indentation
        else:
            ctx.block_indentation = ''

        ctx.block_state = state
        ctx.pos = match.end()

    return callback


class HamlLexer(ExtendedRegexLexer):
    """
    For Haml markup.

    *New in Pygments 1.3.*
    """

    name = 'Haml'
    aliases = ['haml', 'HAML']
    filenames = ['*.haml']
    mimetypes = ['text/x-haml']

    flags = re.IGNORECASE
    # Haml can include " |\n" anywhere,
    # which is ignored and used to wrap long lines.
    # To accomodate this, use this custom faux dot instead.
    _dot = r'(?: \|\n(?=.* \|)|.)'

    # In certain places, a comma at the end of the line
    # allows line wrapping as well.
    _comma_dot = r'(?:,\s*\n|' + _dot + ')'
    tokens = {
        'root': [
            (r'[ \t]*\n', Text),
            (r'[ \t]*', _indentation),
        ],

        'css': [
            (r'\.[a-z0-9_:-]+', Name.Class, 'tag'),
            (r'\#[a-z0-9_:-]+', Name.Function, 'tag'),
        ],

        'eval-or-plain': [
            (r'[&!]?==', Punctuation, 'plain'),
            (r'([&!]?[=~])(' + _comma_dot + '*\n)',
             bygroups(Punctuation, using(RubyLexer)),
             'root'),
            (r'', Text, 'plain'),
        ],

        'content': [
            include('css'),
            (r'%[a-z0-9_:-]+', Name.Tag, 'tag'),
            (r'!!!' + _dot + '*\n', Name.Namespace, '#pop'),
            (r'(/)(\[' + _dot + '*?\])(' + _dot + '*\n)',
             bygroups(Comment, Comment.Special, Comment),
             '#pop'),
            (r'/' + _dot + '*\n', _starts_block(Comment, 'html-comment-block'),
             '#pop'),
            (r'-#' + _dot + '*\n', _starts_block(Comment.Preproc,
                                                 'haml-comment-block'), '#pop'),
            (r'(-)(' + _comma_dot + '*\n)',
             bygroups(Punctuation, using(RubyLexer)),
             '#pop'),
            (r':' + _dot + '*\n', _starts_block(Name.Decorator, 'filter-block'),
             '#pop'),
            include('eval-or-plain'),
        ],

        'tag': [
            include('css'),
            (r'\{(,\n|' + _dot + ')*?\}', using(RubyLexer)),
            (r'\[' + _dot + '*?\]', using(RubyLexer)),
            (r'\(', Text, 'html-attributes'),
            (r'/[ \t]*\n', Punctuation, '#pop:2'),
            (r'[<>]{1,2}(?=[ \t=])', Punctuation),
            include('eval-or-plain'),
        ],

        'plain': [
            (r'([^#\n]|#[^{\n]|(\\\\)*\\#\{)+', Text),
            (r'(#\{)(' + _dot + '*?)(\})',
             bygroups(String.Interpol, using(RubyLexer), String.Interpol)),
            (r'\n', Text, 'root'),
        ],

        'html-attributes': [
            (r'\s+', Text),
            (r'[a-z0-9_:-]+[ \t]*=', Name.Attribute, 'html-attribute-value'),
            (r'[a-z0-9_:-]+', Name.Attribute),
            (r'\)', Text, '#pop'),
        ],

        'html-attribute-value': [
            (r'[ \t]+', Text),
            (r'[a-z0-9_]+', Name.Variable, '#pop'),
            (r'@[a-z0-9_]+', Name.Variable.Instance, '#pop'),
            (r'\$[a-z0-9_]+', Name.Variable.Global, '#pop'),
            (r"'(\\\\|\\'|[^'\n])*'", String, '#pop'),
            (r'"(\\\\|\\"|[^"\n])*"', String, '#pop'),
        ],

        'html-comment-block': [
            (_dot + '+', Comment),
            (r'\n', Text, 'root'),
        ],

        'haml-comment-block': [
            (_dot + '+', Comment.Preproc),
            (r'\n', Text, 'root'),
        ],

        'filter-block': [
            (r'([^#\n]|#[^{\n]|(\\\\)*\\#\{)+', Name.Decorator),
            (r'(#\{)(' + _dot + '*?)(\})',
             bygroups(String.Interpol, using(RubyLexer), String.Interpol)),
            (r'\n', Text, 'root'),
        ],
    }


common_sass_tokens = {
    'value': [
        (r'[ \t]+', Text),
        (r'[!$][\w-]+', Name.Variable),
        (r'url\(', String.Other, 'string-url'),
        (r'[a-z_-][\w-]*(?=\()', Name.Function),
        (r'(azimuth|background-attachment|background-color|'
         r'background-image|background-position|background-repeat|'
         r'background|border-bottom-color|border-bottom-style|'
         r'border-bottom-width|border-left-color|border-left-style|'
         r'border-left-width|border-right|border-right-color|'
         r'border-right-style|border-right-width|border-top-color|'
         r'border-top-style|border-top-width|border-bottom|'
         r'border-collapse|border-left|border-width|border-color|'
         r'border-spacing|border-style|border-top|border|caption-side|'
         r'clear|clip|color|content|counter-increment|counter-reset|'
         r'cue-after|cue-before|cue|cursor|direction|display|'
         r'elevation|empty-cells|float|font-family|font-size|'
         r'font-size-adjust|font-stretch|font-style|font-variant|'
         r'font-weight|font|height|letter-spacing|line-height|'
         r'list-style-type|list-style-image|list-style-position|'
         r'list-style|margin-bottom|margin-left|margin-right|'
         r'margin-top|margin|marker-offset|marks|max-height|max-width|'
         r'min-height|min-width|opacity|orphans|outline|outline-color|'
         r'outline-style|outline-width|overflow|padding-bottom|'
         r'padding-left|padding-right|padding-top|padding|page|'
         r'page-break-after|page-break-before|page-break-inside|'
         r'pause-after|pause-before|pause|pitch|pitch-range|'
         r'play-during|position|quotes|richness|right|size|'
         r'speak-header|speak-numeral|speak-punctuation|speak|'
         r'speech-rate|stress|table-layout|text-align|text-decoration|'
         r'text-indent|text-shadow|text-transform|top|unicode-bidi|'
         r'vertical-align|visibility|voice-family|volume|white-space|'
         r'widows|width|word-spacing|z-index|bottom|left|'
         r'above|absolute|always|armenian|aural|auto|avoid|baseline|'
         r'behind|below|bidi-override|blink|block|bold|bolder|both|'
         r'capitalize|center-left|center-right|center|circle|'
         r'cjk-ideographic|close-quote|collapse|condensed|continuous|'
         r'crop|crosshair|cross|cursive|dashed|decimal-leading-zero|'
         r'decimal|default|digits|disc|dotted|double|e-resize|embed|'
         r'extra-condensed|extra-expanded|expanded|fantasy|far-left|'
         r'far-right|faster|fast|fixed|georgian|groove|hebrew|help|'
         r'hidden|hide|higher|high|hiragana-iroha|hiragana|icon|'
         r'inherit|inline-table|inline|inset|inside|invert|italic|'
         r'justify|katakana-iroha|katakana|landscape|larger|large|'
         r'left-side|leftwards|level|lighter|line-through|list-item|'
         r'loud|lower-alpha|lower-greek|lower-roman|lowercase|ltr|'
         r'lower|low|medium|message-box|middle|mix|monospace|'
         r'n-resize|narrower|ne-resize|no-close-quote|no-open-quote|'
         r'no-repeat|none|normal|nowrap|nw-resize|oblique|once|'
         r'open-quote|outset|outside|overline|pointer|portrait|px|'
         r'relative|repeat-x|repeat-y|repeat|rgb|ridge|right-side|'
         r'rightwards|s-resize|sans-serif|scroll|se-resize|'
         r'semi-condensed|semi-expanded|separate|serif|show|silent|'
         r'slow|slower|small-caps|small-caption|smaller|soft|solid|'
         r'spell-out|square|static|status-bar|super|sw-resize|'
         r'table-caption|table-cell|table-column|table-column-group|'
         r'table-footer-group|table-header-group|table-row|'
         r'table-row-group|text|text-bottom|text-top|thick|thin|'
         r'transparent|ultra-condensed|ultra-expanded|underline|'
         r'upper-alpha|upper-latin|upper-roman|uppercase|url|'
         r'visible|w-resize|wait|wider|x-fast|x-high|x-large|x-loud|'
         r'x-low|x-small|x-soft|xx-large|xx-small|yes)\b', Name.Constant),
        (r'(indigo|gold|firebrick|indianred|darkolivegreen|'
         r'darkseagreen|mediumvioletred|mediumorchid|chartreuse|'
         r'mediumslateblue|springgreen|crimson|lightsalmon|brown|'
         r'turquoise|olivedrab|cyan|skyblue|darkturquoise|'
         r'goldenrod|darkgreen|darkviolet|darkgray|lightpink|'
         r'darkmagenta|lightgoldenrodyellow|lavender|yellowgreen|thistle|'
         r'violet|orchid|ghostwhite|honeydew|cornflowerblue|'
         r'darkblue|darkkhaki|mediumpurple|cornsilk|bisque|slategray|'
         r'darkcyan|khaki|wheat|deepskyblue|darkred|steelblue|aliceblue|'
         r'gainsboro|mediumturquoise|floralwhite|coral|lightgrey|'
         r'lightcyan|darksalmon|beige|azure|lightsteelblue|oldlace|'
         r'greenyellow|royalblue|lightseagreen|mistyrose|sienna|'
         r'lightcoral|orangered|navajowhite|palegreen|burlywood|'
         r'seashell|mediumspringgreen|papayawhip|blanchedalmond|'
         r'peru|aquamarine|darkslategray|ivory|dodgerblue|'
         r'lemonchiffon|chocolate|orange|forestgreen|slateblue|'
         r'mintcream|antiquewhite|darkorange|cadetblue|moccasin|'
         r'limegreen|saddlebrown|darkslateblue|lightskyblue|deeppink|'
         r'plum|darkgoldenrod|sandybrown|magenta|tan|'
         r'rosybrown|pink|lightblue|palevioletred|mediumseagreen|'
         r'dimgray|powderblue|seagreen|snow|mediumblue|midnightblue|'
         r'paleturquoise|palegoldenrod|whitesmoke|darkorchid|salmon|'
         r'lightslategray|lawngreen|lightgreen|tomato|hotpink|'
         r'lightyellow|lavenderblush|linen|mediumaquamarine|'
         r'blueviolet|peachpuff)\b', Name.Entity),
        (r'(black|silver|gray|white|maroon|red|purple|fuchsia|green|'
         r'lime|olive|yellow|navy|blue|teal|aqua)\b', Name.Builtin),
        (r'\!(important|default)', Name.Exception),
        (r'(true|false)', Name.Pseudo),
        (r'(and|or|not)', Operator.Word),
        (r'/\*', Comment.Multiline, 'inline-comment'),
        (r'//[^\n]*', Comment.Single),
        (r'\#[a-z0-9]{1,6}', Number.Hex),
        (r'(-?\d+)(\%|[a-z]+)?', bygroups(Number.Integer, Keyword.Type)),
        (r'(-?\d*\.\d+)(\%|[a-z]+)?', bygroups(Number.Float, Keyword.Type)),
        (r'#{', String.Interpol, 'interpolation'),
        (r'[~\^\*!&%<>\|+=@:,./?-]+', Operator),
        (r'[\[\]()]+', Punctuation),
        (r'"', String.Double, 'string-double'),
        (r"'", String.Single, 'string-single'),
        (r'[a-z_-][\w-]*', Name),
    ],

    'interpolation': [
        (r'\}', String.Interpol, '#pop'),
        include('value'),
    ],

    'selector': [
        (r'[ \t]+', Text),
        (r'\:', Name.Decorator, 'pseudo-class'),
        (r'\.', Name.Class, 'class'),
        (r'\#', Name.Namespace, 'id'),
        (r'[a-zA-Z0-9_-]+', Name.Tag),
        (r'#\{', String.Interpol, 'interpolation'),
        (r'&', Keyword),
        (r'[~\^\*!&\[\]\(\)<>\|+=@:;,./?-]', Operator),
        (r'"', String.Double, 'string-double'),
        (r"'", String.Single, 'string-single'),
    ],

    'string-double': [
        (r'(\\.|#(?=[^\n{])|[^\n"#])+', String.Double),
        (r'#\{', String.Interpol, 'interpolation'),
        (r'"', String.Double, '#pop'),
    ],

    'string-single': [
        (r"(\\.|#(?=[^\n{])|[^\n'#])+", String.Double),
        (r'#\{', String.Interpol, 'interpolation'),
        (r"'", String.Double, '#pop'),
    ],

    'string-url': [
        (r'(\\#|#(?=[^\n{])|[^\n#)])+', String.Other),
        (r'#\{', String.Interpol, 'interpolation'),
        (r'\)', String.Other, '#pop'),
    ],

    'pseudo-class': [
        (r'[\w-]+', Name.Decorator),
        (r'#\{', String.Interpol, 'interpolation'),
        (r'', Text, '#pop'),
    ],

    'class': [
        (r'[\w-]+', Name.Class),
        (r'#\{', String.Interpol, 'interpolation'),
        (r'', Text, '#pop'),
    ],

    'id': [
        (r'[\w-]+', Name.Namespace),
        (r'#\{', String.Interpol, 'interpolation'),
        (r'', Text, '#pop'),
    ],

    'for': [
        (r'(from|to|through)', Operator.Word),
        include('value'),
    ],
}

class SassLexer(ExtendedRegexLexer):
    """
    For Sass stylesheets.

    *New in Pygments 1.3.*
    """

    name = 'Sass'
    aliases = ['sass', 'SASS']
    filenames = ['*.sass']
    mimetypes = ['text/x-sass']

    flags = re.IGNORECASE
    tokens = {
        'root': [
            (r'[ \t]*\n', Text),
            (r'[ \t]*', _indentation),
        ],

        'content': [
            (r'//[^\n]*', _starts_block(Comment.Single, 'single-comment'),
             'root'),
            (r'/\*[^\n]*', _starts_block(Comment.Multiline, 'multi-comment'),
             'root'),
            (r'@import', Keyword, 'import'),
            (r'@for', Keyword, 'for'),
            (r'@(debug|warn|if|while)', Keyword, 'value'),
            (r'(@mixin)( [\w-]+)', bygroups(Keyword, Name.Function), 'value'),
            (r'(@include)( [\w-]+)', bygroups(Keyword, Name.Decorator), 'value'),
            (r'@extend', Keyword, 'selector'),
            (r'@[a-z0-9_-]+', Keyword, 'selector'),
            (r'=[\w-]+', Name.Function, 'value'),
            (r'\+[\w-]+', Name.Decorator, 'value'),
            (r'([!$][\w-]\w*)([ \t]*(?:(?:\|\|)?=|:))',
             bygroups(Name.Variable, Operator), 'value'),
            (r':', Name.Attribute, 'old-style-attr'),
            (r'(?=.+?[=:]([^a-z]|$))', Name.Attribute, 'new-style-attr'),
            (r'', Text, 'selector'),
        ],

        'single-comment': [
            (r'.+', Comment.Single),
            (r'\n', Text, 'root'),
        ],

        'multi-comment': [
            (r'.+', Comment.Multiline),
            (r'\n', Text, 'root'),
        ],

        'import': [
            (r'[ \t]+', Text),
            (r'[^\s]+', String),
            (r'\n', Text, 'root'),
        ],

        'old-style-attr': [
            (r'[^\s:="\[]+', Name.Attribute),
            (r'#{', String.Interpol, 'interpolation'),
            (r'[ \t]*=', Operator, 'value'),
            (r'', Text, 'value'),
        ],

        'new-style-attr': [
            (r'[^\s:="\[]+', Name.Attribute),
            (r'#{', String.Interpol, 'interpolation'),
            (r'[ \t]*[=:]', Operator, 'value'),
        ],

        'inline-comment': [
            (r"(\\#|#(?=[^\n{])|\*(?=[^\n/])|[^\n#*])+", Comment.Multiline),
            (r'#\{', String.Interpol, 'interpolation'),
            (r"\*/", Comment, '#pop'),
        ],
    }
    tokens.update(copy.deepcopy(common_sass_tokens))
    tokens['value'].append((r'\n', Text, 'root'))
    tokens['selector'].append((r'\n', Text, 'root'))


class ScssLexer(RegexLexer):
    """
    For SCSS stylesheets.
    """

    name = 'SCSS'
    aliases = ['scss']
    filenames = ['*.scss']
    mimetypes = ['text/x-scss']

    flags = re.IGNORECASE | re.DOTALL
    tokens = {
        'root': [
            (r'\s+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'@import', Keyword, 'value'),
            (r'@for', Keyword, 'for'),
            (r'@(debug|warn|if|while)', Keyword, 'value'),
            (r'(@mixin)( [\w-]+)', bygroups(Keyword, Name.Function), 'value'),
            (r'(@include)( [\w-]+)', bygroups(Keyword, Name.Decorator), 'value'),
            (r'@extend', Keyword, 'selector'),
            (r'@[a-z0-9_-]+', Keyword, 'selector'),
            (r'(\$[\w-]\w*)([ \t]*:)', bygroups(Name.Variable, Operator), 'value'),
            (r'(?=[^;{}][;}])', Name.Attribute, 'attr'),
            (r'(?=[^;{}:]+:[^a-z])', Name.Attribute, 'attr'),
            (r'', Text, 'selector'),
        ],

        'attr': [
            (r'[^\s:="\[]+', Name.Attribute),
            (r'#{', String.Interpol, 'interpolation'),
            (r'[ \t]*:', Operator, 'value'),
        ],

        'inline-comment': [
            (r"(\\#|#(?=[^{])|\*(?=[^/])|[^#*])+", Comment.Multiline),
            (r'#\{', String.Interpol, 'interpolation'),
            (r"\*/", Comment, '#pop'),
        ],
    }
    tokens.update(copy.deepcopy(common_sass_tokens))
    tokens['value'].extend([(r'\n', Text), (r'[;{}]', Punctuation, 'root')])
    tokens['selector'].extend([(r'\n', Text), (r'[;{}]', Punctuation, 'root')])


class CoffeeScriptLexer(RegexLexer):
    """
    For `CoffeeScript`_ source code.

    .. _CoffeeScript: http://coffeescript.org

    *New in Pygments 1.3.*
    """

    name = 'CoffeeScript'
    aliases = ['coffee-script', 'coffeescript']
    filenames = ['*.coffee']
    mimetypes = ['text/coffeescript']

    flags = re.DOTALL
    tokens = {
        'commentsandwhitespace': [
            (r'\s+', Text),
            (r'#.*?\n', Comment.Single),
        ],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            (r'/(\\.|[^[/\\\n]|\[(\\.|[^\]\\\n])*])+/'
             r'([gim]+\b|\B)', String.Regex, '#pop'),
            (r'(?=/)', Text, ('#pop', 'badregex')),
            (r'', Text, '#pop'),
        ],
        'badregex': [
            ('\n', Text, '#pop'),
        ],
        'root': [
            (r'^(?=\s|/|<!--)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            (r'\+\+|--|~|&&|\band\b|\bor\b|\bis\b|\bisnt\b|\bnot\b|\?|:|'
             r'\|\||\\(?=\n)|(<<|>>>?|==?|!=?|[-<>+*`%&\|\^/])=?',
             Operator, 'slashstartsregex'),
            (r'[{(\[;,]', Punctuation, 'slashstartsregex'),
            (r'[})\].]', Punctuation),
            (r'(for|in|of|while|break|return|continue|switch|when|then|if|else|'
             r'throw|try|catch|finally|new|delete|typeof|instanceof|super|'
             r'extends|this)\b', Keyword, 'slashstartsregex'),
            (r'(true|false|yes|no|on|off|null|NaN|Infinity|undefined)\b',
             Keyword.Constant),
            (r'(Array|Boolean|Date|Error|Function|Math|netscape|'
             r'Number|Object|Packages|RegExp|String|sun|decodeURI|'
             r'decodeURIComponent|encodeURI|encodeURIComponent|'
             r'Error|eval|isFinite|isNaN|parseFloat|parseInt|document|this|'
             r'window)\b', Name.Builtin),
            (r'[$a-zA-Z_][a-zA-Z0-9_\.:]*\s*:\s', Name.Variable,
              'slashstartsregex'),
            (r'@[$a-zA-Z_][a-zA-Z0-9_\.:]*\s*:\s', Name.Variable.Instance,
              'slashstartsregex'),
            (r'@?[$a-zA-Z_][a-zA-Z0-9_]*', Name.Other, 'slashstartsregex'),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
        ]
    }

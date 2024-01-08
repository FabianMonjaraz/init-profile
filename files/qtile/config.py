# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.core.manager import Qtile
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

def go_to_group(name: str):
    def _inner(qtile: Qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].cmd_toscreen()
            return

        #if name in ["I","II","III","IV","V"]:
        if name in "12345":
        
            qtile.focus_screen(0)
            qtile.groups_map[name].cmd_toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].cmd_toscreen()

    return _inner

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Window Fullscreen"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "w", lazy.spawn("firefox"), desc="Web browser"),
    Key([mod, "shift"], "w", lazy.spawn("firefox --private-window"), desc="Web browser"),
    Key([mod], "s", lazy.spawn("scrot -s -e 'xclip -selection clipboard -t image/png < $f && rm $f'"), desc="Screenshot"),
    Key([mod, "shift"], "x", lazy.spawn("shutdown -h now"), desc="Screenshot"),
    #Key([mod, "shift"], "r", lazy.spawn("shutdown -r now"), desc="Screenshot"),
    

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "p", lazy.spawncmd(),
    #    desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.run_extension(extension.DmenuRun(
      #dmenu_prompt='=>',
      #dmenu_font='sans',
      #background='#14524E',
      #foreground='#96EBE5',
      #selected_background='#06524D',
      #selected_foreground='#0FD1C4',

      dmenu_prompt='=>',
      dmenu_font='dejavusans',
      background='#02524E',
      foreground='#07D1C8',
      selected_background='#02524E',
      selected_foreground='#B6EBE5',
    ))),
]

# groups = [
#         Group("I"),
#         Group("II"),
#         Group("III"),
#         Group("IV"),
#         Group("V"),
#         Group("VI"),
#         Group("VII"),
#         Group("VIII"),
#         Group("XI"),
#         Group("X")
#         ]
groups = [Group(i) for i in "1234567890"]
# groups_left = [Group(i) for i in "12345"]
# groups_right = [Group(i) for i in "67890"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        #Key([mod], i.name, lazy.group[i.name].toscreen(),
        Key([mod], i.name, lazy.function(go_to_group(i.name)),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
        #    desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])


#for i in groups:
#    keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))

#for g in groups:
#    keys.append(Key([mod], g.name, lazy.function(go_to_group(i.name))))

layouts = [
    layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(),
    layout.MonadThreeCol(),
     layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='dejavusans',
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
      bottom=bar.Bar(
          [
              widget.Chord(
                  chords_colors={
                      'launch': ("#ff0000", "#ffffff"),
                  },
                  name_transform=lambda name: name.upper(),
              ),
              widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
              widget.WindowName(),
              widget.GroupBox(visible_groups=['1','2','3','4','5'],highlight_method='line'),
          ],
        24,
        background="#00000000"
      ),
    ), 
    Screen(
      bottom=bar.Bar(
        [
            widget.GroupBox(visible_groups=['6','7','8','9','0'],highlight_method='line'),
            #widget.GroupBox(),
            widget.WindowName(),
            widget.Chord(
                chords_colors={
                    'launch': ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
                ),
            #widget.Systray(),
            widget.CurrentLayout(),
            widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
        ],
        24,
        background="#00000000"
      ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

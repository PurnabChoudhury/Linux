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
import os
import subprocess
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
from libqtile import qtile

mod = "mod4"
#terminal = guess_terminal()
file_manager = "pcmanfm"
terminal  = "alacritty"
web_browser = "google-chrome"
web_browser_2 = "firefox"
configpy = "gedit /home/purnab/.config/qtile/config.py"

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn rofi"),
    
    #sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D default sset Master 2%- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D default sset Master 2%+ unmute")),
    
    #brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10")),
    
    #browser
    Key([mod, "shift"], "b", lazy.spawn(web_browser), desc="Launch chrome"),
    Key([mod, "shift"], "n", lazy.spawn(web_browser_2), desc="Launch firefox"),
    
    #file_manager
    Key([mod, "shift"], "f", lazy.spawn(file_manager), desc="Launch terminal"),
    
    #config file
    Key([mod, "control"], "c", lazy.spawn(configpy), desc="Launch config.py"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


config = {'margin':10,'single_margin':10,"border_focus": "e1acff",
          "border_normal": "1D2330"}

#0=black
#1=yellowish white
#2=orange
#3=grey 
#4=yellow
#5=light yellowish white  
#6=red  
#7=blue 
#8=aqua(yellow green ka bhai shayad)  
#9=light blue 
colors = [["#282828", "#282828"],
          ["#ebdbb2", "#ebdbb2"],
          ["#d65d0e", "#d65d0e"],
          ["#928374", "#928374"],
          ["#fabd2f", "#fabd2f"],
          ["#fbf1c7", "#fbf1c7"],
          ["#fb4934", "#fb4934"],
          ["#458588", "#458588"],
          ["#689d61", "#689d61"],
          ["#8f3f71", "#8f3f71"],
          ["#0000ff", "#0000ff"]]

colors2 = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]


layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, margin=8),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**config),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(**config),
    layout.Max(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**config),

]

widget_defaults = dict(
    font="Fantasq Sans Mono",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
            	widget.Sep(
            		linewidth = 0,
            		padding = 6,
            		background=colors2[0]),
                widget.GroupBox(font = "Ubuntu Bold",
                       fontsize = 12,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors2[2],
                       inactive = colors2[7],
                       rounded = False,
                       highlight_color = colors2[1],
                       highlight_method = "line",
                       this_current_screen_border = colors2[6],
                       this_screen_border = colors2[4],
                       other_current_screen_border = colors2[6],
                       other_screen_border = colors2[4],
                       foreground = colors2[2],
                       background = colors2[0]),
                widget.TextBox(
                	font='3270Medium Nerd Font Mono',
                	text='',
                	fontsize=35,
                	padding=-1,
                	background=colors2[7],
                	foreground=colors2[0]),
                widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[2],
                       background = colors2[7],
                       padding = 0,
                       scale = 0.7
                       ),

                widget.TextBox(
                	font='3270Medium Nerd Font Mono',
                	text='',
                	fontsize=35,
                	padding=-1,
                	background=colors[7],
                	foreground=colors2[7]),
                widget.Volume(
                	font="Ubuntu Bold",
                	fmt = ': {}',
                	padding=5,
                	background=colors[7]),
                widget.TextBox(
                	font='3270Medium Nerd Font Mono',
                	text='',
                	fontsize=35,
                	padding=-1,
                	background=colors[4],
                	foreground=colors[7]),
                #widget.Backlight(),
                
                widget.CPU(
                	font="Ubuntu Bold",
                	#font='FantasqSansMono NFM',
                	format = 'CPU: {freq_current}GHz {load_percent}%',
                	background=colors[4],
                	foreground=colors[0],
                	padding=1),
                widget.TextBox(
                	font='3270Medium Nerd Font Mono',
                	text='',
                	fontsize=35,
                	padding=-1,
                	background=colors[0],
                	foreground=colors[4]),
                widget.Prompt(
                	padding=1,
                	background=colors[0]),
                widget.WindowName(
                	font="Ubuntu Bold",
                	background=colors[0]),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.CheckUpdates(distro='Fedora'),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(
                	font="Ubuntu Bold"),
                widget.TextBox(
                       text = '',
                       font = "3270Medium Nerd Font Mono",
                       background = colors[0],
                       foreground = colors[1],
                       padding = -1,
                       fontsize = 35
                       ),
                widget.Clock(format=' %a, %d. %m. %Y. |  %I:%M %p',
                	font="Ubuntu Bold",
			foreground = colors[0],
                	background = colors[1],
                	fontsize=13),
                widget.TextBox(
                       text = '',
                       font = "3270Medium Nerd Font Mono",
                       background = colors[1],
                       foreground = colors[6],
                       padding = -1,
                       fontsize = 35
                       ),
                widget.Battery(
                	font="Ubuntu Bold",
                	charge_char ='',
                    	discharge_char = '',
                    	format = '  {percent:2.0%} {char}',
                	background=colors[6]),
                widget.TextBox(
                       text = '',
                       font = "3270Medium Nerd Font Mono",
                       background = colors[6],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 35
                       ),
                widget.Net(
                	font="Ubuntu Bold",
                       #interface = "enp5s0",
                       format = '{down} ↓↑ {up}',
                       foreground = colors[0],
                       background = colors[4],
                       padding = 5
                       ),

                widget.TextBox(
                       text = '',
                       font = "3270Medium Nerd Font Mono",
                       background = colors[4],
                       foreground = colors2[7],
                       padding = -1,
                       fontsize = 35
                       ),
                widget.Memory(
                	font="Ubuntu Bold",
                       foreground = colors[1],
                       background = colors2[7],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal+ ' -e htop')},
                       fmt = 'Mem: {}',
                       padding = 5
                       ),
                #widget.TaskList(),
                #widget.Systray(),
                widget.TextBox(
		       text = '',
                       font = "3270Medium Nerd Font Mono",
                       background = colors2[7],
                       foreground = colors[6],
                       padding = -1,
                       fontsize = 35
                       ),
		widget.LaunchBar(
			default_icon = "/home/purnab/.config/qtile/python-white.png",
			progs = [('powermenu','~/.local/bin/powermenu.sh','powermenu')],
			mouse_callbacks = {'Button1': lambda: lazy.spawn(' -e ~/.local/bin/powermenu.sh')},
			),
               #widget.QuickExit(
                	#font="Ubuntu Bold",
                	#fmt = 'Q',
                	#fontsize = 12,
                	
                	#background=colors[6])
            ],
            30,
           # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        #height=200
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

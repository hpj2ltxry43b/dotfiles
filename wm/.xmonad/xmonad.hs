import XMonad

import XMonad.Hooks.DynamicLog
import XMonad.Hooks.EwmhDesktops

import XMonad.Layout.Spacing

import XMonad.Util.EZConfig
import XMonad.Util.Loggers
import XMonad.Util.Ungrab

import Graphics.X11.ExtraTypes.XF86

main = statusBar "xmobar ~/.xmonad/.xmobarrc" my_xmobar_pp toggleStrutsKey my_config >>= xmonad . ewmh
    where
        toggleStrutsKey XConfig { modMask = m } = (m, xK_b)

my_config = def
            { terminal = "alacritty"

            , focusFollowsMouse = True
            , clickJustFocuses  = True

            , modMask = my_mod_mask

            , borderWidth        = 10
            , normalBorderColor  = "#222222"
            , focusedBorderColor = "#666666"

            , workspaces = map show [1..9]

            , startupHook =
                startupHook def >>
                sendMessage (ModifySmartBorder $ const False) >>
                spawn "killall -q dunst picom" >>
                spawn "xsetroot -cursor_name left_ptr" >>
                spawn "feh --bg-scale --no-fehbg ~/Firefox_wallpaper.png" >>
                spawn "dunst" >>
                -- spawn "picom --shadow-radius=10 --fade-in-step=0.1 --fade-out-step=0.08 --fade-delta=10 --shadow --fading" >>
                spawn "firefox -p stuff" >>
                spawn "firefox -p lsotnnirhcdfkb"

            , layoutHook =
                spacingRaw True (Border 10 10 10 10) True (Border 10 10 10 10) True $ layoutHook def

            }
            `removeKeys`
                [ (my_mod_mask, xK_p)
                ]
            `additionalKeys`
                [ ((controlMask .|. shiftMask, xK_Print), unGrab >> spawn "scrot -s")
                , ((my_mod_mask, xK_d), spawn "dmenu_run -nb \"#222\" -nf \"#aaa\" -sb \"#444\" -sf \"#eee\" -l 10 -fn \"Biryani:12\"")

                , ((0, xF86XK_AudioRaiseVolume), spawn "pactl -- set-sink-volume @DEFAULT_SINK@ +5%")
                , ((0, xF86XK_AudioLowerVolume), spawn "pactl -- set-sink-volume @DEFAULT_SINK@ -5%")
                , ((0, xF86XK_AudioMute), spawn "pactl -- set-sink-mute @DEFAULT_SINK@ toggle")

                , ((0, xF86XK_AudioPrev), spawn "playerctl previous")
                , ((0, xF86XK_AudioNext), spawn "playerctl next")
                , ((0, xF86XK_AudioPlay), spawn "playerctl play-pause")

                , ((0, xF86XK_MonBrightnessUp),   spawn "xbacklight -inc 5 -time 50")
                , ((0, xF86XK_MonBrightnessDown), spawn "xbacklight -dec 5 -time 50")
                ]

my_mod_mask = mod4Mask

my_xmobar_pp = def
               { ppSep              = "     "

               , ppTitle            = xmobarRaw . shorten 50
               , ppTitleSanitize    = xmobarStrip

               , ppWsSep            = "  "
               , ppCurrent          = xmobarColor "#ffffff" ""
               , ppHidden           = xmobarColor "#999999" ""
               , ppHiddenNoWindows  = xmobarColor "#555555" ""
               , ppUrgent           = xmobarColor "#ffffff" "#ff00000"

               , ppOrder = \ [wses, _, win] -> [wses, win]
               }

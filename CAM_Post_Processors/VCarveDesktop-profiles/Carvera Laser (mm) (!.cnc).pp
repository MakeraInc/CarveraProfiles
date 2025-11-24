+ =======================================
+ ---
+ Version 1
+   Josh     18/11/2022 Written
+ =======================================


POST_NAME = "Carvera Laser (mm) (*.cnc)"


FILE_EXTENSION = "cnc"


UNITS = "MM"

LASER_SUPPORT = "YES"

+------------------------------------------------
+    Line terminating characters
+------------------------------------------------

LINE_ENDING = "[13][10]"

+------------------------------------------------
+    Block numbering
+------------------------------------------------

LINE_NUMBER_START     = 0
LINE_NUMBER_INCREMENT = 10
LINE_NUMBER_MAXIMUM = 999999

+================================================
+
+    Formating for variables
+
+================================================

VAR LINE_NUMBER = [N|A|N|1.0]
VAR SPINDLE_SPEED = [S|A|S|1.0]
VAR FEED_RATE = [F|C|F|1.1]
VAR X_POSITION = [X|C|X|1.3]
VAR Y_POSITION = [Y|C|Y|1.3]
VAR Z_POSITION = [Z|C|Z|1.3]
VAR X_HOME_POSITION = [XH|A|X|1.3]
VAR Y_HOME_POSITION = [YH|A|Y|1.3]
VAR Z_HOME_POSITION = [ZH|A|Z|1.3]
VAR ARC_CENTRE_I_INC_POSITION = [I|A|I|1.3]
VAR ARC_CENTRE_J_INC_POSITION = [J|A|J|1.3]
VAR POWER = [P|C|S|1.2|0.01]



+================================================
+
+    Block definitions for toolpath output
+
+================================================


+---------------------------------------------------
+  Commands output at the start of the file
+---------------------------------------------------

begin HEADER

"(File created: [DATE] - [TIME])"
"(for Carvera from Vectric)"
"G90G54"
"G17"
"G21"
""
"(Laser mode on)"
"M321"
"G0[ZH]"
"G0[XH][YH]"
"M3"


+---------------------------------------------------
+  Commands output for rapid moves
+---------------------------------------------------

begin RAPID_MOVE

"G0[X][Y][Z]"


+---------------------------------------------------
+  Commands output for the first feed rate move
+---------------------------------------------------

begin FIRST_FEED_MOVE

"G1[X][Y][Z][F][P]"


+---------------------------------------------------
+  Commands output for feed rate moves
+---------------------------------------------------

begin FEED_MOVE

"[X][Y][Z][P]"

+---------------------------------------------------
+  Commands output for the first clockwise arc move
+---------------------------------------------------

begin FIRST_CW_ARC_MOVE

"G2[X][Y][I][J][F][P]"


+---------------------------------------------------
+  Commands output for clockwise arc  move
+---------------------------------------------------

begin CW_ARC_MOVE

"G2[X][Y][I][J][P]"


+---------------------------------------------------
+  Commands output for the first counterclockwise arc move
+---------------------------------------------------

begin FIRST_CCW_ARC_MOVE

"G3[X][Y][I][J][F][P]"


+---------------------------------------------------
+  Commands output for counterclockwise arc  move
+---------------------------------------------------

begin CCW_ARC_MOVE

"G3[X][Y][I][J][P]"


+---------------------------------------------------
+  Commands output when the jet is turned on
+---------------------------------------------------

begin JET_TOOL_ON


+---------------------------------------------------
+  Commands output when the jet is turned off
+---------------------------------------------------

begin JET_TOOL_OFF


+---------------------------------------------------
+  Commands output when the jet power is changed
+---------------------------------------------------

begin JET_TOOL_POWER



+---------------------------------------------------
+  Commands output at the end of the file
+---------------------------------------------------

begin FOOTER

"M5"
"G0[ZH]"
"G0[XH][YH]"
"(Laser mode off)"
"M322"
"G28"
"M30"
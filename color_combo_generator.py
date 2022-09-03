#der user wählt basierend auf einer
#erklärung seinen Kontrasttyp aus
#--------------erklärung auf der website-------
#helle haare + heller hautton = low contrast
#helle haare + dunkler hautton = medium
#dunkle haare + dunkler hautton = medium
#dunkle haare + heller hautton = high contrast

contrast = "wird vom user ausgewählt"

if contrast == "high":
  colours_of_clothes = "complimentary"

if contrast == "low":
  colours_of_clothes = "analogue"

else:
  colours_of_clothes = "medium"
  
complimentary_combos = { "color1" : "color7", "color2" : "color8", "color3" : "color9", "color4" : "color10","color5" : "color11", "color6" : "color12",
 "color7" : "color1", "color8" : "color2", "color9" : "color3", "color10" : "color4","color11" : "color5", "color12" : "color6"}

triad_combos1 = { 
"color1" : "color5", "color2" : "color6", "color3" : "color7", "color4" : "color8","color5" : "color9", "color6" : "color10",
 "color7" : "color11", "color8" : "color12", "color9" : "color1", "color10" : "color2","color11" : "color3", "color12" : "color4"}

triad_combos2 = { 
"color1" : "color9", "color2" : "color10", "color3" : "color11", "color4" : "color12","color5" : "color1", "color6" : "color2",
 "color7" : "color3", "color8" : "color4", "color9" : "color5", "color10" : "color6","color11" : "color7", "color12" : "color8"}

analogue_combos1 = { 
"color1" : "color2", "color2" : "color3", "color3" : "color4", "color4" : "color5","color5" : "color6", "color6" : "color7",
 "color7" : "color8", "color8" : "color9", "color9" : "color10", "color10" : "color11","color11" : "color12", "color12" : "color1"}

analogue_combos2 = { 
"color1" : "color12", "color2" : "color1", "color3" : "color2", "color4" : "color3","color5" : "color4", "color6" : "color5",
 "color7" : "color6", "color8" : "color7", "color9" : "color8", "color10" : "color9","color11" : "color10", "color12" : "color11"}


#die farbe, die der nutzer kombinieren möchte, muss hier als user_color festgelegt werden

user_color = "color1"

if colours_of_clothes == "complimentary":
  print(complimentary_combos[user_color])
  print(triad_combos1[user_color])
  print(triad_combos2[user_color])

if colours_of_clothes == "any":
  print(triad_combos1[user_color])
  print(triad_combos2[user_color])
  print(complimentary_combos[user_color])
  print(analogue_combos1[user_color])
  print(analogue_combos2[user_color])
  

if colours_of_clothes == "analogue":
  print(analogue_combos1[user_color])
  print(analogue_combos2[user_color])
  print(triad_combos1[user_color])
  print(triad_combos2[user_color])

#statt der print-befehle müssen die farben
# auf der website angezeigt werden
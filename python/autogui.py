import random
import emoji
import pyautogui as p
import time
message = (emoji.emojize("Chey..I..Love..you...:winking_face_with_tongue::face_blowing_a_kiss::kiss_mark::kiss_mark::heart_exclamation:"),
           emoji.emojize("Osey..chey..endhuku..ala..unnav...:pleading_face::pleading_face::pleading_face::pleading_face:"),
           emoji.emojize("wastefellow:smiling_face_with_open_hands::smiling_face_with_open_hands::smiling_face_with_open_hands:"),
           emoji.emojize("Chaitu..gaaa..emaindhe..."),
           emoji.emojize("Chey..koopanga..unnava...:smiling_face_with_smiling_eyes::smiling_face_with_smiling_eyes::smiling_face_with_smiling_eyes:"))
time.sleep(5)
for i in range(360):
    p.typewrite(random.choice(message))
    p.press("enter")

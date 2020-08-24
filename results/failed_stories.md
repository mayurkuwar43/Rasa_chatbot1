## happy path 1 (C:\Users\admin\AppData\Local\Temp\tmpdbdpsi_s\0e7a607f8b7a43918ba556358fb34feb_conversation_tests.md)
* greet: hello there!
    - utter_greet
    - action_listen   <!-- predicted: utter_first_message -->
* mood_great: amazing   <!-- predicted: greet: amazing -->
    - utter_happy   <!-- predicted: action_listen -->


## happy path 2 (C:\Users\admin\AppData\Local\Temp\tmpdbdpsi_s\0e7a607f8b7a43918ba556358fb34feb_conversation_tests.md)
* greet: hello there!
    - utter_greet
    - action_listen   <!-- predicted: utter_first_message -->
* mood_great: amazing   <!-- predicted: greet: amazing -->
    - utter_happy   <!-- predicted: action_listen -->
* goodbye: bye-bye!   <!-- predicted: greet: bye-bye! -->
    - utter_goodbye   <!-- predicted: action_listen -->


## sad path 1 (C:\Users\admin\AppData\Local\Temp\tmpdbdpsi_s\0e7a607f8b7a43918ba556358fb34feb_conversation_tests.md)
* greet: hello
    - utter_greet
    - action_listen   <!-- predicted: utter_first_message -->
* mood_unhappy: not good   <!-- predicted: greet: not good -->
    - utter_cheer_up   <!-- predicted: action_listen -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: main_menu: yes -->
    - utter_happy   <!-- predicted: action_listen -->


## sad path 2 (C:\Users\admin\AppData\Local\Temp\tmpdbdpsi_s\0e7a607f8b7a43918ba556358fb34feb_conversation_tests.md)
* greet: hello
    - utter_greet
    - action_listen   <!-- predicted: utter_first_message -->
* mood_unhappy: not good   <!-- predicted: greet: not good -->
    - utter_cheer_up   <!-- predicted: action_listen -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: plan_my_trip: not really -->
    - utter_goodbye   <!-- predicted: action_listen -->


## sad path 3 (C:\Users\admin\AppData\Local\Temp\tmpdbdpsi_s\0e7a607f8b7a43918ba556358fb34feb_conversation_tests.md)
* greet: hi
    - utter_greet
    - action_listen   <!-- predicted: utter_first_message -->
* mood_unhappy: very terrible   <!-- predicted: greet: very terrible -->
    - utter_cheer_up   <!-- predicted: action_listen -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: greet: no -->
    - utter_goodbye   <!-- predicted: action_listen -->


## say goodbye (C:\Users\admin\AppData\Local\Temp\tmpdbdpsi_s\0e7a607f8b7a43918ba556358fb34feb_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: greet: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_greet -->


## bot challenge (C:\Users\admin\AppData\Local\Temp\tmpdbdpsi_s\0e7a607f8b7a43918ba556358fb34feb_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: plan_my_trip: are you a bot? -->
    - utter_iamabot   <!-- predicted: action_listen -->


